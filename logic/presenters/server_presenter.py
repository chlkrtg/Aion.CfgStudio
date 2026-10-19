"""Presenter для страницы серверов.

Логика аналогична ProfilePresenter, но с контекстом профиля.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox

from logic.presenters.base_presenter import BasePresenter
from logic.core.i18n import t
from logic.widgets.dialogs import ask_yes_no


class ServerPresenter(BasePresenter):
    """Логика страницы серверов внутри профиля."""

    def __init__(self, view, service, reference):
        super().__init__(view)
        self.service = service
        self.reference = reference
        self.profile_id: int | None = None

    # ============ контекст ============

    def set_profile(self, profile_id: int):
        """Запоминает id профиля, внутри которого работаем."""
        self.profile_id = profile_id

    # ============ жизненный цикл ============

    def on_enter(self):
        self.refresh()

    def on_leave(self) -> bool:
        self.save_note()

        return True

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
        profile_name = self.reference.get_profile_name(self.profile_id)
        if profile_name:
            view.lblTitle.setText(
                t("server.title").format(name=profile_name)
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
            from logic.widgets.empty_state import add_empty_item
            view.listServers.blockSignals(True)
            view.listServers.clear()
            add_empty_item(view.listServers, t("empty.servers"))
            view.listServers.blockSignals(False)
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

        # если ничего не выбрано - очистить
        if current is None:
            view.clear_details()
            return

        server_id = current.data(Qt.ItemDataRole.UserRole)
        server = self.service.repo.get(server_id)
        if not server:
            view.clear_details()
            return

        stats = {
            "configs": self.reference.count_configs_in_server(server_id),
        }
        view.fill_details(server, stats)

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
                self.view,
                t("dialog.error_title"),
                t("server.error.save_note").format(exc=exc),
            )

    # ============ действия ============

    def create(self):
        view = self.view
        if self.profile_id is None:
            return
        name, ok = view.ask_name_hint(
            t("server.dialog.new.title"),
            t("server.dialog.new.label"),
            view.MAX_SERVER_NAME_LEN,
        )
        if not ok:
            return
        try:
            new_id = self.service.create(self.profile_id, name)
        except ValueError as exc:
            QMessageBox.warning(view, t("dialog.error_title"), str(exc))
            return
        self.refresh(select_id=new_id)

    def rename(self):
        view = self.view
        item = view.listServers.currentItem()
        if item is None:
            QMessageBox.information(
                view, t("server.dialog.rename.title"),
                t("server.error.not_found"),
            )
            return
        sid = item.data(Qt.ItemDataRole.UserRole)
        old_name = item.text()
        new_name, ok = view.ask_name_hint(
            t("server.dialog.rename.title"),
            t("server.dialog.rename.label"),
            view.MAX_SERVER_NAME_LEN,
            default=old_name,
        )
        if not ok:
            return
        try:
            self.service.rename(sid, new_name, self.profile_id)
        except ValueError as exc:
            QMessageBox.warning(view, t("dialog.error_title"), str(exc))
            return
        self.refresh(select_id=sid)

    def delete(self):
        view = self.view
        item = view.listServers.currentItem()
        if item is None:
            return
        sid = item.data(Qt.ItemDataRole.UserRole)
        configs = self.reference.count_configs_in_server(sid)
        ans = ask_yes_no(
            view,
            t("server.dialog.delete.title"),
            t("server.confirm.delete").format(
                name=item.text(), c=configs
            )
        )
        if ans:
            self.service.delete(sid)
            self.refresh()

    def duplicate(self):
        view = self.view
        item = view.listServers.currentItem()
        if item is None:
            return
        sid = item.data(Qt.ItemDataRole.UserRole)
        server = self.service.repo.get(sid)
        if not server:
            return
        new_name, ok = view.ask_name_hint(
            t("server.dialog.dup.title"),
            t("server.dialog.dup.label"),
            view.MAX_SERVER_NAME_LEN,
            default=f"{server['name']} {t('server.copy_suffix')}",
        )
        if not ok:
            return
        try:
            new_id = self.service.duplicate(
                sid, new_name, self.profile_id
            )
        except ValueError as exc:
            QMessageBox.warning(view, t("dialog.error_title"), str(exc))
            return
        self.refresh(select_id=new_id)

    def enter(self):
        """Вход в выбранный сервер."""
        view = self.view
        item = view.listServers.currentItem()
        if item is None:
            QMessageBox.information(
                view, t("server.dialog.enter.title"),
                t("server.error.not_found"),
            )
            return
        server_id = item.data(Qt.ItemDataRole.UserRole)
        if server_id is None:  # плейсхолдер
            return
        view.window().go_main(server_id)