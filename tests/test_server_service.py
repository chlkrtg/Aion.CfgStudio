"""Тесты ServerService (валидация, создание, переименование, экспорт)."""
from unittest.mock import MagicMock

import pytest

from logic.services.server_service import ServerService


@pytest.fixture
def repo():
    """Мок репозитория серверов."""
    repo = MagicMock()
    repo.all_for_profile.return_value = []
    return repo


@pytest.fixture
def service(repo):
    return ServerService(repo)


# ============ create ============

def test_create_empty_name(service):
    with pytest.raises(ValueError, match="не может быть пустым"):
        service.create(1, "")


def test_create_too_long(service):
    with pytest.raises(ValueError, match="слишком длинное"):
        service.create(1, "x" * 100)


def test_create_ok(service, repo):
    repo.create.return_value = 42
    sid = service.create(1, "Test")
    assert sid == 42
    repo.create.assert_called_once_with(1, "Test")


def test_create_duplicate(service, repo):
    repo.all_for_profile.return_value = [{"name": "Test"}]
    with pytest.raises(ValueError, match="уже существует"):
        service.create(1, "Test")


# ============ rename ============

def test_rename_not_found(service, repo):
    repo.get.return_value = None
    with pytest.raises(ValueError, match="не найден"):
        service.rename(999, "New", 1)


def test_rename_ok(service, repo):
    repo.get.return_value = {"id": 1, "name": "Old"}
    repo.all_for_profile.return_value = [{"id": 1, "name": "Old"}]
    service.rename(1, "New", 1)
    repo.rename.assert_called_once_with(1, "New")


# ============ update_export_path ============

def test_update_export_path_invalid(service):
    with pytest.raises(ValueError, match="не найдена"):
        service.update_export_path(1, "C:\\nonexistent\\folder")


def test_update_export_path_empty(service, repo):
    # пустой путь — валиден (сбрасывает)
    service.update_export_path(1, "")
    repo.update_export_path.assert_called_once_with(1, "")


def test_update_export_path_ok(service, repo, tmp_path):
    # tmp_path — временная папка, которая точно существует
    service.update_export_path(1, str(tmp_path))
    repo.update_export_path.assert_called_once_with(1, str(tmp_path))


# ============ delete ============

def test_delete(service, repo):
    service.delete(1)
    repo.delete.assert_called_once_with(1)


# ============ duplicate ============

def test_duplicate_ok(service, repo):
    repo.all_for_profile.return_value = []
    repo.duplicate.return_value = 99
    new_id = service.duplicate(1, "Copy", 1)
    assert new_id == 99


def test_duplicate_exists(service, repo):
    repo.all_for_profile.return_value = [{"name": "Copy"}]
    with pytest.raises(ValueError, match="уже существует"):
        service.duplicate(1, "Copy", 1)