"""Тесты ProfileService (валидация)."""
import pytest

from logic.services.profile_service import ProfileService


@pytest.fixture
def service(fake_repo):
    return ProfileService(fake_repo)


def test_create_empty_name(service):
    with pytest.raises(ValueError, match="не может быть пустым"):
        service.create("")


def test_create_too_long(service):
    with pytest.raises(ValueError, match="слишком длинное"):
        service.create("x" * 100)


def test_create_ok(service):
    pid = service.create("Test")
    assert pid > 0


def test_create_duplicate(service):
    service.create("Test")
    with pytest.raises(ValueError, match="уже существует"):
        service.create("Test")

def test_rename_ok(service, fake_repo):
    pid = service.create("Old")
    service.rename(pid, "New")
    assert fake_repo.get(pid)["name"] == "New"


def test_rename_not_found(service):
    with pytest.raises(ValueError, match="не найден"):
        service.rename(999, "New")


def test_delete(service, fake_repo):
    pid = service.create("Test")
    service.delete(pid)
    assert fake_repo.get(pid) is None


def test_duplicate_ok(service):
    pid = service.create("Test")
    new_id = service.duplicate(pid, "Copy")
    assert new_id != pid