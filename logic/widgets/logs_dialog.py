"""Диалог истории изменений с прокруткой."""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QHeaderView, QPushButton, QAbstractItemView, QLineEdit,
)

from logic.core.i18n import t
from logic.widgets.hover_helpers import set_button_variant


class LogsDialog(QDialog):
    """Показывает историю изменений в таблице с прокруткой и поиском."""

    def __init__(self, parent, logs: list, filename: str = ""):
        super().__init__(parent)

        if filename:
            title = t("logs.window_title").format(name=filename)
        else:
            title = t("logs.window_title_short")

        self.setWindowTitle(title)
        self.resize(900, 500)
        self.setFixedSize(900, 500)

        layout = QVBoxLayout(self)

        # ======= поле поиска =======
        self.edit_search = QLineEdit()
        self.edit_search.setPlaceholderText(t("logs.search_placeholder"))
        layout.addWidget(self.edit_search)

        # ======= таблица =======
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            t("logs.col_date"),
            t("logs.col_command"),
            t("logs.col_old"),
            t("logs.col_new"),
        ])
        self.table.setRowCount(len(logs))
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.table.verticalHeader().setVisible(False)
        self.table.setSortingEnabled(True)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.table.setColumnWidth(1, 220)
        self.table.setColumnWidth(2, 180)

        for i, row in enumerate(logs):
            self.table.setItem(i, 0, QTableWidgetItem(str(row["changed_at"])))
            self.table.setItem(i, 1, QTableWidgetItem(str(row["key_name"])))
            self.table.setItem(i, 2, QTableWidgetItem(str(row["old_value"])))
            self.table.setItem(i, 3, QTableWidgetItem(str(row["new_value"])))

        self.table.sortItems(0, Qt.SortOrder.DescendingOrder)
        layout.addWidget(self.table)

        # ======= кнопки =======
        buttons = QHBoxLayout()
        buttons.addStretch()
        btn_close = QPushButton(t("logs.btn_close"))
        btn_close.clicked.connect(self.accept)
        buttons.addWidget(btn_close)
        layout.addLayout(buttons)

        self.edit_search.textChanged.connect(self._filter)

        set_button_variant(btn_close, "ghost")

    def _filter(self, text: str):
        """Скрывает строки, не подходящие под поиск (по всем колонкам)."""
        text = text.lower().strip()
        for i in range(self.table.rowCount()):
            # Собираем текст из всех 4 колонок в одну строку
            row_text = ""
            for col in range(self.table.columnCount()):
                item = self.table.item(i, col)
                if item:
                    row_text += item.text().lower() + " "

            match = text in row_text
            self.table.setRowHidden(i, bool(text) and not match)