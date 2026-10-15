"""Простейшая локализация: словарь + t()."""

CURRENT = "ru"

STRINGS = {
    "ru": {
        "menu.lang":    "Язык",
        "menu.lang.ru": "Русский",
        "menu.lang.en": "English",
    },
    "en": {
        "menu.lang":    "Language",
        "menu.lang.ru": "Русский",
        "menu.lang.en": "English",
    },
}

AVAILABLE_LANGUAGES = ("ru", "en")


def set_language(lang: str) -> None:
    global CURRENT
    if lang in STRINGS:
        CURRENT = lang


def get_language() -> str:
    return CURRENT


def t(key: str) -> str:
    return STRINGS.get(CURRENT, {}).get(key, key)