"""Presenter для страницы серверов.

Логика аналогична ProfilePresenter, но с контекстом профиля.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox

from logic.presenters.base_presenter import BasePresenter


class ServerPresenter(BasePresenter):
    """Логика страницы серверов внутри профиля."""

    def __init__(self, view, service):
        super().__init__(view)
        self.service = service
        self.profile_id: int | None = None

    # ============ контекст ============

    def set_profile(self, profile_id: int):
        """Запоминает id профиля, внутри которого работаем."""
        self.profile_id = profile_id

    # ============ жизненный цикл ============

    def on_enter(self):
        self.refresh()

    def on_leave(self):
        self.save_note()

    # ============ загрузка ============

    def refresh(self, select_id: int | None = None):
        """Перестраивает список серверов."""
        view = self.view

        if self.profile_id is None:
            return

        # сохранить заметку текущего
        self.save_note()

        # запомнить выбор
        if select_id is None:
            current = view.listServers.currentItem()
            if current is not None:
                select_id = current.data(Qt.ItemDataRole.UserRole)

        # обновить заголовок (какой профиль открыт)
        profile = self.service.repo.db.get_profile(self.profile_id)
        if profile:
            view.lblTitle.setText(
                f"Профиль: {profile['name']} / Выберите сервер"
            )

        # перестроить список
        view.listServers.blockSignals(True)
        view.listServers.clear()
        for row in self.service.repo.all_for_profile(self.profile_id):
            item = QListWidgetItem(row["name"])
            item.setData(Qt.ItemDataRole.UserRole, row["id"])
            view.listServers.addItem(item)
        view.listServers.blockSignals(False)

        if not view.listServers.count():
            view.clear_details()
            view.set_controls_enabled(False)
            return

        view.set_controls_enabled(True)

        # выбрать нужный или первый
        target_row = 0
        if select_id is not None:
            for i in range(view.listServers.count()):
                item = view.listServers.item(i)
                if item.data(Qt.ItemDataRole.UserRole) == select_id:
                    target_row = i
                    break
        view.listServers.setCurrentRow(target_row)

    # ============ обработка выбора ============

    def on_server_selected(self, current, previous=None):
        """Заполняет правую панель при выборе сервера."""
        view = self.view

        # сохранить заметку предыдущего
        if previous is not None:
            self._persist_note(previous)

        # если ничего не выбрано — очистить
        if current is None:
            view.clear_details()
            return

        server_id = current.data(Qt.ItemDataRole.UserRole)
        server = self.service.repo.get(server_id)
        if not server:
            view.clear_details()
            return

        view.fill_details(server)

    # ============ заметка ============

    def save_note(self):
        """Сохраняет заметку текущего сервера."""
        self._persist_note(self.view.listServers.currentItem())

    def _persist_note(self, item):
        """Сохраняет заметку для указанного item."""
        if item is None:
            return
        sid = item.data(Qt.ItemDataRole.UserRole)
        text = self.view.editNote.toPlainText()
        try:
            self.service.update_note(sid, text)
        except Exception as exc:
            QMessageBox.warning(
                self.view, "Ошибка",
                f"Не удалось сохранить заметку:\n{exc}"
            )

    # ============ действия ============

    def create(self):
        view = self.view
        if self.profile_id is None:
            return
        name, ok = view.ask_name_hint(
            "Новый сервер", "Имя сервера",
            view.MAX_SERVER_NAME_LEN,
        )
        if not ok:
            return
        try:
            new_id = self.service.create(self.profile_id, name)
        except ValueError as exc:
            QMessageBox.warning(view, "Ошибка", str(exc))
            return
        self.refresh(select_id=new_id)

    def rename(self):
        view = self.view
        item = view.listServers.currentItem()
        if item is None:
            QMessageBox.information(
                view, "Переименование",
                "Не выбран сервер для переименования."
            )
            return
        sid = item.data(Qt.ItemDataRole.UserRole)
        old_name = item.text()
        new_name, ok = view.ask_name_hint(
            "Переименовать сервер", "Новое имя",
            view.MAX_SERVER_NAME_LEN,
            default=old_name,
        )
        if not ok:
            return
        try:
            self.service.rename(sid, new_name, self.profile_id)
        except ValueError as exc:
            QMessageBox.warning(view, "Ошибка", str(exc))
            return
        self.refresh(select_id=sid)

    def delete(self):
        view = self.view
        item = view.listServers.currentItem()
        if item is None:
            QMessageBox.information(
                view, "Удаление",
                "Не выбран сервер для удаления."
            )
            return
        sid = item.data(Qt.ItemDataRole.UserRole)
        configs = self.service.repo.count_configs(sid)
        ans = QMessageBox.question(
            view, "Удалить",
            f"Удалить сервер «{item.text()}» со всеми cfg?\n\n"
            f"Будет удалено: конфигураций - {configs}.",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
        )
        if ans == QMessageBox.StandardButton.Yes:
            self.service.delete(sid)
            self.refresh()

    def duplicate(self):
        view = self.view
        item = view.listServers.currentItem()
        if item is None:
            QMessageBox.information(
                view, "Дублирование",
                "Не выбран сервер для дублирования."
            )
            return
        sid = item.data(Qt.ItemDataRole.UserRole)
        server = self.service.repo.get(sid)
        if not server:
            return
        new_name, ok = view.ask_name_hint(
            "Дублировать сервер", "Имя нового сервера",
            view.MAX_SERVER_NAME_LEN,
            default=f"{server['name']} (копия)",
        )
        if not ok:
            return
        try:
            new_id = self.service.duplicate(
                sid, new_name, self.profile_id
            )
        except ValueError as exc:
            QMessageBox.warning(view, "Ошибка", str(exc))
            return
        self.refresh(select_id=new_id)

    def enter(self):
        """Вход в выбранный сервер."""
        view = self.view
        item = view.listServers.currentItem()
        if item is None:
            QMessageBox.information(
                view, "Вход",
                "Не выбран сервер для входа."
            )
            return
        server_id = item.data(Qt.ItemDataRole.UserRole)
        view.window().go_main(server_id)