"""Бизнес-логика конфигурационных файлов.

Импорт / экспорт, CRUD cfg, парсинг content -> ConfigValues.
Не знает о Qt.
"""
import os
import re

from logic.constants import MAX_CONFIG_NAME_LEN
from parsers.cfg_crypto import (
    decrypt, encrypt, looks_like_encrypted,
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
            raise ValueError("Конфиг не найден.")

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

    def _validate_name(self, name: str) -> str:
        name = name.strip()
        if not name:
            raise ValueError("Имя файла не может быть пустым.")
        if len(name) > MAX_CONFIG_NAME_LEN:
            raise ValueError(
                f"Имя слишком длинное (макс. {MAX_CONFIG_NAME_LEN})."
            )
        return name

    @staticmethod
    def default_name_from_path(path: str) -> str:
        """Имя файла по умолчанию (из пути)."""
        return os.path.basename(path)