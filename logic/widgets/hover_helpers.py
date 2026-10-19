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

# ==================== Варианты кнопок ====================

VARIANTS = {
    "secondary": {
        "bg_normal": QColor("#2a2a3a"),
        "bg_hover": QColor("#3a3a4a"),
        "border_normal": QColor("#444444"),
        "border_hover": QColor("#d4a95a"),
        "text": "#e0e0e0",
    },
    "primary": {
        "bg_normal": QColor("#d4a95a"),
        "bg_hover": QColor("#e8bd6e"),
        "border_normal": QColor("#d4a95a"),
        "border_hover": QColor("#e8bd6e"),
        "text": "#1e2026",
    },
    "ghost": {
        "bg_normal": QColor(0, 0, 0, 0),   # прозрачный
        "bg_hover": QColor("#2a2a3a"),
        "border_normal": QColor("#2a2a3a"),
        "border_hover": QColor("#3a3a4a"),
        "text": "#e0e0e0",
    },
    "danger": {
        "bg_normal": QColor("#2a2a3a"),
        "bg_hover": QColor("#3a2020"),
        "border_normal": QColor("#444444"),
        "border_hover": QColor("#e05a5a"),
        "text": "#e05a5a",
    },
}

DEFAULT_VARIANT = "secondary"


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

    def __init__(self, button: QPushButton, variant: str = DEFAULT_VARIANT):
        super().__init__(button)
        self._button = button
        self._variant = variant

        # анимация от 0.0 до 1.0
        self._anim = QVariantAnimation(self)
        self._anim.setDuration(DURATION_MS)
        self._anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self._anim.valueChanged.connect(self._on_value)

        # перехватываем события Enter/Leave
        button.installEventFilter(self)

        # стартовое состояние
        self._apply(0.0)

    def set_variant(self, variant: str):
        if variant not in VARIANTS:
            variant = DEFAULT_VARIANT
        if self._variant == variant:
            return
        self._variant = variant
        self._apply(float(self._anim.currentValue() or 0.0))

    def eventFilter(self, obj, event):
        if obj is not self._button:
            return False

        if event.type() == QEvent.Type.EnabledChange:
            self._apply(
                float(self._anim.currentValue() or 0.0)
            )
            return False

        if not self._button.isEnabled():
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
        colors = VARIANTS.get(self._variant, VARIANTS[DEFAULT_VARIANT])

        if not self._button.isEnabled():
            self._button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {colors['bg_normal'].name(QColor.NameFormat.HexArgb)};
                    color: #666666;
                    border: 1px solid {colors['border_normal'].name()};
                    border-radius: 3px;
                    padding: 4px 10px;
                }}
            """)
            return

        bg = _lerp_color(colors['bg_normal'], colors['bg_hover'], t)
        border = _lerp_color(colors['border_normal'], colors['border_hover'], t)

        bg_pressed = bg.darker(115)
        border_pressed = border.darker(110)

        self._button.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg.name(QColor.NameFormat.HexArgb)};
                color: {colors['text']};
                border: 1px solid {border.name()};
                border-radius: 3px;
                padding: 4px 10px;
            }}
            QPushButton:pressed {{
                background-color: {bg_pressed.name(QColor.NameFormat.HexArgb)};
                border: 1px solid {border_pressed.name()};
                padding-top: 5px;
                padding-bottom: 3px;
            }}
        """)


def install_hover_animation(button: QPushButton, variant: str = DEFAULT_VARIANT):
    """Навешивает плавный hover на одну кнопку.

    Если уже навешено — ничего не делает.
    """
    if getattr(button, "_hover_animator", None) is not None:
        return
    button._hover_animator = _HoverAnimator(button, variant)


def install_hover_for_all(widget: QWidget):
    """Навешивает плавный hover на все QPushButton внутри widget.

    Вызывается один раз после setupUi.
    """
    for button in widget.findChildren(QPushButton):
        install_hover_animation(button)

def set_button_variant(button: QPushButton, variant: str):
    """Переключает вариант стиля у кнопки (если hover-аниматор уже есть)."""
    animator = getattr(button, "_hover_animator", None)
    if animator is None:
        install_hover_animation(button, variant)
        return
    animator.set_variant(variant)