"""Делегат для колонки значений в редакторе команд.

Один делегат на всю таблицу - вместо 1114 виджетов.
Редактор (QComboBox/QSpinBox/QLineEdit) создаётся ТОЛЬКО когда
пользователь кликает на ячейку, и удаляется после редактирования.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QStyledItemDelegate, QComboBox, QSpinBox, QLineEdit,
)


class ValueDelegate(QStyledItemDelegate):
    """Рисует и редактирует ячейку значения команды."""

    # роль для хранения метаданных команды в item
    CMD_TYPE_ROLE = Qt.ItemDataRole.UserRole + 10
    CMD_POSSIBLE_ROLE = Qt.ItemDataRole.UserRole + 11
    CMD_MIN_ROLE = Qt.ItemDataRole.UserRole + 12
    CMD_MAX_ROLE = Qt.ItemDataRole.UserRole + 13

    # ============ создание редактора ============

    def createEditor(self, parent, option, index):
        """Создаёт редактор только при клике на ячейку."""
        print(f"[createEditor] vtype={index.data(self.CMD_TYPE_ROLE)}, "
              f"possible={index.data(self.CMD_POSSIBLE_ROLE)}")
        vtype = index.data(self.CMD_TYPE_ROLE) or "string"
        possible = index.data(self.CMD_POSSIBLE_ROLE)

        # bool или перечисление → QComboBox
        if vtype == "bool" or (possible and "," in possible):
            w = QComboBox(parent)
            if possible:
                for v in possible.split(","):
                    w.addItem(v.strip())
            else:
                w.addItem("0")
                w.addItem("1")
            return w

        # int → QSpinBox
        if vtype == "int":
            w = QSpinBox(parent)
            min_v = index.data(self.CMD_MIN_ROLE)
            max_v = index.data(self.CMD_MAX_ROLE)
            w.setMinimum(int(min_v) if min_v else -999999)
            w.setMaximum(int(max_v) if max_v else 999999)
            return w

        # всё остальное → QLineEdit
        return QLineEdit(parent)

    # ============ передача данных в редактор ============

    def setEditorData(self, editor, index):
        """Переносит значение из ячейки в редактор при открытии."""
        value = index.data(Qt.ItemDataRole.EditRole)

        if isinstance(editor, QComboBox):
            idx = editor.findText(str(value))
            if idx >= 0:
                editor.setCurrentIndex(idx)
        elif isinstance(editor, QSpinBox):
            try:
                editor.setValue(int(value))
            except (ValueError, TypeError):
                pass
        elif isinstance(editor, QLineEdit):
            editor.setText(str(value) if value is not None else "")

    # ============ передача данных обратно в ячейку ============

    def setModelData(self, editor, model, index):
        """Сохраняет значение из редактора в ячейку."""
        if isinstance(editor, QComboBox):
            model.setData(index, editor.currentText(), Qt.ItemDataRole.EditRole)
        elif isinstance(editor, QSpinBox):
            model.setData(index, str(editor.value()), Qt.ItemDataRole.EditRole)
        elif isinstance(editor, QLineEdit):
            model.setData(index, editor.text().strip(), Qt.ItemDataRole.EditRole)