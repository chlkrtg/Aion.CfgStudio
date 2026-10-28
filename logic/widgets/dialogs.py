"""Хелперы для локализованных диалогов."""
import os
import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

from logic.core.i18n import t


def info(parent, title: str, text: str):
    msg = _build(parent, title, text, "info")
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.exec()


def warn(parent, title: str, text: str):
    msg = _build(parent, title, text, "warning")
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.exec()


def error(parent, title: str, text: str):
    msg = _build(parent, title, text, "error")
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.exec()


def ask_yes_no(parent, title: str, text: str,
               yes_text=None, no_text=None) -> bool:
    msg = _build(parent, title, text, "question")
    btn_yes = msg.addButton(
        yes_text or t("dialog.yes"),
        QMessageBox.ButtonRole.YesRole,
    )
    msg.addButton(
        no_text or t("dialog.no"),
        QMessageBox.ButtonRole.NoRole,
    )
    msg.setDefaultButton(btn_yes)
    msg.exec()
    return msg.clickedButton() is btn_yes


def ask_yes_no_cancel(parent, title: str, text: str,
                      yes_text=None, no_text=None,
                      cancel_text=None) -> str:
    msg = _build(parent, title, text, "question")
    btn_yes = msg.addButton(
        yes_text or t("dialog.yes"),
        QMessageBox.ButtonRole.YesRole,
    )
    btn_no = msg.addButton(
        no_text or t("dialog.no"),
        QMessageBox.ButtonRole.NoRole,
    )
    msg.addButton(
        cancel_text or t("dialog.cancel"),
        QMessageBox.ButtonRole.RejectRole,
    )
    msg.exec()
    clicked = msg.clickedButton()
    if clicked is btn_yes:
        return "yes"
    if clicked is btn_no:
        return "no"
    return "cancel"


def ask_choice(parent, title: str, text: str,
               choices: list[tuple[str, str]]) -> str | None:
    """Диалог с несколькими кнопками.

    choices: [(button_id, button_text), ...]
    Возвращает button_id выбранной кнопки или None при отмене.
    """
    msg = _build(parent, title, text, "question")

    buttons = {}
    for btn_id, btn_text in choices:
        btn = msg.addButton(btn_text, QMessageBox.ButtonRole.AcceptRole)
        buttons[btn] = btn_id

    cancel_btn = msg.addButton(
        t("editor.btn_cancel"),
        QMessageBox.ButtonRole.RejectRole,
    )

    msg.exec()
    clicked = msg.clickedButton()

    if clicked is cancel_btn:
        return None
    return buttons.get(clicked)


def _icon(name: str) -> QIcon:
    base = getattr(
        sys, "_MEIPASS",
        os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))))
    )
    path = os.path.join(base, "resources", "icons", f"{name}.svg")
    if not os.path.exists(path):
        return QIcon()
    return QIcon(path)


def _build(parent, title: str, text: str, icon_name: str) -> QMessageBox:
    msg = QMessageBox(parent)
    msg.setWindowTitle(title)
    msg.setText(text)

    icon = _icon(icon_name)
    if not icon.isNull():
        pix = icon.pixmap(64, 64)
        if not pix.isNull():
            msg.setIconPixmap(pix)
        else:
            msg.setIcon(QMessageBox.Icon.NoIcon)
    else:
        msg.setIcon(QMessageBox.Icon.NoIcon)

    return msg