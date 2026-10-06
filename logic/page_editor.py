"""Страница редактора cfg.

Вся логика - в EditorPresenter.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QShortcut, QKeySequence
from PyQt6.QtWidgets import (
    QTableWidgetItem, QHeaderView, QAbstractItemView
)

from logic.base_page import BasePage
from logic.constants import MAX_CONFIG_NAME_LEN
from logic.repositories import ConfigRepository, CommandRepository
from logic.value_delegate import ValueDelegate
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

        t.setEditTriggers(
            QAbstractItemView.EditTrigger.CurrentChanged
            | QAbstractItemView.EditTrigger.DoubleClicked
            | QAbstractItemView.EditTrigger.EditKeyPressed
        )

        t.setColumnWidth(0, 50)
        t.setColumnWidth(1, 220)
        t.setColumnWidth(2, 140)
        t.setColumnWidth(3, 100)

        # ← делегат для колонки значений
        t.setItemDelegateForColumn(2, ValueDelegate(t))

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

        # ← сигнал изменения item (включая чекбоксы)
        self.tableCommands.itemChanged.connect(
            self.presenter.on_item_changed
        )

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
        self.tableCommands.clearSelection()
        self.tableCommands.setCurrentCell(-1, -1)
        self.presenter.on_leave()

    # ============== UI-хелперы (зовёт презентер) ==============

    def make_group_header(self, row: int, code: str, name: str):
        """Рисует заголовок группы в строке row."""
        t = self.tableCommands

        font = QFont()
        font.setBold(True)
        font.setPointSize(font.pointSize() + 1)

        # чекбокс через item (не виджет)
        chk_item = QTableWidgetItem()
        chk_item.setFlags(
            Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsUserCheckable
        )
        chk_item.setCheckState(Qt.CheckState.Unchecked)
        chk_item.setData(Qt.ItemDataRole.UserRole, f"GROUP:{code}")
        t.setItem(row, 0, chk_item)

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
        chk_item = QTableWidgetItem()
        chk_item.setFlags(
            Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsUserCheckable
        )
        chk_item.setCheckState(Qt.CheckState.Unchecked)
        chk_item.setData(Qt.ItemDataRole.UserRole, f"CMD:{cmd['id']}")
        t.setItem(row, 0, chk_item)

        # 1. имя команды
        item_key = QTableWidgetItem(cmd["key_name"])
        item_key.setFlags(Qt.ItemFlag.ItemIsEnabled)
        t.setItem(row, 1, item_key)

        # 2. значение — данные для делегата
        value_item = QTableWidgetItem(str(cmd["default_value"] or ""))

        # если команда не отмечена — ячейка «выключена»
        value_item.setFlags(
            Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable
        )

        # метаданные для делегата
        value_item.setData(
            ValueDelegate.CMD_TYPE_ROLE,
            (cmd["value_type"] or "string").lower()
        )
        value_item.setData(
            ValueDelegate.CMD_POSSIBLE_ROLE,
            cmd["possible_values"]
        )
        value_item.setData(ValueDelegate.CMD_MIN_ROLE, cmd["min_value"])
        value_item.setData(ValueDelegate.CMD_MAX_ROLE, cmd["max_value"])
        t.setItem(row, 2, value_item)

        # 3. дефолт
        item_def = QTableWidgetItem(str(cmd["default_value"] or "—"))
        item_def.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item_def.setFlags(Qt.ItemFlag.ItemIsEnabled)
        t.setItem(row, 3, item_def)

        # 4. описание
        item_desc = QTableWidgetItem(cmd["description"] or "")
        item_desc.setFlags(Qt.ItemFlag.ItemIsEnabled)
        t.setItem(row, 4, item_desc)

    def set_value_enabled(self, row: int, enabled: bool):
        """Включает/выключает ячейку значения в строке row."""
        item = self.tableCommands.item(row, 2)
        if item is None:
            return
        flags = item.flags()
        if enabled:
            flags |= Qt.ItemFlag.ItemIsEditable
        else:
            flags &= ~Qt.ItemFlag.ItemIsEditable
        item.setFlags(flags)

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