"""Presenter для редактора хоткеев.

Логика диалога: загрузка дерева действий по секциям scope,
изменение / сброс клавиш, обработка конфликтов.

Не знает о Qt-виджетах напрямую - только зовёт методы View.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QTreeWidgetItem

from logic.actions import ACTIONS, Scope, by_scope
from logic.presenters.base_presenter import BasePresenter


# Отображаемые имена секций (в порядке показа)
SCOPE_TITLES = [
    (Scope.GLOBAL,  "Глобальные"),
    (Scope.PROFILE, "Профили"),
    (Scope.SERVER,  "Серверы"),
    (Scope.MAIN,    "Cfg-файлы"),
    (Scope.EDITOR,  "Редактор"),
    # Scope.VIDEO - пока не показываем: actions не зарегистрированы
]


EMPTY_MARK = "—"


class ShortcutPresenter(BasePresenter):
    """Логика диалога редактора хоткеев."""

    def __init__(self, view, service):
        super().__init__(view)
        self.service = service

        # {action_id: QTreeWidgetItem} - чтобы быстро находить строку
        self._items: dict[str, QTreeWidgetItem] = {}

    # ============ жизненный цикл ============

    def on_enter(self):
        """Заполняет дерево при открытии диалога."""
        self._build_tree()

    # ============ построение дерева ============

    def _build_tree(self):
        """Строит дерево: секция scope → действия."""
        view = self.view
        view.treeShortcuts.clear()
        self._items.clear()

        for scope, title in SCOPE_TITLES:
            actions = by_scope(scope)
            if not actions:
                continue

            section = QTreeWidgetItem([title, "", ""])
            section.setFirstColumnSpanned(True)
            section.setFlags(Qt.ItemFlag.ItemIsEnabled)

            font = section.font(0)
            font.setBold(True)
            section.setFont(0, font)

            view.treeShortcuts.addTopLevelItem(section)

            for action in actions:
                item = QTreeWidgetItem([
                    action.title,
                    self._display_key(action.id),
                    self._display_default(action),
                ])
                item.setData(0, Qt.ItemDataRole.UserRole, action.id)
                section.addChild(item)
                self._items[action.id] = item

            section.setExpanded(True)

    def _display_key(self, action_id: str) -> str:
        if self.service.has_override(action_id):
            return self.service.current_key(action_id) or EMPTY_MARK
        # override нет - показываем дефолт с extra_keys
        keys = ACTIONS[action_id].all_default_keys()
        return " / ".join(keys) if keys else EMPTY_MARK

    def _display_default(self, action) -> str:
        """Что показать в колонке «Дефолт»."""
        keys = action.all_default_keys()
        if not keys:
            return EMPTY_MARK
        return " / ".join(keys)

    # ============ обработка действий ============

    def current_action_id(self) -> str | None:
        """action_id выбранной строки (или None, если выбрана секция)."""
        item = self.view.treeShortcuts.currentItem()
        if item is None:
            return None
        return item.data(0, Qt.ItemDataRole.UserRole)

    def on_change(self):
        """«Изменить...» - открыть capture и сохранить клавишу."""
        action_id = self.current_action_id()
        if action_id is None:
            return

        new_key = self.view.ask_key(action_id)
        if new_key is None:
            return  # отмена

        try:
            self.service.set_key(action_id, new_key)
        except ValueError as exc:
            QMessageBox.warning(self.view, "Конфликт", str(exc))
            return

        self._refresh_row(action_id)

    def on_reset(self):
        """«Сбросить» - снять override у выбранного действия."""
        action_id = self.current_action_id()
        if action_id is None:
            return

        self.service.reset_key(action_id)
        self._refresh_row(action_id)

    def on_reset_all(self):
        """«Сбросить всё» - с подтверждением."""
        ans = QMessageBox.question(
            self.view, "Сбросить все хоткеи?",
            "Все переназначенные клавиши вернутся к значениям "
            "по умолчанию. Продолжить?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
        )
        if ans != QMessageBox.StandardButton.Yes:
            return

        self.service.reset_all()
        self._build_tree()

    # ============ обновление строки ============

    def _refresh_row(self, action_id: str):
        """Обновляет колонку «Клавиша» в строке действия."""
        item = self._items.get(action_id)
        if item is None:
            return
        item.setText(1, self._display_key(action_id))