"""Хелперы для работы с QShortcut."""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence, QShortcut

from logic.core.actions import ACTIONS

# Контексты срабатывания (псевдонимы)
FOCUSED = Qt.ShortcutContext.WidgetShortcut
WITH_CHILDREN = Qt.ShortcutContext.WidgetWithChildrenShortcut
WINDOW = Qt.ShortcutContext.WindowShortcut

# Маппинг строковых псевдонимов из Action.context в Qt-контексты
CONTEXTS = {
    "focused": FOCUSED,
    "with_children": WITH_CHILDREN,
    "window": WINDOW,
}


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


def bind_action(widget, action_id: str, slot,
                key_override: str | None = None,
                context_override=None):
    """Вешает один QShortcut по action_id.

    Клавишу берём из key_override (позже - из БД через ShortcutService),
    иначе - из ACTIONS[action_id].default_key.
    Возвращает список QShortcut (может быть >1 из-за extra_keys).
    """
    action = ACTIONS[action_id]

    # если override задан, вешаем только его (пользователь явно переопределил)
    if key_override:
        keys = (key_override,)
    else:
        keys = action.all_default_keys()

    ctx = context_override or CONTEXTS[action.context]

    result = []
    for key in keys:
        if not key:
            continue
        result.append(bind_shortcut(widget, key, slot, ctx))
    return result


def bind_actions(widget, bindings: dict, keys: dict | None = None):
    """Вешает пачку действий по реестру.

    bindings: {action_id: slot}
    keys:     {action_id: key} - переопределения из БД (или None)

    Разводит хоткеи по виджетам-получателям:
      - context="window"          -> widget (страница)
      - context="focused"         -> getattr(widget, action.target)

    Возвращает {action_id: [QShortcut, ...]}.
    """
    keys = keys or {}
    result = {}

    for action_id, slot in bindings.items():
        action = ACTIONS[action_id]

        if action.context == "window" or not action.target:
            host = widget
        else:
            host = getattr(widget, action.target, None)
            if host is None:
                raise AttributeError(
                    f"Действие '{action_id}' ожидает виджет "
                    f"'{action.target}' на {type(widget).__name__}"
                )

        result[action_id] = bind_action(
            host, action_id, slot,
            key_override=keys.get(action_id),
        )
    return result