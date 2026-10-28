"""Бизнес-логика конфигурационных файлов.

Импорт / экспорт, CRUD cfg, парсинг content -> ConfigValues.
Не знает о Qt.
"""
import os
import re
import stat

from logic.core.constants import MAX_CONFIG_NAME_LEN
from logic.core.i18n import t
from parsers.cfg_crypto import (
    decrypt,
    encrypt,
    looks_like_encrypted,
)

# Регулярка для строк cfg вида: key = "value"  или  key = value
_CFG_KV_RE = re.compile(
    r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*"?([^"]*)"?\s*$'
)


class ConfigService:
    """Импорт, экспорт, CRUD cfg."""

    def __init__(self, repo, command_repo=None):
        """command_repo нужен для populate_values_from_content.

        Если не передан - парсинг не работает, но всё остальное
        функционирует (обратная совместимость).
        """
        self.repo = repo
        self.command_repo = command_repo

    # =========== импорт ===========

    def import_from_file(self, path: str, server_id: int,
                         name: str) -> int:
        """Читает файл, расшифровывает при необходимости, создаёт cfg.

        Raises:
            OSError: файл не читается.
            ValueError: имя невалидно.
        """
        with open(path, "rb") as f:
            raw = f.read()

        if looks_like_encrypted(raw):
            content = decrypt(raw)
        else:
            content = raw.decode("latin1", errors="replace")

        name = self._validate_name(name)
        config_id = self.repo.create(server_id, name, content)

        # сразу наполняем ConfigValues, если есть command_repo
        if self.command_repo is not None:
            self.populate_values_from_content(config_id, content)

        return config_id

    def create_from_content(self, server_id: int, name: str,
                            content: str) -> int:
        """Создаёт cfg из готового текста (без чтения файла).

        Используется редактором при сохранении нового cfg.
        """
        name = self._validate_name(name)
        return self.repo.create(server_id, name, content)

    # =========== парсинг cfg -> ConfigValues ===========

    def populate_values_from_content(self, config_id: int, content: str):
        """Публичный метод: используется при импорте.

        Загружает команды заново — не критично, импорт редкий.
        """
        if self.command_repo is None:
            return
        all_commands = self.command_repo.all("debug")
        key_to_id = {c["key_name"]: c["id"] for c in all_commands}
        self._populate_values_from_content(config_id, content, key_to_id)

    # =========== экспорт ===========

    def export_to_file(self, config_id: int, path: str, encrypted: bool):
        cfg = self.repo.get(config_id)
        if not cfg:
            raise ValueError(t("config.error.not_found"))

        content = cfg["content"] or ""

        existed = os.path.exists(path)
        was_readonly = False
        if existed:
            try:
                was_readonly = not (os.stat(path).st_mode & stat.S_IWRITE)
            except OSError:
                was_readonly = False

        if was_readonly:
            try:
                os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
            except OSError as exc:
                raise OSError(
                    t("config.error.cannot_unlock").format(path=path)
                ) from exc

        try:
            if encrypted:
                with open(path, "wb") as f:
                    f.write(encrypt(content))
            else:
                with open(path, "w", encoding="latin1",
                          errors="replace") as f:
                    f.write(content)
        finally:
            try:
                os.chmod(path, stat.S_IREAD)
            except OSError:
                pass

    # =========== CRUD ===========

    def rename(self, config_id: int, new_name: str):
        new_name = self._validate_name(new_name)
        self.repo.rename(config_id, new_name)

    def delete(self, config_id: int):
        self.repo.delete(config_id)

    def duplicate(self, config_id: int, new_name: str) -> int:
        new_name = self._validate_name(new_name)
        return self.repo.duplicate(config_id, new_name)

    # =========== вспомогательное ===========

    def load_local_overrides(self, path: str) -> dict[str, str]:
        """Читает один SystemCfgLocal.cfg и возвращает {key: value}."""
        if not path or not os.path.isfile(path):
            return {}

        for encoding in ("utf-8", "cp1251", "latin1"):
            try:
                with open(path, "r", encoding=encoding) as f:
                    text = f.read()
            except UnicodeDecodeError:
                continue
            except OSError:
                return {}

            parsed = self._parse_content(text)
            if parsed:  # если что-то распарсилось — значит, кодировка правильная
                return parsed

        return {}

    def find_local_overrides(self, server_root: str) -> dict[str, str]:
        """Ищет SystemCfgLocal.cfg в L10N\\* и сливает в один dict.

        Если файлов несколько (разные локали) — union: при конфликте
        побеждает значение из более позднего файла (алфавитный порядок).
        """
        if not server_root or not os.path.isdir(server_root):
            return {}

        l10n_dir = os.path.join(server_root, "L10N")
        if not os.path.isdir(l10n_dir):
            return {}

        result: dict[str, str] = {}
        for locale_name in sorted(os.listdir(l10n_dir)):
            locale_dir = os.path.join(l10n_dir, locale_name)
            if not os.path.isdir(locale_dir):
                continue
            local_cfg = os.path.join(locale_dir, "SystemCfgLocal.cfg")
            if not os.path.isfile(local_cfg):
                continue
            parsed = self.load_local_overrides(local_cfg)
            result.update(parsed)

        return result

    def get_server_overrides(self, server_repo, server_id) -> dict[str, str]:
        if server_id is None or server_repo is None:
            return {}
        server = server_repo.get(server_id)
        if not server:
            return {}
        return self.find_local_overrides(server["export_path"] or "")

    def save_content(self, config_id: int, text: str) -> tuple[int, int]:
        """Сохраняет текст cfg + пишет историю изменений.

        Возвращает (отсечено_неизвестных, удалено_дубликатов).
        """
        # 1. Загружаем команды ОДИН раз
        all_commands = (
            self.command_repo.all("debug")
            if self.command_repo is not None
            else []
        )
        key_to_id = {c["key_name"]: c["id"] for c in all_commands}
        id_to_key = {c["id"]: c["key_name"] for c in all_commands}
        known = set(key_to_id.keys())

        # 2. Фильтрация (возвращает списки)
        cleaned, unknown_list, duplicates_list = (
            self._filter_known_commands(text, known)
        )

        # 3. Старое состояние ДО сохранения
        old_values = {
            row["command_id"]: row["custom_value"]
            for row in self.repo.values(config_id)
        }

        # 4. Сохраняем текст + очищаем ConfigValues
        self.repo.update(config_id, cleaned)
        self.repo.clear_values(config_id)

        # 5. Заполняем ConfigValues заново
        self._populate_values_from_content(
            config_id, cleaned, key_to_id
        )

        # 6. Логи — value changes
        self._write_content_logs(
            config_id, old_values, cleaned, key_to_id, id_to_key
        )

        # 7. Логи — удалённые дубли и неизвестные
        self._write_filter_logs(
            config_id, unknown_list, duplicates_list
        )

        return len(unknown_list), len(duplicates_list)

    def _write_filter_logs(
            self, config_id: int,
            unknown_list: list, duplicates_list: list,
    ):
        """Пишет в лог удалённые дубли и неизвестные команды."""
        if not unknown_list and not duplicates_list:
            return

        changes = []
        for key, value in unknown_list:
            changes.append((
                f"{key} {t('logs.type.unknown')}",
                str(value)[:200] if value else "",
                t("logs.value.removed"),
            ))
        for key, value in duplicates_list:
            changes.append((
                f"{key} {t('logs.type.duplicate')}",
                str(value)[:200] if value else "",
                t("logs.value.dup_removed"),
            ))

        if not changes:
            return

        try:
            self.repo.log_change_bulk(config_id, changes)
        except Exception as exc:
            print(f"[ConfigService] write_filter_logs failed: {exc}")

    def _populate_values_from_content(
            self, config_id: int, content: str, key_to_id: dict
    ):
        """Парсит content и заполняет ConfigValues.

        key_to_id: {key_name: command_id} — готовый словарь,
        чтобы не звать command_repo.all() заново.
        """
        if not key_to_id:
            return

        parsed: dict[str, str] = {}
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith(("--", "//", "#")):
                continue
            m = _CFG_KV_RE.match(line)
            if m:
                parsed[m.group(1)] = m.group(2)

        if not parsed:
            return

        rows = []
        for key, value in parsed.items():
            cmd_id = key_to_id.get(key)
            if cmd_id is not None:
                rows.append((cmd_id, 1, value))

        if rows:
            self.repo.save_values_bulk(config_id, rows)

    def _parse_content(self, text: str) -> dict[str, str]:
        """Парсит текст cfg в {key_name: value}."""
        parsed = {}
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith(("--", "//", "#")):
                continue
            m = _CFG_KV_RE.match(line)
            if m:
                parsed[m.group(1)] = m.group(2)
        return parsed

    def _write_content_logs(
            self, config_id: int, old_values: dict,
            cleaned_text: str, key_to_id: dict, id_to_key: dict,
    ):
        """Пишет историю изменений — bulk.

        old_values: {cmd_id: value | None}
        key_to_id / id_to_key: готовые словари.
        """
        if not key_to_id:
            return

        parsed = self._parse_content(cleaned_text)
        new_values = {}
        for key, value in parsed.items():
            cmd_id = key_to_id.get(key)
            if cmd_id is not None:
                new_values[cmd_id] = value

        all_ids = set(old_values) | set(new_values)
        changes = []

        for cmd_id in all_ids:
            old_val = old_values.get(cmd_id)
            new_val = new_values.get(cmd_id)

            old_norm = None if old_val is None else str(old_val).strip()
            new_norm = None if new_val is None else str(new_val).strip()

            if old_norm == new_norm:
                continue

            key = id_to_key.get(cmd_id)
            if key is None:
                continue

            old_display = old_norm if old_norm is not None else t("logs.value.removed")
            new_display = new_norm if new_norm is not None else t("logs.value.removed")

            changes.append((key, old_display, new_display))

        if not changes:
            return

        try:
            self.repo.log_change_bulk(config_id, changes)
        except Exception as exc:
            print(f"[ConfigService] write_logs failed: {exc}")

    def _filter_known_commands(self, text, known):
        if not known:
            return text, [], []

        # Проход 1: последнее вхождение и все предыдущие
        last_value: dict[str, str] = {}
        prev_values: dict[str, list[str]] = {}

        for line in text.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith(("--", "//", "#")):
                continue
            m = _CFG_KV_RE.match(stripped)
            if m and m.group(1) in known:
                key = m.group(1)
                if key in last_value:
                    # предыдущее вхождение — в duplicates
                    prev_m = _CFG_KV_RE.match(last_value[key].strip())
                    if prev_m:
                        prev_values.setdefault(key, []).append(
                            (key, prev_m.group(2))
                        )
                last_value[key] = line

        # Проход 2: собрать результат
        result = []
        seen = set()
        unknown_list = []
        duplicates_list = []

        for line in text.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith(("--", "//", "#")):
                result.append(line)
                continue
            m = _CFG_KV_RE.match(stripped)
            if m and m.group(1) in known:
                key = m.group(1)
                if key in seen:
                    continue  # уже обработали
                seen.add(key)
                result.append(last_value[key])
                duplicates_list.extend(prev_values.get(key, []))
            else:
                if m:
                    unknown_list.append((m.group(1), m.group(2)))
                else:
                    unknown_list.append((stripped, ""))

        return "\n".join(result), unknown_list, duplicates_list

    def _validate_name(self, name: str) -> str:
        name = name.strip()
        if not name:
            raise ValueError(t("config.error.empty_name"))
        if len(name) > MAX_CONFIG_NAME_LEN:
            raise ValueError(
                t("config.error.too_long_name").format(
                    n=MAX_CONFIG_NAME_LEN
                )
            )
        return name

    @staticmethod
    def default_name_from_path(path: str) -> str:
        """Имя файла по умолчанию (из пути)."""
        return os.path.basename(path)