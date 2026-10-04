"""Страница редактора cfg."""
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QShortcut, QKeySequence
from PyQt6.QtWidgets import (
    QMessageBox, QCheckBox, QLineEdit, QSpinBox, QComboBox,
    QTableWidgetItem, QHeaderView,
)

from logic.base_page import BasePage
from ui.command_editor import Ui_CommandEditorDialog

# =================== константы оформления ===================

MODE_SIMPLE = {"simple"}
MODE_ADVANCED = {"simple", "advanced"}


class PageEditor(BasePage, Ui_CommandEditorDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # контекст
        self.config_id: int | None = None
        self.server_id: int | None = None
        self._built = False

        # кэш данных, чтобы не читать БД повторно
        self._commands: list | None = None
        self._prefixes: dict | None = None

        # связки «строка таблицы -> данные»
        self._cmd_by_row: dict[int, dict] = {}  # row -> {command, group_code}
        self._group_rows: dict[str, list[int]] = {}  # код префикса -> список строк команд
        self._group_header_row: dict[str, int] = {}  # код префикса -> номер строки-заголовка
        self._group_chk: dict[str, QCheckBox] = {}

        # debounce для поиска
        self._search_timer = QTimer(self)
        self._search_timer.setSingleShot(True)
        self._search_timer.setInterval(200)
        self._search_timer.timeout.connect(self._apply_filters)

        self._connect_signals()

        # хоткеи, работающие на всей странице
        QShortcut(QKeySequence("F1"), self.listPrefixes).activated.connect(lambda: self.window().go_video())
        QShortcut(QKeySequence("Ctrl+Q"), self.listPrefixes).activated.connect(self._on_cancel)

        self._setup_table()

    # ============= настройки таблицы =============

    def _setup_table(self):
        """Подготовка таблицы с командами."""
        t = self.tableCommands
        t.setColumnCount(5)
        t.setHorizontalHeaderLabels(
            ["Исп.", "Команда", "Значение", "Дефолт", "Описание"]
        )
        t.verticalHeader().setDefaultSectionSize(32)
        t.verticalHeader().setVisible(False)

        header = t.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        t.setColumnWidth(0, 50)
        t.setColumnWidth(1, 220)
        t.setColumnWidth(2, 140)
        t.setColumnWidth(3, 100)

        # отключение горизонтального скролл-бара у префиксов
        self.listPrefixes.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.listPrefixes.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        t.setAlternatingRowColors(False)

    # ============= сигналы =============

    def _connect_signals(self):
        self.comboMode.currentIndexChanged.connect(self._on_mode_changed)
        self.editSearch.textChanged.connect(self._on_search_changed)
        self.listPrefixes.currentItemChanged.connect(self._on_prefix_changed)
        self.btnResetAll.clicked.connect(self._reset_all)
        self.btnCancel.clicked.connect(self._on_cancel)
        self.btnApply.clicked.connect(self._on_apply)

    def _on_search_changed(self, _text: str):
        self._search_timer.start()

    def _on_mode_changed(self, _index: int):
        self._apply_filters()

    def _on_prefix_changed(self, _current, _prev=None):
        self._apply_filters()

    # ============= контекст =============

    def set_context(self, config_id: int | None, server_id: int | None):
        self.config_id = config_id
        self.server_id = server_id

    def on_enter(self):
        self.refresh()

    def on_leave(self):
        """Автосохранение при уходе со страницы.

        - Существующий cfg - сохраняем отметки в ConfigValues.
        - Новый cfg с отметками - спрашиваем, сохранять ли как system.cfg.
        """

        if self.config_id is not None:
            try:
                self._save_values_to_db()
            except Exception as exc:
                print(f"[PageEditor] autosave failed: {exc}")
            return

        # Новый cfg - сохранять некуда, но если есть отметки, спросим
        if self._has_checked_commands():
            ans = QMessageBox.question(
                self, "Несохранённый конфиг",
                "Вы отметили команды, но не сохранили конфиг.\n"
                "Сохранить как system.cfg перед выходом?",
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No,
            )
            if ans == QMessageBox.StandardButton.Yes:
                self._apply_silent()

    def refresh(self):
        self._update_file_label()
        self._load_prefixes()
        if not self._built:
            self._build_all_rows()
            self._built = True
        self._load_saved_values()
        self._apply_filters()

    # ---------- файл и префиксы ----------

    def _update_file_label(self):
        if self.config_id is None:
            self.lblFileName.setText("Файл: (новый)")
            return
        cfg = self.db.get_config(self.config_id)
        if cfg:
            self.lblFileName.setText(f"Файл: {cfg['filename']}")
        else:
            self.lblFileName.setText("Файл: —")

    def _load_prefixes(self):
        # запоминаем текущий выбор
        current_code = None
        item = self.listPrefixes.currentItem()
        if item is not None and not item.text().startswith("Все"):
            current_code = item.text().split(" ")[0]

        self.listPrefixes.blockSignals(True)
        self.listPrefixes.clear()
        self.listPrefixes.addItem("Все команды")
        if self._prefixes is None:
            self._prefixes = {row["id"]: dict(row)
                              for row in self.db.list_prefixes()}
        for row in self._prefixes.values():
            self.listPrefixes.addItem(f"{row['code']} — {row['name']}")

        # восстанавливаем выбор
        target_row = 0
        if current_code is not None:
            for i in range(self.listPrefixes.count()):
                if self.listPrefixes.item(i).text().startswith(current_code + " "):
                    target_row = i
                    break
        self.listPrefixes.setCurrentRow(target_row)
        self.listPrefixes.blockSignals(False)

    def _current_mode(self) -> str:
        idx = self.comboMode.currentIndex()
        return {0: "simple", 1: "advanced"}.get(idx, "advanced")

    # ============= построение =============

    def _build_all_rows(self):
        """Строит все строки таблицы: заголовки групп + команды."""
        if self._prefixes is None:
            self._prefixes = {row["id"]: dict(row)
                              for row in self.db.list_prefixes()}

        if self._commands is None:
            self._commands = list(self.db.list_commands("debug"))

        t = self.tableCommands
        t.setRowCount(0)
        self._cmd_by_row.clear()
        self._group_rows.clear()
        self._group_header_row.clear()

        current_prefix = None
        row = 0

        for cmd in self._commands:
            pid = cmd["prefix_id"]
            if pid is None or pid not in self._prefixes:
                continue
            prefix = self._prefixes[pid]
            pcode = prefix["code"]

            if pcode != current_prefix:
                t.insertRow(row)

                font = QFont()
                font.setBold(True)
                font.setPointSize(font.pointSize() + 1)

                group_chk = QCheckBox()
                group_chk.setStyleSheet(
                    "QCheckBox { margin-left: 12px; }"
                    "QCheckBox::indicator { width: 14px; height: 14px; }"
                )
                t.setCellWidget(row, 0, group_chk)

                header = QTableWidgetItem(f"{pcode} — {prefix['name']}")
                header.setData(Qt.ItemDataRole.FontRole, font)
                header.setFlags(Qt.ItemFlag.ItemIsEnabled)
                t.setItem(row, 1, header)

                for col in (2, 3, 4):
                    empty = QTableWidgetItem("")
                    empty.setFlags(Qt.ItemFlag.ItemIsEnabled)
                    t.setItem(row, col, empty)

                # высота строки заголовка
                t.setRowHeight(row, 36)

                group_chk.clicked.connect(
                    lambda _checked, c=pcode: self._toggle_group(c)
                )

                self._group_header_row[pcode] = row
                self._group_chk[pcode] = group_chk
                self._group_rows[pcode] = []
                current_prefix = pcode
                row += 1

            # строка команды
            t.insertRow(row)
            self._fill_command_row(row, cmd)
            self._cmd_by_row[row] = {
                "command": cmd,
                "group_code": pcode,
            }
            self._group_rows[pcode].append(row)
            row += 1

    def _fill_command_row(self, row: int, cmd):
        t = self.tableCommands

        # 0. чекбокс Исп.
        chk = QCheckBox()
        chk.setStyleSheet("QCheckBox { margin-left: 12px; }"
                          "QCheckBox::indicator { width: 14px; height: 14px; }")
        t.setCellWidget(row, 0, chk)

        # 1. имя команды
        item_key = QTableWidgetItem(cmd["key_name"])
        item_key.setFlags(Qt.ItemFlag.ItemIsEnabled)
        t.setItem(row, 1, item_key)

        # 2. виджет значения
        w = self._make_value_widget(cmd)
        t.setCellWidget(row, 2, w)
        w.setEnabled(False)

        # 3. дефолт
        item_def = QTableWidgetItem(str(cmd["default_value"] or "—"))
        item_def.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item_def.setFlags(Qt.ItemFlag.ItemIsEnabled)
        t.setItem(row, 3, item_def)

        # 4. описание
        item_desc = QTableWidgetItem(cmd["description"] or "")
        item_desc.setFlags(Qt.ItemFlag.ItemIsEnabled)
        t.setItem(row, 4, item_desc)

        # связка чекбокса и виджета
        chk.toggled.connect(
            lambda checked, ww=w: ww.setEnabled(checked)
        )
        chk.toggled.connect(
            lambda _c: self._update_group_checks()
        )

    def _make_value_widget(self, cmd):
        vtype = (cmd["value_type"] or "string").lower()
        possible = cmd["possible_values"]

        if vtype == "bool" or (possible and "," in possible):
            w = QComboBox()
            if possible:
                for v in possible.split(","):
                    w.addItem(v.strip())
            else:
                w.addItem("0")
                w.addItem("1")
            if cmd["default_value"] is not None:
                idx = w.findText(str(cmd["default_value"]))
                if idx >= 0:
                    w.setCurrentIndex(idx)
            return w

        if vtype == "int":
            w = QSpinBox()
            w.setMinimum(int(cmd["min_value"]) if cmd["min_value"] else -999999)
            w.setMaximum(int(cmd["max_value"]) if cmd["max_value"] else 999999)
            if cmd["default_value"]:
                try:
                    w.setValue(int(cmd["default_value"]))
                except ValueError:
                    pass
            return w

        w = QLineEdit()
        if cmd["default_value"] is not None:
            w.setText(str(cmd["default_value"]))
        return w

    def _load_saved_values(self):
        """Подтягивает сохранённые значения из ConfigValues в таблицу.

        Сначала сбрасывает все чекбоксы и значения к дефолтам, потом
        применяет сохранённые значения.
        """
        t = self.tableCommands

        # 1. сброс: снимаем все чекбоксы и возвращаем дефолтные значения
        for table_row, info in self._cmd_by_row.items():
            chk = t.cellWidget(table_row, 0)
            w = t.cellWidget(table_row, 2)
            if not isinstance(chk, QCheckBox):
                continue

            chk.blockSignals(True)
            chk.setChecked(False)
            chk.blockSignals(False)
            w.setEnabled(False)

            # вернуть значение виджета к дефолту из команды
            default_value = info["command"]["default_value"]
            if default_value is not None:
                self._apply_value_to_widget(w, str(default_value))

        # 2. если cfg не выбран - на этом всё
        if self.config_id is None:
            self._update_group_checks()
            return

        # 3. применяем сохранённые значения
        saved = {}
        for row in self.db.list_config_values(self.config_id):
            saved[row["command_id"]] = (row["use_custom"], row["custom_value"])

        for table_row, info in self._cmd_by_row.items():
            cmd_id = info["command"]["id"]
            chk = t.cellWidget(table_row, 0)
            w = t.cellWidget(table_row, 2)
            if not isinstance(chk, QCheckBox):
                continue

            if cmd_id in saved:
                use_custom, custom_value = saved[cmd_id]
                if use_custom and custom_value is not None:
                    chk.blockSignals(True)
                    chk.setChecked(True)
                    chk.blockSignals(False)
                    self._apply_value_to_widget(w, custom_value)
                    w.setEnabled(True)

        self._update_group_checks()

    def _save_values_to_db(self):
        """Сохраняет отмеченные / снятые команды в ConfigValues одним запросом."""
        if self.config_id is None:
            return

        t = self.tableCommands
        rows: list[tuple] = []

        for table_row, info in self._cmd_by_row.items():
            cmd_id = info["command"]["id"]
            chk = t.cellWidget(table_row, 0)
            w = t.cellWidget(table_row, 2)
            if not isinstance(chk, QCheckBox):
                continue

            if chk.isChecked():
                if isinstance(w, QComboBox):
                    val = w.currentText()
                elif isinstance(w, QSpinBox):
                    val = str(w.value())
                elif isinstance(w, QLineEdit):
                    val = w.text().strip()
                else:
                    val = ""
                rows.append((cmd_id, 1, val))
            else:
                rows.append((cmd_id, 0, None))

        self.db.save_config_values_bulk(self.config_id, rows)

    def _apply_value_to_widget(self, widget, value: str):
        """Подставляет значение из БД в виджет ввода."""
        if isinstance(widget, QComboBox):
            idx = widget.findText(str(value))
            if idx >= 0:
                widget.setCurrentIndex(idx)
        elif isinstance(widget, QSpinBox):
            try:
                widget.setValue(int(value))
            except (ValueError, TypeError):
                pass
        elif isinstance(widget, QLineEdit):
            widget.setText(str(value))

    def _update_group_checks(self):
        """Синхронизирует групповые чекбоксы с состоянием строк."""
        t = self.tableCommands
        for code, group_chk in self._group_chk.items():
            rows = self._group_rows.get(code, [])
            checked = 0
            total = 0
            for r in rows:
                if t.isRowHidden(r):
                    continue
                chk = t.cellWidget(r, 0)
                if isinstance(chk, QCheckBox):
                    total += 1
                    if chk.isChecked():
                        checked += 1

            if total == 0 or checked == 0:
                state = Qt.CheckState.Unchecked
            elif checked == total:
                state = Qt.CheckState.Checked
            else:
                state = Qt.CheckState.PartiallyChecked

            group_chk.blockSignals(True)
            group_chk.setCheckState(state)
            group_chk.blockSignals(False)

    def _has_checked_commands(self) -> bool:
        """Проверяет, есть ли хотя бы одна отмеченная команда."""
        t = self.tableCommands
        for row in self._cmd_by_row:
            chk = t.cellWidget(row, 0)
            if isinstance(chk, QCheckBox) and chk.isChecked():
                return True
        return False

    def _collect_values(self) -> dict[str, str]:
        """Собирает отмеченные команды в словарь {key_name: value}."""
        values: dict[str, str] = {}
        t = self.tableCommands

        for row, info in self._cmd_by_row.items():
            chk = t.cellWidget(row, 0)
            if not isinstance(chk, QCheckBox) or not chk.isChecked():
                continue

            cmd = info["command"]
            w = t.cellWidget(row, 2)

            if isinstance(w, QComboBox):
                val = w.currentText()
            elif isinstance(w, QSpinBox):
                val = str(w.value())
            elif isinstance(w, QLineEdit):
                val = w.text().strip()
            else:
                val = ""

            values[cmd["key_name"]] = val

        return values

    def _build_content(self, values: dict[str, str]) -> str:
        """Собирает содержимое system.cfg из словаря значений."""
        lines = [
            "-- [System-Configuration Ver1.0]",
            "-- Attention: This file is generated by the system, do not modify!",
            "",
        ]
        for key, value in values.items():
            lines.append(f'{key} = "{value}"')
        return "\n".join(lines)

    # ============= фильтрация =============

    def _apply_filters(self):
        mode_allowed = {
            "simple": MODE_SIMPLE,
            "advanced": MODE_ADVANCED,
        }[self._current_mode()]

        prefix_item = self.listPrefixes.currentItem()
        prefix_code = None
        if prefix_item and not prefix_item.text().startswith("Все"):
            prefix_code = prefix_item.text().split(" ")[0]

        search = self.editSearch.text().lower().strip()

        t = self.tableCommands

        # 1. скрываем / показываем строки команд
        for row, info in self._cmd_by_row.items():
            cmd = info["command"]
            visible = (
                    cmd["mode"] in mode_allowed
                    and (prefix_code is None or info["group_code"] == prefix_code)
                    and (not search or search in cmd["key_name"].lower())
            )
            t.setRowHidden(row, not visible)

        # 2. скрываем заголовки групп без видимых строк
        for code, rows in self._group_rows.items():
            has_visible = any(not t.isRowHidden(r) for r in rows)
            if prefix_code is not None and code != prefix_code:
                has_visible = False
            t.setRowHidden(self._group_header_row[code], not has_visible)

        self._update_group_checks()

    def _toggle_group(self, prefix_code: str):
        """Отмечает / снимает все ВИДИМЫЕ команды указанной группы.

        Клик работает как отметить всё / снять всё - не зависит
        от текущего состояния группового чекбокса.
        """
        group_chk = self._group_chk.get(prefix_code)
        if group_chk is None:
            return

        # если не все отмечены - отметить, иначе снять
        t = self.tableCommands
        rows = self._group_rows.get(prefix_code, [])
        checked = sum(
            1 for r in rows
            if not t.isRowHidden(r)
            and isinstance(t.cellWidget(r, 0), QCheckBox)
            and t.cellWidget(r, 0).isChecked()
        )
        visible = sum(1 for r in rows if not t.isRowHidden(r))
        target = checked < visible  # отметить оставшиеся

        for r in rows:
            if t.isRowHidden(r):
                continue
            chk = t.cellWidget(r, 0)
            if isinstance(chk, QCheckBox):
                chk.setChecked(target)

    # ============= кнопки =============

    def _reset_all(self):
        """Снимает все чекбоксы и возвращает значения к дефолтам."""
        t = self.tableCommands
        for row, info in self._cmd_by_row.items():
            chk = t.cellWidget(row, 0)
            w = t.cellWidget(row, 2)
            if isinstance(chk, QCheckBox):
                chk.setChecked(False)
            default_value = info["command"]["default_value"]
            if default_value is not None:
                self._apply_value_to_widget(w, str(default_value))
        self._update_group_checks()

    def _on_cancel(self):
        win = self.window()
        win.go_main(win.current_server_id)

    def _apply_silent(self) -> bool:
        """Сохраняет cfg без перехода на главную и без финального Готово.

        Используется в on_leave для автосохранения нового cfg.
        Возвращает True при успехе, False при ошибке или отсутствии данных.
        """
        values = self._collect_values()
        if not values:
            return False

        content = self._build_content(values)

        try:
            if self.config_id is None:
                if self.server_id is None:
                    print("[PageEditor] _apply_silent: server_id не задан")
                    return False
                self.config_id = self.db.create_config(
                    self.server_id, "system.cfg", content
                )
            else:
                self.db.update_config(self.config_id, content)

            # 1. старые значения до сохранения
            old_values = {}
            for row in self.db.list_config_values(self.config_id):
                old_values[row["command_id"]] = row["custom_value"]

            # 2. новые значения
            self._save_values_to_db()

            # 3. логи
            self._write_logs(old_values)

            return True
        except Exception as exc:
            print(f"[PageEditor] _apply_silent failed: {exc}")
            return False

    def _on_apply(self):
        """Полное сохранение: обновляет cfg + переходит на главную."""
        values = self._collect_values()
        if not values:
            QMessageBox.information(
                self, "Нечего сохранять",
                "Не отмечено ни одной команды."
            )
            return

        if not self._apply_silent():
            QMessageBox.critical(
                self, "Ошибка сохранения",
                "Не удалось сохранить конфигурацию."
            )
            return

        QMessageBox.information(self, "Готово", "Конфигурация сохранена.")
        win = self.window()
        win.go_main(win.current_server_id)

    def _write_logs(self, old_values: dict):
        """Записывает изменившиеся значения в Logs.

        Логирует:
          - включение команды (было выкл -> стало вкл);
          - выключение команды (было вкл -> стало выкл);
          - смену значения у включённой команды.
        """
        if self.config_id is None:
            return

        t = self.tableCommands
        for row, info in self._cmd_by_row.items():
            cmd = info["command"]
            cmd_id = cmd["id"]
            chk = t.cellWidget(row, 0)
            w = t.cellWidget(row, 2)
            if not isinstance(chk, QCheckBox):
                continue

            # новое состояние
            is_checked = chk.isChecked()
            if is_checked:
                if isinstance(w, QComboBox):
                    new_val = w.currentText()
                elif isinstance(w, QSpinBox):
                    new_val = str(w.value())
                elif isinstance(w, QLineEdit):
                    new_val = w.text().strip()
                else:
                    new_val = ""
            else:
                new_val = None

            # старое состояние
            old_val = old_values.get(cmd_id)

            old_norm = None if old_val is None else str(old_val).strip()
            new_norm = None if new_val is None else str(new_val).strip()
            if old_norm == new_norm:
                continue

            # формируем читаемые значения для лога
            old_display = old_norm if old_norm is not None else "(выключено)"
            new_display = new_norm if new_norm is not None else "(выключено)"

            try:
                self.db.log_change(
                    self.config_id,
                    cmd["key_name"],
                    old_display,
                    new_display,
                )
            except Exception as exc:
                print(f"[PageEditor] log_change failed: {exc}")

    # ============= меню =============

    def build_menus(self) -> dict:
        win = self.window()
        m = win.page_main
        return {
            "Помощь": [
                m.actionVideoHelp,
                m.actionAbout,
            ],
        }
