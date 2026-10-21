"""Виджет для отображения номеров строк в QPlainTextEdit."""
from PyQt6.QtCore import QRect, QSize, Qt
from PyQt6.QtGui import QColor, QPainter, QTextFormat
from PyQt6.QtWidgets import QPlainTextEdit, QWidget

from logic.widgets.theme import BG_PANEL, TEXT_DIM, BORDER


class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.codeEditor = editor

    def sizeHint(self):
        return QSize(self.codeEditor.line_number_area_width(), 0)

    def paintEvent(self, event):
        self.codeEditor.line_number_area_paint_event(event)


class CodeEditor(QPlainTextEdit):
    """QPlainTextEdit с номерами строк."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.lineNumberArea = LineNumberArea(self)

        self._search_term = ""
        self._search_highlights = []

        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)

        self.update_line_number_area_width(0)
        self.highlight_current_line()

    def line_number_area_width(self):
        digits = 1
        max_num = max(1, self.blockCount())
        while max_num >= 10:
            max_num //= 10
            digits += 1
        space = 10 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def update_line_number_area_width(self, _):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.line_number_area_width(), cr.height()))

    def line_number_area_paint_event(self, event):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), QColor(BG_PANEL))

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(QColor(TEXT_DIM))
                painter.drawText(0, int(top), self.lineNumberArea.width() - 5, self.fontMetrics().height(),
                                 Qt.AlignmentFlag.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            block_number += 1

    def highlight_current_line(self):
        """Подсветка текущей строки + поиска."""
        self._update_extra_selections()

    def set_search_term(self, term: str):
        """Устанавливает текст для поиска и обновляет подсветку."""
        self._search_term = term
        self._update_extra_selections()

    def _update_extra_selections(self):
        """Собирает все ExtraSelections: текущая строка + поиск."""
        from PyQt6.QtGui import QTextFormat
        from PyQt6.QtWidgets import QTextEdit
        from logic.widgets.theme import ACCENT, BG_PANEL

        selections = []

        # 1. Текущая строка (как было)
        line_selection = QTextEdit.ExtraSelection()
        line_color = QColor(BG_PANEL)
        line_color.setAlpha(100)
        line_selection.format.setBackground(line_color)
        line_selection.format.setProperty(QTextFormat.Property.FullWidthSelection, True)
        line_selection.cursor = self.textCursor()
        line_selection.cursor.clearSelection()
        selections.append(line_selection)

        # 2. Подсветка поиска
        if self._search_term:
            # Настройки цветов (как в Google: желтый для всех, оранжевый для текущего)
            highlight_color = QColor(255, 235, 59, 100)  # Желтый полупрозрачный
            current_color = QColor(255, 152, 0, 150)  # Оранжевый для активного

            # Собираем все вхождения
            doc = self.document()
            cursor = doc.find(self._search_term, 0)

            # Запоминаем текущую позицию курсора, чтобы понять, какое вхождение активное
            user_cursor_pos = self.textCursor().selectionStart()

            while not cursor.isNull():
                start = cursor.selectionStart()
                end = cursor.selectionEnd()

                sel = QTextEdit.ExtraSelection()
                sel.cursor = cursor

                # Если это вхождение пересекается с текущим выделением пользователя — красим ярче
                if start <= user_cursor_pos <= end:
                    sel.format.setBackground(current_color)
                else:
                    sel.format.setBackground(highlight_color)

                selections.append(sel)

                # Ищем следующее
                cursor = doc.find(self._search_term, end)

        self.setExtraSelections(selections)