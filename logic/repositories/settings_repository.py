"""Репозиторий настроек приложения (key-value)."""

class SettingsRepository:
    def __init__(self, db):
        self.db = db

    def get(self, key: str, default: str | None = None) -> str | None:
        return self.db.get_setting(key, default)

    def set(self, key: str, value: str):
        self.db.set_setting(key, value)

    def delete(self, key: str):
        self.db.delete_setting(key)