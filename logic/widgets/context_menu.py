"""Хелперы для построения контекстных меню."""
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu


def build_context_menu(parent, items: list) -> QMenu:
    """Строит QMenu из списка элементов."""
    menu = QMenu(parent)
    for item in items:
        if item is None:
            menu.addSeparator()
            continue
        label, callback = item
        action = QAction(label, parent)
        action.triggered.connect(callback)
        menu.addAction(action)
    return menu