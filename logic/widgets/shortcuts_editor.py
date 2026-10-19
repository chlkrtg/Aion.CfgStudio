"""Диалог редактора горячих клавиш.

Отдельное модальное окно (не страница стека).
Логика в ShortcutPresenter.

Здесь:
  - KeyCaptureDialog  - ловит нажатие клавиши и возвращает QKeySequence-строку
  - ShortcutsEditorDialog - само окно с деревом действий
"""
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QDialog, QLabel, QVBoxLayout, QHeaderView,
)

from logic.presenters import ShortcutPresenter
from logic.widgets.hover_helpers import set_button_variant
from ui.shortcuts_editor import Ui_ShortcutsEditorDialog
from logic.core.i18n import t


# Клавиши, которые нельзя назначать (конфликт с системой / Qt)
FORBIDDEN_KEYS = {
    Qt.Key.Key_Escape,   # закрывает диалог
    Qt.Key.Key_Tab,      # уводит фокус
    Qt.Key.Key_Backtab,  # Shift+Tab
}

MODIFIER_KEYS = {
    Qt.Key.Key_Shift,
    Qt.Key.Key_Control,
    Qt.Key.Key_Alt,
    Qt.Key.Key_Meta,
    Qt.Key.Key_AltGr,
    Qt.Key.Key_CapsLock,
    Qt.Key.Key_NumLock,
    Qt.Key.Key_ScrollLock,
}


class KeyCaptureDialog(QDialog):
    """Модальное окно: ловит одну клавишу (или комбинацию).

    Собирает строку вида "Ctrl+S", "F2", "Delete" вручную —
    не через QKeySequence, потому что на Python 3.14 + PyQt6
    QKeySequence крашится, а в русской раскладке возвращает
    символ вместо физической клавиши.
    """

    # Qt при зажатом Shift передаёт СИМВОЛ, а не физическую клавишу.
    # В русской и английской раскладках один и тот же Shift+клавиша
    # даёт разные символы - учитываем оба варианта.
    #
    # При коллизиях (один код - две разные физические клавиши)
    # приоритет у РУССКОЙ раскладки: пользователь русскоязычный.
    SHIFT_SYMBOLS = {
        # ============ цифровой ряд (обе раскладки) ============
        0x21: "1",  # ! — англ. Shift+1, рус. Shift+1
        0x40: "2",  # @ — англ. Shift+2
        0x22: "2",  # " — рус. Shift+2   (приоритет)
        0x23: "3",  # # — англ. Shift+3
        0x2116: "3",  # № — рус. Shift+3
        0x24: "4",  # $ — англ. Shift+4
        0x3B: "4",  # ; — рус. Shift+4   (приоритет)
        0x25: "5",  # % — обе
        0x5E: "6",  # ^ — англ. Shift+6
        0x3A: "6",  # : — рус. Shift+6   (приоритет)
        0x26: "7",  # & — англ. Shift+7
        0x3F: "7",  # ? — рус. Shift+7   (приоритет)
        0x2A: "8",  # * — обе
        0x28: "9",  # ( — обе
        0x29: "0",  # ) — обе

        # ============ символы (англ. раскладка) ============
        0x5F: "Minus",  # _ - Shift+-
        0x2B: "Equal",  # + - Shift+=
        0x7B: "BracketLeft",  # { - Shift+[
        0x7D: "BracketRight",  # } - Shift+]
        0x7C: "Backslash",  # | - Shift+\
        0x3C: "Comma",  # < - Shift+,
        0x3E: "Period",  # > - Shift+.
        0x2F: "Slash",  # / - Shift+/ в англ. (без сдвига)
        0x7E: "QuoteLeft",  # ~ - Shift+`

        # ============ символы (рус. раскладка) ============
        # В русской раскладке Shift+цифра даёт символ, но некоторые
        # уже перечислены выше (0x3B, 0x3A, 0x3F). Остальные:
        0x2C: "Slash",  # Shift+\ в рус. даёт \, не покрываем
        # Русская раскладка для остальных клавиш совпадает с англ.

        # ============ особые случаи ============
        0x2212: "Minus",  # − (U+2212, минус) - на всякий
        0x2013: "Minus", # – (en dash)
    }

    RU_TO_EN = {
        'й': 'Q', 'ц': 'W', 'у': 'E', 'к': 'R', 'е': 'T',
        'н': 'Y', 'г': 'U', 'ш': 'I', 'щ': 'O', 'з': 'P',
        'х': 'BracketLeft', 'ъ': 'BracketRight',
        'ф': 'A', 'ы': 'S', 'в': 'D', 'а': 'F', 'п': 'G',
        'р': 'H', 'о': 'J', 'л': 'K', 'д': 'L', 'ж': 'Semicolon',
        'э': 'Apostrophe',
        'я': 'Z', 'ч': 'X', 'с': 'C', 'м': 'V', 'и': 'B',
        'т': 'N', 'ь': 'M', 'б': 'Comma', 'ю': 'Period',
        'ё': 'QuoteLeft',
    }

    def __init__(self, parent, action_title: str):
        super().__init__(parent)
        self.setWindowTitle(t("shortcuts.capture.title"))
        self.setModal(True)
        self.setMinimumWidth(360)

        self._result: str | None = None

        layout = QVBoxLayout(self)

        self._lblAction = QLabel(
            t("shortcuts.capture.action").format(title=action_title)
        )
        font = self._lblAction.font()
        font.setBold(True)
        self._lblAction.setFont(font)
        layout.addWidget(self._lblAction)

        self._lblHint = QLabel(t("shortcuts.capture.hint"))
        self._lblHint.setWordWrap(True)
        self._lblHint.setStyleSheet("color: #888;")
        layout.addWidget(self._lblHint)

        self._lblPreview = QLabel(t("shortcuts.capture.preview_empty"))
        self._lblPreview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._lblPreview.setStyleSheet(
            "font-size: 20px; padding: 12px; "
            "border: 1px solid #888; border-radius: 6px;"
        )
        layout.addWidget(self._lblPreview)

    # ============ результат ============

    @property
    def result_key(self) -> str | None:
        """Клавиша, введённая пользователем, или None."""
        return self._result

    # ============ перехват клавиш ============

    def keyPressEvent(self, event):
        key = event.key()
        mods = event.modifiers()

        # Esc без модификаторов - отмена
        if (key == Qt.Key.Key_Escape
                and mods == Qt.KeyboardModifier.NoModifier):
            self._result = None
            self.reject()
            return

        # чистые модификаторы - ждём «настоящую» клавишу
        if key in MODIFIER_KEYS:
            return

        # запрещённые клавиши (без модификаторов)
        if mods == Qt.KeyboardModifier.NoModifier and key in FORBIDDEN_KEYS:
            return

        # собираем строку вручную
        name = self._key_name(key)
        if name is None:
            return

        parts = []
        if mods & Qt.KeyboardModifier.ControlModifier:
            parts.append("Ctrl")
        if mods & Qt.KeyboardModifier.ShiftModifier:
            parts.append("Shift")
        if mods & Qt.KeyboardModifier.AltModifier:
            parts.append("Alt")
        if mods & Qt.KeyboardModifier.MetaModifier:
            parts.append("Meta")
        parts.append(name)

        self._result = "+".join(parts)
        self.accept()

    # ============ Qt.Key -> строка ============

    @classmethod
    def _key_name(cls, key: int) -> str | None:
        """Qt.Key -> строка для QKeySequence.fromString."""

        # Кириллица → латиница
        if 0x410 <= key <= 0x44F:
            ch = chr(key).lower()
            return cls.RU_TO_EN.get(ch)

        # Буквы A-Z (физические)
        if Qt.Key.Key_A <= key <= Qt.Key.Key_Z:
            return chr(ord("A") + (key - Qt.Key.Key_A))

        # Цифры 0-9
        if Qt.Key.Key_0 <= key <= Qt.Key.Key_9:
            return chr(ord("0") + (key - Qt.Key.Key_0))

        # Функциональные F1-F35
        if Qt.Key.Key_F1 <= key <= Qt.Key.Key_F35:
            return f"F{key - Qt.Key.Key_F1 + 1}"

        # Сдвинутые символы
        if key in cls.SHIFT_SYMBOLS:
            return cls.SHIFT_SYMBOLS[key]

        # Специальные
        SPECIAL = {
            Qt.Key.Key_Space: "Space",
            Qt.Key.Key_Return: "Return",
            Qt.Key.Key_Enter: "Enter",
            Qt.Key.Key_Tab: "Tab",
            Qt.Key.Key_Backspace: "Backspace",
            Qt.Key.Key_Delete: "Delete",
            Qt.Key.Key_Insert: "Insert",
            Qt.Key.Key_Home: "Home",
            Qt.Key.Key_End: "End",
            Qt.Key.Key_PageUp: "PgUp",
            Qt.Key.Key_PageDown: "PgDown",
            Qt.Key.Key_Left: "Left",
            Qt.Key.Key_Right: "Right",
            Qt.Key.Key_Up: "Up",
            Qt.Key.Key_Down: "Down",
            Qt.Key.Key_Plus: "Plus",
            Qt.Key.Key_Minus: "Minus",
            Qt.Key.Key_Equal: "Equal",
            Qt.Key.Key_Comma: "Comma",
            Qt.Key.Key_Period: "Period",
            Qt.Key.Key_Slash: "Slash",
            Qt.Key.Key_Backslash: "Backslash",
            Qt.Key.Key_Semicolon: "Semicolon",
            Qt.Key.Key_Apostrophe: "Apostrophe",
            Qt.Key.Key_BracketLeft: "BracketLeft",
            Qt.Key.Key_BracketRight: "BracketRight",
            Qt.Key.Key_QuoteLeft: "QuoteLeft",
        }
        return SPECIAL.get(key)

class ShortcutsEditorDialog(QDialog, Ui_ShortcutsEditorDialog):
    """Окно редактора горячих клавиш."""

    #: Сигнал: хоткеи изменились, страницам надо перевесить QShortcut'ы
    shortcuts_changed = pyqtSignal()

    def __init__(self, parent, service):
        super().__init__(parent)
        self.setupUi(self)

        # ============ презентер ============
        self.presenter = ShortcutPresenter(self, service)

        # ============ UI ============
        self._setup_tree()
        self._connect_signals()

        # заполнить дерево
        self.presenter.on_enter()
        self.presenter.retranslate()

    # ============ настройка ============

    def _setup_tree(self):
        header = self.treeShortcuts.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(
            1, QHeaderView.ResizeMode.ResizeToContents
        )
        header.setSectionResizeMode(
            2, QHeaderView.ResizeMode.ResizeToContents
        )

    def _connect_signals(self):
        self.btnChange.clicked.connect(self.presenter.on_change)
        self.btnReset.clicked.connect(self.presenter.on_reset)
        self.btnResetAll.clicked.connect(self.presenter.on_reset_all)
        self.btnClose.clicked.connect(self.accept)

        # двойной клик по строке = «Изменить...»
        self.treeShortcuts.itemDoubleClicked.connect(
            lambda _item, _col: self.presenter.on_change()
        )

        set_button_variant(self.btnChange, "secondary")
        set_button_variant(self.btnClose, "primary")
        set_button_variant(self.btnReset, "ghost")
        set_button_variant(self.btnResetAll, "ghost")

    # ============ View-хелперы (зовёт презентер) ============

    def ask_key(self, action_id: str) -> str | None:
        from logic.core.actions import ACTIONS
        action = ACTIONS[action_id]

        dlg = KeyCaptureDialog(self, t(action.title))
        if dlg.exec() != QDialog.DialogCode.Accepted:
            return None
        return dlg.result_key

    # ============ закрытие ============

    def accept(self):
        """Закрытие через «Закрыть»."""
        self.shortcuts_changed.emit()
        super().accept()

    def reject(self):
        """Закрытие через Esc или крестик."""
        self.shortcuts_changed.emit()
        super().reject()