"""Presenter для страницы cfg-файлов.

Дерево конфигов, превью, импорт / экспорт, логи, контекстное меню.
"""
import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QTreeWidgetItem, QFileDialog, QInputDialog, QMessageBox,
)

from logic.presenters.base_presenter import BasePresenter


class MainPresenter(BasePresenter):
    """Логика страницы cfg."""

    def __init__(self, view, service, reference):
        super().__init__(view)
        self.service = service
        self.reference = reference
        self.profile_id: int | None = None
        self.server_id: int | None = None

    # ============= контекст =============

    def set_context(self, profile_id: int, server_id: int):
        """Запоминает контекст и сбрасывает фильтр при смене сервера."""
        server_changed = (self.server_id != server_id)
        self.profile_id = profile_id
        self.server_id = server_id
        if server_changed:
            self.view.editFilter.clear()

    # ============= жизненный цикл =============

    def on_enter(self):
        self.refresh()

    def on_leave(self):
        self.view.clear_preview()
        self.view.treeConfigs.clearSelection()

    # ============= загрузка =============

    def refresh(self, select_id: int | None = None):
        """Перестраивает дерево cfg."""
        view = self.view

        # запомнить выбор
        if select_id is None:
            current = view.treeConfigs.currentItem()
            if current is not None:
                select_id = current.data(0, Qt.ItemDataRole.UserRole)

        # обновить заголовок окна
        profile_name = (
            self.reference.get_profile_name(self.profile_id)
            if self.profile_id else None
        )
        server_name = (
            self.reference.get_server_name(self.server_id)
            if self.server_id else None
        )

        title = "Aion.CfgStudio"
        if profile_name:
            title += f" — {profile_name}"
        if server_name:
            title += f" / {server_name}"
        view.window().setWindowTitle(title)

        view.treeConfigs.clear()

        if self.server_id is None:
            view.clear_preview()
            view.set_controls_enabled(False)
            return

        # заполнить дерево
        for cfg in self.service.repo.all_for_server(self.server_id):
            node = QTreeWidgetItem([
                cfg["filename"],
                cfg["modified_at"] or "",
            ])
            node.setData(0, Qt.ItemDataRole.UserRole, cfg["id"])
            view.treeConfigs.addTopLevelItem(node)

        # восстановить выбор
        selected = False
        if select_id is not None:
            for i in range(view.treeConfigs.topLevelItemCount()):
                node = view.treeConfigs.topLevelItem(i)
                if node.data(0, Qt.ItemDataRole.UserRole) == select_id:
                    view.treeConfigs.setCurrentItem(node)
                    selected = True
                    break

        # если не нашли - первый
        if not selected and view.treeConfigs.topLevelItemCount() > 0:
            view.treeConfigs.setCurrentItem(
                view.treeConfigs.topLevelItem(0)
            )
            selected = True

        if not selected:
            view.clear_preview()

        view.set_controls_enabled(selected)
        self.apply_filter(view.editFilter.text())

    # ============= обработка выбора =============

    def on_selection(self):
        """Показывает превью выбранного cfg."""
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            view.clear_preview()
            view.set_controls_enabled(False)
            return
        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        if config_id is None:
            view.clear_preview()
            view.set_controls_enabled(False)
            return

        cfg = self.service.repo.get(config_id)
        if not cfg:
            view.set_controls_enabled(False)
            return

        view.lblPreviewName.setText(cfg["filename"])
        view.editPreview.setPlainText(cfg["content"] or "")
        view.set_controls_enabled(True)

    # ============= фильтр =============

    def apply_filter(self, text: str):
        """Фильтр по имени/дате. Прячет неподходящие, выделяет первый видимый."""
        view = self.view
        text = text.lower().strip()

        # скрыть / показать
        for i in range(view.treeConfigs.topLevelItemCount()):
            item = view.treeConfigs.topLevelItem(i)
            name = item.text(0).lower()
            date = item.text(1).lower()
            match = text in name or text in date
            item.setHidden(bool(text) and not match)

        # проверить, виден ли текущий
        current = view.treeConfigs.currentItem()
        if current is not None and not current.isHidden():
            return

        # найти первый видимый
        first_visible = None
        for i in range(view.treeConfigs.topLevelItemCount()):
            item = view.treeConfigs.topLevelItem(i)
            if not item.isHidden():
                first_visible = item
                break

        if first_visible is not None:
            view.treeConfigs.setCurrentItem(first_visible)
        else:
            view.treeConfigs.setCurrentItem(None)
            view.treeConfigs.clearSelection()
            view.clear_preview()
            view.set_controls_enabled(False)

    # ============= действия =============

    def import_config(self):
        """Импорт cfg через диалог."""
        view = self.view
        path, _ = QFileDialog.getOpenFileName(
            view, "Импорт cfg", "", "Cfg (*.cfg);;Все файлы (*)"
        )
        if not path:
            return

        default_name = os.path.basename(path)
        name, ok = view.ask_name_hint(
            "Имя файла в проекте", "Имя",
            view.MAX_CONFIG_NAME_LEN,
            default=default_name,
        )
        if not ok:
            return

        try:
            config_id = self.service.import_from_file(
                path, self.server_id, name
            )
        except OSError as exc:
            QMessageBox.critical(view, "Ошибка чтения", str(exc))
            return
        except ValueError as exc:
            QMessageBox.warning(view, "Ошибка", str(exc))
            return

        self.refresh(select_id=config_id)

    def export_config(self):
        """Экспорт выбранного cfg (зашифрованный или plain)."""
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(
                view, "Ошибка",
                "Не выбран конфигурационный файл."
            )
            return

        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.service.repo.get(config_id)
        if not cfg:
            return

        path, _ = QFileDialog.getSaveFileName(
            view, "Экспорт cfg", cfg["filename"],
            "Cfg (*.cfg);;Все файлы (*)"
        )
        if not path:
            return

        fmt, ok = QInputDialog.getItem(
            view, "Формат экспорта",
            "Выберите формат:",
            ["Зашифрованный (для игры)",
             "Plain-текст (для чтения)"],
            0, False,
        )
        if not ok:
            return

        encrypted = fmt.startswith("Зашифрованный")
        try:
            self.service.export_to_file(config_id, path, encrypted)
        except (OSError, ValueError) as exc:
            QMessageBox.critical(view, "Ошибка записи", str(exc))
            return

        QMessageBox.information(
            view, "Готово", f"Сохранено в {path}"
        )

    def rename_config(self):
        """Переименование cfg."""
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(
                view, "Ошибка",
                "Не выбран конфигурационный файл."
            )
            return

        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.service.repo.get(config_id)
        if not cfg:
            return

        new_name, ok = view.ask_name_hint(
            "Переименовать cfg", "Новое имя",
            view.MAX_CONFIG_NAME_LEN,
            default=cfg["filename"],
        )
        if not ok:
            return

        try:
            self.service.rename(config_id, new_name)
        except ValueError as exc:
            QMessageBox.warning(view, "Ошибка", str(exc))
            return

        self.refresh(select_id=config_id)

    def delete_config(self):
        """Удаление cfg."""
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(
                view, "Ошибка",
                "Не выбран конфигурационный файл."
            )
            return

        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        ans = QMessageBox.question(
            view, "Удалить",
            f"Удалить cfg «{item.text(0)}»?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
        )
        if ans == QMessageBox.StandardButton.Yes:
            self.service.delete(config_id)
            view.treeConfigs.clearSelection()
            self.refresh()

    def duplicate_config(self):
        """Дублирование cfg."""
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            return

        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.service.repo.get(config_id)
        if not cfg:
            return

        base = cfg["filename"]
        if base.endswith(".cfg"):
            base = base[:-4]
        default = f"{base}_copy.cfg"

        new_name, ok = view.ask_name_hint(
            "Дублировать cfg", "Имя нового файла",
            view.MAX_CONFIG_NAME_LEN,
            default=default,
        )
        if not ok:
            return

        try:
            new_id = self.service.duplicate(config_id, new_name)
        except ValueError as exc:
            QMessageBox.warning(view, "Ошибка", str(exc))
            return

        self.refresh(select_id=new_id)

    def open_selected(self):
        """Открытие редактора для выбранного cfg."""
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(
                view, "Ошибка",
                "Не выбран конфигурационный файл."
            )
            return
        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        view.window().go_editor(config_id)

    def show_logs(self):
        """Открытие диалога истории изменений."""
        from logic.logs_dialog import LogsDialog

        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(
                view, "Ошибка",
                "Не выбран конфигурационный файл."
            )
            return

        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.service.repo.get(config_id)
        if not cfg:
            return

        logs = self.service.repo.logs(config_id)
        if not logs:
            QMessageBox.information(
                view, "История",
                f"Изменений нет для файла «{cfg['filename']}»."
            )
            return

        dialog = LogsDialog(view, logs, filename=cfg["filename"])
        dialog.exec()

    def change_server(self):
        """Возврат к выбору сервера в текущем профиле."""
        if self.profile_id is None:
            return
        self.view.window().go_server(self.profile_id)