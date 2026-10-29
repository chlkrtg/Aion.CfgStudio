"""Константы приложения: ограничения по длине и конфигурация."""
from importlib.metadata import PackageNotFoundError, version

# =================== Ограничения длины ===================
MAX_PROFILE_NAME_LEN = 32
MAX_SERVER_NAME_LEN = 32
MAX_CONFIG_NAME_LEN = 32
MAX_DESCRIPTION_LEN = 256
MAX_NOTE_LEN = 256
MAX_CFG_SIZE = 10 * 1024 * 1024  # 10 МБ (с запасом)

# =================== Приложение ===================
APP_NAME = "Aion.CfgStudio"

try:
    APP_VERSION = version("aion-cfgstudio")
except PackageNotFoundError:
    APP_VERSION = "0.0.0-dev"