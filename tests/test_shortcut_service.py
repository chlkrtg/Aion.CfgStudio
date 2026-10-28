"""Тесты ShortcutService (конфликты, override'ы, extra_keys)."""

import pytest

from logic.services.shortcut_service import ShortcutService


@pytest.fixture
def repo():
    """Фейковый репозиторий override'ов."""
    class FakeRepo:
        def __init__(self):
            self._data = {}

        def all(self):
            return [{"action_id": k, "key": v}
                    for k, v in self._data.items()]

        def upsert(self, action_id, key):
            self._data[action_id] = key

        def delete(self, action_id):
            self._data.pop(action_id, None)

        def delete_all(self):
            self._data.clear()

    return FakeRepo()


@pytest.fixture
def service(repo):
    return ShortcutService(repo)


def test_default_key(service):
    assert service.current_key("main.open") == "Ctrl+E"


def test_set_key(service):
    service.set_key("main.open", "Ctrl+Shift+E")
    assert service.current_key("main.open") == "Ctrl+Shift+E"
    assert service.has_override("main.open")


def test_reset_key(service):
    service.set_key("main.open", "Ctrl+Shift+E")
    service.reset_key("main.open")
    assert service.current_key("main.open") == "Ctrl+E"
    assert not service.has_override("main.open")


def test_set_key_removes_override_if_matches_default(service):
    service.set_key("main.open", "Ctrl+Shift+E")
    service.set_key("main.open", "Ctrl+E")  # вернули дефолт
    assert not service.has_override("main.open")


def test_conflict_detected(service):
    # main.open по умолчанию Ctrl+E, попробуем назначить его на main.create
    with pytest.raises(ValueError, match="уже занята"):
        service.set_key("main.create", "Ctrl+E")


def test_conflict_with_extra_keys(service):
    # profile.enter имеет default_key="Return", extra_keys=("Enter",)
    # Попытка назначить "Enter" на profile.create должна быть конфликтом
    with pytest.raises(ValueError, match="уже занята"):
        service.set_key("profile.create", "Enter")


def test_reset_all(service):
    service.set_key("main.open", "Ctrl+Shift+E")
    service.set_key("main.create", "Ctrl+Shift+N")
    service.reset_all()
    assert not service.has_override("main.open")
    assert not service.has_override("main.create")


def test_keys_for_scope(service):
    service.set_key("main.open", "Ctrl+Shift+E")
    keys = service.keys_for_scope("main")
    assert "main.open" in keys
    assert keys["main.open"] == "Ctrl+Shift+E"

def test_is_modifier_only(service):
    assert service._is_modifier_only("Shift")
    assert service._is_modifier_only("Ctrl+Shift")
    assert not service._is_modifier_only("Ctrl+A")
    assert not service._is_modifier_only("A")