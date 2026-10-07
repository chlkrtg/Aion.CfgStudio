"""Единое окно с QStackedWidget. Переключает страницы."""
from PyQt6.QtWidgets import QMainWindow, QStackedWidget

from database.db_manager import DBManager
from logic.repositories import (
    ProfileRepository, ServerRepository,
    ConfigRepository, CommandRepository,
)
from logic.services import (
    ProfileService, ServerService,
    ConfigService, EditorService,
    ReferenceService,
)

from logic.page_profile import PageProfile
from logic.page_server import PageServer
from logic.page_main import PageMain
from logic.page_editor import PageEditor
from logic.page_video import PageVideo


class AppWindow(QMainWindow):
    def __init__(self, db: DBManager):
        super().__init__()
        self.db = db
        self.setWindowTitle("Aion.CfgStudio")
        self.resize(700, 700)

        # ============= репозитории  =============
        self.profile_repo = ProfileRepository(db)
        self.server_repo = ServerRepository(db)
        self.config_repo = ConfigRepository(db)
        self.command_repo = CommandRepository(db)

        # ============= сервисы =============
        self.profile_service = ProfileService(self.profile_repo)
        self.server_service = ServerService(self.server_repo)
        self.config_service = ConfigService(
            self.config_repo, self.command_repo
        )
        self.editor_service = EditorService(
            self.config_repo, self.command_repo, self.config_service
        )
        self.reference_service = ReferenceService(
            self.profile_repo, self.server_repo, self.config_repo
        )

        # ============= UI =============
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.current_profile_id = None
        self.current_server_id = None
        self.current_config_id = None

        self.page_profile = PageProfile(self, self.profile_service)
        self.page_server = PageServer(self, self.server_service)
        self.page_main = PageMain(self, self.config_service)
        self.page_editor = PageEditor(self, self.editor_service)
        self.page_video = PageVideo(self, self.command_repo)

        for page in (self.page_profile, self.page_server,
                     self.page_main, self.page_editor, self.page_video):
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
        """Вызов функций при смене страниц"""
        old = self.stack.currentWidget()
        if old and hasattr(old, "on_leave"):
            old.on_leave()

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

    def go_video(self):
        self._previous_page = self.stack.currentWidget()
        self._switch(self.page_video)

    def go_back_from_video(self):
        """Возвращает на страницу, откуда (!) открыли видео"""
        if self._previous_page is not None:
            self._switch(self._previous_page)
            self._previous_page = None
        else:
            self.go_profile()
