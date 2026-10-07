"""Главная страница: дерево cfg-файлов выбранного сервера.

Вся логика - в MainPresenter.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QShortcut, QKeySequence

from logic.base_page import BasePage
from logic.context_menu import build_context_menu
from logic.shortcuts import bind_shortcuts, FOCUSED
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

        # хоткеи
        bind_shortcuts(self.treeConfigs, {
            "F1": lambda: self.window().go_video(),
            "F2": self.presenter.rename_config,
            "Delete": self.presenter.delete_config,
            "Ctrl+N": lambda: self.window().go_editor(None),
            "Ctrl+O": self.presenter.import_config,
            "Ctrl+S": self.presenter.export_config,
            "Ctrl+E": self.presenter.open_selected,
        }, FOCUSED)

        # Ctrl+Q - назад к выбору сервера
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(
            self.presenter.change_server
        )

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

    # ============== контекст ==============

    def set_context(self, profile_id: int, server_id: int):
        """Делегирует презентеру - какой профиль / сервер открыт."""
        self.presenter.set_context(profile_id, server_id)

    # ============== жизненный цикл ==============

    def on_enter(self):
        self.presenter.on_enter()

    def on_leave(self):
        self.presenter.on_leave()

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