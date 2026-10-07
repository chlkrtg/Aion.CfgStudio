"""Presenter для страницы профилей.

Вся логика страницы профилей: список, автосохранение описания,
CRUD, обработка выбора. View только рисует.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox

from logic.presenters.base_presenter import BasePresenter


class ProfilePresenter(BasePresenter):
    """Логика страницы профилей."""

    def __init__(self, view, service, reference):
        super().__init__(view)
        self.service = service
        self.reference = reference

    # ============ жизненный цикл ============

    def on_enter(self):
        """Загрузка списка при входе."""
        self.refresh()

    def on_leave(self):
        """Сохранение описания при уходе."""
        self.save_description()

    # ============ загрузка ============

    def refresh(self, select_id: int | None = None):
        """Перестраивает список профилей.

        Если select_id не задан - пытается сохранить текущий выбор.
        """
        view = self.view

        # запомнить текущий выбор
        if select_id is None:
            current = view.listProfiles.currentItem()
            if current is not None:
                select_id = current.data(Qt.ItemDataRole.UserRole)

        # сохранить описание текущего перед перестройкой
        self.save_description()

        # перестроить список
        view.listProfiles.blockSignals(True)
        view.listProfiles.clear()
        for row in self.service.repo.all():
            item = QListWidgetItem(row["name"])
            item.setData(Qt.ItemDataRole.UserRole, row["id"])
            view.listProfiles.addItem(item)
        view.listProfiles.blockSignals(False)

        if not view.listProfiles.count():
            view.clear_details()
            view.set_controls_enabled(False)
            return

        view.set_controls_enabled(True)

        # выбрать нужный профиль (или первый)
        target_row = 0
        if select_id is not None:
            for i in range(view.listProfiles.count()):
                item = view.listProfiles.item(i)
                if item.data(Qt.ItemDataRole.UserRole) == select_id:
                    target_row = i
                    break
        view.listProfiles.setCurrentRow(target_row)

    # ============ обработка выбора ============

    def on_profile_selected(self, current, previous=None):
        """Заполняет правую панель при выборе профиля.

        Перед заполнением сохраняет описание предыдущего профиля.
        """
        view = self.view

        # сохранить описание предыдущего
        if previous is not None:
            self._persist_description(previous)

        # если ничего не выбрано - очистить
        if current is None:
            view.clear_details()
            return

        # получить профиль из БД
        profile_id = current.data(Qt.ItemDataRole.UserRole)
        profile = self.service.repo.get(profile_id)
        if not profile:
            view.clear_details()
            return

        # заполнить панель (View сам знает, как это рисовать)
        stats = {
            "servers": self.reference.count_servers(profile_id),
            "configs": self.reference.count_configs_in_profile(profile_id),
        }
        view.fill_details(profile, stats)

    # ============ автосохранение описания ============

    def save_description(self):
        """Сохраняет описание текущего профиля.

        Вызывается из on_leave и из refresh (перед перестройкой).
        """
        self._persist_description(self.view.listProfiles.currentItem())

    def _persist_description(self, item):
        """Сохраняет описание для указанного item."""
        if item is None:
            return
        pid = item.data(Qt.ItemDataRole.UserRole)
        text = self.view.editDescription.toPlainText()
        try:
            self.service.update_description(pid, text)
        except Exception as exc:
            QMessageBox.warning(
                self.view, "Ошибка",
                f"Не удалось сохранить описание профиля:\n{exc}"
            )

    # ============ действия ============

    def create(self):
        """Создаёт профиль."""
        view = self.view
        name, ok = view.ask_name_hint(
            "Новый профиль", "Имя профиля",
            view.MAX_PROFILE_NAME_LEN,
        )
        if not ok:
            return

        try:
            new_id = self.service.create(name)
        except ValueError as exc:
            QMessageBox.warning(view, "Ошибка", str(exc))
            return

        self.refresh(select_id=new_id)

    def rename(self):
        """Переименовывает профиль."""
        view = self.view
        item = view.listProfiles.currentItem()
        if item is None:
            QMessageBox.information(
                view, "Переименование",
                "Не выбран профиль для переименования."
            )
            return

        pid = item.data(Qt.ItemDataRole.UserRole)
        old_name = item.text()

        new_name, ok = view.ask_name_hint(
            "Переименовать профиль", "Новое имя",
            view.MAX_PROFILE_NAME_LEN,
            default=old_name,
        )
        if not ok:
            return

        try:
            self.service.rename(pid, new_name)
        except ValueError as exc:
            QMessageBox.warning(view, "Ошибка", str(exc))
            return

        self.refresh(select_id=pid)

    def delete(self):
        """Удаляет профиль."""
        view = self.view
        item = view.listProfiles.currentItem()
        if item is None:
            QMessageBox.information(
                view, "Удаление",
                "Не выбран профиль для удаления."
            )
            return

        pid = item.data(Qt.ItemDataRole.UserRole)
        servers = self.service.repo.count_servers(pid)
        configs = self.service.repo.count_configs(pid)

        ans = QMessageBox.question(
            view, "Удалить",
            f"Удалить профиль «{item.text()}» со всем содержимым?\n\n"
            f"Будет удалено: серверов - {servers}, "
            f"конфигураций - {configs}.",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
        )
        if ans == QMessageBox.StandardButton.Yes:
            self.service.delete(pid)
            self.refresh()

    def duplicate(self):
        """Дублирует профиль."""
        view = self.view
        item = view.listProfiles.currentItem()
        if item is None:
            QMessageBox.information(
                view, "Дублирование",
                "Не выбран профиль для дублирования."
            )
            return

        pid = item.data(Qt.ItemDataRole.UserRole)
        profile = self.service.repo.get(pid)
        if not profile:
            return

        new_name, ok = view.ask_name_hint(
            "Дублировать профиль", "Имя нового профиля",
            view.MAX_PROFILE_NAME_LEN,
            default=f"{profile['name']} (копия)",
        )
        if not ok:
            return

        try:
            new_id = self.service.duplicate(pid, new_name)
        except ValueError as exc:
            QMessageBox.warning(view, "Ошибка", str(exc))
            return

        self.refresh(select_id=new_id)

    def enter(self):
        """Вход в выбранный профиль."""
        view = self.view
        item = view.listProfiles.currentItem()
        if item is None:
            QMessageBox.information(
                view, "Вход",
                "Не выбран профиль для входа."
            )
            return
        profile_id = item.data(Qt.ItemDataRole.UserRole)
        view.window().go_server(profile_id)