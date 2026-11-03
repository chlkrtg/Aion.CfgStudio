"""Виджет для отображения номеров строк в QPlainTextEdit."""
from PyQt6.QtCore import QRect, QSize, Qt, QTimer
from PyQt6.QtGui import QColor, QPainter, QTextFormat
from PyQt6.QtWidgets import QPlainTextEdit, QWidget
from logic.widgets.theme import BG_PANEL, TEXT_DIM
from logic.widgets.overview_bar import OverviewBar, _WIDTH as _OVERVIEW_W


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

        # --- мини-карта проблем (справа, отдельная колонка) ---
        self.overviewBar = OverviewBar(self)
        self.overviewBar.lineClicked.connect(self._on_overview_click)
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self._overview_timer = QTimer(self)
        self._overview_timer.setSingleShot(True)
        self._overview_timer.setInterval(150)
        self._overview_timer.timeout.connect(self._recalc_overview)

        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)

        self.blockCountChanged.connect(lambda _: self._overview_timer.start())
        self.textChanged.connect(lambda: self._overview_timer.start())

        self.update_line_number_area_width(0)
        self.highlight_current_line()

        # первый кадр — спозиционировать мини-карту после того, как Qt посчитает размеры
        QTimer.singleShot(0, self._place_overview)

    def line_number_area_width(self):
        digits = 1
        max_num = max(1, self.blockCount())
        while max_num >= 10:
            max_num //= 10
            digits += 1
        space = 10 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def update_line_number_area_width(self, _):
        self.setViewportMargins(
            self.line_number_area_width(), 0, _OVERVIEW_W, 0
        )

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
        self.lineNumberArea.setGeometry(
            QRect(cr.left(), cr.top(), self.line_number_area_width(), cr.height())
        )
        self._place_overview()

    def _place_overview(self):
        """Ставит OverviewBar в правый margin (справа от скроллбара)."""
        vp = self.viewport()
        if vp is None or not hasattr(self, "overviewBar"):
            return
        x = self.width() - _OVERVIEW_W
        self.overviewBar.setGeometry(x, vp.y(), _OVERVIEW_W, vp.height())
        self.overviewBar.raise_()

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
        from PyQt6.QtWidgets import QTextEdit

        from logic.widgets.theme import BG_PANEL

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

    def set_completion_words(self, words: list[str]):
        """Устанавливает список слов для автодополнения."""
        from PyQt6.QtCore import QStringListModel, Qt
        from PyQt6.QtWidgets import QCompleter

        self._completer_model = QStringListModel(words, self)
        self._completer = QCompleter(self._completer_model, self)
        self._completer.setWidget(self)
        self._completer.setCompletionMode(
            QCompleter.CompletionMode.PopupCompletion
        )
        self._completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self._completer.setFilterMode(Qt.MatchFlag.MatchStartsWith)
        self._completer.activated.connect(self._insert_completion)

    def keyPressEvent(self, event):
        # Если completer открыт — отдаём ему управление
        if (self._completer and self._completer.popup().isVisible()
            and event.key() in (
                    Qt.Key.Key_Enter, Qt.Key.Key_Return,
                    Qt.Key.Key_Escape, Qt.Key.Key_Tab,
                    Qt.Key.Key_Backtab,
            )):
                event.ignore()
                return

        super().keyPressEvent(event)

        if not self._completer:
            return

        # Получаем слово под курсором
        cursor = self.textCursor()
        cursor.select(cursor.SelectionType.WordUnderCursor)
        prefix = cursor.selectedText()

        if len(prefix) >= 2:  # показываем только от 2 символов
            self._completer.setCompletionPrefix(prefix)
            if self._completer.completionCount() > 0:
                rect = self.cursorRect()
                rect.setWidth(
                    self._completer.popup().sizeHintForColumn(0)
                    + self._completer.popup().verticalScrollBar().sizeHint().width()
                )
                self._completer.complete(rect)
            else:
                self._completer.popup().hide()
        else:
            self._completer.popup().hide()

    def _insert_completion(self, completion: str):
        cursor = self.textCursor()
        cursor.select(cursor.SelectionType.WordUnderCursor)
        cursor.insertText(completion)
        self.setTextCursor(cursor)

    def _recalc_overview(self):
        """Пересчитать метки проблем (debounce 150 мс)."""
        highlighter = getattr(self, "_highlighter", None)
        if highlighter is None:
            return
        marks = highlighter.get_problem_lines()
        self.overviewBar.set_marks(marks, max(1, self.blockCount()))

    def _on_overview_click(self, line: int):
        block = self.document().findBlockByNumber(line)
        if not block.isValid():
            return
        cursor = self.textCursor()
        cursor.setPosition(block.position())
        self.setTextCursor(cursor)
        self.centerCursor()  # или ensureCursorVisible / scrollTo top

    def refresh_overview(self):
        self._overview_timer.stop()
        self._recalc_overview()