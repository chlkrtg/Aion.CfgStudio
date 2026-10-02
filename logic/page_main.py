"""Главная страница: дерево cfg-файлов выбранного сервера."""
import os
import re

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QTreeWidgetItem,
                             QFileDialog, QInputDialog, QMessageBox)
from PyQt6.QtGui import QShortcut, QKeySequence

from logic.context_menu import build_context_menu
from logic.base_page import BasePage
from logic.shortcuts import bind_shortcuts, FOCUSED
from logic.constants import MAX_CONFIG_NAME_LEN
from ui.main_window import Ui_MainWindow
from parsers.cfg_crypto import decrypt, encrypt, looks_like_encrypted


class PageMain(BasePage, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # очень важные поля!
        self.profile_id = None
        self.server_id = None

        # подключение контекстного меню
        self.treeConfigs.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeConfigs.customContextMenuRequested.connect(self._show_context_menu)

        self._connect_signals()

        # знаменитые хоткеи
        bind_shortcuts(self.treeConfigs, {
            "F1": lambda: self.window().go_video(),
            "F2": self._rename_config,
            "Delete": self._delete_config,
            "Ctrl+N": lambda: self.window().go_editor(None),
            "Ctrl+O": self._import_config,
            "Ctrl+S": self._export_config,
            "Ctrl+E": self._open_selected,
        }, FOCUSED)

        # Ctrl+Q — глобально на странице
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(self._on_change_server)

    def _connect_signals(self):
        self.btnAddConfig.clicked.connect(
            lambda: self.window().go_editor(None)
        )
        self.btnOpenEditor.clicked.connect(self._open_selected)
        self.btnImportConfig.clicked.connect(self._import_config)
        self.btnExportConfig.clicked.connect(self._export_config)
        self.btnDeleteConfig.clicked.connect(self._delete_config)
        self.btnShowLogs.clicked.connect(self._show_logs)
        self.btnRenameConfig.clicked.connect(self._rename_config)
        self.treeConfigs.itemSelectionChanged.connect(self._on_selection)
        self.editFilter.textChanged.connect(self._on_filter_changed)

        # actions
        self.actionChangeServer.triggered.connect(self._on_change_server)
        self.actionRename.triggered.connect(self._rename_config)
        self.actionVideoHelp.triggered.connect(
            lambda: self.window().go_video()
        )
        self.actionChangeProfile.triggered.connect(
            lambda: self.window().go_profile()
        )
        self.actionImportCfg.triggered.connect(self._import_config)
        self.actionExportCfg.triggered.connect(self._export_config)
        self.actionAbout.triggered.connect(self._show_about)
        self.actionNewConfig.triggered.connect(
            lambda: self.window().go_editor(None)
        )

    def set_context(self, profile_id: int, server_id: int):
        """Запоминает все данные, выбранные на предыдущих шагах."""
        server_changed = (self.server_id != server_id)
        self.profile_id = profile_id
        self.server_id = server_id
        if server_changed:
            self.editFilter.clear()

    # =================== обработчики ===================

    def _on_change_server(self):
        """Возвращает к выбору сервера в текущем профиле."""
        if self.profile_id is None:
            return
        self.window().go_server(self.profile_id)

    def _on_selection(self):
        """Обработка выбора конфига."""
        item = self.treeConfigs.currentItem()
        if item is None:
            self._clear_preview()
            self._set_controls_enabled(False)
            return
        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        if config_id is None:
            self._clear_preview()
            self._set_controls_enabled(False)
            return
        cfg = self.db.get_config(config_id)
        if not cfg:
            self._set_controls_enabled(False)
            return
        self.lblPreviewName.setText(cfg["filename"])
        self.editPreview.setPlainText(cfg["content"] or "")
        self._set_controls_enabled(True)

    def on_enter(self):
        """Загружает конфиги для выбранной пары профиль-сервер"""
        self.refresh()

    def on_leave(self):
        """Сбрасывает превью и фокус с конфига при уходе со страницы"""
        self._clear_preview()
        self.treeConfigs.clearSelection()

    def _on_filter_changed(self, text: str):
        """Поиск конфига по имени / дате изменения.

        После фильтрации:
          - если текущий выбранный cfg скрыт - выделяем первый видимый;
          - если видимых нет - сбрасываем превью и гасим кнопки.
        """
        text = text.lower().strip()

        # 1. прячем / показываем элементы
        for i in range(self.treeConfigs.topLevelItemCount()):
            item = self.treeConfigs.topLevelItem(i)
            name = item.text(0).lower()
            date = item.text(1).lower()
            match = text in name or text in date
            item.setHidden(bool(text) and not match)

        # 2. проверяем, виден ли текущий
        current = self.treeConfigs.currentItem()
        current_visible = current is not None and not current.isHidden()

        if current_visible:
            return  # всё ок - ничего не меняем

        # 3. ищем первый видимый
        first_visible = None
        for i in range(self.treeConfigs.topLevelItemCount()):
            item = self.treeConfigs.topLevelItem(i)
            if not item.isHidden():
                first_visible = item
                break

        if first_visible is not None:
            # выделяем первый видимый - превью и кнопки обновятся автоматически
            self.treeConfigs.setCurrentItem(first_visible)
        else:
            # ничего не видно - полный сброс
            self.treeConfigs.setCurrentItem(None)
            self.treeConfigs.clearSelection()
            self._clear_preview()
            self._set_controls_enabled(False)

    def _set_controls_enabled(self, enabled: bool):
        """Включает / выключает контролы, требующие выбранного cfg."""
        self.set_controls_enabled(
            enabled,
            self.btnOpenEditor,
            self.btnExportConfig,
            self.btnDeleteConfig,
            self.btnShowLogs,
            self.btnRenameConfig,
        )

    def refresh(self,  select_id: int | None = None):
        # запоминаем, какой cfg был выбран
        prev_id = select_id
        if prev_id is None:
            current = self.treeConfigs.currentItem()
            if current is not None:
                prev_id = current.data(0, Qt.ItemDataRole.UserRole)

        profile = self.db.get_profile(self.profile_id) if self.profile_id else None
        server = self.db.get_server(self.server_id) if self.server_id else None

        title = "Aion.CfgStudio"
        if profile:
            title += f" — {profile['name']}"
        if server:
            title += f" / {server['name']}"
        self.window().setWindowTitle(title)

        self.treeConfigs.clear()

        if self.server_id is None:
            self._clear_preview()
            self._set_controls_enabled(False)
            return

        # загрузка конфигов
        for cfg in self.db.list_configs(self.server_id):
            node = QTreeWidgetItem([
                cfg["filename"],
                cfg["modified_at"] or "",
            ])
            node.setData(0, Qt.ItemDataRole.UserRole, cfg["id"])
            self.treeConfigs.addTopLevelItem(node)

        # восстанавливаем выбор
        selected = False
        if prev_id is not None:
            for i in range(self.treeConfigs.topLevelItemCount()):
                node = self.treeConfigs.topLevelItem(i)
                if node.data(0, Qt.ItemDataRole.UserRole) == prev_id:
                    self.treeConfigs.setCurrentItem(node)
                    selected = True
                    break

        # если не нашли - выбираем первый доступный
        if not selected and self.treeConfigs.topLevelItemCount() > 0:
            self.treeConfigs.setCurrentItem(self.treeConfigs.topLevelItem(0))
            selected = True

        if not selected:
            self._clear_preview()

        self._set_controls_enabled(selected)
        self._on_filter_changed(self.editFilter.text())

    def _populate_config_values(self, config_id: int, content: str):
        """Парсит content и заполняет ConfigValues найденными значениями.

        Работает после импорта, чтобы редактор открывался с уже
        отмеченными командами и подставленными значениями.
        """
        CFG_KV_RE = re.compile(
            r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*"?([^"]*)"?\s*$'
        )

        parsed: dict[str, str] = {}
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith(("--", "//", "#")):
                continue
            m = CFG_KV_RE.match(line)
            if m:
                parsed[m.group(1)] = m.group(2)

        if not parsed:
            return

        # карта key_name -> command_id
        all_commands = self.db.list_commands("debug")
        key_to_id = {c["key_name"]: c["id"] for c in all_commands}

        rows = []
        for key, value in parsed.items():
            cmd_id = key_to_id.get(key)
            if cmd_id is not None:
                rows.append((cmd_id, 1, value))

        if rows:
            self.db.save_config_values_bulk(config_id, rows)

    # =============== кнопки ===============

    def _clear_preview(self):
        """Сбрасывает панель предпросмотра."""
        self.lblPreviewName.setText("— файл не выбран —")
        self.editPreview.clear()

    def _import_config(self):
        """Импорт конфига без защиты от дубликатов. Расшифровка + подстановка в превью."""
        path, _ = QFileDialog.getOpenFileName(
            self, "Импорт cfg", "", "Cfg (*.cfg);;Все файлы (*)"
        )
        if not path:
            return

        try:
            with open(path, "rb") as f:
                raw = f.read()
        except OSError as exc:
            QMessageBox.critical(self, "Ошибка чтения", str(exc))
            return

        # если файл зашифрован - расшифровываем
        if looks_like_encrypted(raw):
            content = decrypt(raw)
        else:
            # уже plain-текст (или комментарии)
            try:
                content = raw.decode("latin1", errors="replace")
            except Exception:
                content = raw.decode("utf-8", errors="replace")

        default_name = os.path.basename(path)
        name, ok = self.ask_name(
            "Имя файла в проекте", "Имя:",
            default=default_name,
            max_len=MAX_CONFIG_NAME_LEN,
        )
        if not ok:
            return

        name = self.validate_name(name, MAX_CONFIG_NAME_LEN, "Имя файла")
        if name is None:
            return

        try:
            config_id = self.db.create_config(self.server_id, name, content)
            self._populate_config_values(config_id, content)
        except Exception as exc:
            QMessageBox.critical(self, "Ошибка БД", str(exc))
            return
        self.refresh(select_id=config_id)

    def _export_config(self):
        """Экспорт выбранного конфига в нужном режиме (шифр / текст)"""
        item = self.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(self, "Ошибка", "Не выбран конфигурационный файл.")
            return
        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.db.get_config(config_id)
        if not cfg:
            return

        path, _ = QFileDialog.getSaveFileName(
            self, "Экспорт cfg", cfg["filename"], "Cfg (*.cfg);;Все файлы (*)"
        )
        if not path:
            return

        # спрашиваем формат
        fmt, ok = QInputDialog.getItem(
            self, "Формат экспорта",
            "Выберите формат:",
            ["Зашифрованный (для игры)", "Plain-текст (для чтения)"],
            0, False,
        )
        if not ok:
            return

        content = cfg["content"] or ""
        try:
            if fmt.startswith("Зашифрованный"):
                with open(path, "wb") as f:
                    f.write(encrypt(content))
            else:
                with open(path, "w", encoding="latin1", errors="replace") as f:
                    f.write(content)
        except OSError as exc:
            QMessageBox.critical(self, "Ошибка записи", str(exc))
            return

        QMessageBox.information(self, "Готово", f"Сохранено в {path}")

    def _open_selected(self):
        """Открытие редактора для выбранного конфига."""
        item = self.treeConfigs.currentItem()

        if item is None:
            QMessageBox.warning(self, "Ошибка", "Не выбран конфигурационный файл.")
            return
        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        self.window().go_editor(config_id)

    def _rename_config(self):
        """Ренейм выбранного конфига."""
        item = self.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(self, "Ошибка", "Не выбран конфигурационный файл.")
            return

        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.db.get_config(config_id)
        if not cfg:
            return

        new_name, ok = self.ask_name(
            "Переименовать cfg",
            "Новое имя:",
            default=cfg["filename"],
            max_len=MAX_CONFIG_NAME_LEN,
        )
        if not ok:
            return

        new_name = self.validate_name(new_name, MAX_CONFIG_NAME_LEN, "Имя файла")
        if new_name is None:
            return

        if new_name == cfg["filename"]:
            return

        try:
            self.db.rename_config(config_id, new_name)
        except Exception as exc:
            QMessageBox.critical(self, "Ошибка", str(exc))
            return

        self.refresh()

    def _duplicate_config(self):
        """Дублирует выбранный конфиг."""
        item = self.treeConfigs.currentItem()
        if item is None:
            return

        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        cfg = self.db.get_config(config_id)
        if not cfg:
            return

        # имя по умолчанию: "system_copy.cfg"
        base_name = cfg["filename"]
        if base_name.endswith(".cfg"):
            base_name = base_name[:-4]
        default_name = f"{base_name}_copy.cfg"

        new_name, ok = self.ask_name(
            "Дублировать cfg",
            "Имя нового файла:",
            default=default_name,
            max_len=MAX_CONFIG_NAME_LEN,
        )
        if not ok:
            return

        new_name = self.validate_name(new_name, MAX_CONFIG_NAME_LEN, "Имя файла")
        if new_name is None:
            return

        try:
            new_id = self.db.duplicate_config(config_id, new_name)
        except Exception as exc:
            QMessageBox.warning(self, "Ошибка", str(exc))
            return

        self.refresh(select_id=new_id)

    def _delete_config(self):
        """Удаление выбранного конфига."""
        item = self.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(self, "Ошибка", "Не выбран конфигурационный файл.")
            return
        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        ans = QMessageBox.question(
            self, "Удалить",
            f"Удалить cfg «{item.text(0)}»?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if ans == QMessageBox.StandardButton.Yes:
            self.db.delete_config(config_id)
            self.treeConfigs.clearSelection()
            self.refresh()

    def _show_logs(self):
        """Отображение логов изменений выранного конфига."""
        item = self.treeConfigs.currentItem()
        if item is None:
            QMessageBox.warning(self, "Ошибка", "Не выбран конфигурационный файл.")
            return
        config_id = item.data(0, Qt.ItemDataRole.UserRole)
        logs = self.db.list_logs(config_id)
        if not logs:
            QMessageBox.information(self, "История", "Изменений нет.")
            return
        text = "\n".join(
            f"{row['changed_at']}: {row['key_name']} "
            f"{row['old_value']} → {row['new_value']}"
            for row in logs
        )
        QMessageBox.information(self, "История изменений", text)

    def build_menus(self) -> dict:
        return {
            "Файл": [
                self.actionNewConfig,
                self.actionImportCfg,
                self.actionExportCfg,
                None,
                self.actionChangeProfile,
                self.actionChangeServer,
            ],
            "Помощь": [
                self.actionVideoHelp,
                self.actionAbout,
            ],
        }

    def _show_about(self):
        QMessageBox.about(
            self, "О программе",
            "Aion.CfgStudio v1.0  by @chealkrtengghnle\n\nРедактор конфигурационного файла system.cfg для Aion."
        )

    def _show_context_menu(self, pos):
        """Показывает контекстное меню для выбранного конфига."""
        item = self.treeConfigs.itemAt(pos)
        if item is None:
            return

        self.treeConfigs.setCurrentItem(item)

        menu = build_context_menu(self, [
            ("Редактировать", self._open_selected),
            None,
            ("Дублировать", self._duplicate_config),
            None,
            ("Переименовать (F2)", self._rename_config),
            None,
            ("Экспортировать (Ctrl + S)", self._export_config),
            None,
            ("Удалить (Delete)", self._delete_config),
        ])
        menu.exec(self.treeConfigs.mapToGlobal(pos))
