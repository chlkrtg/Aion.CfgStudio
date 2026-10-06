"""Репозиторий профилей.

Единая точка доступа к профилям в БД.
Все SQL-запросы идут через DBManager, а репозиторий лишь
предоставляет удобный интерфейс для конкретной сущности.
"""


class ProfileRepository:
    """Репозиторий профилей."""

    def __init__(self, db):
        """Принимает DBManager."""
        self.db = db

    # =============== чтение ===============

    def all(self):
        """Все профили (список sqlite3.Row)."""
        return self.db.list_profiles()

    def get(self, profile_id: int):
        """Один профиль по id (или None)."""
        return self.db.get_profile(profile_id)

    def count_servers(self, profile_id: int) -> int:
        """Сколько серверов внутри профиля."""
        return self.db.count_servers(profile_id)

    def count_configs(self, profile_id: int) -> int:
        """Сколько cfg внутри профиля (через все серверы)."""
        return self.db.count_configs(profile_id)

    # =============== запись ===============

    def create(self, name: str, description: str = "") -> int:
        """Создаёт профиль. Возвращает id."""
        return self.db.create_profile(name, description)

    def rename(self, profile_id: int, new_name: str):
        """Переименовывает профиль."""
        self.db.rename_profile(profile_id, new_name)

    def update_description(self, profile_id: int, text: str):
        """Обновляет описание профиля."""
        self.db.update_profile_description(profile_id, text)

    def delete(self, profile_id: int):
        """Удаляет профиль со всем содержимым (каскад)."""
        self.db.delete_profile(profile_id)

    def duplicate(self, profile_id: int, new_name: str) -> int:
        """Дублирует профиль со всем содержимым. Возвращает id копии."""
        return self.db.duplicate_profile(profile_id, new_name)