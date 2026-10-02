"""Хелперы для работы с QShortcut. """
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QShortcut, QKeySequence


# Контексты срабатывания (псевдонимы для читаемости)
FOCUSED = Qt.ShortcutContext.WidgetShortcut
WITH_CHILDREN = Qt.ShortcutContext.WidgetWithChildrenShortcut
WINDOW = Qt.ShortcutContext.WindowShortcut


def bind_shortcut(widget, key: str, slot, context=FOCUSED):
    """Вешает QShortcut на виджет с заданным контекстом."""
    sc = QShortcut(QKeySequence(key), widget)
    sc.setContext(context)
    sc.activated.connect(slot)
    return sc


def bind_shortcuts(widget, bindings: dict, context=FOCUSED):
    """Вешает пачку хоткеев одной командой."""
    result = {}
    for key, slot in bindings.items():
        result[key] = bind_shortcut(widget, key, slot, context)
    return result