"""Плавная подсветка кнопок при наведении курсора.

Используется QVariantAnimation + интерполяция цвета.
Не требует подкласса QPushButton, работает с любыми кнопками.

Применение:
    from logic.widgets.hover_helpers import install_hover_animation

    install_hover_animation(self.btnSave)
    # или
    install_hover_for_all(self)   # все QPushButton внутри виджета
"""
from PyQt6.QtCore import (
    QEvent, QEasingCurve, QObject, QVariantAnimation,
)
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QPushButton, QWidget


# Цвета для анимации (можно менять)
BG_NORMAL = QColor("#2a2a3a")
BG_HOVER = QColor("#3a3a4a")
BORDER_NORMAL = QColor("#444444")
BORDER_HOVER = QColor("#d4a95a")
TEXT_COLOR = "#e0e0e0"

DURATION_MS = 180       # длительность анимации


def _lerp_color(c1: QColor, c2: QColor, t: float) -> QColor:
    """Линейная интерполяция между двумя цветами.

    t=0.0 — c1, t=1.0 — c2.
    """
    r = int(c1.red() + (c2.red() - c1.red()) * t)
    g = int(c1.green() + (c2.green() - c1.green()) * t)
    b = int(c1.blue() + (c2.blue() - c1.blue()) * t)
    return QColor(r, g, b)


class _HoverAnimator(QObject):
    """Навешивает плавную анимацию hover на QPushButton.

    Хранится как атрибут кнопки (button._hover_animator),
    чтобы не быть собранным сборщиком мусора.
    """

    def __init__(self, button: QPushButton):
        super().__init__(button)
        self._button = button

        # анимация от 0.0 до 1.0
        self._anim = QVariantAnimation(self)
        self._anim.setDuration(DURATION_MS)
        self._anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self._anim.valueChanged.connect(self._on_value)

        # перехватываем события Enter/Leave
        button.installEventFilter(self)

        # стартовое состояние
        self._apply(0.0)

    def eventFilter(self, obj, event):
        if obj is not self._button:
            return False

        if event.type() == QEvent.Type.Enter:
            self._animate_to(1.0)
        elif event.type() == QEvent.Type.Leave:
            self._animate_to(0.0)

        return False

    def _animate_to(self, target: float):
        """Запускает анимацию до target (0.0 или 1.0)."""
        current = float(self._anim.currentValue() or 0.0)
        self._anim.stop()
        self._anim.setStartValue(current)
        self._anim.setEndValue(target)
        self._anim.start()

    def _on_value(self, value):
        """Промежуточное значение анимации → применяем стиль."""
        self._apply(float(value))

    def _apply(self, t: float):
        """Применяет стиль с интерполяцией по t (0..1)."""
        bg = _lerp_color(BG_NORMAL, BG_HOVER, t)
        border = _lerp_color(BORDER_NORMAL, BORDER_HOVER, t)

        self._button.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg.name()};
                color: {TEXT_COLOR};
                border: 1px solid {border.name()};
                border-radius: 3px;
                padding: 4px 10px;
            }}
        """)


def install_hover_animation(button: QPushButton):
    """Навешивает плавный hover на одну кнопку.

    Если уже навешено — ничего не делает.
    """
    if getattr(button, "_hover_animator", None) is not None:
        return
    button._hover_animator = _HoverAnimator(button)


def install_hover_for_all(widget: QWidget):
    """Навешивает плавный hover на все QPushButton внутри widget.

    Вызывается один раз после setupUi.
    """
    for button in widget.findChildren(QPushButton):
        install_hover_animation(button)