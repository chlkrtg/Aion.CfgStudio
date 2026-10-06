"""Репозиторий серверов.

Единая точка доступа к серверам в БД.
"""


class ServerRepository:
    """Репозиторий серверов."""

    def __init__(self, db):
        self.db = db

    # ============== чтение ==============

    def all_for_profile(self, profile_id: int):
        """Все серверы внутри профиля."""
        return self.db.list_servers(profile_id)

    def get(self, server_id: int):
        """Один сервер по id."""
        return self.db.get_server(server_id)

    def count_configs(self, server_id: int) -> int:
        """Сколько cfg внутри сервера."""
        return self.db.count_configs_in_server(server_id)

    # ============== запись ==============

    def create(self, profile_id: int, name: str) -> int:
        """Создаёт сервер в профиле. Возвращает id."""
        return self.db.create_server(profile_id, name)

    def rename(self, server_id: int, new_name: str):
        self.db.rename_server(server_id, new_name)

    def update_note(self, server_id: int, note: str):
        """Обновляет заметку сервера."""
        self.db.update_server_note(server_id, note)

    def delete(self, server_id: int):
        """Удаляет сервер со всеми cfg (каскад)."""
        self.db.delete_server(server_id)

    def duplicate(self, server_id: int, new_name: str) -> int:
        """Дублирует сервер со всем содержимым."""
        return self.db.duplicate_server(server_id, new_name)