"""Делегат для чекбоксов в таблице с кастомным стилем."""
from PyQt6.QtCore import QPointF, QRect, QSize, Qt
from PyQt6.QtGui import QColor, QPainter, QPen
from PyQt6.QtWidgets import QStyle, QStyledItemDelegate, QStyleOptionViewItem
from logic.widgets.theme import (
    ACCENT, BG_APP, BG_INPUT_HOVER,
    BORDER_HOVER, TEXT_DIM,
)


def _state_val(value) -> int:
    if value is None:
        return 0
    if hasattr(value, "value"):
        return value.value
    return int(value)

class CheckboxDelegate(QStyledItemDelegate):
    """Рисует кастомный чекбокс в ячейке."""

    SIZE = 18
    RADIUS = 3

    BG_NORMAL = QColor(BG_APP)
    BG_HOVER = QColor(BG_INPUT_HOVER)
    BORDER = QColor(TEXT_DIM)
    BORDER_HOVER = QColor(BORDER_HOVER)
    BG_CHECKED = QColor(ACCENT)
    CHECK_COLOR = QColor(BG_APP)

    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.features &= ~QStyleOptionViewItem.ViewItemFeature.HasCheckIndicator

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index):
        state = index.data(Qt.ItemDataRole.CheckStateRole)
        marker = index.data(Qt.ItemDataRole.UserRole)

        # фон ячейки — стандартный (для selection, striped)
        bg_opt = QStyleOptionViewItem(option)
        self.initStyleOption(bg_opt, index)
        bg_opt.text = ""

        style = option.widget.style() if option.widget else None
        if style is not None:
            style.drawControl(
                QStyle.ControlElement.CE_ItemViewItem,
                bg_opt, painter,
            )

        # rect для чекбокса
        rect = option.rect
        size = self.SIZE
        x = rect.x() + (rect.width() - size) // 2
        y = rect.y() + (rect.height() - size) // 2
        cb = QRect(x, y, size, size)

        current_val = _state_val(state)
        checked = (current_val == 2)
        partial = (current_val == 1)
        hover = bool(option.state & QStyle.StateFlag.State_MouseOver)

        # изолируем состояние painter — критично после drawControl
        painter.save()
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setOpacity(1.0)

        # фон / рамка
        if checked or partial:
            painter.setBrush(self.BG_CHECKED)
            painter.setPen(Qt.PenStyle.NoPen)
        else:
            painter.setBrush(self.BG_HOVER if hover else self.BG_NORMAL)
            painter.setPen(QPen(
                self.BORDER_HOVER if hover else self.BORDER, 1
            ))

        painter.drawRoundedRect(cb, self.RADIUS, self.RADIUS)

        # знак
        if checked:
            pen = QPen(self.CHECK_COLOR, 2.2)
            pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
            painter.setPen(pen)
            painter.setBrush(Qt.BrushStyle.NoBrush)

            p1 = QPointF(cb.left() + cb.width() * 0.22,
                         cb.top() + cb.height() * 0.55)
            p2 = QPointF(cb.left() + cb.width() * 0.42,
                         cb.top() + cb.height() * 0.75)
            p3 = QPointF(cb.left() + cb.width() * 0.78,
                         cb.top() + cb.height() * 0.28)
            painter.drawLine(p1, p2)
            painter.drawLine(p2, p3)
        elif partial:
            pen = QPen(self.CHECK_COLOR, 2.2)
            pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            painter.setPen(pen)
            painter.drawLine(
                QPointF(cb.left() + cb.width() * 0.25,
                        cb.center().y()),
                QPointF(cb.right() - cb.width() * 0.25,
                        cb.center().y()),
            )

        painter.restore()

    def sizeHint(self, option, index):
        size = super().sizeHint(option, index)
        return QSize(
            max(size.width(), self.SIZE + 8),
            max(size.height(), 32),
        )

    def editorEvent(self, event, model, option, index):
        """Клик по ячейке — переключает состояние чекбокса."""
        from PyQt6.QtCore import QEvent

        if event.type() == QEvent.Type.MouseButtonRelease:
            pos = (event.position().toPoint()
                   if hasattr(event, "position") else event.pos())
            if option.rect.contains(pos):
                current = index.data(Qt.ItemDataRole.CheckStateRole)
                current_val = _state_val(current)
                new_state = (
                    Qt.CheckState.Unchecked
                    if current_val == 2
                    else Qt.CheckState.Checked
                )
                model.setData(
                    index, new_state, Qt.ItemDataRole.CheckStateRole
                )
                return True
        return super().editorEvent(event, model, option, index)