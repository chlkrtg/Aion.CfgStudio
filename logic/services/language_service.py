"""Сервис текущего языка приложения.

Тонкий: хранит код языка, синхронизирует с БД и с i18n.
"""
from logic.core import i18n


SETTING_KEY = "language"
DEFAULT_LANG = "ru"


class LanguageService:
    """Текущий язык приложения."""

    def __init__(self, repo):
        self.repo = repo

        # читаем из БД, падаем на дефолт при отсутствии
        saved = repo.get(SETTING_KEY, DEFAULT_LANG)
        if saved not in i18n.AVAILABLE_LANGUAGES:
            saved = DEFAULT_LANG

        self._lang = saved
        i18n.set_language(self._lang)

    # ============ чтение ============

    @property
    def current(self) -> str:
        """Текущий код языка: 'ru' или 'en'."""
        return self._lang

    # ============ запись ============

    def set(self, lang: str) -> bool:
        if lang not in i18n.AVAILABLE_LANGUAGES:
            return False
        if lang == self._lang:
            return False

        self._lang = lang
        i18n.set_language(lang)
        self.repo.set(SETTING_KEY, lang)
        return True