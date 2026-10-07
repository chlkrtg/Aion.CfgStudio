"""Репозиторий команд и префиксов.

Единая точка доступа к справочникам.
"""


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
        return self.db.list_commands(mode)

    def prefixes(self):
        """Все префиксы (категории команд)."""
        return self.db.list_prefixes()

    def video_chapters(self):
        """Все главы видео-руководства."""
        return self.db.list_video_chapters()