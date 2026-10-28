
import pytest

from logic.services.language_service import LanguageService


@pytest.fixture
def repo():
    class FakeRepo:
        def __init__(self):
            self._data = {}
        def get(self, key, default=None):
            return self._data.get(key, default)
        def set(self, key, value):
            self._data[key] = value
    return FakeRepo()


def test_default_language(repo):
    service = LanguageService(repo)
    assert service.current == "ru"


def test_set_language(repo):
    service = LanguageService(repo)
    assert service.set("en") is True
    assert service.current == "en"


def test_set_same_language(repo):
    service = LanguageService(repo)
    assert service.set("ru") is False  # уже ru


def test_set_unknown_language(repo):
    service = LanguageService(repo)
    assert service.set("de") is False
    assert service.current == "ru"