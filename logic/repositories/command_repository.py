"""Репозиторий команд и префиксов.

Единая точка доступа к справочникам.
"""
from logic.core import i18n


class CommandRepository:
    """Репозиторий команд, префиксов и глав видео."""

    def __init__(self, db):
        self.db = db

    def all(self, mode: str = "debug"):
        """Все команды с заданным режимом.

        mode:
            "simple" - только simple
            "advanced" - simple + advanced
            "debug" - все команды
        """
        lang = i18n.get_language()
        return self.db.list_commands(mode, lang=lang)

    def prefixes(self):
        """Все префиксы (категории команд)."""
        lang = i18n.get_language()
        return self.db.list_prefixes(lang=lang)

    def update_defaults(self, updates: list):
        """updates: [(command_id, new_default_value), ...]"""
        self.db.update_command_defaults(updates)