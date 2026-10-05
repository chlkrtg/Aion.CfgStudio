"""Базовый класс для всех страниц."""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QMessageBox, QInputDialog, QLineEdit


class BasePage(QWidget):
    """Общий предок страниц. Не вызывать напрямую — только наследовать!!!"""

    @property
    def db(self):
        """Доступ к БД через родительское окно."""
        return self.window().db

    # ==================== Жизненный цикл ====================

    def on_enter(self):
        """Вызывается, когда страница становится активной."""

    def on_leave(self):
        """Вызывается перед уходом со страницы."""

    def build_menus(self) -> dict:
        """Возвращает {заголовок: [действия]}."""
        return {}

    # ==================== Управление контролами ====================

    def set_controls_enabled(self, enabled: bool, *widgets):
        """Включает/выключает переданные виджеты."""
        for w in widgets:
            w.setEnabled(enabled)

    # ==================== Сохранение текста ====================

    def persist_text(self, item, text: str, max_len: int,
                     save_func, label: str) -> bool:
        """Сохраняет текст с обрезкой и обработкой ошибок."""
        if item is None:
            return False

        item_id = item.data(Qt.ItemDataRole.UserRole)
        if len(text) > max_len:
            text = text[:max_len]

        try:
            save_func(item_id, text)
            return True
        except Exception as exc:
            QMessageBox.warning(
                self, "Ошибка",
                f"Не удалось сохранить {label}:\n{exc}"
            )
            return False

    # ==================== Валидация имён ====================

    def validate_name(self, value: str, max_len: int, field: str) -> str | None:
        """Проверяет имя. Возвращает очищенное значение или None при ошибке."""
        value = value.strip()
        if not value:
            QMessageBox.warning(self, "Ошибка", f"{field} не может быть пустым.")
            return None
        if len(value) > max_len:
            QMessageBox.warning(
                self, "Ошибка",
                f"{field} слишком длинное: {len(value)} символов.\n"
                f"Максимум - {max_len}."
            )
            return None
        return value

    def ask_name(self, title: str, label: str, default: str = "",
                 max_len: int = 64) -> tuple[str, bool]:
        """QInputDialog.getText с ограничением длины ввода. Возвращает (значение, ok)."""
        dialog = QInputDialog(self)
        dialog.setWindowTitle(title)
        dialog.setLabelText(label)
        dialog.setTextValue(default)
        dialog.setInputMode(QInputDialog.InputMode.TextInput)

        line_edit = dialog.findChild(QLineEdit)
        if line_edit is not None:
            line_edit.setMaxLength(max_len)

        ok = dialog.exec() == QInputDialog.DialogCode.Accepted
        return dialog.textValue(), ok

    def ask_name_hint(self, title: str, label: str, max_len: int,
                      default: str = "") -> tuple[str, bool]:
        """ask_name с подсказкой о максимальной длине."""
        return self.ask_name(
            title,
            f"{label} (макс. {max_len}):",
            default=default,
            max_len=max_len,
        )
