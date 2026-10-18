"""Хелперы для локализованных диалогов."""
from PyQt6.QtWidgets import QMessageBox
from logic.core.i18n import t


def ask_yes_no(
    parent, title: str, text: str,
    yes_text: str | None = None,
    no_text: str | None = None,
) -> bool:
    """Задаёт вопрос с кнопками Да / Нет на текущем языке.

    Возвращает True, если нажато «Да».
    """
    msg = QMessageBox(parent)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setIcon(QMessageBox.Icon.Question)

    btn_yes = msg.addButton(
        yes_text or t("dialog.yes"),
        QMessageBox.ButtonRole.YesRole,
    )
    btn_no = msg.addButton(
        no_text or t("dialog.no"),
        QMessageBox.ButtonRole.NoRole,
    )
    msg.setDefaultButton(btn_yes)

    msg.exec()
    return msg.clickedButton() is btn_yes


def ask_yes_no_cancel(
    parent, title: str, text: str,
    yes_text: str | None = None,
    no_text: str | None = None,
    cancel_text: str | None = None,
) -> str:
    """Возвращает 'yes' / 'no' / 'cancel'."""
    msg = QMessageBox(parent)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setIcon(QMessageBox.Icon.Question)

    btn_yes = msg.addButton(
        yes_text or t("dialog.yes"),
        QMessageBox.ButtonRole.YesRole,
    )
    btn_no = msg.addButton(
        no_text or t("dialog.no"),
        QMessageBox.ButtonRole.NoRole,
    )
    btn_cancel = msg.addButton(
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


def info(parent, title: str, text: str):
    QMessageBox.information(
        parent, title, text,
        QMessageBox.StandardButton.Ok,
    )


def warn(parent, title: str, text: str):
    QMessageBox.warning(
        parent, title, text,
        QMessageBox.StandardButton.Ok,
    )


def error(parent, title: str, text: str):
    QMessageBox.critical(
        parent, title, text,
        QMessageBox.StandardButton.Ok,
    )