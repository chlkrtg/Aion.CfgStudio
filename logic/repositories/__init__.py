"""Репозитории для доступа к БД.

Репозиторий - это «обёртка» над DBManager, которая предоставляет
удобный интерфейс для конкретной сущности (профиль, сервер, cfg).
"""
from logic.repositories.command_repository import CommandRepository
from logic.repositories.config_repository import ConfigRepository
from logic.repositories.profile_repository import ProfileRepository
from logic.repositories.server_repository import ServerRepository
from logic.repositories.settings_repository import SettingsRepository
from logic.repositories.shortcut_repository import ShortcutRepository

__all__ = [
    "CommandRepository",
    "ConfigRepository",
    "ProfileRepository",
    "ServerRepository",
    "SettingsRepository",
    "ShortcutRepository",
]