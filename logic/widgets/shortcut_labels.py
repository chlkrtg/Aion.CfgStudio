"""Хелпер: подпись виджета + хоткей из сервиса.

Используется в retranslate() на страницах, чтобы подписи кнопок
и пунктов меню всегда отражали актуальную клавишу, включая
случай, когда пользователь переназначил её в редакторе хоткеев.
"""


def with_hotkey(text: str, shortcut_service, action_id: str) -> str:
    """«Переименовать» --> «Переименовать (F2)».

    Если у действия нет клавиши (default_key пустой и override нет),
    возвращает текст без скобок.
    """
    if not action_id:
        return text
    key = shortcut_service.current_key(action_id)
    if not key:
        return text
    return f"{text} ({key})"