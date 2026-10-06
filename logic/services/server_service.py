"""Бизнес-логика серверов.

Все методы бросают ValueError при нарушении правил.
"""
from logic.constants import MAX_SERVER_NAME_LEN, MAX_NOTE_LEN


class ServerService:
    """Правила и валидация для серверов."""

    def __init__(self, repo):
        self.repo = repo

    # =========== создание ===========

    def create(self, profile_id: int, name: str) -> int:
        """Создаёт сервер в профиле.

        Raises:
            ValueError: имя пустое, слишком длинное или занято
                        в этом профиле.
        """
        name = self._validate_name(name)
        if any(
            s["name"] == name
            for s in self.repo.all_for_profile(profile_id)
        ):
            raise ValueError(
                f"Сервер «{name}» уже существует в этом профиле."
            )
        return self.repo.create(profile_id, name)

    # =========== переименование ===========

    def rename(self, server_id: int, new_name: str, profile_id: int):
        """Переименовывает сервер.

        profile_id нужен, чтобы проверить уникальность имени
        внутри профиля.

        Raises:
            ValueError: сервер не найден или имя занято.
        """
        new_name = self._validate_name(new_name)

        server = self.repo.get(server_id)
        if not server:
            raise ValueError("Сервер не найден.")

        if server["name"] == new_name:
            return

        if any(
            s["name"] == new_name and s["id"] != server_id
            for s in self.repo.all_for_profile(profile_id)
        ):
            raise ValueError(
                f"Сервер «{new_name}» уже существует в этом профиле."
            )

        self.repo.rename(server_id, new_name)

    # =========== заметка ===========

    def update_note(self, server_id: int, text: str):
        """Сохраняет заметку с обрезкой до MAX_NOTE_LEN."""
        if len(text) > MAX_NOTE_LEN:
            text = text[:MAX_NOTE_LEN]
        self.repo.update_note(server_id, text)

    # =========== удаление / дублирование ===========

    def delete(self, server_id: int):
        self.repo.delete(server_id)

    def duplicate(self, server_id: int, new_name: str,
                  profile_id: int) -> int:
        """Дублирует сервер со всем содержимым.

        Raises:
            ValueError: имя пустое или занято.
        """
        new_name = self._validate_name(new_name)
        if any(
            s["name"] == new_name
            for s in self.repo.all_for_profile(profile_id)
        ):
            raise ValueError(
                f"Сервер «{new_name}» уже существует."
            )
        return self.repo.duplicate(server_id, new_name)

    # =========== вспомогательное ===========

    def _validate_name(self, name: str) -> str:
        name = name.strip()
        if not name:
            raise ValueError("Имя не может быть пустым.")
        if len(name) > MAX_SERVER_NAME_LEN:
            raise ValueError(
                f"Имя слишком длинное (макс. {MAX_SERVER_NAME_LEN})."
            )
        return name