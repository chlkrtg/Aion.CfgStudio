"""Presenter для страницы cfg-файлов.

Дерево конфигов, превью, импорт / экспорт, логи, контекстное меню.
"""
import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QTreeWidgetItem, QFileDialog, QInputDialog, QMessageBox,
)

from logic.presenters.base_presenter import BasePresenter
from logic.core.i18n import t
from logic.widgets.dialogs import ask_yes_no, ask_yes_no_cancel
from logic.widgets.empty_state import add_empty_node


class MainPresenter(BasePresenter):
    """Логика страницы cfg."""

    def __init__(self, view, service, reference):
        super().__init__(view)
        self.service = service
        self.reference = reference
        self.profile_id: int | None = None
        self.server_id: int | None = None

        # Хранилище состояний редактора для каждого cfg
        # {config_id: {"scroll": int, "search": str, "cursor": int}}
        self._editor_states: dict[int, dict] = {}

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
        if self._has_unsaved_changes():
            ans = ask_yes_no_cancel(
                self.view,
                t("editor.dialog.unsaved.title"),
                t("editor.dialog.unsaved.text")
            )
            if ans == "cancel":
                return False
            if ans == "yes":
                self.save_preview()
        self.view.clear_preview()
        self.view.treeConfigs.clearSelection()
        return True

    def _has_unsaved_changes(self) -> bool:
        """Проверяет, отличается ли текст превью от БД (с нормализацией)."""
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            return False

        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.service.repo.get(config_id)
        if not cfg:
            return False

        # Нормализация: приводим к единому виду
        def normalize(text: str) -> str:
            if not text:
                return ""
            # Убираем \r (Windows), обрезаем пробелы в конце файла
            return text.replace("\r\n", "\n").strip()

        current_text = normalize(view.editPreview.toPlainText())
        saved_text = normalize(cfg["content"] or "")

        return current_text != saved_text

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

        # прочитать cfg из БД
        cfgs = self.service.repo.all_for_server(self.server_id)
        if not cfgs:
            view.treeConfigs.blockSignals(True)
            add_empty_node(view.treeConfigs, t("empty.configs"))
            view.treeConfigs.setCurrentItem(None)
            view.treeConfigs.blockSignals(False)
            view.editFilter.blockSignals(True)
            view.editFilter.clear()
            view.editFilter.blockSignals(False)
            view.editFilter.setEnabled(False)
            view.clear_preview()
            view.set_controls_enabled(False)
            return

        view.editFilter.setEnabled(True)

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
            view, t("main.dialog.import.title"), "",
            "Cfg (*.cfg);;Все файлы (*)"
        )
        if not path:
            return

        default_name = os.path.basename(path)
        name, ok = view.ask_name_hint(
            t("main.dialog.import.title"),
            t("main.dialog.import.label"),
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
            QMessageBox.critical(
                view, t("main.error.read"), str(exc)
            )
            return
        except ValueError as exc:
            QMessageBox.warning(
                view, t("dialog.error_title"), str(exc)
            )
            return

        self.refresh(select_id=config_id)

    def export_config(self):
        """Экспорт выбранного cfg (зашифрованный или plain)."""
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(
                view, t("dialog.error_title"),
                t("main.error.no_selection"),
            )
            return

        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.service.repo.get(config_id)
        if not cfg:
            return

        path, _ = QFileDialog.getSaveFileName(
            view,
            t("main.dialog.export.filename_title"),  # ← новый ключ
            cfg["filename"],
            "Cfg (*.cfg);;Все файлы (*)",  # ← фильтр не переводим
        )
        if not path:
            return

        fmt, ok = QInputDialog.getItem(
            view,
            t("main.dialog.export.format"),
            t("main.dialog.export.label"),
            [
                t("main.dialog.export.encrypted"),
                t("main.dialog.export.plain"),
            ],
            0, False,
        )
        if not ok:
            return

        encrypted = fmt == t("main.dialog.export.encrypted")
        try:
            self.service.export_to_file(config_id, path, encrypted)
        except (OSError, ValueError) as exc:
            QMessageBox.critical(
                view, t("main.error.write"), str(exc)
            )
            return
        QMessageBox.information(
            view, t("main.info.done"),
            t("main.info.exported").format(path=path),
        )

    def rename_config(self):
        """Переименование cfg."""
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(
                view, t("dialog.error_title"),
                t("main.error.no_selection"),
            )
            return
        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.service.repo.get(config_id)
        if not cfg:
            return
        new_name, ok = view.ask_name_hint(
            t("main.dialog.rename.title"),
            t("main.dialog.rename.label"),
            view.MAX_CONFIG_NAME_LEN,
            default=cfg["filename"],
        )
        if not ok:
            return
        try:
            self.service.rename(config_id, new_name)
        except ValueError as exc:
            QMessageBox.warning(
                view, t("dialog.error_title"), str(exc)
            )
            return
        self.refresh(select_id=config_id)

    def delete_config(self):
        """Удаление cfg."""
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(
                view, t("dialog.error_title"),
                t("main.error.no_selection"),
            )
            return
        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        ans = ask_yes_no(
            view,
            t("main.dialog.delete.title"),
            t("main.confirm.delete").format(name=item.text(0)),
        )
        if ans:
            self.service.delete(config_id)
            self._editor_states.pop(config_id, None)
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
        default = f"{base}_{t('main.copy_suffix')}.cfg"
        new_name, ok = view.ask_name_hint(
            t("main.dialog.dup.title"),
            t("main.dialog.dup.label"),
            view.MAX_CONFIG_NAME_LEN,
            default=default,
        )
        if not ok:
            return
        try:
            new_id = self.service.duplicate(config_id, new_name)
        except ValueError as exc:
            QMessageBox.warning(
                view, t("dialog.error_title"), str(exc)
            )
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
        if config_id is None:  # плейсхолдер
            return
        view.window().go_editor(config_id)

    def show_logs(self):
        """Открытие диалога истории изменений."""
        from logic.widgets.logs_dialog import LogsDialog
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(
                view, t("dialog.error_title"),
                t("main.error.no_selection"),
            )
            return
        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.service.repo.get(config_id)
        if not cfg:
            return
        logs = self.service.repo.logs(config_id)
        if not logs:
            QMessageBox.information(
                view,
                t("main.dialog.logs.title"),
                t("main.info.no_logs").format(name=cfg["filename"]),
            )
            return
        dialog = LogsDialog(view, logs, filename=cfg["filename"])
        dialog.exec()

    def change_server(self):
        """Возврат к выбору сервера в текущем профиле."""
        if self.profile_id is None:
            return
        self.view.window().go_server(self.profile_id)

    def save_preview(self):
        """Сохраняет текст из окна предпросмотра в cfg.

        Команды, которых нет в БД, отсекаются.
        Дубликаты схлопываются в одно вхождение.
        """
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(
                view, t("dialog.error_title"),
                t("main.error.no_selection"),
            )
            return
        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        text = view.editPreview.toPlainText()

        if not text.strip():
            ans = ask_yes_no(
                view,
                t("main.dialog.clear.title"),  # ключ надо добавить
                t("main.confirm.clear")
            )
            if not ans:
                return

        try:
            unknown, duplicates = self.service.save_content(config_id, text)
        except ValueError as exc:
            QMessageBox.warning(
                view, t("dialog.error_title"), str(exc)
            )
            return

        msgs = []
        if unknown:
            msgs.append(
                t("main.info.unknown_commands").format(n=unknown)
            )
        if duplicates:
            msgs.append(
                t("main.info.duplicates").format(n=duplicates)
            )

        if msgs:
            QMessageBox.information(
                view,
                t("main.info.saved"),
                t("main.info.saved_with_details").format(
                    details="\n".join(msgs)
                ),
            )
        else:
            QMessageBox.information(
                view,
                t("main.info.done"),
                t("main.info.saved"),
            )
        self.refresh(select_id=config_id)

    def revert_preview(self):
        """Сбрасывает правки в превью, возвращает текст из БД."""
        view = self.view
        item = view.treeConfigs.currentItem()
        if item is None:
            return

        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.service.repo.get(config_id)
        if not cfg:
            return

        view.editPreview.setPlainText(cfg["content"] or "")

    def _save_editor_state(self, config_id: int):
        """Сохраняет позицию скролла, курсора и текст поиска для cfg."""
        if config_id is None:
            return

        editor = self.view.editPreview
        scroll_pos = editor.verticalScrollBar().value()
        cursor_pos = editor.textCursor().position()
        search_term = self.view.search_panel.edit.text()

        self._editor_states[config_id] = {
            "scroll": scroll_pos,
            "cursor": cursor_pos,
            "search": search_term,
        }

    def _restore_editor_state(self, config_id: int):
        """Восстанавливает состояние при открытии cfg."""
        editor = self.view.editPreview
        state = self._editor_states.get(config_id)

        if state is None:
            # Если состояния нет (первое открытие) — сбрасываем на начало и закрываем поиск
            editor.verticalScrollBar().setValue(0)
            editor.moveCursor(editor.textCursor().MoveOperation.Start)
            if self.view.search_panel.isVisible():
                self.view.search_panel.hide_panel()
            return

        # 1. Восстанавливаем скролл (через QTimer, чтобы Qt успел пересчитать размеры)
        from PyQt6.QtCore import QTimer
        QTimer.singleShot(10, lambda: editor.verticalScrollBar().setValue(state["scroll"]))

        # 2. Восстанавливаем курсор
        cursor = editor.textCursor()
        cursor.setPosition(state["cursor"])
        editor.setTextCursor(cursor)

        # 3. Восстанавливаем поиск
        if state["search"]:
            self.view.search_panel.edit.setText(state["search"])
            if not self.view.search_panel.isVisible():
                self.view.search_panel.show_panel()
        else:
            if self.view.search_panel.isVisible():
                self.view.search_panel.hide_panel()