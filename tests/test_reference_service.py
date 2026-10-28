from unittest.mock import MagicMock

from logic.services.reference_service import ReferenceService


def test_get_profile_name():
    profile_repo = MagicMock()
    profile_repo.get.return_value = {"name": "Test"}
    service = ReferenceService(profile_repo, MagicMock(), MagicMock())
    assert service.get_profile_name(1) == "Test"


def test_get_profile_name_not_found():
    profile_repo = MagicMock()
    profile_repo.get.return_value = None
    service = ReferenceService(profile_repo, MagicMock(), MagicMock())
    assert service.get_profile_name(1) is None


def test_get_server_name():
    server_repo = MagicMock()
    server_repo.get.return_value = {"name": "Server"}
    service = ReferenceService(MagicMock(), server_repo, MagicMock())
    assert service.get_server_name(1) == "Server"


def test_get_server_export_path():
    server_repo = MagicMock()
    server_repo.get.return_value = {"export_path": "C:\\EuroAion"}
    service = ReferenceService(MagicMock(), server_repo, MagicMock())
    assert service.get_server_export_path(1) == "C:\\EuroAion"


def test_get_server_export_path_none():
    service = ReferenceService(MagicMock(), MagicMock(), MagicMock())
    assert service.get_server_export_path(None) == ""