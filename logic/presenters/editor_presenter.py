"""Presenter для страницы редактора cfg.

Вся логика редактора: построение таблицы, загрузка / сохранение
значений, фильтрация, групповые чекбоксы, логи, автосохранение
при уходе со страницы.

Diff изменений для логов считается прямо здесь (EditorService.diff_logs
не используется - он неполный).
"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QCheckBox

from logic.presenters.base_presenter import BasePresenter


MODE_SIMPLE = {"simple"}
MODE_ADVANCED = {"simple", "advanced"}


class EditorPresenter(BasePresenter):
    """Логика страницы редактора."""

    def __init__(self, view, service):
        super().__init__(view)
        self.service = service

        # контекст
        self.config_id: int | None = None
        self.server_id: int | None = None

        # построено ли дерево строк
        self._built = False

        # кэш данных
        self._commands: list | None = None
        self._prefixes: dict | None = None

        # связки «строка таблицы -> данные»
        self._cmd_by_row: dict[int, dict] = {}
        self._group_rows: dict[str, list[int]] = {}
        self._group_header_row: dict[str, int] = {}
        self._group_chk: dict[str, QCheckBox] = {}

    # ============ контекст ============

    def set_context(self, config_id: int | None,
                    server_id: int | None):
        self.config_id = config_id
        self.server_id = server_id

    # ============ жизненный цикл ============

    def on_enter(self):
        self.refresh()

    def on_leave(self):
        """Автосохранение при уходе.

        - существующий cfg - сохраняем ConfigValues;
        - новый cfg с отметками - спрашиваем, сохранять ли как system.cfg.
        """
        if self.config_id is not None:
            try:
                self._save_values_to_db()
            except Exception as exc:
                print(f"[EditorPresenter] autosave failed: {exc}")
            return

        if self._has_checked_commands():
            ans = QMessageBox.question(
                self.view, "Несохранённый конфиг",
                "Вы отметили команды, но не сохранили конфиг.\n"
                "Сохранить как system.cfg перед выходом?",
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No,
            )
            if ans == QMessageBox.StandardButton.Yes:
                self.apply_silent()

    # ============ refresh ============

    def refresh(self):
        self._update_file_label()
        self._load_prefixes()
        if not self._built:
            self._build_all_rows()
            self._built = True
        self._load_saved_values()
        self.apply_filters()

    # ============ заголовок файла ============

    def _update_file_label(self):
        if self.config_id is None:
            self.view.lblFileName.setText("Файл: (новый)")
            return
        cfg = self.service.config_repo.get(self.config_id)
        if cfg:
            self.view.lblFileName.setText(f"Файл: {cfg['filename']}")
        else:
            self.view.lblFileName.setText("Файл: —")

    # ============ префиксы ============

    def _load_prefixes(self):
        view = self.view
        current_code = None
        item = view.listPrefixes.currentItem()
        if item is not None and not item.text().startswith("Все"):
            current_code = item.text().split(" ")[0]

        view.listPrefixes.blockSignals(True)
        view.listPrefixes.clear()
        view.listPrefixes.addItem("Все команды")

        if self._prefixes is None:
            self._prefixes = {
                row["id"]: dict(row)
                for row in self.service.all_prefixes()
            }

        for row in self._prefixes.values():
            view.listPrefixes.addItem(f"{row['code']} — {row['name']}")

        target_row = 0
        if current_code is not None:
            for i in range(view.listPrefixes.count()):
                if view.listPrefixes.item(i).text().startswith(
                    current_code + " "
                ):
                    target_row = i
                    break
        view.listPrefixes.setCurrentRow(target_row)
        view.listPrefixes.blockSignals(False)

    # ============ построение таблицы ============

    def _build_all_rows(self):
        """Строит все строки: заголовки групп + команды."""
        view = self.view
        t = view.tableCommands

        if self._prefixes is None:
            self._prefixes = {
                row["id"]: dict(row)
                for row in self.service.all_prefixes()
            }

        if self._commands is None:
            self._commands = list(self.service.all_commands())

        t.setRowCount(0)
        self._cmd_by_row.clear()
        self._group_rows.clear()
        self._group_header_row.clear()
        self._group_chk.clear()

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
                view.make_group_header(row, pcode, prefix["name"])

                chk = t.cellWidget(row, 0)
                self._group_chk[pcode] = chk
                self._group_header_row[pcode] = row
                self._group_rows[pcode] = []

                chk.clicked.connect(
                    lambda _checked, c=pcode: self.toggle_group(c)
                )

                current_prefix = pcode
                row += 1

            t.insertRow(row)
            view.fill_command_row(row, cmd)
            self._cmd_by_row[row] = {
                "command": cmd,
                "group_code": pcode,
            }
            self._group_rows[pcode].append(row)
            row += 1

        # связываем чекбоксы строк с обновлением групповых
        for r in self._cmd_by_row:
            chk = t.cellWidget(r, 0)
            if isinstance(chk, QCheckBox):
                chk.toggled.connect(self._update_group_checks)

    # ============ загрузка сохранённых значений ============

    def _load_saved_values(self):
        view = self.view
        t = view.tableCommands

        # 1. сброс всех к дефолтам
        for table_row, info in self._cmd_by_row.items():
            chk = t.cellWidget(table_row, 0)
            w = t.cellWidget(table_row, 2)
            if not isinstance(chk, QCheckBox):
                continue
            chk.blockSignals(True)
            chk.setChecked(False)
            chk.blockSignals(False)
            w.setEnabled(False)

            default_value = info["command"]["default_value"]
            if default_value is not None:
                view.apply_value_to_widget(w, str(default_value))

        # 2. если cfg не выбран - всё
        if self.config_id is None:
            self._update_group_checks()
            return

        # 3. применяем сохранённые
        saved = self.service.saved_values(self.config_id)

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
                    view.apply_value_to_widget(w, custom_value)
                    w.setEnabled(True)

        self._update_group_checks()

    # ============ сохранение значений ============

    def _save_values_to_db(self):
        """Сохраняет отмеченные/снятые команды в ConfigValues."""
        if self.config_id is None:
            return

        t = self.view.tableCommands
        rows: list[tuple] = []

        for table_row, info in self._cmd_by_row.items():
            cmd_id = info["command"]["id"]
            chk = t.cellWidget(table_row, 0)
            w = t.cellWidget(table_row, 2)
            if not isinstance(chk, QCheckBox):
                continue

            if chk.isChecked():
                val = self.view.read_widget_value(w)
                rows.append((cmd_id, 1, val))
            else:
                rows.append((cmd_id, 0, None))

        self.service.save_values(self.config_id, rows)

    # ============ групповые чекбоксы ============

    def _update_group_checks(self):
        """Синхронизирует групповые чекбоксы с состоянием строк."""
        t = self.view.tableCommands
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

    def toggle_group(self, prefix_code: str):
        """Отмечает/снимает все ВИДИМЫЕ команды группы."""
        t = self.view.tableCommands
        if prefix_code not in self._group_chk:
            return

        rows = self._group_rows.get(prefix_code, [])
        checked = sum(
            1 for r in rows
            if not t.isRowHidden(r)
            and isinstance(t.cellWidget(r, 0), QCheckBox)
            and t.cellWidget(r, 0).isChecked()
        )
        visible = sum(1 for r in rows if not t.isRowHidden(r))
        target = checked < visible

        for r in rows:
            if t.isRowHidden(r):
                continue
            chk = t.cellWidget(r, 0)
            if isinstance(chk, QCheckBox):
                chk.setChecked(target)

    # ============ фильтры ============

    def _current_mode(self) -> str:
        idx = self.view.comboMode.currentIndex()
        return {0: "simple", 1: "advanced"}.get(idx, "advanced")

    def apply_filters(self):
        """Публичный метод - дёргается из View при смене фильтров."""
        mode_allowed = {
            "simple": MODE_SIMPLE,
            "advanced": MODE_ADVANCED,
        }[self._current_mode()]

        view = self.view
        prefix_item = view.listPrefixes.currentItem()
        prefix_code = None
        if prefix_item and not prefix_item.text().startswith("Все"):
            prefix_code = prefix_item.text().split(" ")[0]

        search = view.editSearch.text().lower().strip()
        t = view.tableCommands

        # 1. строки команд
        for row, info in self._cmd_by_row.items():
            cmd = info["command"]
            visible = (
                cmd["mode"] in mode_allowed
                and (prefix_code is None
                     or info["group_code"] == prefix_code)
                and (not search or search in cmd["key_name"].lower())
            )
            t.setRowHidden(row, not visible)

        # 2. заголовки групп без видимых строк
        for code, rows in self._group_rows.items():
            has_visible = any(not t.isRowHidden(r) for r in rows)
            if prefix_code is not None and code != prefix_code:
                has_visible = False
            t.setRowHidden(self._group_header_row[code], not has_visible)

        self._update_group_checks()

    # ============ проверки ============

    def _has_checked_commands(self) -> bool:
        t = self.view.tableCommands
        for row in self._cmd_by_row:
            chk = t.cellWidget(row, 0)
            if isinstance(chk, QCheckBox) and chk.isChecked():
                return True
        return False

    # ============ сбор данных ============

    def _collect_values(self) -> dict[str, str]:
        """Собирает отмеченные команды в {key_name: value}."""
        values: dict[str, str] = {}
        t = self.view.tableCommands

        for row, info in self._cmd_by_row.items():
            chk = t.cellWidget(row, 0)
            if not isinstance(chk, QCheckBox) or not chk.isChecked():
                continue
            cmd = info["command"]
            w = t.cellWidget(row, 2)
            values[cmd["key_name"]] = self.view.read_widget_value(w)

        return values

    # ============ применение ============

    def apply_silent(self) -> bool:
        """Сохраняет cfg без перехода на главную.

        Возвращает True при успехе.
        """
        values = self._collect_values()
        if not values:
            return False

        content = self.service.collect_content(values)

        try:
            # 1. создать или обновить cfg
            self.config_id = self.service.ensure_config(
                self.config_id, self.server_id,
                "system.cfg", content,
            )

            # 2. старые значения до сохранения
            old_values = {
                row["command_id"]: row["custom_value"]
                for row in self.service.config_repo.values(
                    self.config_id
                )
            }

            # 3. новые значения
            self._save_values_to_db()

            # 4. логи
            self._write_logs(old_values)

            return True
        except Exception as exc:
            print(f"[EditorPresenter] apply_silent failed: {exc}")
            return False

    def on_apply(self):
        """Полное сохранение + переход на главную."""
        values = self._collect_values()
        if not values:
            QMessageBox.information(
                self.view, "Нечего сохранять",
                "Не отмечено ни одной команды."
            )
            return

        if not self.apply_silent():
            QMessageBox.critical(
                self.view, "Ошибка сохранения",
                "Не удалось сохранить конфигурацию."
            )
            return

        QMessageBox.information(
            self.view, "Готово", "Конфигурация сохранена."
        )
        win = self.view.window()
        win.go_main(win.current_server_id)

    def reset_all(self):
        """Снимает все чекбоксы и возвращает значения к дефолтам."""
        t = self.view.tableCommands
        for row, info in self._cmd_by_row.items():
            chk = t.cellWidget(row, 0)
            w = t.cellWidget(row, 2)
            if isinstance(chk, QCheckBox):
                chk.setChecked(False)
            default_value = info["command"]["default_value"]
            if default_value is not None:
                self.view.apply_value_to_widget(w, str(default_value))
        self._update_group_checks()

    def cancel(self):
        """Отмена - назад, на главную."""
        win = self.view.window()
        win.go_main(win.current_server_id)

    # ============ логи (diff внутри презентера) ============

    def _write_logs(self, old_values: dict):
        """Пишет изменившиеся значения в Logs.

        Сравниваются ВСЕ команды, а не только отмеченные.
        Если команда была отмечена, а стала снята — она тоже
        попадёт в лог (new_val = None → "(выключено)").

        old_values: {cmd_id: old_value} из БД до сохранения.
        """
        if self.config_id is None:
            return

        t = self.view.tableCommands
        changes = []

        for row, info in self._cmd_by_row.items():
            cmd = info["command"]
            cmd_id = cmd["id"]
            chk = t.cellWidget(row, 0)
            w = t.cellWidget(row, 2)
            if not isinstance(chk, QCheckBox):
                continue

            # новое состояние
            if chk.isChecked():
                new_val = self.view.read_widget_value(w)
            else:
                new_val = None

            # старое состояние
            old_val = old_values.get(cmd_id)

            old_norm = None if old_val is None else str(old_val).strip()
            new_norm = None if new_val is None else str(new_val).strip()
            if old_norm == new_norm:
                continue

            old_display = (
                old_norm if old_norm is not None else "(выключено)"
            )
            new_display = (
                new_norm if new_norm is not None else "(выключено)"
            )

            changes.append((cmd["key_name"], old_display, new_display))

        if not changes:
            return

        try:
            self.service.write_logs(self.config_id, changes)
        except Exception as exc:
            print(f"[EditorPresenter] write_logs failed: {exc}")