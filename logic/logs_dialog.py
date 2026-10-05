"""Диалог истории изменений с прокруткой."""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QHeaderView, QPushButton, QAbstractItemView, QLineEdit,
)


class LogsDialog(QDialog):
    """Показывает историю изменений в таблице с прокруткой и поиском."""

    def __init__(self, parent, logs: list, filename: str = ""):
        super().__init__(parent)
        title = "История изменений"
        if filename:
            title += f" — {filename}"
        self.setWindowTitle(title)
        self.resize(900, 500)

        self.setFixedSize(900, 500)

        layout = QVBoxLayout(self)

        # ======= поле поиска =======
        self.edit_search = QLineEdit()
        self.edit_search.setPlaceholderText("Поиск по команде или дате...")
        layout.addWidget(self.edit_search)

        # ======= таблица =======
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ["Дата", "Команда", "Было", "Стало"]
        )
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

        # сортируем по дате, новые сверху
        self.table.sortItems(0, Qt.SortOrder.DescendingOrder)

        layout.addWidget(self.table)

        # ======= кнопки =======
        buttons = QHBoxLayout()
        buttons.addStretch()
        btn_close = QPushButton("Закрыть")
        btn_close.clicked.connect(self.accept)
        buttons.addWidget(btn_close)
        layout.addLayout(buttons)

        # ======= фильтр =======
        self.edit_search.textChanged.connect(self._filter)

    def _filter(self, text: str):
        """Скрывает строки, не подходящие под поиск (по команде или дате)."""
        text = text.lower().strip()
        for i in range(self.table.rowCount()):
            date_item = self.table.item(i, 0)
            key_item = self.table.item(i, 1)
            date_text = date_item.text().lower() if date_item else ""
            key_text = key_item.text().lower() if key_item else ""

            match = (text in key_text) or (text in date_text)
            self.table.setRowHidden(i, bool(text) and not match)