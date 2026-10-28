"""Единое окно с QStackedWidget. Переключает страницы."""
import webbrowser

from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QAction, QActionGroup
from PyQt6.QtWidgets import QMainWindow, QStackedWidget

from database.db_manager import DBManager
from logic.core.i18n import t
from logic.page_editor import PageEditor
from logic.page_main import PageMain
from logic.page_profile import PageProfile
from logic.page_server import PageServer
from logic.repositories import (
    CommandRepository,
    ConfigRepository,
    ProfileRepository,
    ServerRepository,
    SettingsRepository,
    ShortcutRepository,
)
from logic.services import (
    ConfigService,
    EditorService,
    LanguageService,
    ProfileService,
    ReferenceService,
    ServerService,
    ShortcutService,
)

VIDEO_URL = "https://www.youtube.com/watch?v=TK2jVAArRhM"

class AppWindow(QMainWindow):
    def __init__(self, db: DBManager):
        super().__init__()
        self.db = db
        self.setWindowTitle("Aion.CfgStudio")
        self.resize(700, 700)

        # Восстанавливаем геометрию (если была сохранена)
        settings = QSettings("Aion", "CfgStudio")
        geometry = settings.value("window/geometry")
        if geometry is not None:
            self.restoreGeometry(geometry)
        state = settings.value("window/state")
        if state is not None:
            self.restoreState(state)

        # ============= репозитории  =============
        self.settings_repo = SettingsRepository(db)
        self.profile_repo = ProfileRepository(db)
        self.server_repo = ServerRepository(db)
        self.config_repo = ConfigRepository(db)
        self.command_repo = CommandRepository(db)
        self.shortcut_repo = ShortcutRepository(db)

        # ============= сервисы =============
        self.language_service = LanguageService(self.settings_repo)
        self.profile_service = ProfileService(self.profile_repo)
        self.server_service = ServerService(self.server_repo)
        self.config_service = ConfigService(
            self.config_repo, self.command_repo
        )
        self.editor_service = EditorService(
            self.config_repo, self.command_repo, self.config_service,
            server_repo=self.server_repo,
        )
        self.reference_service = ReferenceService(
            self.profile_repo, self.server_repo, self.config_repo
        )
        self.shortcut_service = ShortcutService(self.shortcut_repo)

        # ============= действия окна =============

        self.actionShortcuts = QAction(t("menu.shortcuts"), self)
        self.actionShortcuts.triggered.connect(self._open_shortcuts_editor)

        # ---- меню «Язык» ----
        self.actionGroupLang = QActionGroup(self)
        self.actionGroupLang.setExclusive(True)

        self.actionLangRu = QAction(t("menu.lang.ru"), self, checkable=True)
        self.actionLangEn = QAction(t("menu.lang.en"), self, checkable=True)

        self.actionGroupLang.addAction(self.actionLangRu)
        self.actionGroupLang.addAction(self.actionLangEn)

        self.actionLangRu.triggered.connect(
            lambda: self._change_language("ru")
        )
        self.actionLangEn.triggered.connect(
            lambda: self._change_language("en")
        )

        # отметить текущий
        if self.language_service.current == "ru":
            self.actionLangRu.setChecked(True)
        else:
            self.actionLangEn.setChecked(True)

        # ============= UI =============
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.current_profile_id = None
        self.current_server_id = None
        self.current_config_id = None

        self.page_profile = PageProfile(
            self, self.profile_service, self.reference_service
        )
        self.page_server = PageServer(
            self, self.server_service, self.reference_service
        )
        self.page_main = PageMain(
            self, self.config_service, self.reference_service
        )
        self.page_editor = PageEditor(self, self.editor_service)

        for page in (self.page_profile, self.page_server,
                     self.page_main, self.page_editor):
            self.stack.addWidget(page)

        self.go_profile()

    # ========== меню ==========

    def _rebuild_menus(self, page):
        """Пересобирает меню под текущую страницу;
                build_menus() определяется у каждой страницы, если меню нужно"""

        menubar = self.menuBar()
        menubar.clear()

        menus = page.build_menus() if hasattr(page, "build_menus") else {}

        for title, items in menus.items():
            menu = menubar.addMenu(title)
            for item in items:
                if item is None:
                    menu.addSeparator()
                else:
                    menu.addAction(item)

        menubar.setVisible(bool(menus))

    # ========== навигация ==========

    def _switch(self, page):
        """Вызов функций при смене страниц.

        Если on_leave вернул False — навигация отменяется.
        """
        old = self.stack.currentWidget()
        if old and hasattr(old, "on_leave"):
            result = old.on_leave()
            if result is not True:
                return

        self.stack.setCurrentWidget(page)

        if hasattr(page, "on_enter"):
            page.on_enter()

        self._rebuild_menus(page)

    def go_profile(self):
        self._switch(self.page_profile)

    def go_server(self, profile_id: int):
        self.current_profile_id = profile_id
        self.page_server.set_profile(profile_id)
        self._switch(self.page_server)

    def go_main(self, server_id: int):
        self.current_server_id = server_id
        self.page_main.set_context(self.current_profile_id, server_id)
        self._switch(self.page_main)

    def go_editor(self, config_id):
        self.current_config_id = config_id
        self.page_editor.set_context(config_id, self.current_server_id)
        self._switch(self.page_editor)

    def _open_shortcuts_editor(self):
        """Открывает модальный редактор хоткеев."""
        from logic.widgets.shortcuts_editor import ShortcutsEditorDialog

        dlg = ShortcutsEditorDialog(self, self.shortcut_service)
        dlg.shortcuts_changed.connect(self.refresh_shortcuts)
        dlg.exec()

    def _change_language(self, lang: str):
        """Переключение языка."""
        if not self.language_service.set(lang):
            return
        self.retranslate_all()

    def retranslate_all(self):
        """Обновляет все тексты приложения после смены языка."""
        # 1. действия окна
        self.actionShortcuts.setText(t("menu.shortcuts"))
        self.actionLangRu.setText(t("menu.lang.ru"))
        self.actionLangEn.setText(t("menu.lang.en"))

        # 2. страницы (в 3.3 сюда добавим их retranslate)
        for page in (self.page_profile, self.page_server,
                     self.page_main, self.page_editor):
            if hasattr(page, "retranslate"):
                page.retranslate()

        # 3. меню текущей страницы
        current = self.stack.currentWidget()
        self._rebuild_menus(current)

    def refresh_shortcuts(self):
        """Перевешивает хоткеи и обновляет подписи на всех страницах."""
        for page in (self.page_profile, self.page_server,
                     self.page_main, self.page_editor):
            if hasattr(page, "rebind_shortcuts"):
                page.rebind_shortcuts()
            if hasattr(page, "retranslate"):
                page.retranslate()

    def go_video(self):
        webbrowser.open(VIDEO_URL)

    def closeEvent(self, event):
        page = self.stack.currentWidget()
        if page and hasattr(page, "on_leave"):
            result = page.on_leave()
            if result is not True:
                event.ignore()
                return

        # Сохраняем геометрию окна
        settings = QSettings("Aion", "CfgStudio")
        settings.setValue("window/geometry", self.saveGeometry())
        settings.setValue("window/state", self.saveState())

        super().closeEvent(event)