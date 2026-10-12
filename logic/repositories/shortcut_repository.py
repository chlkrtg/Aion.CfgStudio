"""Репозиторий хоткеев.

Тонкая обёртка над DBManager. Только доступ к БД.
"""


class ShortcutRepository:
    """Репозиторий override'ов хоткеев."""

    def __init__(self, db):
        self.db = db

    # ============== чтение ==============

    def all(self):
        """Все override'ы: список sqlite3.Row с полями action_id, key."""
        return self.db.list_shortcuts()

    # ============== запись ==============

    def upsert(self, action_id: str, key: str):
        """Сохраняет override (INSERT или UPDATE)."""
        self.db.upsert_shortcut(action_id, key)

    def delete(self, action_id: str):
        """Удаляет override, действие вернётся к дефолту."""
        self.db.delete_shortcut(action_id)

    def delete_all(self):
        """Удаляет ВСЕ override, сброс к дефолтам."""
        self.db.delete_all_shortcuts()