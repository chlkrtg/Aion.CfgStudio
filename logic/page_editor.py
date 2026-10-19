"""Страница редактора cfg.

Вся логика - в EditorPresenter.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import (
    QTableWidgetItem, QHeaderView, QAbstractItemView
)

from logic.widgets.base_page import BasePage
from logic.core.constants import MAX_CONFIG_NAME_LEN
from logic.widgets.hover_helpers import set_button_variant
from logic.widgets.shortcuts import bind_actions
from logic.widgets.value_delegate import ValueDelegate
from logic.widgets.shortcut_labels import with_hotkey
from logic.presenters import EditorPresenter
from logic.core.i18n import t, plural_ru
from ui.command_editor import Ui_CommandEditorDialog
from logic.widgets.checkbox_delegate import CheckboxDelegate


class PageEditor(BasePage, Ui_CommandEditorDialog):

    MAX_CONFIG_NAME_LEN = MAX_CONFIG_NAME_LEN

    def __init__(self, parent, service):
        super().__init__(parent)
        self.setupUi(self)

        # ================== презентер ==================
        self.presenter = EditorPresenter(self, service)

        # ================== UI ==================
        self._setup_table()
        self._connect_signals()

        # хоткеи (см. rebind_shortcuts)
        self._shortcut_handles: dict[str, list] = {}
        self.rebind_shortcuts()
        self.retranslate()

        self.lblFileName.setStyleSheet(
            "font-size: 13pt; font-weight: 600; color: #d4a95a; "
            "background: transparent;"
        )
        self.lblPrefixesTitle.setStyleSheet(
            "font-size: 11pt; font-weight: 700; color: #b0b0c0; "
            "background: transparent;"
        )

    # ============== настройка таблицы ==============

    def _setup_table(self):
        tbl = self.tableCommands
        tbl.setColumnCount(5)
        tbl.setHorizontalHeaderLabels([
            t("editor.col_use"),
            t("editor.col_command"),
            t("editor.col_value"),
            t("editor.col_default"),
            t("editor.col_description"),
        ])
        tbl.verticalHeader().setDefaultSectionSize(32)
        tbl.verticalHeader().setVisible(False)

        header = tbl.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        tbl.setEditTriggers(
            QAbstractItemView.EditTrigger.CurrentChanged
            | QAbstractItemView.EditTrigger.DoubleClicked
            | QAbstractItemView.EditTrigger.EditKeyPressed
        )

        tbl.setColumnWidth(0, 50)
        tbl.setColumnWidth(1, 220)
        tbl.setColumnWidth(2, 140)
        tbl.setColumnWidth(3, 100)

        # делегат для колонки значений
        tbl.setItemDelegateForColumn(2, ValueDelegate(tbl))

        # делегат для чекбокса
        tbl.setItemDelegateForColumn(0, CheckboxDelegate(tbl))

        self.listPrefixes.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.listPrefixes.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        tbl.setAlternatingRowColors(False)

    # ============== сигналы ==============

    def _connect_signals(self):
        self.editSearch.textChanged.connect(
            lambda _t: self.presenter.apply_filters()
        )
        self.listPrefixes.currentItemChanged.connect(
            lambda _c, _p: self.presenter.apply_filters()
        )
        self.btnMakeDefaults.clicked.connect(
            self.presenter.on_make_defaults
        )
        self.btnResetAll.clicked.connect(self.presenter.reset_all)
        self.btnCancel.clicked.connect(self.presenter.cancel)
        self.btnApply.clicked.connect(self.presenter.on_apply)

        # ← сигнал изменения item (включая чекбоксы)
        self.tableCommands.itemChanged.connect(
            self.presenter.on_item_changed
        )

    def _bindings(self) -> dict:
        return {
            "global.video": lambda: self.window().go_video(),
            "editor.cancel": self.presenter.cancel,
        }

    def rebind_shortcuts(self):
        for handles in self._shortcut_handles.values():
            for sc in handles:
                sc.setEnabled(False)
                sc.deleteLater()
        self._shortcut_handles.clear()

        self._shortcut_handles = bind_actions(
            self,
            self._bindings(),
            keys=self.window().shortcut_service.keys_for_scope("editor"),
        )

    def retranslate(self):
        """Обновляет подписи кнопок с актуальными хоткеями."""
        svc = self.window().shortcut_service

        # счётчик обновится в apply_filters

        self.setWindowTitle(t("editor.window_title"))
        self.editSearch.setPlaceholderText(t("editor.search_placeholder"))

        self.lblPrefixesTitle.setText(t("editor.lbl_prefixes_title"))
        self.lblPrefixInfo.setText(t("editor.lbl_prefix_info"))

        self.tableCommands.setHorizontalHeaderLabels([
            t("editor.col_use"),
            t("editor.col_command"),
            t("editor.col_value"),
            t("editor.col_default"),
            t("editor.col_description"),
        ])

        self.btnResetAll.setText(t("editor.btn_reset_all"))
        self.btnMakeDefaults.setText(t("editor.btn_make_defaults"))
        self.btnCancel.setText(
            with_hotkey(t("editor.btn_cancel"), svc, "editor.cancel")
        )
        self.btnApply.setText(t("editor.btn_apply"))

        if self.presenter._commands is not None:
            # 1. синхронизировать _state с текущей таблицей
            self.presenter._sync_state_from_table()
            saved_state = dict(self.presenter._state)

            # 2. перезагрузить команды / префиксы
            self.presenter._commands = None
            self.presenter._prefixes = None
            self.presenter.refresh()

            # 3. восстановить состояние (галочки / значения)
            self.presenter._state = saved_state
            self.presenter.apply_filters(sync=False)

        set_button_variant(self.btnApply, "primary")
        set_button_variant(self.btnCancel, "ghost")
        set_button_variant(self.btnResetAll, "ghost")

    def set_command_count(self, n: int):
        """Обновляет счётчик видимых команд."""
        from logic.core.i18n import t
        from logic.core import i18n

        if i18n.get_language() == "ru":
            text = plural_ru(n, "команда", "команды", "команд")
        else:
            text = "command" if n == 1 else "commands"

        self.lblCommandCount.setText(f"{n} {text}")

    # ============== контекст ==============

    def set_context(self, config_id, server_id):
        """Делегирует презентеру."""
        self.presenter.set_context(config_id, server_id)

    # ============== жизненный цикл ==============

    def on_enter(self):
        self.presenter.on_enter()

    def on_leave(self) -> bool:
        # сначала спрашиваем презентер (диалог сохранения)
        result = self.presenter.on_leave()
        if result is not True:
            return False  # отмена: не чистим UI и не уходим

        # только если уходим, сбрасываем выделение
        self.tableCommands.clearSelection()
        self.tableCommands.setCurrentCell(-1, -1)

        return True

    # ============== UI-хелперы (зовёт презентер) ==============

    def make_group_header(self, row, code, name,
                          visible_count=0, total_count=0):
        t = self.tableCommands

        font = QFont()
        font.setBold(True)
        font.setPointSize(font.pointSize() + 1)

        accent = QColor("#d4a95a")
        bg = QColor("#23252e")  # слегка светлее обычного

        # 0. чекбокс — обычный фон
        chk_item = QTableWidgetItem()
        chk_item.setFlags(
            Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsUserCheckable
        )
        chk_item.setCheckState(Qt.CheckState.Unchecked)
        chk_item.setData(Qt.ItemDataRole.UserRole, f"GROUP:{code}")
        chk_item.setBackground(bg)
        t.setItem(row, 0, chk_item)

        # 1. заголовок — accent текст
        label = f"{code} — {name}"
        if visible_count and visible_count < total_count:
            label += f"   ({visible_count} из {total_count})"

        header = QTableWidgetItem(label)
        header.setData(Qt.ItemDataRole.FontRole, font)
        header.setFlags(Qt.ItemFlag.ItemIsEnabled)
        header.setForeground(accent)
        header.setBackground(bg)
        t.setItem(row, 1, header)

        for col in (2, 3, 4):
            empty = QTableWidgetItem("")
            empty.setFlags(Qt.ItemFlag.ItemIsEnabled)
            empty.setBackground(bg)
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
            t("menu.settings"): [
                win.actionShortcuts,
                None,
                win.actionLangRu,
                win.actionLangEn,
            ],
            t("menu.help"): [
                m.actionVideoHelp,
                m.actionAbout,
            ],
        }