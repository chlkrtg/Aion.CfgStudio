"""Главная страница: дерево cfg-файлов выбранного сервера.

Вся логика - в MainPresenter.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton

from logic.core.constants import MAX_CONFIG_NAME_LEN
from logic.core.i18n import t
from logic.core.i18n import t as _t
from logic.presenters import MainPresenter
from logic.widgets.base_page import BasePage
from logic.widgets.cfg_highlighter import CfgHighlighter
from logic.widgets.context_menu import build_context_menu
from logic.widgets.hover_helpers import set_button_variant
from logic.widgets.legend_dialog import LegendDialog
from logic.widgets.line_numbers import CodeEditor
from logic.widgets.search_panel import SearchPanel
from logic.widgets.shortcut_labels import with_hotkey
from logic.widgets.shortcuts import bind_actions
from logic.widgets.theme import (
    ACCENT,
    DANGER,
    SYNTAX_OVERRIDDEN_KEY,
    SYNTAX_UNKNOWN_KEY,
)
from ui.main_window import Ui_MainWindow


class PageMain(BasePage, Ui_MainWindow):

    # константы доступны презентеру через view.MAX_*
    MAX_CONFIG_NAME_LEN = MAX_CONFIG_NAME_LEN

    def __init__(self, parent, service, reference):
        super().__init__(parent)
        self.setupUi(self)

        # Заменяем стандартный QPlainTextEdit на наш CodeEditor
        old_editor = self.editPreview
        new_editor = CodeEditor(self.gbPreview)

        # Копируем настройки (если нужно)
        new_editor.setReadOnly(old_editor.isReadOnly())

        # Заменяем в layout
        layout = old_editor.parentWidget().layout()
        layout.replaceWidget(old_editor, new_editor)
        old_editor.deleteLater()

        # Переназначаем переменную
        self.editPreview = new_editor

        # Кнопка вызова справки
        self.btn_help = QPushButton("?")
        self.btn_help.setFixedSize(28, 28)
        self.btn_help.setCursor(Qt.CursorShape.PointingHandCursor)

        self.btn_help.setStyleSheet(f"""
                    QPushButton {{
                        background-color: transparent;
                        color: #b0b0c0;
                        border: 1px solid #555555;
                        border-radius: 14px;
                        padding: 0px;
                        font-weight: bold;
                        font-size: 12px;
                    }}
                    QPushButton:hover {{
                        color: {ACCENT};
                        border: 1px solid {ACCENT};
                    }}
                """)

        # Привязываем открытие диалога
        self.btn_help.clicked.connect(self._show_legend)

        # Добавляем кнопку в layout, где лежат "Открыть редактор" и "История изменений"
        self.previewButtons.addWidget(self.btn_help)

        # ============ подсветка синтаксиса ==============
        known_keys = set()
        if hasattr(service, 'command_repo') and service.command_repo:
            # Загружаем все команды из базы
            commands = service.command_repo.all("debug")
            known_keys = {cmd["key_name"] for cmd in commands}

        self._highlighter = CfgHighlighter(self.editPreview.document(), known_keys)
        self.editPreview.set_completion_words(sorted(known_keys))

        self.editPreview.document().contentsChange.connect(
            lambda _pos, _rem, _add: self._update_preview_stats()
        )

        # --- Панель поиска ---
        self.search_panel = SearchPanel(self.editPreview, self.gbPreview)
        preview_layout = self.gbPreview.layout()
        index = preview_layout.indexOf(self.editPreview)
        preview_layout.insertWidget(index, self.search_panel)
        self.search_panel.hide()  # Скрываем по умолчанию

        # Включаем подсветку текущей строки
        self.editPreview.setCursorWidth(2)  # Чуть шире курсор для удобства

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

        self.lblTreeTitle.setStyleSheet(
            "font-size: 12pt; font-weight: 700; color: #b0b0c0; "
            "background: transparent;"
        )
        self.lblPreviewTitle.setStyleSheet(
            "font-size: 12pt; font-weight: 700; color: #b0b0c0; "
            "background: transparent;"
        )

        self.treeConfigs.setWordWrap(True)

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
            self._on_selection_changed
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
        self.treeConfigs.itemDoubleClicked.connect(
            lambda _item, _col: self.presenter.open_selected()
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
            "main.find":    self.toggle_search,
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
        svc = self.window().shortcut_service

        # Поиск
        self.search_panel.lbl.setText(t("main.search"))
        self.search_panel.edit.setPlaceholderText(t("main.search.placeholder"))

        # заголовки
        self.lblTreeTitle.setText(t("main.lbl_tree_title"))
        self.lblPreviewTitle.setText(t("main.lbl_preview_title"))
        self.editPreview.setPlaceholderText(t("empty.preview"))

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
        self._update_preview_stats()

        # переприменить текущее состояние
        item = self.treeConfigs.currentItem()
        if item is not None:
            config_id = item.data(0, Qt.ItemDataRole.UserRole)
            cfg = self.presenter.service.repo.get(config_id)
            if cfg:
                self.lblPreviewName.setText(cfg["filename"])
            else:
                self.clear_preview()
        else:
            self.lblPreviewName.setText(t("main.lbl_preview_none"))

        # обновить плейсхолдер (если список пуст)
        if self.treeConfigs.topLevelItemCount() == 0 or (
                self.treeConfigs.topLevelItemCount() == 1
                and self.treeConfigs.topLevelItem(0).data(
            0, Qt.ItemDataRole.UserRole) is None
        ):
            self.treeConfigs.clear()
            from logic.widgets.empty_state import add_empty_node
            self.treeConfigs.blockSignals(True)
            add_empty_node(self.treeConfigs, _t("empty.configs"))
            self.treeConfigs.setCurrentItem(None)
            self.treeConfigs.blockSignals(False)

        set_button_variant(self.btnOpenEditor, "primary")
        set_button_variant(self.btnDeleteConfig, "danger")

    # ============== контекст ==============

    def set_context(self, profile_id: int, server_id: int):
        """Делегирует презентеру - какой профиль / сервер открыт."""
        self.presenter.set_context(profile_id, server_id)
        overrides = self.presenter.service.get_server_overrides(
            self.window().server_repo, server_id
        )
        self._highlighter.set_overridden_keys(overrides)
        self._update_preview_stats()

    # ============== жизненный цикл ==============

    def on_enter(self):
        self.editFilter.blockSignals(True)
        self.editFilter.clear()
        self.editFilter.blockSignals(False)
        self.presenter.on_enter()

    def on_leave(self) -> bool:
        return self.presenter.on_leave()

    def _on_selection_changed(self):
        """Слот выбора файла: сохраняет/восстанавливает состояние."""
        item = self.treeConfigs.currentItem()
        config_id = item.data(0, Qt.ItemDataRole.UserRole) if item else None

        if not hasattr(self, '_last_config_id'):
            self._last_config_id = None

        # Если файл реально сменился
        if config_id != self._last_config_id:
            # 1. Сохраняем состояние СТАРОГО файла
            if self._last_config_id is not None:
                self.presenter._save_editor_state(self._last_config_id)

            # 2. Обновляем ID текущего
            self._last_config_id = config_id

        # 3. Презентер обновляет текст
        self.presenter.on_selection()

        # 4. Восстанавливаем состояние НОВОГО файла (включая поиск)
        if config_id is not None:
            self.presenter._restore_editor_state(config_id)

    # ============== UI-хелперы (зовёт презентер) ==============

    def apply_filter(self, text: str):
        """Слот textChanged - делегирует презентеру."""
        self.presenter.apply_filter(text)

    def clear_preview(self):
        """Сбрасывает панель предпросмотра."""
        self.lblPreviewName.setText(t("main.lbl_preview_none"))
        self.editPreview.setPlainText("")
        self.editPreview.setPlaceholderText(t("empty.preview"))

        if hasattr(self, 'search_panel') and self.search_panel.isVisible():
            self.search_panel.hide_panel()

        if hasattr(self, 'lblPreviewStats'):
            self.lblPreviewStats.setText("")

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

        from logic.core.constants import APP_VERSION
        from logic.core.i18n import t

        QMessageBox.about(
            self,
            t("dialog.about_title"),
            t("dialog.about_text").format(version=APP_VERSION),
        )

    def _show_legend(self):
        """Открывает диалог со справкой по превью."""
        dialog = LegendDialog(self, self.window().shortcut_service)
        dialog.exec()

    def _update_preview_stats(self):
        """Обновляет счётчики в заголовке превью."""
        if not hasattr(self, 'lblPreviewStats'):
            return

        stats = self._highlighter.get_stats()
        parts = []

        # Ошибки (красный)
        if stats["errors"]:
            n = stats["errors"]
            from logic.core.i18n import get_language, plural_ru
            if get_language() == "ru":
                word = plural_ru(n, "ошибка", "ошибки", "ошибок")
            else:
                word = "error" if n == 1 else "errors"
            parts.append(
                f"<span style='color:{DANGER};'>{n} {word}</span>"
            )

        # Дубли (жёлтый)
        if stats["duplicates"]:
            n = stats["duplicates"]
            from logic.core.i18n import get_language, plural_ru
            if get_language() == "ru":
                word = plural_ru(n, "дубль", "дубля", "дублей")
            else:
                word = "duplicate" if n == 1 else "duplicates"
            parts.append(
                f"<span style='color:{ACCENT};'>{n} {word}</span>"
            )

        # Неизвестные (серый)
        if stats["unknowns"]:
            n = stats["unknowns"]
            from logic.core.i18n import get_language, plural_ru
            if get_language() == "ru":
                word = plural_ru(n, "неизвестная", "неизвестные", "неизвестных")
            else:
                word = "unknown" if n == 1 else "unknowns"
            parts.append(
                f"<span style='color:{SYNTAX_UNKNOWN_KEY};'>{n} {word}</span>"
            )

        # Переопределения (оранжевый)
        if stats["overrides"]:
            n = stats["overrides"]
            from logic.core.i18n import get_language, plural_ru
            if get_language() == "ru":
                word = plural_ru(n, "переопределение", "переопределения", "переопределений")
            else:
                word = "override" if n == 1 else "overrides"
            parts.append(
                f"<span style='color:{SYNTAX_OVERRIDDEN_KEY};'>{n} {word}</span>"
            )

        # Собираем строку через разделитель
        if parts:
            self.lblPreviewStats.setText(" · ".join(parts))
        else:
            self.lblPreviewStats.setText("")

    # ============== контекстное меню ==============

    def _show_context_menu(self, pos):
        item = self.treeConfigs.itemAt(pos)
        if item is None:
            return
        if item.data(0, Qt.ItemDataRole.UserRole) is None:
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

    def toggle_search(self):
        """Показать/скрыть панель поиска."""
        # Проверяем, есть ли реальные конфиги
        count = self.treeConfigs.topLevelItemCount()

        has_configs = False
        if count > 0:
            # Если элемент один, проверяем, не плейсхолдер ли это
            if count == 1:
                item = self.treeConfigs.topLevelItem(0)
                if item.data(0, Qt.ItemDataRole.UserRole) is not None:
                    has_configs = True
            else:
                has_configs = True

        # Если конфигов нет — ничего не делаем
        if not has_configs:
            return

        if self.search_panel.isVisible():
            self.search_panel.hide_panel()
        else:
            self.search_panel.show_panel()