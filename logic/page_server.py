"""Страница выбора сервера внутри профиля.

Вся логика - в ServerPresenter.
"""
from PyQt6.QtCore import Qt, QTimer

from logic.core.constants import MAX_NOTE_LEN, MAX_SERVER_NAME_LEN
from logic.core.i18n import t
from logic.core.i18n import t as _t
from logic.presenters import ServerPresenter
from logic.widgets.base_page import BasePage
from logic.widgets.context_menu import build_context_menu
from logic.widgets.hover_helpers import set_button_variant
from logic.widgets.shortcut_labels import with_hotkey
from logic.widgets.shortcuts import bind_actions
from ui.server_select import Ui_ServerSelectDialog


class PageServer(BasePage, Ui_ServerSelectDialog):

    # константы доступны презентеру через view.MAX_*
    MAX_SERVER_NAME_LEN = MAX_SERVER_NAME_LEN
    MAX_NOTE_LEN = MAX_NOTE_LEN

    def __init__(self, parent, service, reference):
        super().__init__(parent)
        self.setupUi(self)

        # =========== презентер ===========
        self.presenter = ServerPresenter(self, service, reference)

        # =========== UI ===========
        self.listServers.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )
        self.listServers.customContextMenuRequested.connect(
            self._show_context_menu
        )

        # скрыть блок Регион: пока неактуально
        self.lblRegionCaption.hide()
        self.lblRegionValue.hide()

        self.editNote.setReadOnly(False)
        self.btnBrowseExport.clicked.connect(self._browse_export_path)
        self.btnClearExportPath.clicked.connect(self._clear_export_path)

        # debounce заметки - как в профиле
        self._save_timer = QTimer(self)
        self._save_timer.setSingleShot(True)
        self._save_timer.setInterval(1000)
        self._save_timer.timeout.connect(self.presenter.save_note)
        self.editNote.textChanged.connect(
            lambda: self._save_timer.start()
        )

        self._connect_signals()

        # хоткеи через реестр (см. rebind_shortcuts)
        self._shortcut_handles: dict[str, list] = {}
        self.rebind_shortcuts()
        self.retranslate()

        self.lblTitle.setStyleSheet(
            "font-size: 14pt; font-weight: 700; color: #d4a95a; "
            "background: transparent;"
        )

        self.lblServersTitle.setStyleSheet(
            "font-size: 12pt; font-weight: 700; color: #b0b0c0; "
            "background: transparent;"
        )
        self.lblServerDetailsTitle.setStyleSheet(
            "font-size: 12pt; font-weight: 700; color: #b0b0c0; "
            "background: transparent;"
        )

    # ============== сигналы ==============

    def _connect_signals(self):
        self.btnNewServer.clicked.connect(self.presenter.create)
        self.btnRenameServer.clicked.connect(self.presenter.rename)
        self.btnDeleteServer.clicked.connect(self.presenter.delete)
        self.btnEnter.clicked.connect(self.presenter.enter)

        self.listServers.currentItemChanged.connect(
            self.presenter.on_server_selected
        )
        self.listServers.itemDoubleClicked.connect(
            lambda _: self.presenter.enter()
        )
        self.btnVideoHelp.clicked.connect(
            lambda: self.window().go_video()
        )
        self.btnCancel.clicked.connect(
            lambda: self.window().go_profile()
        )

    def _bindings(self) -> dict:
        return {
            "global.video":  lambda: self.window().go_video(),
            "server.enter":  self.presenter.enter,
            "server.create": self.presenter.create,
            "server.rename": self.presenter.rename,
            "server.delete": self.presenter.delete,
            "server.quit":   lambda: self.window().go_profile(),
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
            keys=self.window().shortcut_service.keys_for_scope("server"),
        )

    def retranslate(self):
        """Обновляет подписи кнопок с актуальными хоткеями."""
        svc = self.window().shortcut_service

        self.setWindowTitle(t("server.window_title"))

        self.lblServersTitle.setText(t("server.lbl_servers"))
        self.lblServerDetailsTitle.setText(t("server.lbl_details"))
        self.lblRegionCaption.setText(t("server.lbl_region"))
        self.lblConfigsCaption.setText(t("server.lbl_configs"))

        self.editNote.setPlaceholderText(
            t("server.note_placeholder").format(n=MAX_NOTE_LEN)
        )

        self.btnNewServer.setText(
            with_hotkey(t("server.btn_new"), svc, "server.create")
        )
        self.btnRenameServer.setText(
            with_hotkey(t("server.btn_rename"), svc, "server.rename")
        )
        self.btnDeleteServer.setText(
            with_hotkey(t("server.btn_delete"), svc, "server.delete")
        )
        self.btnEnter.setText(
            with_hotkey(t("server.btn_enter"), svc, "server.enter")
        )
        self.btnVideoHelp.setText(
            with_hotkey(t("server.btn_video"), svc, "global.video")
        )
        self.btnCancel.setText(
            with_hotkey(t("server.btn_back"), svc, "server.quit")
        )

        self.lblExportPathCaption.setText(t("server.lbl_export_path"))
        self.editExportPath.setPlaceholderText(
            t("server.export_path_placeholder")
        )
        self.btnBrowseExport.setText(t("server.btn_browse"))
        self.btnClearExportPath.setText(t("server.btn_clear"))

        # переприменить текущее состояние
        self.presenter.on_server_selected(
            self.listServers.currentItem(), None
        )

        # обновить плейсхолдер (если список пуст)
        if self.listServers.count() == 0 or (
                self.listServers.count() == 1
                and self.listServers.item(0).data(
            Qt.ItemDataRole.UserRole) is None
        ):
            self.listServers.clear()
            from logic.widgets.empty_state import add_empty_item
            self.listServers.blockSignals(True)
            add_empty_item(self.listServers, _t("empty.servers"))
            self.listServers.setCurrentItem(None)
            self.listServers.blockSignals(False)

        set_button_variant(self.btnEnter, "primary")
        set_button_variant(self.btnCancel, "ghost")
        set_button_variant(self.btnDeleteServer, "danger")

    # ============== жизненный цикл ==============

    def set_profile(self, profile_id: int):
        """Делегирует презентеру - какой профиль открыт."""
        self.presenter.set_profile(profile_id)

    def on_enter(self):
        self.presenter.on_enter()

    def on_leave(self) -> bool:
        if self._save_timer.isActive():
            self._save_timer.stop()
        self.presenter.on_leave()

        return True

    # ============== UI-хелперы (зовёт презентер) ==============

    def fill_details(self, server, stats):
        """Заполняет правую панель данными сервера."""
        self.lblServerName.setText(
            t("server.lbl_selected").format(name=server["name"])
        )
        self.lblRegionValue.setText(server["region"] or "—")
        self.lblConfigsValue.setText(str(stats["configs"]))

        self.editNote.blockSignals(True)
        self.editNote.setPlainText(server["note"] or "")
        self.editNote.blockSignals(False)

        self.editExportPath.setText(server["export_path"] or "")

        first_letter = (server["name"] or "?")[0].upper()
        self.lblServerIcon.setText(first_letter)
        self.lblServerIcon.setStyleSheet(
            "font-size: 60px; color: #d4a95a; font-weight: bold;"
        )

    def clear_details(self):
        """Очищает правую панель."""
        self.lblServerName.setText(t("server.lbl_none"))
        self.lblRegionValue.setText("—")
        self.lblConfigsValue.setText("0")
        self.editNote.blockSignals(True)
        self.editNote.clear()
        self.editNote.blockSignals(False)
        self.editExportPath.clear()
        self.lblServerIcon.clear()

    def set_controls_enabled(self, enabled: bool):
        """Включает/выключает контролы, требующие выбранного сервера."""
        super().set_controls_enabled(
            enabled,
            self.btnRenameServer,
            self.btnDeleteServer,
            self.btnEnter,
            self.editNote,
            self.editExportPath,
            self.btnBrowseExport,
            self.btnClearExportPath,
        )

    # ============== контекстное меню ==============

    def _show_context_menu(self, pos):
        item = self.listServers.itemAt(pos)
        if item is None:
            return

        if item.data(Qt.ItemDataRole.UserRole) is None:
            return

        self.listServers.setCurrentItem(item)
        svc = self.window().shortcut_service

        menu = build_context_menu(self, [
            (with_hotkey(t("ctx.enter"), svc, "server.enter"),
             self.presenter.enter),
            None,
            (t("ctx.duplicate"), self.presenter.duplicate),
            None,
            (with_hotkey(t("ctx.rename"), svc, "server.rename"),
             self.presenter.rename),
            None,
            (with_hotkey(t("ctx.delete"), svc, "server.delete"),
             self.presenter.delete),
        ])
        menu.exec(self.listServers.mapToGlobal(pos))

    def _browse_export_path(self):
        """Открывает выбор папки для экспорта по умолчанию."""
        from PyQt6.QtWidgets import QFileDialog
        current = self.editExportPath.text().strip()
        path = QFileDialog.getExistingDirectory(
            self,
            t("server.dialog.export_path.title"),
            current or "",
        )
        if not path:
            return
        self.presenter.update_export_path(path)

    def _clear_export_path(self):
        """Очищает путь экспорта по умолчанию."""
        self.presenter.update_export_path("")

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