"""Страница выбора профиля."""
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox

from logic.context_menu import build_context_menu
from logic.base_page import BasePage
from logic.constants import MAX_PROFILE_NAME_LEN, MAX_DESCRIPTION_LEN
from logic.shortcuts import bind_shortcuts, FOCUSED
from ui.profile_select import Ui_ProfileSelectDialog


class PageProfile(BasePage, Ui_ProfileSelectDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # подключение контекстного меню
        self.listProfiles.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.listProfiles.customContextMenuRequested.connect(self._show_context_menu)

        # поле описания редактируемое
        self.editDescription.setReadOnly(False)
        self.editDescription.setPlaceholderText(
            f"Сохраняется автоматически (до {MAX_DESCRIPTION_LEN} символов)...")
        # debounce: сохранять через 1 сек после последнего изменения
        self._save_timer = QTimer(self)
        self._save_timer.setSingleShot(True)
        self._save_timer.setInterval(1000)
        self._save_timer.timeout.connect(self._save_description)

        self._connect_signals()

        # горячие клавиши
        bind_shortcuts(self.listProfiles, {
            "F1": lambda: self.window().go_video(),
            "F2": self._rename,
            "Return": self._enter,
            "Enter": self._enter,
            "Ctrl+N": self._create,
            "Delete": self._delete,
        }, FOCUSED)

        # Ctrl+Q глобально на странице
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(
            lambda: self.window().close()
        )

    def _connect_signals(self):
        self.btnNew.clicked.connect(self._create)
        self.btnRename.clicked.connect(self._rename)
        self.btnDelete.clicked.connect(self._delete)
        self.btnEnter.clicked.connect(self._enter)

        # заполнение информации о профиле
        self.listProfiles.currentItemChanged.connect(self._on_profile_selected)
        self.editDescription.textChanged.connect(self._on_description_changed)

        # переходы к другим страницам
        self.listProfiles.itemDoubleClicked.connect(
            lambda _: self._enter()
        )
        self.btnCancel.clicked.connect(
            lambda: self.window().close()
        )
        self.btnVideoHelp.clicked.connect(
            lambda: self.window().go_video()
        )

    # ============== жизненный цикл ==============

    def on_enter(self):
        """Подгружает список порфилей при загрузке страницы ."""
        self.refresh()

    def on_leave(self):
        """Сохраняет описание при уходе со страницы."""
        if self._save_timer.isActive():
            self._save_timer.stop()
        self._save_description()

    # ============== автосохранение ==============

    def _on_description_changed(self):
        """Запускает таймер автосохранения при каждом изменении описания профиля."""
        self._save_timer.start()

    def _save_description(self):
        """Сохраняет описание текущего профиля в БД."""
        self._persist_description(self.listProfiles.currentItem())

    def _persist_description(self, item):
        """Сохраняет описание для указанного item.
                Возвращает True при успехе, и False, если item нет или БД упала.
        """
        return self.persist_text(
            item,
            self.editDescription.toPlainText(),
            MAX_DESCRIPTION_LEN,
            self.db.update_profile_description,
            "описание профиля",
        )

    # ============== загрузка профилей ==============

    def refresh(self, select_id: int | None = None):
        """Обновление страницы при разных действиях."""
        # сохранить правки текущего профиля
        if self._save_timer.isActive():
            self._save_timer.stop()
        self._persist_description(self.listProfiles.currentItem())

        # если select_id не задан, берём текущий выбранный
        if select_id is None:
            current = self.listProfiles.currentItem()
            if current is not None:
                select_id = current.data(Qt.ItemDataRole.UserRole)

        self.listProfiles.blockSignals(True)
        self.listProfiles.clear()
        for row in self.db.list_profiles():
            item = QListWidgetItem(row["name"])
            item.setData(Qt.ItemDataRole.UserRole, row["id"])
            self.listProfiles.addItem(item)
        self.listProfiles.blockSignals(False)

        if not self.listProfiles.count():
            self._clear_details()
            self._set_controls_enabled(False)
            return

        self._set_controls_enabled(True)

        # выбрать нужный профиль (или первый)
        target_row = 0
        if select_id is not None:
            for i in range(self.listProfiles.count()):
                if self.listProfiles.item(i).data(Qt.ItemDataRole.UserRole) == select_id:
                    target_row = i
                    break
        self.listProfiles.setCurrentRow(target_row)

    def _set_controls_enabled(self, enabled: bool):
        """Включает / выключает контролы, требующие выбранного профиля."""
        self.set_controls_enabled(
            enabled,
            self.btnRename,
            self.btnDelete,
            self.btnEnter,
            self.editDescription,
        )

    # ============== обработка выбора ==============

    def _on_profile_selected(self, current, previous=None):
        """Заполняет правую панель при выборе профиля.
                Перед заполнением сохраняет описание предыдущего профиля."""
        # 1. сохранить описание предыдущего (если было изменено)
        if previous is not None:
            if self._save_timer.isActive():
                self._save_timer.stop()
            self._persist_description(previous)

        # 2. если новый профиль не выбран, очистить панель
        if current is None:
            self._clear_details()
            return

        # 3. заполнить панель новым профилем
        profile_id = current.data(Qt.ItemDataRole.UserRole)
        profile = self.db.get_profile(profile_id)
        if not profile:
            self._clear_details()
            return

        # блокируем сигнал textChanged, чтобы не запускать автосохранение
        self.editDescription.blockSignals(True)
        self.editDescription.setPlainText(profile["description"] or "")
        self.editDescription.blockSignals(False)

        self.lblName.setText(f"Выбранный профиль: {profile["name"]}")

        servers = self.db.count_servers(profile_id)
        configs = self.db.count_configs(profile_id)
        self.lblStats.setText(f"Серверов: {servers} | Конфигураций: {configs}")

        # аватар - первая буква имени, золотая!
        first_letter = (profile["name"] or "?")[0].upper()
        self.lblAvatar.setText(first_letter)
        self.lblAvatar.setStyleSheet(
            "font-size: 60px; color: #d4a95a; font-weight: bold;"
        )

    def _clear_details(self):
        self.lblName.setText("— профиль не выбран —")
        self.editDescription.blockSignals(True)
        self.editDescription.clear()
        self.editDescription.blockSignals(False)
        self.lblStats.setText("Серверов: 0 | Конфигураций: 0")
        self.lblAvatar.clear()

    # ============== кнопки ==============

    def _create(self):
        """Создаёт профиль, загружая в БД, с проверкой на уникальность имени."""
        name, ok = self.ask_name_hint(
            "Новый профиль", "Имя профиля",
            MAX_PROFILE_NAME_LEN,
        )
        if not ok:
            return

        name = self.validate_name(name, MAX_PROFILE_NAME_LEN, "Имя профиля")
        if name is None:
            return

        existing = [p for p in self.db.list_profiles() if p["name"] == name]
        if existing:
            QMessageBox.warning(
                self, "Ошибка",
                f"Профиль с именем «{name}» уже существует."
            )
            return

        try:
            new_id = self.db.create_profile(name)
        except Exception as exc:
            QMessageBox.warning(self, "Ошибка", str(exc))
            return

        self.refresh(select_id=new_id)

    def _rename(self):
        """Ренейм профиля с последующей подгрузкой в БД и проверкой на уникальность."""
        item = self.listProfiles.currentItem()
        if item is None:
            QMessageBox.information(self, "Переименование",
                                    "Не выбран профиль для переименования.")
            return

        pid = item.data(Qt.ItemDataRole.UserRole)
        old_name = item.text()

        new_name, ok = self.ask_name_hint(
            "Переименовать профиль", "Новое имя",
            MAX_PROFILE_NAME_LEN,
            old_name
        )
        if not ok:
            return

        new_name = self.validate_name(new_name, MAX_PROFILE_NAME_LEN, "Имя профиля")
        if new_name is None:
            return

        if new_name == old_name:
            return

        if any(
                p["name"] == new_name and p["id"] != pid
                for p in self.db.list_profiles()
        ):
            QMessageBox.warning(
                self, "Ошибка",
                f"Профиль «{new_name}» уже существует.\n"
                "Пожалуйста, выберите другое имя."
            )
            return

        try:
            self.db.rename_profile(pid, new_name)
        except Exception as exc:
            QMessageBox.warning(self, "Ошибка", str(exc))
            return

        self.refresh()

    def _delete(self):
        """Удаление профиля с соответствующими изменениями в БД."""
        item = self.listProfiles.currentItem()
        if item is None:
            QMessageBox.information(self, "Удаление",
                                    "Не выбран профиль для удаления.")
            return

        pid = item.data(Qt.ItemDataRole.UserRole)
        servers = self.db.count_servers(pid)
        configs = self.db.count_configs(pid)
        ans = QMessageBox.question(
            self, "Удалить",
            f"Удалить профиль «{item.text()}» со всем содержимым?\n\n"
            f"Будет удалено: серверов - {servers}, конфигураций - {configs}.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if ans == QMessageBox.StandardButton.Yes:
            self.db.delete_profile(pid)
            self.refresh()

    def _enter(self):
        """Вход в выбранный профиль"""
        item = self.listProfiles.currentItem()
        if item is None:
            QMessageBox.information(self, "Вход", "Не выбран профиль для входа.")
            return

        self.window().go_server(item.data(Qt.ItemDataRole.UserRole))

    def _duplicate(self):
        """Дублирует профиль со всем содержимым и проверкой
                на уникальность нового имени; новое имя - старое + (копия)"""
        item = self.listProfiles.currentItem()
        if item is None:
            QMessageBox.information(self, "Дублирование",
                                    "Не выбран профиль для дублирования.")
            return

        pid = item.data(Qt.ItemDataRole.UserRole)
        profile = self.db.get_profile(pid)
        if not profile:
            return

        new_name, ok = self.ask_name_hint(
            "Дублировать профиль", "Имя нового профиля",
            MAX_PROFILE_NAME_LEN, f"{profile['name']} (копия)"
        )
        if not ok:
            return

        new_name = self.validate_name(new_name, MAX_PROFILE_NAME_LEN, "Имя профиля")
        if new_name is None:
            return

        if any(p["name"] == new_name for p in self.db.list_profiles()):
            QMessageBox.warning(self, "Ошибка",
                                f"Профиль «{new_name}» уже существует.")
            return

        try:
            new_id = self.db.duplicate_profile(pid, new_name)
        except Exception as exc:
            QMessageBox.warning(self, "Ошибка", str(exc))
            return

        self.refresh(select_id=new_id)

    def _show_context_menu(self, pos):
        """Показывает контекстное меню для профиля."""
        item = self.listProfiles.itemAt(pos)
        if item is None:
            return

        self.listProfiles.setCurrentItem(item)

        menu = build_context_menu(self, [
            ("Войти", self._enter),
            None,
            ("Дублировать", self._duplicate),
            None,
            ("Переименовать (F2)", self._rename),
            None,
            ("Удалить (Delete)", self._delete),
        ])
        menu.exec(self.listProfiles.mapToGlobal(pos))
