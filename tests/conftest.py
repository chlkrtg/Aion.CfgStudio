"""Общие фикстуры для тестов."""
import pytest


@pytest.fixture
def fake_repo():
    """In-memory репозиторий на dict."""
    class FakeRepo:
        def __init__(self):
            self._data = {}
            self._next_id = 1

        def create(self, *args, **kwargs):
            id_ = self._next_id
            self._next_id += 1
            data = {"id": id_}

            if len(args) == 1:
                # ProfileService.create(name)
                data["name"] = args[0]
            elif len(args) == 3:
                # ConfigService.create_from_content(server_id, name, content)
                data["server_id"] = args[0]
                data["filename"] = args[1]
                data["content"] = args[2]
            elif len(args) == 2:
                # ServerService.create(profile_id, name)
                data["profile_id"] = args[0]
                data["name"] = args[1]

            data.update(kwargs)
            self._data[id_] = data
            return id_

        def get(self, id_):
            return self._data.get(id_)

        def all(self):
            return list(self._data.values())

        def delete(self, id_):
            self._data.pop(id_, None)

        def rename(self, id_, new_name):
            if id_ in self._data:
                if "filename" in self._data[id_]:
                    self._data[id_]["filename"] = new_name
                else:
                    self._data[id_]["name"] = new_name

        def duplicate(self, id_, new_name):
            """Дублирует запись."""
            if id_ not in self._data:
                raise ValueError("Исходная запись не найдена")
            new_id = self._next_id
            self._next_id += 1
            import copy
            new_data = copy.deepcopy(self._data[id_])
            new_data["id"] = new_id
            new_data["name"] = new_name
            self._data[new_id] = new_data
            return new_id

    return FakeRepo()

def test_create_profile(db):
    from logic.repositories import ProfileRepository
    repo = ProfileRepository(db)
    pid = repo.create("Test")
    assert repo.get(pid)["name"] == "Test"


def test_delete_profile_cascades(db):
    from logic.repositories import ConfigRepository, ProfileRepository, ServerRepository
    profile_repo = ProfileRepository(db)
    server_repo = ServerRepository(db)
    config_repo = ConfigRepository(db)

    pid = profile_repo.create("Test")
    sid = server_repo.create(pid, "Server")
    cid = config_repo.create(sid, "system.cfg", "content")

    profile_repo.delete(pid)
    assert server_repo.get(sid) is None
    assert config_repo.get(cid) is None