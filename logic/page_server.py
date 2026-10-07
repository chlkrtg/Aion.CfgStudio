"""Страница выбора сервера внутри профиля.

Вся логика - в ServerPresenter.
"""
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QShortcut, QKeySequence

from logic.base_page import BasePage
from logic.context_menu import build_context_menu
from logic.shortcuts import bind_shortcuts, FOCUSED
from logic.constants import MAX_SERVER_NAME_LEN, MAX_NOTE_LEN
from logic.presenters import ServerPresenter
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
        self.editNote.setPlaceholderText(
            f"Сохраняется автоматически (до {MAX_NOTE_LEN} символов)..."
        )

        # debounce заметки - как в профиле
        self._save_timer = QTimer(self)
        self._save_timer.setSingleShot(True)
        self._save_timer.setInterval(1000)
        self._save_timer.timeout.connect(self.presenter.save_note)
        self.editNote.textChanged.connect(
            lambda: self._save_timer.start()
        )

        self._connect_signals()

        # хоткеи
        bind_shortcuts(self.listServers, {
            "F1": lambda: self.window().go_video(),
            "F2": self.presenter.rename,
            "Return": self.presenter.enter,
            "Enter": self.presenter.enter,
            "Ctrl+N": self.presenter.create,
            "Delete": self.presenter.delete,
        }, FOCUSED)

        # Ctrl+Q на странице - назад к выбору профиля
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(
            lambda: self.window().go_profile()
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

    # ============== жизненный цикл ==============

    def set_profile(self, profile_id: int):
        """Делегирует презентеру - какой профиль открыт."""
        self.presenter.set_profile(profile_id)

    def on_enter(self):
        self.presenter.on_enter()

    def on_leave(self):
        if self._save_timer.isActive():
            self._save_timer.stop()
        self.presenter.on_leave()

    # ============== UI-хелперы (зовёт презентер) ==============

    def fill_details(self, server, stats):
        """Заполняет правую панель данными сервера."""
        self.lblServerName.setText(
            f"Выбранный сервер: {server['name']}"
        )
        self.lblRegionValue.setText(server["region"] or "—")

        self.lblConfigsValue.setText(str(stats["configs"]))

        # заметка: блокируем сигналы, чтобы не запускать автосохранение
        self.editNote.blockSignals(True)
        self.editNote.setPlainText(server["note"] or "")
        self.editNote.blockSignals(False)

        # иконка - первая буква имени
        first_letter = (server["name"] or "?")[0].upper()
        self.lblServerIcon.setText(first_letter)
        self.lblServerIcon.setStyleSheet(
            "font-size: 60px; color: #d4a95a; font-weight: bold;"
        )

    def clear_details(self):
        """Очищает правую панель."""
        self.lblServerName.setText("— сервер не выбран —")
        self.lblRegionValue.setText("—")
        self.lblConfigsValue.setText("0")
        self.editNote.blockSignals(True)
        self.editNote.clear()
        self.editNote.blockSignals(False)
        self.lblServerIcon.clear()

    def set_controls_enabled(self, enabled: bool):
        """Включает/выключает контролы, требующие выбранного сервера."""
        super().set_controls_enabled(
            enabled,
            self.btnRenameServer,
            self.btnDeleteServer,
            self.btnEnter,
            self.editNote,
        )

    # ============== контекстное меню ==============

    def _show_context_menu(self, pos):
        item = self.listServers.itemAt(pos)
        if item is None:
            return

        self.listServers.setCurrentItem(item)

        menu = build_context_menu(self, [
            ("Войти", self.presenter.enter),
            None,
            ("Дублировать", self.presenter.duplicate),
            None,
            ("Переименовать (F2)", self.presenter.rename),
            None,
            ("Удалить (Delete)", self.presenter.delete),
        ])
        menu.exec(self.listServers.mapToGlobal(pos))