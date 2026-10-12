"""Бизнес-логика хоткеев.

Сервис знает о реестре действий (ACTIONS) и о репозитории.
Не знает о Qt и о страницах.
"""
from logic.actions import ACTIONS, Scope


class ShortcutService:
    """Правила для хоткеев: merge с дефолтами, конфликты, override'ы."""

    def __init__(self, repo):
        self.repo = repo
        self._overrides: dict[str, str] = {}
        self._load()

    # ============ загрузка ============

    def _load(self):
        """Читает override'ы из БД и фильтрует по актуальному реестру."""
        self._overrides = {
            row["action_id"]: row["key"]
            for row in self.repo.all()
            if row["action_id"] in ACTIONS
        }

    # ============ чтение ============

    def current_key(self, action_id: str) -> str:
        """Клавиша действия: override из БД или дефолт из реестра."""
        return self._overrides.get(
            action_id, ACTIONS[action_id].default_key
        )

    def keys_for_scope(self, scope: str) -> dict[str, str]:
        """Override'ы для страницы: GLOBAL + указанный scope.

        Возвращает только реально переопределённые действия.
        Дефолты подставит bind_action.
        """
        scope_enum = Scope(scope)
        result = {}
        for action_id, key in self._overrides.items():
            action = ACTIONS[action_id]
            if action.scope in (scope_enum, Scope.GLOBAL):
                result[action_id] = key
        return result

    # ============ запись ============

    def set_key(self, action_id: str, key: str):
        """Сохраняет override.

        Если key совпадает с дефолтом, override удаляется.
        """
        action = ACTIONS[action_id]
        if key == action.default_key:
            self.repo.delete(action_id)
            self._overrides.pop(action_id, None)
        else:
            self.repo.upsert(action_id, key)
            self._overrides[action_id] = key

    def reset_key(self, action_id: str):
        """Сбрасывает одно действие к дефолту."""
        self.repo.delete(action_id)
        self._overrides.pop(action_id, None)

    def reset_all(self):
        """Сбрасывает все override'ы."""
        self.repo.delete_all()
        self._overrides.clear()

    # ============ конфликты ============

    def find_conflict(self, action_id: str, key: str) -> str | None:
        """Ищет действие в том же scope с такой же клавишей.

        Возвращает action_id конфликтующего действия или None.
        Дефолты тоже учитываются.
        """
        target = ACTIONS[action_id]
        for other_id, other in ACTIONS.items():
            if other_id == action_id:
                continue
            if not self._scopes_overlap(target.scope, other.scope):
                continue
            if self.current_key(other_id) == key:
                return other_id
        return None

    @staticmethod
    def _scopes_overlap(a: Scope, b: Scope) -> bool:
        """GLOBAL пересекается со всеми, остальные - только сами с собой."""
        if a == Scope.GLOBAL or b == Scope.GLOBAL:
            return True
        return a == b