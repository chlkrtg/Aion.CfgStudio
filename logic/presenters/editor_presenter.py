"""Presenter для страницы редактора cfg.

Ленивая загрузка: строки строятся только для видимых команд
(под текущий фильтр). Состояние всех команд хранится в self._state -
это позволяет сохранять и логировать изменения скрытых команд тоже.
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

        self.config_id: int | None = None
        self.server_id: int | None = None

        # кэш данных из БД
        self._commands: list | None = None
        self._prefixes: dict | None = None

        # снимок состояния ВСЕХ команд: {cmd_id: (use, value)}
        self._state: dict[int, tuple[int, str | None]] = {}

        # что сейчас в таблице
        self._cmd_by_row: dict[int, dict] = {}
        self._group_rows: dict[str, list[int]] = {}
        self._group_header_row: dict[str, int] = {}

    # ============ контекст ============

    def set_context(self, config_id, server_id):
        self.config_id = config_id
        self.server_id = server_id

    # ============ жизненный цикл ============

    def on_enter(self):
        self.refresh()

    def on_leave(self):
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
        self._load_commands_cache()
        self._load_state_snapshot()
        self.apply_filters(sync=False)

    def _update_file_label(self):
        if self.config_id is None:
            self.view.lblFileName.setText("Файл: (новый)")
            return
        cfg = self.service.config_repo.get(self.config_id)
        if cfg:
            self.view.lblFileName.setText(f"Файл: {cfg['filename']}")
        else:
            self.view.lblFileName.setText("Файл: —")

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

    def _load_commands_cache(self):
        if self._commands is None:
            self._commands = list(self.service.all_commands())
        if self._prefixes is None:
            self._prefixes = {
                row["id"]: dict(row)
                for row in self.service.all_prefixes()
            }

    def _load_state_snapshot(self):
        """Загружает ВСЕ значения cfg в self._state."""
        self._state = {}
        if self.config_id is None:
            for cmd in self._commands:
                self._state[cmd["id"]] = (0, None)
            return

        saved = self.service.saved_values(self.config_id)
        for cmd in self._commands:
            cmd_id = cmd["id"]
            if cmd_id in saved:
                self._state[cmd_id] = saved[cmd_id]
            else:
                self._state[cmd_id] = (0, None)

    # ============ фильтры ============

    def _current_mode(self) -> str:
        idx = self.view.comboMode.currentIndex()
        return {0: "simple", 1: "advanced"}.get(idx, "advanced")

    def apply_filters(self, sync=True):
        """Определяет видимые команды и перестраивает таблицу.

        sync=True — синхронизировать _state с текущей таблицей.
        sync=False — не синхронизировать (при входе на страницу).
        """
        if sync:
            self._sync_state_from_table()

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

        visible = []
        for cmd in self._commands:
            pid = cmd["prefix_id"]
            if pid is None or pid not in self._prefixes:
                continue
            pcode = self._prefixes[pid]["code"]

            if cmd["mode"] not in mode_allowed:
                continue
            if prefix_code is not None and pcode != prefix_code:
                continue
            if search and search not in cmd["key_name"].lower():
                continue

            visible.append((cmd, pcode))

        self._rebuild_table(visible)

    def _rebuild_table(self, visible_commands):
        view = self.view
        t = view.tableCommands

        self._cmd_by_row.clear()
        self._group_rows.clear()
        self._group_header_row.clear()
        self._group_chk.clear()

        t.blockSignals(True)  # ← блокируем сигналы
        t.setUpdatesEnabled(False)
        t.setRowCount(0)

        current_prefix = None
        row = 0

        for cmd, pcode in visible_commands:
            prefix = self._prefixes[cmd["prefix_id"]]

            if pcode != current_prefix:
                t.insertRow(row)
                view.make_group_header(row, pcode, prefix["name"])

                chk_item = t.item(row, 0)
                self._group_header_row[pcode] = row
                self._group_rows[pcode] = []

                current_prefix = pcode
                row += 1

            t.insertRow(row)
            view.fill_command_row(row, cmd)
            self._cmd_by_row[row] = {
                "command": cmd,
                "group_code": pcode,
            }
            self._group_rows[pcode].append(row)

            # применить сохранённое состояние
            use, val = self._state.get(cmd["id"], (0, None))
            chk_item = t.item(row, 0)
            val_item = t.item(row, 2)
            if use and val is not None:
                chk_item.setCheckState(Qt.CheckState.Checked)
                val_item.setText(str(val))
                view.set_value_enabled(row, True)
            else:
                chk_item.setCheckState(Qt.CheckState.Unchecked)
                view.set_value_enabled(row, False)

            row += 1

        t.setUpdatesEnabled(True)
        t.blockSignals(False)  # ← разблокируем

        self._update_group_checks()

    # ============ синхронизация состояния ============

    def _sync_state_from_table(self):
        """Обновляет self._state тем, что сейчас в таблице."""
        t = self.view.tableCommands
        for row, info in self._cmd_by_row.items():
            cmd_id = info["command"]["id"]
            chk_item = t.item(row, 0)
            val_item = t.item(row, 2)
            if chk_item is None or val_item is None:
                continue

            checked = (chk_item.checkState() == Qt.CheckState.Checked)
            if checked:
                val = val_item.text().strip()
                self._state[cmd_id] = (1, val)
            else:
                self._state[cmd_id] = (0, None)

    # ============ групповые чекбоксы ============

    def _update_group_checks(self):
        t = self.view.tableCommands
        for code, chk_row in self._group_header_row.items():
            rows = self._group_rows.get(code, [])
            checked = 0
            total = 0
            for r in rows:
                chk_item = t.item(r, 0)
                if chk_item is not None:
                    total += 1
                    if chk_item.checkState() == Qt.CheckState.Checked:
                        checked += 1

            if total == 0 or checked == 0:
                state = Qt.CheckState.Unchecked
            elif checked == total:
                state = Qt.CheckState.Checked
            else:
                state = Qt.CheckState.PartiallyChecked

            group_item = t.item(chk_row, 0)
            if group_item is not None:
                t.blockSignals(True)
                group_item.setCheckState(state)
                t.blockSignals(False)

    # ============ сохранение ============

    def _save_values_to_db(self):
        """Сохраняет ВСЕ значения (и видимые, и скрытые)."""
        if self.config_id is None:
            return

        self._sync_state_from_table()

        rows = []
        for cmd in self._commands:
            cmd_id = cmd["id"]
            use, val = self._state.get(cmd_id, (0, None))
            rows.append((cmd_id, use, val))

        self.service.save_values(self.config_id, rows)

    def _has_checked_commands(self) -> bool:
        self._sync_state_from_table()
        return any(use for use, _ in self._state.values())

    # ============ сборка content ============

    def _collect_values(self) -> dict[str, str]:
        self._sync_state_from_table()

        values = {}
        for cmd in self._commands:
            use, val = self._state.get(cmd["id"], (0, None))
            if use and val is not None:
                values[cmd["key_name"]] = val
        return values

    # ============ применение ============

    def apply_silent(self) -> bool:
        values = self._collect_values()
        if not values:
            return False

        content = self.service.collect_content(values)

        try:
            # 1. старое состояние из БД
            old_state = {}
            if self.config_id is not None:
                saved = self.service.saved_values(self.config_id)
                for cmd in self._commands:
                    cmd_id = cmd["id"]
                    if cmd_id in saved:
                        old_state[cmd_id] = saved[cmd_id]
                    else:
                        old_state[cmd_id] = (0, None)
            else:
                for cmd in self._commands:
                    old_state[cmd["id"]] = (0, None)

            # 2. создать или обновить cfg
            self.config_id = self.service.ensure_config(
                self.config_id, self.server_id,
                "system.cfg", content,
            )

            # 3. синхронизировать и сохранить
            self._sync_state_from_table()
            self._save_values_to_db()

            # 4. логи
            self._write_logs(old_state)

            return True
        except Exception as exc:
            print(f"[EditorPresenter] apply_silent failed: {exc}")
            return False

    def on_apply(self):
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

    def on_item_changed(self, item):
        """Вызывается при ЛЮБОМ изменении ячейки.

        Обрабатываем два случая:
          1. Изменился чекбокс команды → обновить групповой чекбокс.
          2. Изменился групповой чекбокс → отметить/снять все видимые в группе.
        """
        if item.column() != 0:
            return

        t = self.view.tableCommands
        marker = item.data(Qt.ItemDataRole.UserRole)

        if marker is None:
            return

        # 1. групповой чекбокс
        if isinstance(marker, str) and marker.startswith("GROUP:"):
            code = marker[6:]
            state = item.checkState()

            # блокируем сигналы, чтобы не сработал itemChanged на командах
            t.blockSignals(True)
            if state == Qt.CheckState.Checked:
                for r in self._group_rows.get(code, []):
                    chk_item = t.item(r, 0)
                    if chk_item is not None:
                        chk_item.setCheckState(Qt.CheckState.Checked)
            elif state == Qt.CheckState.Unchecked:
                for r in self._group_rows.get(code, []):
                    chk_item = t.item(r, 0)
                    if chk_item is not None:
                        chk_item.setCheckState(Qt.CheckState.Unchecked)
            t.blockSignals(False)

            self._update_group_checks()
            return

        # 2. чекбокс команды
        if isinstance(marker, str) and marker.startswith("CMD:"):
            row = t.row(item)
            # включить/выключить ячейку значения
            checked = (item.checkState() == Qt.CheckState.Checked)
            self.view.set_value_enabled(row, checked)

            # обновить групповой чекбокс
            self._update_group_checks()
            return

    def reset_all(self):
        t = self.view.tableCommands
        t.blockSignals(True)
        for row, info in self._cmd_by_row.items():
            chk_item = t.item(row, 0)
            val_item = t.item(row, 2)
            if chk_item is not None:
                chk_item.setCheckState(Qt.CheckState.Unchecked)
            default_value = info["command"]["default_value"]
            if val_item is not None and default_value is not None:
                val_item.setText(str(default_value))
            self.view.set_value_enabled(row, False)
        t.blockSignals(False)
        self._update_group_checks()

    def cancel(self):
        win = self.view.window()
        win.go_main(win.current_server_id)

    # ============ логи ============

    def _write_logs(self, old_state: dict):
        if self.config_id is None:
            return

        id_to_key = {
            cmd["id"]: cmd["key_name"]
            for cmd in self._commands
        }

        changes = []
        for cmd_id, (old_use, old_val) in old_state.items():
            new_use, new_val = self._state.get(cmd_id, (0, None))

            old_norm = old_val if old_use else None
            new_norm = new_val if new_use else None

            old_str = None if old_norm is None else str(old_norm).strip()
            new_str = None if new_norm is None else str(new_norm).strip()

            if old_str == new_str:
                continue

            key = id_to_key.get(cmd_id)
            if key is None:
                continue

            old_display = old_str if old_str is not None else "(выключено)"
            new_display = new_str if new_str is not None else "(выключено)"

            changes.append((key, old_display, new_display))

        if not changes:
            return

        try:
            self.service.write_logs(self.config_id, changes)
        except Exception as exc:
            print(f"[EditorPresenter] write_logs failed: {exc}")