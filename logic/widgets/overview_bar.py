"""Мини-карта проблем справа от редактора (как в VS Code).

Цветные метки на узкой полосе: ошибки / переопределения / дубли / неизвестные.
Клик по полосе — сигнал lineClicked(0-based номер строки).
"""
from PyQt6.QtCore import QRect, Qt, pyqtSignal
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QWidget

from logic.widgets.theme import (
    ACCENT,
    DANGER,
    SYNTAX_OVERRIDDEN_KEY,
    SYNTAX_UNKNOWN_KEY,
)

_COLORS = {
    "error":     QColor(DANGER),
    "override":  QColor(SYNTAX_OVERRIDDEN_KEY),
    "duplicate": QColor(ACCENT),
    "unknown":   QColor(SYNTAX_UNKNOWN_KEY),
}

_MIN_H = 6   # минимальная высота метки, px
_WIDTH = 5   # ширина колонки (используется в line_numbers как margin справа)


class OverviewBar(QWidget):
    """Узкая полоса справа: цветные метки проблемных строк."""

    lineClicked = pyqtSignal(int)  # 0-based номер строки

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("background: transparent; border: none;")
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
        self.setAutoFillBackground(False)

        self._marks: dict[int, str] = {}  # line -> type
        self._total = 1                   # всего строк (для пропорций)

        for c in _COLORS.values():
            c.setAlpha(255)

    # ---- API ----

    def set_marks(self, marks: dict[int, str], total_lines: int):
        """marks: {line_number (0-based): type}, total_lines: blockCount()."""
        self._marks = marks
        self._total = max(1, total_lines)
        self.update()

    # ---- paint ----

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 0))

        h = self.height()
        if h <= 0:
            return

        for line, typ in self._marks.items():
            if typ not in _COLORS:
                continue
            y = int(line / self._total * h)
            bar_h = max(_MIN_H, int(h / self._total) + 1)
            rect = QRect(0, y, self.width(), min(bar_h, h - y))
            painter.fillRect(rect, _COLORS[typ])

    # ---- mouse ----

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.height() > 0:
            line = int(event.position().y() / self.height() * self._total)
            line = max(0, min(line, self._total - 1))
            self.lineClicked.emit(line)
            event.accept()
            return
        super().mousePressEvent(event)