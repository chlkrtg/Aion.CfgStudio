"""Страница редактора cfg.

Вся логика - в EditorPresenter.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QShortcut, QKeySequence
from PyQt6.QtWidgets import (
    QCheckBox, QComboBox, QLineEdit, QSpinBox,
    QTableWidgetItem, QHeaderView,
)

from logic.base_page import BasePage
from logic.constants import MAX_CONFIG_NAME_LEN
from logic.repositories import ConfigRepository, CommandRepository
from logic.services import ConfigService, EditorService
from logic.presenters import EditorPresenter
from ui.command_editor import Ui_CommandEditorDialog


class PageEditor(BasePage, Ui_CommandEditorDialog):

    MAX_CONFIG_NAME_LEN = MAX_CONFIG_NAME_LEN

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # ================== презентер ==================
        config_repo = ConfigRepository(self.db)
        command_repo = CommandRepository(self.db)
        config_service = ConfigService(config_repo, command_repo)
        service = EditorService(
            config_repo, command_repo, config_service
        )
        self.presenter = EditorPresenter(self, service)

        # ================== UI ==================
        self._setup_table()
        self._connect_signals()
        self._setup_shortcuts()

    # ============== настройка таблицы ==============

    def _setup_table(self):
        """Подготовка таблицы с командами."""
        t = self.tableCommands
        t.setColumnCount(5)
        t.setHorizontalHeaderLabels(
            ["Исп.", "Команда", "Значение", "Дефолт", "Описание"]
        )
        t.verticalHeader().setDefaultSectionSize(32)
        t.verticalHeader().setVisible(False)

        header = t.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        t.setColumnWidth(0, 50)
        t.setColumnWidth(1, 220)
        t.setColumnWidth(2, 140)
        t.setColumnWidth(3, 100)

        self.listPrefixes.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.listPrefixes.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        t.setAlternatingRowColors(False)

    # ============== сигналы ==============

    def _connect_signals(self):
        self.comboMode.currentIndexChanged.connect(
            lambda _i: self.presenter.apply_filters()
        )
        self.editSearch.textChanged.connect(
            lambda _t: self.presenter.apply_filters()
        )
        self.listPrefixes.currentItemChanged.connect(
            lambda _c, _p: self.presenter.apply_filters()
        )
        self.btnResetAll.clicked.connect(self.presenter.reset_all)
        self.btnCancel.clicked.connect(self.presenter.cancel)
        self.btnApply.clicked.connect(self.presenter.on_apply)

    def _setup_shortcuts(self):
        """Хоткеи, работающие на странице."""
        QShortcut(
            QKeySequence("F1"), self.listPrefixes
        ).activated.connect(lambda: self.window().go_video())

        QShortcut(
            QKeySequence("Ctrl+Q"), self.listPrefixes
        ).activated.connect(self.presenter.cancel)

    # ============== контекст ==============

    def set_context(self, config_id, server_id):
        """Делегирует презентеру."""
        self.presenter.set_context(config_id, server_id)

    # ============== жизненный цикл ==============

    def on_enter(self):
        self.presenter.on_enter()

    def on_leave(self):
        self.presenter.on_leave()

    # ============== UI-хелперы (зовёт презентер) ==============

    def make_group_header(self, row: int, code: str, name: str):
        """Рисует заголовок группы в строке row."""
        t = self.tableCommands

        font = QFont()
        font.setBold(True)
        font.setPointSize(font.pointSize() + 1)

        chk = QCheckBox()
        chk.setStyleSheet(
            "QCheckBox { margin-left: 12px; }"
            "QCheckBox::indicator { width: 14px; height: 14px; }"
        )
        t.setCellWidget(row, 0, chk)

        header = QTableWidgetItem(f"{code} — {name}")
        header.setData(Qt.ItemDataRole.FontRole, font)
        header.setFlags(Qt.ItemFlag.ItemIsEnabled)
        t.setItem(row, 1, header)

        for col in (2, 3, 4):
            empty = QTableWidgetItem("")
            empty.setFlags(Qt.ItemFlag.ItemIsEnabled)
            t.setItem(row, col, empty)

        t.setRowHeight(row, 36)

    def fill_command_row(self, row: int, cmd):
        """Рисует строку команды."""
        t = self.tableCommands

        # 0. чекбокс Исп.
        chk = QCheckBox()
        chk.setStyleSheet(
            "QCheckBox { margin-left: 12px; }"
            "QCheckBox::indicator { width: 14px; height: 14px; }"
        )
        t.setCellWidget(row, 0, chk)

        # 1. имя команды
        item_key = QTableWidgetItem(cmd["key_name"])
        item_key.setFlags(Qt.ItemFlag.ItemIsEnabled)
        t.setItem(row, 1, item_key)

        # 2. виджет значения
        w = self._make_value_widget(cmd)
        t.setCellWidget(row, 2, w)
        w.setEnabled(False)

        # 3. дефолт
        item_def = QTableWidgetItem(str(cmd["default_value"] or "—"))
        item_def.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item_def.setFlags(Qt.ItemFlag.ItemIsEnabled)
        t.setItem(row, 3, item_def)

        # 4. описание
        item_desc = QTableWidgetItem(cmd["description"] or "")
        item_desc.setFlags(Qt.ItemFlag.ItemIsEnabled)
        t.setItem(row, 4, item_desc)

        # чекбокс включает/выключает виджет значения
        chk.toggled.connect(
            lambda checked, ww=w: ww.setEnabled(checked)
        )

    def _make_value_widget(self, cmd):
        """Создаёт виджет значения в зависимости от типа команды."""
        vtype = (cmd["value_type"] or "string").lower()
        possible = cmd["possible_values"]

        if vtype == "bool" or (possible and "," in possible):
            w = QComboBox()
            if possible:
                for v in possible.split(","):
                    w.addItem(v.strip())
            else:
                w.addItem("0")
                w.addItem("1")
            if cmd["default_value"] is not None:
                idx = w.findText(str(cmd["default_value"]))
                if idx >= 0:
                    w.setCurrentIndex(idx)
            return w

        if vtype == "int":
            w = QSpinBox()
            w.setMinimum(
                int(cmd["min_value"]) if cmd["min_value"] else -999999
            )
            w.setMaximum(
                int(cmd["max_value"]) if cmd["max_value"] else 999999
            )
            if cmd["default_value"]:
                try:
                    w.setValue(int(cmd["default_value"]))
                except ValueError:
                    pass
            return w

        w = QLineEdit()
        if cmd["default_value"] is not None:
            w.setText(str(cmd["default_value"]))
        return w

    def apply_value_to_widget(self, widget, value: str):
        """Подставляет значение из БД в виджет ввода."""
        if isinstance(widget, QComboBox):
            idx = widget.findText(str(value))
            if idx >= 0:
                widget.setCurrentIndex(idx)
        elif isinstance(widget, QSpinBox):
            try:
                widget.setValue(int(value))
            except (ValueError, TypeError):
                pass
        elif isinstance(widget, QLineEdit):
            widget.setText(str(value))

    @staticmethod
    def read_widget_value(widget) -> str:
        """Читает значение из виджета."""
        if isinstance(widget, QComboBox):
            return widget.currentText()
        if isinstance(widget, QSpinBox):
            return str(widget.value())
        if isinstance(widget, QLineEdit):
            return widget.text().strip()
        return ""

    # ============== меню ==============

    def build_menus(self) -> dict:
        win = self.window()
        m = win.page_main
        return {
            "Помощь": [
                m.actionVideoHelp,
                m.actionAbout,
            ],
        }