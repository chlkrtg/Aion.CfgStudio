"""Бизнес-логика конфигурационных файлов.

Импорт / экспорт, CRUD cfg, парсинг content -> ConfigValues.
Не знает о Qt.
"""
import os
import re

from logic.core.constants import MAX_CONFIG_NAME_LEN
from parsers.cfg_crypto import (
    decrypt, encrypt, looks_like_encrypted,
)
from logic.core.i18n import t


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
        try:
            with open(path, "rb") as f:
                raw = f.read()
        except OSError:
            raise

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

    def populate_values_from_content(self, config_id: int,
                                     content: str):
        """Парсит content и заполняет ConfigValues найденными значениями.

        Работает после импорта, чтобы редактор открывался
        с уже отмеченными командами и подставленными значениями.
        """
        if self.command_repo is None:
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

        # карта key_name -> command_id
        all_commands = self.command_repo.all("debug")
        key_to_id = {c["key_name"]: c["id"] for c in all_commands}

        rows = []
        for key, value in parsed.items():
            cmd_id = key_to_id.get(key)
            if cmd_id is not None:
                rows.append((cmd_id, 1, value))

        if rows:
            self.repo.save_values_bulk(config_id, rows)

    # =========== экспорт ===========

    def export_to_file(self, config_id: int, path: str,
                       encrypted: bool):
        """Экспортирует cfg в файл.

        Raises:
            ValueError: cfg не найден.
            OSError: файл не записывается.
        """
        cfg = self.repo.get(config_id)
        if not cfg:
            raise ValueError(t("config.error.not_found"))

        content = cfg["content"] or ""
        try:
            if encrypted:
                with open(path, "wb") as f:
                    f.write(encrypt(content))
            else:
                with open(path, "w", encoding="latin1",
                          errors="replace") as f:
                    f.write(content)
        except OSError:
            raise

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

    def save_content(self, config_id: int, text: str) -> tuple[int, int]:
        """Сохраняет текст cfg + пишет историю изменений.

        Возвращает (отсечено_неизвестных, удалено_дубликатов).

        Логика:
          - старое состояние ConfigValues читается ДО сохранения
          - ConfigValues полностью очищаются, потом заполняются заново
            (это синхронизирует их с текстом cfg)
          - история пишется только для реально изменившихся значений
        """
        cleaned, unknown, duplicates = self._filter_known_commands(text)

        # 1. старое состояние ДО сохранения
        old_values = {
            row["command_id"]: row["custom_value"]
            for row in self.repo.values(config_id)
        }

        # 2. сохраняем текст
        self.repo.update(config_id, cleaned)

        # 3. очищаем ConfigValues (синхронизация с новым текстом)
        self.repo.clear_values(config_id)

        # 4. заполняем заново из очищенного текста
        self.populate_values_from_content(config_id, cleaned)

        # 5. логи: сравниваем старое и новое
        self._write_content_logs(config_id, old_values, cleaned)

        return unknown, duplicates

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

    def _write_content_logs(self, config_id: int,
                            old_values: dict, cleaned_text: str):
        """Пишет историю изменений.

        old_values: {cmd_id: value | None} — что было в ConfigValues
        cleaned_text: текст cfg после очистки
        """
        if self.command_repo is None:
            return

        # карты
        all_commands = self.command_repo.all("debug")
        key_to_id = {c["key_name"]: c["id"] for c in all_commands}
        id_to_key = {c["id"]: c["key_name"] for c in all_commands}

        # новое состояние: {cmd_id: value}
        parsed = self._parse_content(cleaned_text)
        new_values = {}
        for key, value in parsed.items():
            cmd_id = key_to_id.get(key)
            if cmd_id is not None:
                new_values[cmd_id] = value

        # сравниваем
        all_ids = set(old_values) | set(new_values)
        changes = []

        for cmd_id in all_ids:
            old_val = old_values.get(cmd_id)
            new_val = new_values.get(cmd_id)

            old_norm = (
                None if old_val is None else str(old_val).strip()
            )
            new_norm = (
                None if new_val is None else str(new_val).strip()
            )

            if old_norm == new_norm:
                continue

            key = id_to_key.get(cmd_id)
            if key is None:
                continue

            old_display = (
                old_norm if old_norm is not None else "(выключено)"
            )
            new_display = (
                new_norm if new_norm is not None else "(выключено)"
            )

            changes.append((key, old_display, new_display))

        if not changes:
            return

        try:
            for key, old, new in changes:
                self.repo.log_change(config_id, key, old, new)
        except Exception as exc:
            print(f"[ConfigService] write_logs failed: {exc}")

    def _filter_known_commands(self, text: str) -> tuple[str, int, int]:
        """Убирает из текста неизвестные команды и дубликаты.

        Возвращает (очищенный текст, отсечено_неизвестных, удалено_дубликатов).

        Логика:
          - пустые строки и комментарии (--, //, #) — оставляем
          - команды: оставляем ТОЛЬКО первое вхождение каждого ключа,
            значение берём из ПОСЛЕДНЕГО вхождения
          - неизвестные команды — отсекаем (unknown)
          - повторные вхождения известных — схлопываем (duplicates)
        """
        if self.command_repo is None:
            return text, 0, 0

        known = {c["key_name"] for c in self.command_repo.all("debug")}

        # проход 1: последнее вхождение для каждой команды
        last_value: dict[str, str] = {}
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith(("--", "//", "#")):
                continue
            m = _CFG_KV_RE.match(stripped)
            if m and m.group(1) in known:
                last_value[m.group(1)] = line

        # проход 2
        result = []
        seen = set()
        unknown = 0
        duplicates = 0

        for line in text.splitlines():
            stripped = line.strip()

            if not stripped or stripped.startswith(("--", "//", "#")):
                result.append(line)
                continue

            m = _CFG_KV_RE.match(stripped)
            if m and m.group(1) in known:
                key = m.group(1)
                if key in seen:
                    duplicates += 1
                    continue
                seen.add(key)
                result.append(last_value[key])
            else:
                unknown += 1

        return "\n".join(result), unknown, duplicates

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