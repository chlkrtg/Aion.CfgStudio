"""Страница выбора сервера внутри профиля."""
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox

from logic.context_menu import build_context_menu
from logic.shortcuts import bind_shortcuts, FOCUSED
from logic.base_page import BasePage
from logic.constants import MAX_SERVER_NAME_LEN, MAX_NOTE_LEN
from ui.server_select import Ui_ServerSelectDialog


class PageServer(BasePage, Ui_ServerSelectDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # самое важное поле
        self.profile_id = None

        # подключение контекстного меню
        self.listServers.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.listServers.customContextMenuRequested.connect(self._show_context_menu)

        # скрыть блок Регион: пока неактуально
        self.lblRegionCaption.hide()
        self.lblRegionValue.hide()

        # поле заметки редактируемое
        self.editNote.setReadOnly(False)
        # debounce: сохранять через 1 сек после последнего изменения
        self._save_timer = QTimer(self)
        self._save_timer.setSingleShot(True)
        self._save_timer.setInterval(1000)
        self._save_timer.timeout.connect(self._save_note)

        self._connect_signals()

        bind_shortcuts(self.listServers, {
            "F1": lambda: self.window().go_video(),
            "F2": self._rename,
            "Return": self._enter,
            "Enter": self._enter,
            "Ctrl+N": self._create,
            "Delete": self._delete,
        }, FOCUSED)

        # Ctrl+Q глобально на странице
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(
            lambda: self.window().go_profile()
        )

    def _connect_signals(self):
        self.btnNewServer.clicked.connect(self._create)
        self.btnRenameServer.clicked.connect(self._rename)
        self.btnDeleteServer.clicked.connect(self._delete)
        self.btnEnter.clicked.connect(self._enter)
        self.listServers.currentItemChanged.connect(self._on_server_selected)
        self.editNote.textChanged.connect(self._on_note_changed)
        self.btnVideoHelp.clicked.connect(
            lambda: self.window().go_video()
        )
        self.btnCancel.clicked.connect(
            lambda: self.window().go_profile()
        )
        self.listServers.itemDoubleClicked.connect(
            lambda _: self._enter()
        )

    # ============== жизненный цикл ==============

    def set_profile(self, profile_id: int):
        """Запоминает ИД профиля."""
        self.profile_id = profile_id

    def on_enter(self):
        """Подгружает список доступных серверов
                для конкретного профиля при загрузке страницы."""
        self.refresh()

    def on_leave(self):
        """Сохраняет заметку при уходе со страницы."""
        if self._save_timer.isActive():
            self._save_timer.stop()
        self._save_note()

    # ============== автосохранение заметки ==============

    def _on_note_changed(self):
        """Запускает таймер автосохранения при каждом изменении описания сервера."""
        self._save_timer.start()

    def _save_note(self):
        """Сохраняет заметку текущего сервера."""
        self._persist_note(self.listServers.currentItem())

    def _persist_note(self, item):
        """Сохраняет заметку для указанного item.
                Возвращает True при успехе, и False, если item нет или БД упала.
        """
        return self.persist_text(
            item,
            self.editNote.toPlainText(),
            MAX_NOTE_LEN,
            self.db.update_server_note,
            "описание сервера",
        )

    # ============== загрузка ==============

    def refresh(self, select_id: int | None = None):
        """Обновление страницы при разных действиях."""
        if self.profile_id is None:
            return
        if self._save_timer.isActive():
            self._save_timer.stop()
        self._persist_note(self.listServers.currentItem())

        if select_id is None:
            current = self.listServers.currentItem()
            if current is not None:
                select_id = current.data(Qt.ItemDataRole.UserRole)

        profile = self.db.get_profile(self.profile_id)
        if profile:
            self.lblTitle.setText(
                f"Профиль: {profile['name']} / Выберите сервер"
            )

        self.listServers.blockSignals(True)
        self.listServers.clear()
        for row in self.db.list_servers(self.profile_id):
            item = QListWidgetItem(row["name"])
            item.setData(Qt.ItemDataRole.UserRole, row["id"])
            self.listServers.addItem(item)
        self.listServers.blockSignals(False)

        if not self.listServers.count():
            self._clear_details()
            self._set_controls_enabled(False)
            return

        self._set_controls_enabled(True)

        # выбрать нужный сервер (или первый)
        target_row = 0
        if select_id is not None:
            for i in range(self.listServers.count()):
                if self.listServers.item(i).data(Qt.ItemDataRole.UserRole) == select_id:
                    target_row = i
                    break
        self.listServers.setCurrentRow(target_row)

    def _set_controls_enabled(self, enabled: bool):
        """Включает / выключает контролы, требующие выбранного сервера."""
        self.set_controls_enabled(
            enabled,
            self.btnRenameServer,
            self.btnDeleteServer,
            self.btnEnter,
            self.editNote,
        )

    # ============== обработка выбора ==============

    def _on_server_selected(self, current, previous=None):
        """Заполняет правую панель при выборе сервера."""
        # 1. сохранить заметку предыдущего сервера
        if previous is not None:
            if self._save_timer.isActive():
                self._save_timer.stop()
            self._persist_note(previous)

        # 2. если сервер не выбран, очистить
        if current is None:
            self._clear_details()
            return

        # 3. заполнить панель
        server_id = current.data(Qt.ItemDataRole.UserRole)
        server = self.db.get_server(server_id)
        if not server:
            self._clear_details()
            return

        self.lblServerName.setText(f"Выбранный сервер: {server["name"]}")
        self.lblRegionValue.setText(server["region"] or "—")

        configs = self.db.count_configs_in_server(server_id)
        self.lblConfigsValue.setText(str(configs))

        # заметка: блокируем сигналы, чтобы не запускать автосохранение
        self.editNote.blockSignals(True)
        self.editNote.setPlainText(server["note"] or "")
        self.editNote.blockSignals(False)

        # иконка - первая буква имени, тоже золотая!
        first_letter = (server["name"] or "?")[0].upper()
        self.lblServerIcon.setText(first_letter)
        self.lblServerIcon.setStyleSheet(
            "font-size: 60px; color: #d4a95a; font-weight: bold;"
        )

    def _clear_details(self):
        self.lblServerName.setText("— сервер не выбран —")
        self.lblRegionValue.setText("—")
        self.lblConfigsValue.setText("0")
        self.editNote.blockSignals(True)
        self.editNote.clear()
        self.editNote.blockSignals(False)
        self.lblServerIcon.clear()

    # ============== кнопки ==============

    def _create(self):
        """Создаёт сервер, загружая в БД, с проверкой на уникальность имени."""
        name, ok = self.ask_name(
            "Новый сервер", "Имя сервера:",
            max_len=MAX_SERVER_NAME_LEN,
        )
        if not ok:
            return

        name = self.validate_name(name, MAX_SERVER_NAME_LEN, "Имя сервера")
        if name is None:
            return

        # проверка на дубликат среди серверов этого профиля
        if any(s["name"] == name for s in self.db.list_servers(self.profile_id)):
            QMessageBox.warning(
                self, "Ошибка",
                f"Сервер «{name}» уже существует в этом профиле.\n"
                "Выберите другое имя."
            )
            return

        try:
            new_id = self.db.create_server(self.profile_id, name)
        except Exception as exc:
            QMessageBox.warning(self, "Ошибка", str(exc))
            return

        self.refresh(select_id=new_id)

    def _rename(self):
        """Ренейм сервера с последующей подгрузкой в БД и проверкой на уникальность."""
        item = self.listServers.currentItem()
        if item is None:
            QMessageBox.information(self, "Переименование",
                                    "Не выбран сервер для переименования.")
            return
        sid = item.data(Qt.ItemDataRole.UserRole)
        old_name = item.text()

        new_name, ok = self.ask_name(
            "Переименовать", "Новое имя:",
            default=old_name,
            max_len=MAX_SERVER_NAME_LEN,
        )
        if not ok:
            return

        new_name = self.validate_name(new_name, MAX_SERVER_NAME_LEN, "Имя сервера")
        if new_name is None:
            return

        if new_name == old_name:
            return

        if any(
                s["name"] == new_name and s["id"] != sid
                for s in self.db.list_servers(self.profile_id)
        ):
            QMessageBox.warning(
                self, "Ошибка",
                f"Сервер «{new_name}» уже существует в этом профиле.\n"
                "Выберите другое имя."
            )
            return

        try:
            self.db.rename_server(sid, new_name)
        except Exception as exc:
            QMessageBox.warning(self, "Ошибка", str(exc))
            return

        self.refresh()

    def _delete(self):
        """Удаление сервера с соответствующими изменениями в БД."""
        item = self.listServers.currentItem()
        if item is None:
            QMessageBox.information(self, "Удаление",
                                    "Не выбран сервер для удаления.")
            return
        sid = item.data(Qt.ItemDataRole.UserRole)
        ans = QMessageBox.question(
            self, "Удалить",
            f"Удалить сервер «{item.text()}» со всеми cfg?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if ans == QMessageBox.StandardButton.Yes:
            self.db.delete_server(sid)
            self.refresh()

    def _enter(self):
        """Вход в выбранный сервер"""
        item = self.listServers.currentItem()
        if item is None:
            QMessageBox.information(self, "Вход", "Не выбран сервер для входа.")
            return
        self.window().go_main(item.data(Qt.ItemDataRole.UserRole))

    def _duplicate(self):
        """Дублирует сервер со всеми cfg."""
        item = self.listServers.currentItem()
        if item is None:
            QMessageBox.information(self, "Дублирование",
                                    "Не выбран сервер для дублирования.")
            return

        sid = item.data(Qt.ItemDataRole.UserRole)
        server = self.db.get_server(sid)
        if not server:
            return

        new_name, ok = self.ask_name(
            "Дублировать сервер",
            "Имя нового сервера:",
            default=f"{server['name']} (копия)",
            max_len=MAX_SERVER_NAME_LEN,
        )
        if not ok:
            return

        new_name = self.validate_name(new_name, MAX_SERVER_NAME_LEN, "Имя сервера")
        if new_name is None:
            return

        if any(s["name"] == new_name for s in self.db.list_servers(self.profile_id)):
            QMessageBox.warning(self, "Ошибка",
                                f"Сервер «{new_name}» уже существует.")
            return

        try:
            new_id = self.db.duplicate_server(sid, new_name)
        except Exception as exc:
            QMessageBox.warning(self, "Ошибка", str(exc))
            return

        self.refresh(select_id=new_id)

    def _show_context_menu(self, pos):
        """Показывает контекстное меню для сервера."""
        item = self.listServers.itemAt(pos)
        if item is None:
            return

        self.listServers.setCurrentItem(item)

        menu = build_context_menu(self, [
            ("Войти", self._enter),
            None,
            ("Дублировать", self._duplicate),
            None,
            ("Переименовать (F2)", self._rename),
            None,
            ("Удалить (Delete)", self._delete),
        ])
        menu.exec(self.listServers.mapToGlobal(pos))