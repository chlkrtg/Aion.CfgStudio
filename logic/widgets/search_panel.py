"""Панель поиска для текстового редактора."""
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QLineEdit, QPushButton, QLabel
)

from logic.widgets.theme import BORDER, BG_PANEL, TEXT_MUTED
from logic.widgets.hover_helpers import set_button_variant
from logic.core.i18n import t


class SearchPanel(QWidget):
    """Панель поиска, которая появляется над текстовым полем."""

    closed = pyqtSignal()

    def __init__(self, editor, parent=None):
        super().__init__(parent)
        self._editor = editor

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 5)
        layout.setSpacing(5)

        # Иконка/текст "Поиск"
        self.lbl = QLabel(t("main.search"))
        self.lbl.setStyleSheet(f"color: {TEXT_MUTED};")

        self.edit = QLineEdit()
        self.edit.setPlaceholderText(t("main.search.placeholder"))
        # Добавляем легкую рамку, чтобы поле не сливалось с фоном
        self.edit.setStyleSheet(f"border: 1px solid {BORDER}; border-radius: 3px; padding: 2px 5px;")

        self.btn_prev = QPushButton("↑")
        self.btn_prev.setFixedSize(28, 28)

        self.btn_next = QPushButton("↓")
        self.btn_next.setFixedSize(28, 28)

        self.btn_close = QPushButton("✕")
        self.btn_close.setFixedSize(28, 28)

        set_button_variant(self.btn_prev, "ghost")
        set_button_variant(self.btn_next, "ghost")
        set_button_variant(self.btn_close, "ghost")

        layout.addWidget(self.lbl)
        layout.addWidget(self.edit)
        layout.addWidget(self.btn_prev)
        layout.addWidget(self.btn_next)
        layout.addWidget(self.btn_close)

        # --- Сигналы ---
        self.btn_close.clicked.connect(self.hide_panel)
        self.btn_next.clicked.connect(self.find_next)
        self.btn_prev.clicked.connect(self.find_prev)
        self.edit.returnPressed.connect(self.find_next)
        self.edit.textChanged.connect(self._on_text_changed)

    def show_panel(self):
        """Показывает панель и ставит фокус в поле ввода."""
        self.show()
        self.edit.setFocus()
        self.edit.selectAll()

    def _on_text_changed(self, text: str):
        """Обновляем текст поиска в редакторе."""
        self._editor.set_search_term(text)

        if text:
            # При вводе текста сбрасываем курсор на начало,
            # чтобы первое совпадение сразу выделилось оранжевым
            cursor = self._editor.textCursor()
            cursor.movePosition(cursor.MoveOperation.Start)
            self._editor.setTextCursor(cursor)
            self.find_next()

    def hide_panel(self):
        """Скрывает панель, сбрасывает поиск и возвращает фокус."""
        self.hide()
        self._editor.set_search_term("")  # Очищаем подсветку
        self._editor.setFocus()
        self.closed.emit()

    def find_next(self):
        text = self.edit.text()
        if not text:
            return

        # Принудительно обновляем подсветку, чтобы текущий выбор стал оранжевым
        self._editor.set_search_term(text)

        if not self._editor.find(text):
            cursor = self._editor.textCursor()
            cursor.movePosition(cursor.MoveOperation.Start)
            self._editor.setTextCursor(cursor)
            self._editor.find(text)
        else:
            # После find() нужно обновить ExtraSelections, чтобы оранжевый цвет
            # переехал на новое активное совпадение
            self._editor._update_extra_selections()

    def find_prev(self):
        text = self.edit.text()
        if not text:
            return

        # QPlainTextEdit.find ищет вперед. Для поиска назад используем флаги
        from PyQt6.QtGui import QTextDocument
        found = self._editor.find(text, QTextDocument.FindFlag.FindBackward)
        if not found:
            # Если не нашли до начала — переходим в конец
            cursor = self._editor.textCursor()
            cursor.movePosition(cursor.MoveOperation.End)
            self._editor.setTextCursor(cursor)
            self._editor.find(text, QTextDocument.FindFlag.FindBackward)