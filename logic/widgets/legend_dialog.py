"""Диалог с легендой предпросмотра."""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
)

from logic.widgets.theme import BG_PANEL, TEXT, ACCENT, DANGER, SUCCESS, SYNTAX_OVERRIDDEN_KEY
from logic.widgets.hover_helpers import set_button_variant
from logic.core.i18n import t


class LegendDialog(QDialog):
    """Модальное окно со справкой по цветам предпросмотра."""

    def __init__(self, parent=None, shortcut_service=None):
        super().__init__(parent)
        self.setWindowTitle(t("legend.title"))
        self.setFixedWidth(550)
        self.setModal(True)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        # --- Заголовок ---
        lbl_header = QLabel(t("legend.header"))
        lbl_header.setStyleSheet(
            f"font-size: 14pt; font-weight: 700; color: {ACCENT}; "
            "background: transparent;"
        )
        lbl_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lbl_header)

        # --- Легенда цветов ---
        legend_html = (
            f"<span style='color:{SUCCESS};'>{t('legend.color.green')}</span><br>"
            f"<span style='color:#6e6968;'>{t('legend.color.gray')}</span><br>"
            f"<span style='color:{ACCENT};'>{t('legend.color.yellow')}</span><br>"
            f"<span style='color:{SYNTAX_OVERRIDDEN_KEY};'>{t('legend.color.orange')}</span><br>"
            f"<span style='color:{DANGER};'>{t('legend.color.red')}</span>"
        )
        lbl_legend = QLabel(legend_html)
        lbl_legend.setTextFormat(Qt.TextFormat.RichText)
        lbl_legend.setStyleSheet(f"font-size: 12pt; color: {TEXT}; background: transparent;")
        layout.addWidget(lbl_legend)

        # --- Разделитель ---
        line = QLabel()
        line.setFixedHeight(1)
        line.setStyleSheet("background-color: #444444; margin: 10px 0;")
        layout.addWidget(line)

        # --- Поиск (динамический хоткей) ---
        key = "Ctrl+F"  # fallback
        if shortcut_service:
            actual_key = shortcut_service.current_key("main.find")
            if actual_key:
                key = actual_key

        search_html = (
            f"<b>{t('legend.search.header')}</b> "
            f"<span style='color:{ACCENT};'>{key}</span> "
            f"{t('legend.search.open')}<br>"
            f"<i>{t('legend.search.hint')}</i>"
        )
        lbl_search = QLabel(search_html)
        lbl_search.setTextFormat(Qt.TextFormat.RichText)
        lbl_search.setStyleSheet(f"font-size: 12pt; color: {TEXT}; background: transparent;")
        layout.addWidget(lbl_search)

        # --- Разделитель ---
        line2 = QLabel()
        line2.setFixedHeight(1)
        line2.setStyleSheet("background-color: #444444; margin: 10px 0;")
        layout.addWidget(line2)

        # --- Сохранение / Отмена ---
        save_html = (
            f"<b>{t('legend.save.header')}</b><br>"
            f"{t('legend.save.text')}"
        )

        lbl_save = QLabel(save_html)
        lbl_save.setTextFormat(Qt.TextFormat.RichText)
        lbl_save.setWordWrap(True)
        lbl_save.setStyleSheet(
            f"font-size: 12pt; color: {TEXT}; background: transparent;"
        )
        layout.addWidget(lbl_save)

        # --- Кнопка закрытия ---
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        btn_close = QPushButton(t("legend.btn_close"))
        btn_close.clicked.connect(self.accept)
        set_button_variant(btn_close, "primary")
        buttons_layout.addWidget(btn_close)
        layout.addLayout(buttons_layout)