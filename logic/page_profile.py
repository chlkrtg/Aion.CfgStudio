"""Страница выбора профиля.

Вся логика - в ProfilePresenter.
"""
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QShortcut, QKeySequence

from logic.base_page import BasePage
from logic.context_menu import build_context_menu
from logic.shortcuts import bind_shortcuts, FOCUSED
from logic.constants import MAX_PROFILE_NAME_LEN, MAX_DESCRIPTION_LEN
from logic.repositories import ProfileRepository
from logic.services import ProfileService
from logic.presenters import ProfilePresenter
from ui.profile_select import Ui_ProfileSelectDialog


class PageProfile(BasePage, Ui_ProfileSelectDialog):

    # константы доступны презентеру через view.MAX_*
    MAX_PROFILE_NAME_LEN = MAX_PROFILE_NAME_LEN
    MAX_DESCRIPTION_LEN = MAX_DESCRIPTION_LEN

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # =========== презентер ===========
        repo = ProfileRepository(self.db)
        service = ProfileService(repo)
        self.presenter = ProfilePresenter(self, service)

        # =========== UI ===========
        self.listProfiles.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )
        self.listProfiles.customContextMenuRequested.connect(
            self._show_context_menu
        )

        self.editDescription.setReadOnly(False)
        self.editDescription.setPlaceholderText(
            f"Сохраняется автоматически (до {MAX_DESCRIPTION_LEN} символов)..."
        )

        self._save_timer = QTimer(self)
        self._save_timer.setSingleShot(True)
        self._save_timer.setInterval(1000)
        self._save_timer.timeout.connect(self.presenter.save_description)
        self.editDescription.textChanged.connect(
            lambda: self._save_timer.start()
        )

        self._connect_signals()

        # хоткеи
        bind_shortcuts(self.listProfiles, {
            "F1": lambda: self.window().go_video(),
            "F2": self.presenter.rename,
            "Return": self.presenter.enter,
            "Enter": self.presenter.enter,
            "Ctrl+N": self.presenter.create,
            "Delete": self.presenter.delete,
        }, FOCUSED)

        # Ctrl+Q на странице
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(
            lambda: self.window().close()
        )

    # ============== сигналы ==============

    def _connect_signals(self):
        self.btnNew.clicked.connect(self.presenter.create)
        self.btnRename.clicked.connect(self.presenter.rename)
        self.btnDelete.clicked.connect(self.presenter.delete)
        self.btnEnter.clicked.connect(self.presenter.enter)

        self.listProfiles.currentItemChanged.connect(
            self.presenter.on_profile_selected
        )
        self.listProfiles.itemDoubleClicked.connect(
            lambda _: self.presenter.enter()
        )
        self.btnCancel.clicked.connect(
            lambda: self.window().close()
        )
        self.btnVideoHelp.clicked.connect(
            lambda: self.window().go_video()
        )

    # ============== жизненный цикл ==============

    def on_enter(self):
        self.presenter.on_enter()

    def on_leave(self):
        if self._save_timer.isActive():
            self._save_timer.stop()
        self.presenter.on_leave()

    # ============== UI-хелперы (зовёт презентер) ==============

    def fill_details(self, profile):
        """Заполняет правую панель данными профиля."""
        self.editDescription.blockSignals(True)
        self.editDescription.setPlainText(profile["description"] or "")
        self.editDescription.blockSignals(False)

        self.lblName.setText(f"Выбранный профиль: {profile['name']}")

        pid = profile["id"]
        servers = self.presenter.service.repo.count_servers(pid)
        configs = self.presenter.service.repo.count_configs(pid)
        self.lblStats.setText(
            f"Серверов: {servers} | Конфигураций: {configs}"
        )

        first_letter = (profile["name"] or "?")[0].upper()
        self.lblAvatar.setText(first_letter)
        self.lblAvatar.setStyleSheet(
            "font-size: 60px; color: #d4a95a; font-weight: bold;"
        )

    def clear_details(self):
        """Очищает правую панель."""
        self.lblName.setText("— профиль не выбран —")
        self.editDescription.blockSignals(True)
        self.editDescription.clear()
        self.editDescription.blockSignals(False)
        self.lblStats.setText("Серверов: 0 | Конфигураций: 0")
        self.lblAvatar.clear()

    def set_controls_enabled(self, enabled: bool):
        """Включает/выключает контролы, требующие выбранного профиля."""
        super().set_controls_enabled(
            enabled,
            self.btnRename,
            self.btnDelete,
            self.btnEnter,
            self.editDescription,
        )

    # ============== контекстное меню ==============

    def _show_context_menu(self, pos):
        item = self.listProfiles.itemAt(pos)
        if item is None:
            return

        self.listProfiles.setCurrentItem(item)

        menu = build_context_menu(self, [
            ("Войти", self.presenter.enter),
            None,
            ("Дублировать", self.presenter.duplicate),
            None,
            ("Переименовать (F2)", self.presenter.rename),
            None,
            ("Удалить (Delete)", self.presenter.delete),
        ])
        menu.exec(self.listProfiles.mapToGlobal(pos))