"""Тесты локализации."""
from logic.core import i18n


def test_plural_ru_one():
    assert i18n.plural_ru(1, "команда", "команды", "команд") == "команда"


def test_plural_ru_few():
    assert i18n.plural_ru(2, "команда", "команды", "команд") == "команды"
    assert i18n.plural_ru(4, "команда", "команды", "команд") == "команды"


def test_plural_ru_many():
    assert i18n.plural_ru(5, "команда", "команды", "команд") == "команд"
    assert i18n.plural_ru(11, "команда", "команды", "команд") == "команд"
    assert i18n.plural_ru(21, "команда", "команды", "команд") == "команда"


def test_set_language():
    i18n.set_language("en")
    assert i18n.get_language() == "en"
    assert i18n.t("menu.file") == "File"

    i18n.set_language("ru")
    assert i18n.get_language() == "ru"
    assert i18n.t("menu.file") == "Файл"


def test_set_language_unknown():
    i18n.set_language("ru")
    i18n.set_language("de")  # неизвестный
    assert i18n.get_language() == "ru"  # не изменилось


def test_t_missing_key():
    assert i18n.t("nonexistent.key") == "nonexistent.key"