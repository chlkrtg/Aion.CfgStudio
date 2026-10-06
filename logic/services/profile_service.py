"""Бизнес-логика профилей.

Все методы бросают ValueError при нарушении правил.
UI-слой сам решает, как показать ошибку.
"""
from logic.constants import (
    MAX_PROFILE_NAME_LEN,
    MAX_DESCRIPTION_LEN,
)


class ProfileService:
    """Правила и валидация для профилей."""

    def __init__(self, repo):
        self.repo = repo

    # =========== создание ===========

    def create(self, name: str) -> int:
        """Создаёт профиль. Возвращает id.

        Raises:
            ValueError: имя пустое, слишком длинное или занято.
        """
        name = self._validate_name(name)
        if any(p["name"] == name for p in self.repo.all()):
            raise ValueError(f"Профиль «{name}» уже существует.")
        return self.repo.create(name)

    # =========== переименование ===========

    def rename(self, profile_id: int, new_name: str):
        """Переименовывает профиль.

        Raises:
            ValueError: профиль не найден или имя занято.
        """
        new_name = self._validate_name(new_name)

        profile = self.repo.get(profile_id)
        if not profile:
            raise ValueError("Профиль не найден.")

        if profile["name"] == new_name:
            return  # ничего не меняем

        if any(
            p["name"] == new_name and p["id"] != profile_id
            for p in self.repo.all()
        ):
            raise ValueError(f"Профиль «{new_name}» уже существует.")

        self.repo.rename(profile_id, new_name)

    # =========== удаление ===========

    def delete(self, profile_id: int):
        """Удаляет профиль со всем содержимым."""
        self.repo.delete(profile_id)

    # =========== описание ===========

    def update_description(self, profile_id: int, text: str):
        """Сохраняет описание с обрезкой до MAX_DESCRIPTION_LEN."""
        if len(text) > MAX_DESCRIPTION_LEN:
            text = text[:MAX_DESCRIPTION_LEN]
        self.repo.update_description(profile_id, text)

    # =========== дублирование ===========

    def duplicate(self, profile_id: int, new_name: str) -> int:
        """Дублирует профиль со всем содержимым.

        Raises:
            ValueError: имя пустое или занято.
        """
        new_name = self._validate_name(new_name)
        if any(p["name"] == new_name for p in self.repo.all()):
            raise ValueError(f"Профиль «{new_name}» уже существует.")
        return self.repo.duplicate(profile_id, new_name)

    # =========== вспомогательное ===========

    def _validate_name(self, name: str) -> str:
        """Проверяет и нормализует имя профиля."""
        name = name.strip()
        if not name:
            raise ValueError("Имя не может быть пустым.")
        if len(name) > MAX_PROFILE_NAME_LEN:
            raise ValueError(
                f"Имя слишком длинное (макс. {MAX_PROFILE_NAME_LEN})."
            )
        return name