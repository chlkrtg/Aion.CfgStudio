"""Репозиторий конфигурационных файлов.

Единая точка доступа к cfg и их значениям.
"""


class ConfigRepository:
    """Репозиторий cfg."""

    def __init__(self, db):
        self.db = db

    # ============== чтение ==============

    def all_for_server(self, server_id: int):
        """Все cfg внутри сервера."""
        return self.db.list_configs(server_id)

    def get(self, config_id: int):
        """Один cfg по id."""
        return self.db.get_config(config_id)

    def values(self, config_id: int):
        """Все значения команд в cfg (ConfigValues)."""
        return self.db.list_config_values(config_id)

    def logs(self, config_id: int):
        """История изменений cfg."""
        return self.db.list_logs(config_id)

    # ============== запись ==============

    def create(self, server_id: int, filename: str, content: str) -> int:
        """Создаёт cfg. Возвращает id."""
        return self.db.create_config(server_id, filename, content)

    def update(self, config_id: int, content: str):
        """Обновляет содержимое и modified_at."""
        self.db.update_config(config_id, content)

    def rename(self, config_id: int, new_name: str):
        self.db.rename_config(config_id, new_name)

    def delete(self, config_id: int):
        """Удаляет cfg с значениями и логами (каскад)."""
        self.db.delete_config(config_id)

    def duplicate(self, config_id: int, new_name: str) -> int:
        """Дублирует cfg с значениями."""
        return self.db.duplicate_config(config_id, new_name)

    def save_values_bulk(self, config_id: int, values: list):
        """Массовое сохранение значений.

        values: [(command_id, use_custom, custom_value), ...]
        """
        self.db.save_config_values_bulk(config_id, values)

    def log_change(self, config_id: int, key: str, old: str, new: str):
        """Запись в историю изменений."""
        self.db.log_change(config_id, key, old, new)