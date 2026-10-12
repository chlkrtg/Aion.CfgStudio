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
        self.actionRename.triggered.connect(
            self.presenter.rename_config
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
        self.lblPreviewName.setText("— файл не выбран —")
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
        )

    # ============== меню ==============

    def build_menus(self) -> dict:
        win = self.window()
        return {
            "Файл": [
                self.actionNewConfig,
                self.actionImportCfg,
                self.actionExportCfg,
                None,
                self.actionChangeProfile,
                self.actionChangeServer,
            ],
            "Помощь": [
                win.actionShortcuts,
                None,
                self.actionVideoHelp,
                self.actionAbout,
            ],
        }

    def _show_about(self):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.about(
            self, "О программе",
            "Aion.CfgStudio v1.0  by @chealkrtengghnle\n\n"
            "Редактор конфигурационного файла system.cfg для Aion."
        )

    # ============== контекстное меню ==============

    def _show_context_menu(self, pos):
        item = self.treeConfigs.itemAt(pos)
        if item is None:
            return

        self.treeConfigs.setCurrentItem(item)

        menu = build_context_menu(self, [
            ("Редактировать", self.presenter.open_selected),
            None,
            ("Дублировать", self.presenter.duplicate_config),
            None,
            ("Переименовать (F2)", self.presenter.rename_config),
            None,
            ("Экспортировать (Ctrl + S)", self.presenter.export_config),
            None,
            ("Удалить (Delete)", self.presenter.delete_config),
        ])
        menu.exec(self.treeConfigs.mapToGlobal(pos))