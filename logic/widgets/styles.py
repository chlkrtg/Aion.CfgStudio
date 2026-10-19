"""Хелперы для применения QSS-свойств."""
from PyQt6.QtWidgets import QWidget


def set_variant(widget: QWidget, variant: str):
    """Устанавливает property variant и перерисовывает виджет."""
    widget.setProperty("variant", variant)
    style = widget.style()
    if style is not None:
        style.unpolish(widget)
        style.polish(widget)