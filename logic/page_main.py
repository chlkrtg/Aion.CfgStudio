"""Главная страница: дерево cfg-файлов выбранного сервера.

Вся логика - в MainPresenter.
"""
from PyQt6.QtCore import Qt

from logic.base_page import BasePage
from logic.context_menu import build_context_menu
from logic.shortcuts import bind_actions
from logic.constants import MAX_CONFIG_NAME_LEN
from logic.presenters import MainPresenter
from ui.main_window import Ui_MainWindow


class PageMain(BasePage, Ui_MainWindow):

    # константы доступны презентеру через view.MAX_*
    MAX_CONFIG_NAME_LEN = MAX_CONFIG_NAME_LEN

    def __init__(self, parent, service, reference):
        super().__init__(parent)
        self.setupUi(self)

        # =============== презентер ===============
        self.presenter = MainPresenter(self, service, reference)

        # =============== UI ===============
        self.treeConfigs.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )
        self.treeConfigs.customContextMenuRequested.connect(
            self._show_context_menu
        )

        self.treeConfigs.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.editFilter.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self._connect_signals()

        # хоткеи через реестр (см. rebind_shortcuts)
        self._shortcut_handles: dict[str, list] = {}
        self.rebind_shortcuts()
        self.retranslate()

    # ============== сигналы ==============

    def _connect_signals(self):
        self.btnAddConfig.clicked.connect(
            lambda: self.window().go_editor(None)
        )
        self.btnOpenEditor.clicked.connect(self.presenter.open_selected)
        self.btnImportConfig.clicked.connect(self.presenter.import_config)
        self.btnExportConfig.clicked.connect(self.presenter.export_config)
        self.btnDeleteConfig.clicked.connect(self.presenter.delete_config)
        self.btnShowLogs.clicked.connect(self.presenter.show_logs)
        self.btnRenameConfig.clicked.connect(self.presenter.rename_config)
        self.btnSavePreview.clicked.connect(self.presenter.save_preview)
        self.btnRevertPreview.clicked.connect(self.presenter.revert_preview)

        self.treeConfigs.itemSelectionChanged.connect(
            self.presenter.on_selection
        )
        self.editFilter.textChanged.connect(self.apply_filter)

        # actions (меню)
        self.actionChangeServer.triggered.connect(
            self.presenter.change_server
        )
        self.actionVideoHelp.triggered.connect(
            lambda: self.window().go_video()
        )
        self.actionChangeProfile.triggered.connect(
            lambda: self.window().go_profile()
        )
        self.actionImportCfg.triggered.connect(
            self.presenter.import_config
        )
        self.actionExportCfg.triggered.connect(
            self.presenter.export_config
        )
        self.actionAbout.triggered.connect(self._show_about)
        self.actionNewConfig.triggered.connect(
            lambda: self.window().go_editor(None)
        )

    def _bindings(self) -> dict:
        return {
            "global.video": lambda: self.window().go_video(),
            "main.open":    self.presenter.open_selected,
            "main.create":  lambda: self.window().go_editor(None),
            "main.import":  self.presenter.import_config,
            "main.export":  self.presenter.export_config,
            "main.rename":  self.presenter.rename_config,
            "main.delete":  self.presenter.delete_config,
            "main.save":    self.presenter.save_preview,
            "main.quit":    self.presenter.change_server,
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
            keys=self.window().shortcut_service.keys_for_scope("main"),
        )

    def retranslate(self):
        """Обновляет подписи кнопок с актуальными хоткеями."""
        from logic.i18n import t
        from logic.shortcut_labels import with_hotkey
        svc = self.window().shortcut_service

        # заголовки
        self.lblTreeTitle.setText(t("main.lbl_tree_title"))
        self.lblPreviewTitle.setText(t("main.lbl_preview_title"))

        # колонки дерева
        self.treeConfigs.setHeaderLabels([
            t("main.col_name"),
            t("main.col_modified"),
        ])

        # placeholder фильтра
        self.editFilter.setPlaceholderText(t("main.filter_placeholder"))

        # кнопки с хоткеями
        self.btnAddConfig.setText(
            with_hotkey(t("main.btn_new"), svc, "main.create")
        )
        self.btnImportConfig.setText(
            with_hotkey(t("main.btn_import"), svc, "main.import")
        )
        self.btnExportConfig.setText(
            with_hotkey(t("main.btn_export"), svc, "main.export")
        )
        self.btnRenameConfig.setText(
            with_hotkey(t("main.btn_rename"), svc, "main.rename")
        )
        self.btnDeleteConfig.setText(
            with_hotkey(t("main.btn_delete"), svc, "main.delete")
        )
        self.btnSavePreview.setText(
            with_hotkey(t("main.btn_save"), svc, "main.save")
        )
        self.btnOpenEditor.setText(
            with_hotkey(t("main.btn_open_editor"), svc, "main.open")
        )

        # кнопки без хоткеев
        self.btnRevertPreview.setText(t("main.btn_revert"))
        self.btnShowLogs.setText(t("main.btn_show_logs"))

        # QAction
        self.actionNewConfig.setText(t("main.action_new_config"))
        self.actionImportCfg.setText(t("main.action_import_cfg"))
        self.actionExportCfg.setText(t("main.action_export_cfg"))
        self.actionChangeProfile.setText(t("main.action_change_profile"))
        self.actionChangeServer.setText(t("main.action_change_server"))
        self.actionVideoHelp.setText(t("main.action_video_help"))
        self.actionAbout.setText(t("main.action_about"))

        # переприменить текущее состояние
        self.presenter.on_selection()

    # ============== контекст ==============

    def set_context(self, profile_id: int, server_id: int):
        """Делегирует презентеру - какой профиль / сервер открыт."""
        self.presenter.set_context(profile_id, server_id)

    # ============== жизненный цикл ==============

    def on_enter(self):
        self.presenter.on_enter()

    def on_leave(self) -> bool:
        return self.presenter.on_leave()

    # ============== UI-хелперы (зовёт презентер) ==============

    def apply_filter(self, text: str):
        """Слот textChanged - делегирует презентеру."""
        self.presenter.apply_filter(text)

    def clear_preview(self):
        """Сбрасывает панель предпросмотра."""
        from logic.i18n import t
        self.lblPreviewName.setText(t("main.lbl_preview_none"))
        self.editPreview.clear()

    def set_controls_enabled(self, enabled: bool):
        """Включает/выключает контролы, требующие выбранного cfg."""
        super().set_controls_enabled(
            enabled,
            self.btnOpenEditor,
            self.btnExportConfig,
            self.btnDeleteConfig,
            self.btnShowLogs,
            self.btnRenameConfig,
            self.btnSavePreview,
            self.btnRevertPreview,
            self.editPreview,
        )

    # ============== меню ==============

    def build_menus(self) -> dict:
        from logic.i18n import t
        win = self.window()
        return {
            t("menu.file"): [
                self.actionNewConfig,
                self.actionImportCfg,
                self.actionExportCfg,
                None,
                self.actionChangeProfile,
                self.actionChangeServer,
            ],
            t("menu.settings"): [
                win.actionShortcuts,
                None,
                win.actionLangRu,
                win.actionLangEn,
            ],
            t("menu.help"): [
                self.actionVideoHelp,
                self.actionAbout,
            ],
        }

    def _show_about(self):
        from PyQt6.QtWidgets import QMessageBox
        from logic.i18n import t
        QMessageBox.about(
            self,
            t("dialog.about_title"),
            t("dialog.about_text"),
        )

    # ============== контекстное меню ==============

    def _show_context_menu(self, pos):
        from logic.i18n import t
        from logic.shortcut_labels import with_hotkey

        item = self.treeConfigs.itemAt(pos)
        if item is None:
            return

        self.treeConfigs.setCurrentItem(item)
        svc = self.window().shortcut_service

        menu = build_context_menu(self, [
            (with_hotkey(t("ctx.edit"), svc, "main.open"),
             self.presenter.open_selected),
            None,
            (t("ctx.duplicate"), self.presenter.duplicate_config),
            None,
            (with_hotkey(t("ctx.rename"), svc, "main.rename"),
             self.presenter.rename_config),
            None,
            (with_hotkey(t("ctx.export"), svc, "main.export"),
             self.presenter.export_config),
            None,
            (with_hotkey(t("ctx.delete"), svc, "main.delete"),
             self.presenter.delete_config),
        ])
        menu.exec(self.treeConfigs.mapToGlobal(pos))