"""Диалог активации раннего доступа."""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from logic.core.i18n import t
from logic.core.license import get_hwid, validate_code
from logic.widgets.hover_helpers import set_button_variant
from logic.widgets.theme import DANGER, TEXT_DIM


class ActivationDialog(QDialog):
    """Показывает HWID и просит код активации."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(t("license.title"))
        self.setMinimumWidth(520)
        self.setModal(True)
        self._code: str | None = None

        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        # --- HWID ---
        self._hwid = get_hwid()

        lbl_hwid_title = QLabel(t("license.hwid_title"))
        font = lbl_hwid_title.font()
        font.setBold(True)
        lbl_hwid_title.setFont(font)
        layout.addWidget(lbl_hwid_title)

        lbl_hwid = QLabel(self._hwid)
        lbl_hwid.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        lbl_hwid.setStyleSheet(
            "font-family: Consolas, monospace; "
            f"color: {TEXT_DIM}; padding: 4px; "
            "border: 1px solid #444; border-radius: 3px;"
        )
        layout.addWidget(lbl_hwid)

        btn_copy = QPushButton(t("license.copy_hwid"))
        btn_copy.clicked.connect(self._copy_hwid)
        set_button_variant(btn_copy, "ghost")
        layout.addWidget(btn_copy)

        # --- Подсказка ---
        lbl_hint = QLabel(t("license.hint"))
        lbl_hint.setWordWrap(True)
        lbl_hint.setStyleSheet(f"color: {TEXT_DIM};")
        layout.addWidget(lbl_hint)

        # --- Поле ввода ---
        self.edit_code = QLineEdit()
        self.edit_code.setPlaceholderText(t("license.placeholder"))
        self.edit_code.returnPressed.connect(self._on_activate)
        layout.addWidget(self.edit_code)

        # --- Ошибка ---
        self.lbl_error = QLabel("")
        self.lbl_error.setStyleSheet(f"color: {DANGER};")
        self.lbl_error.setWordWrap(True)
        layout.addWidget(self.lbl_error)

        # --- Кнопки ---
        btn_activate = QPushButton(t("license.activate"))
        btn_activate.clicked.connect(self._on_activate)
        set_button_variant(btn_activate, "primary")
        layout.addWidget(btn_activate)

        btn_cancel = QPushButton(t("license.cancel"))
        btn_cancel.clicked.connect(self.reject)
        set_button_variant(btn_cancel, "ghost")
        layout.addWidget(btn_cancel)

        self.edit_code.setFocus()

    # ============ действия ============

    def _copy_hwid(self):
        QGuiApplication.clipboard().setText(self._hwid)
        self.lbl_error.setText(t("license.copied"))
        self.lbl_error.setStyleSheet(f"color: {TEXT_DIM};")

    def _on_activate(self):
        code = self.edit_code.text().strip()
        ok, reason = validate_code(code)
        if not ok:
            self.lbl_error.setStyleSheet(f"color: {DANGER};")
            self.lbl_error.setText(reason)
            return
        self._code = code
        self.accept()

    # ============ результат ============

    @property
    def code(self) -> str | None:
        return self._code