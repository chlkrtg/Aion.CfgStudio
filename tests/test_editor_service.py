from unittest.mock import MagicMock

from logic.services.editor_service import EditorService


def test_load_local_overrides_no_server_repo():
    service = EditorService(MagicMock(), MagicMock(), MagicMock())
    assert service.load_local_overrides(1) == {}


def test_load_local_overrides_no_server():
    server_repo = MagicMock()
    server_repo.get.return_value = None
    service = EditorService(MagicMock(), MagicMock(), MagicMock(), server_repo=server_repo)
    assert service.load_local_overrides(1) == {}


def test_collect_content():
    service = EditorService(MagicMock(), MagicMock())
    content = service.collect_content({"e_beach": "0", "g_maxfov": "60"})
    assert 'e_beach = "0"' in content
    assert 'g_maxfov = "60"' in content
    assert content.startswith("-- [System-Configuration")


def test_ensure_config_update():
    config_repo = MagicMock()
    service = EditorService(config_repo, MagicMock())
    service.ensure_config(5, 1, "system.cfg", "content")
    config_repo.update.assert_called_once_with(5, "content")


def test_ensure_config_create():
    config_repo = MagicMock()
    config_service = MagicMock()
    config_service.create_from_content.return_value = 42
    service = EditorService(config_repo, MagicMock(), config_service)
    result = service.ensure_config(None, 1, "system.cfg", "content")
    assert result == 42
    config_service.create_from_content.assert_called_once_with(1, "system.cfg", "content")

def test_saved_values():
    config_repo = MagicMock()
    config_repo.values.return_value = [
        {"command_id": 1, "use_custom": 1, "custom_value": "0"},
        {"command_id": 2, "use_custom": 0, "custom_value": None},
    ]
    service = EditorService(config_repo, MagicMock())
    result = service.saved_values(1)
    assert result == {1: (1, "0"), 2: (0, None)}


def test_make_defaults():
    command_repo = MagicMock()
    service = EditorService(MagicMock(), command_repo)
    service.make_defaults([(1, "0"), (2, "60")])
    command_repo.update_defaults.assert_called_once_with([(1, "0"), (2, "60")])


def test_write_logs():
    config_repo = MagicMock()
    service = EditorService(config_repo, MagicMock())
    service.write_logs(1, [("e_beach", "0", "1")])
    config_repo.log_change_bulk.assert_called_once_with(1, [("e_beach", "0", "1")])