"""Репозитории для доступа к БД.

Репозиторий - это «обёртка» над DBManager, которая предоставляет
удобный интерфейс для конкретной сущности (профиль, сервер, cfg).
"""
from logic.repositories.profile_repository import ProfileRepository
from logic.repositories.server_repository import ServerRepository
from logic.repositories.config_repository import ConfigRepository
from logic.repositories.command_repository import CommandRepository

__all__ = [
    "ProfileRepository",
    "ServerRepository",
    "ConfigRepository",
    "CommandRepository",
]