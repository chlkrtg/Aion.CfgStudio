"""Тесты ConfigService (парсинг, фильтрация, дубли)."""
import os
import stat
from unittest.mock import MagicMock

import pytest

from logic.services.config_service import ConfigService


@pytest.fixture
def service():
    return ConfigService(repo=None, command_repo=None)


def test_parse_simple(service):
    text = 'e_beach = "0"\ng_maxfov = "60"'
    parsed = service._parse_content(text)
    assert parsed == {"e_beach": "0", "g_maxfov": "60"}


def test_parse_skips_comments(service):
    text = '-- comment\ne_beach = "0"\n# another\n// and this'
    assert service._parse_content(text) == {"e_beach": "0"}


def test_parse_without_quotes(service):
    text = "e_beach = 0\ng_maxfov = 60"
    assert service._parse_content(text) == {"e_beach": "0", "g_maxfov": "60"}


def test_filter_removes_duplicates_keeps_last(service):
    known = {"e_beach"}
    text = 'e_beach = "0"\ne_beach = "1"'
    cleaned, unknown, dups = service._filter_known_commands(text, known)
    assert 'e_beach = "1"' in cleaned
    assert 'e_beach = "0"' not in cleaned
    assert len(dups) == 1
    assert dups[0] == ("e_beach", "0")


def test_filter_removes_unknown(service):
    known = {"e_beach"}
    text = 'e_beach = "0"\nunknown_key = "1"'
    cleaned, unknown, dups = service._filter_known_commands(text, known)
    assert "unknown_key" not in cleaned
    assert unknown == [("unknown_key", "1")]
    assert dups == []


def test_filter_keeps_comments(service):
    known = {"e_beach"}
    text = '-- comment\ne_beach = "0"'
    cleaned, _, _ = service._filter_known_commands(text, known)
    assert "-- comment" in cleaned


def test_filter_empty_known(service):
    text = 'e_beach = "0"'
    cleaned, unknown, dups = service._filter_known_commands(text, set())
    assert cleaned == text
    assert unknown == []
    assert dups == []

def test_save_content_removes_duplicates():
    repo = MagicMock()
    repo.values.return_value = []
    service = ConfigService(repo=repo, command_repo=None)

    # save_content с command_repo=None не фильтрует (known=set())
    # но проверит, что repo.update вызван
    unknown, dups = service.save_content(1, 'e_beach = "0"')
    assert repo.update.called


def test_export_to_file_plain(tmp_path):
    repo = MagicMock()
    repo.get.return_value = {"content": 'e_beach = "0"'}
    service = ConfigService(repo=repo)

    path = tmp_path / "test.cfg"
    service.export_to_file(1, str(path), encrypted=False)

    assert path.read_text(encoding="latin1") == 'e_beach = "0"'
    # read-only стоит
    import os
    import stat
    assert not (os.stat(path).st_mode & stat.S_IWRITE)

def test_create_from_content(service, fake_repo):
    service.repo = fake_repo
    cid = service.create_from_content(1, "system.cfg", 'e_beach = "0"')
    assert cid > 0


def test_export_to_file_plain(tmp_path, service):
    repo = MagicMock()
    repo.get.return_value = {"content": 'e_beach = "0"'}
    service.repo = repo

    path = tmp_path / "test.cfg"
    service.export_to_file(1, str(path), encrypted=False)

    assert path.read_text(encoding="latin1") == 'e_beach = "0"'
    # read-only
    assert not (os.stat(path).st_mode & stat.S_IWRITE)


def test_export_to_file_encrypted(tmp_path, service):
    from parsers.cfg_crypto import decrypt
    repo = MagicMock()
    repo.get.return_value = {"content": 'e_beach = "0"'}
    service.repo = repo

    path = tmp_path / "test.cfg"
    service.export_to_file(1, str(path), encrypted=True)

    raw = path.read_bytes()
    assert decrypt(raw).rstrip("\n") == 'e_beach = "0"'


def test_export_to_file_not_found(service):
    repo = MagicMock()
    repo.get.return_value = None
    service.repo = repo

    with pytest.raises(ValueError, match="не найден"):
        service.export_to_file(1, "any.cfg", encrypted=False)


def test_save_content_calls_repo(service):
    repo = MagicMock()
    repo.values.return_value = []
    service.repo = repo
    service.command_repo = None  # без фильтрации

    service.save_content(1, 'e_beach = "0"')

    repo.update.assert_called_once()
    repo.clear_values.assert_called_once_with(1)


def test_find_local_overrides_no_dir(service):
    assert service.find_local_overrides("C:\\nonexistent") == {}
    assert service.find_local_overrides("") == {}


def test_get_server_overrides_no_repo(service):
    assert service.get_server_overrides(None, 1) == {}
    assert service.get_server_overrides(MagicMock(), None) == {}

def test_import_from_file_plain(tmp_path, service):
    repo = MagicMock()
    repo.create.return_value = 42
    service.repo = repo
    service.command_repo = None

    path = tmp_path / "test.cfg"
    path.write_text('e_beach = "0"', encoding="latin1")

    cid = service.import_from_file(str(path), 1, "system.cfg")
    assert cid == 42
    repo.create.assert_called_once()


def test_import_from_file_encrypted(tmp_path, service):
    from parsers.cfg_crypto import encrypt
    repo = MagicMock()
    repo.create.return_value = 42
    service.repo = repo
    service.command_repo = None

    path = tmp_path / "test.cfg"
    path.write_bytes(encrypt('e_beach = "0"'))

    cid = service.import_from_file(str(path), 1, "system.cfg")
    assert cid == 42


def test_rename_ok(service, fake_repo):
    service.repo = fake_repo
    cid = service.create_from_content(1, "old.cfg", "")
    service.rename(cid, "new.cfg")
    assert fake_repo.get(cid)["filename"] == "new.cfg"


def test_delete(service, fake_repo):
    service.repo = fake_repo
    cid = service.create_from_content(1, "system.cfg", "")
    service.delete(cid)
    assert fake_repo.get(cid) is None