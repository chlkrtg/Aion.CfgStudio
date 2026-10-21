"""Подсветка синтаксиса cfg-файла для QPlainTextEdit.

Формат строк:
    -- комментарий
    key = "value"
    key = value
    [System-Configuration Ver1.0]

Дубли ключей подсвечиваются красным (и ключ, и значение).
"""
import re

from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QColor, QFont, QSyntaxHighlighter, QTextCharFormat

from logic.widgets.theme import (
    SYNTAX_COMMENT, SYNTAX_KEY, SYNTAX_VALUE,
    SYNTAX_SECTION, SYNTAX_EQUALS,
    SYNTAX_DUP_KEY, SYNTAX_DUP_VALUE, SYNTAX_DUP_BG,
    SYNTAX_UNKNOWN_KEY, SYNTAX_UNKNOWN_VALUE
)


def _fmt(color_hex: str, bold: bool = False) -> QTextCharFormat:
    f = QTextCharFormat()
    f.setForeground(QColor(color_hex))
    if bold:
        f.setFontWeight(QFont.Weight.Bold)
    return f


class CfgHighlighter(QSyntaxHighlighter):
    """Подсветка cfg-файла + подсветка дублей ключей."""

    def __init__(self, document, known_keys: set[str] | None = None):
        super().__init__(document)

        self._known_keys = known_keys or set()

        # --- статические форматы ---
        self._re_comment = QRegularExpression(r"(?:--|//|#).*$")
        self._fmt_comment = _fmt(SYNTAX_COMMENT)

        self._re_section = QRegularExpression(r"^\s*\[.*\]\s*$")
        self._fmt_section = _fmt(SYNTAX_SECTION, bold=True)

        # Регулярка стала чуть лояльнее: не требует жесткого закрытия кавычки
        self._re_kv = QRegularExpression(
            r'^\s*([A-Za-z_][A-Za-z0-9_]*)(\s*=\s*)(.*)$'
        )
        self._fmt_key = _fmt(SYNTAX_KEY)
        self._fmt_equals = _fmt(SYNTAX_EQUALS)
        self._fmt_value = _fmt(SYNTAX_VALUE)

        # --- дубли ---
        self._fmt_dup_key = _fmt(SYNTAX_DUP_KEY)
        self._fmt_dup_value = _fmt(SYNTAX_DUP_VALUE)
        self._fmt_dup_bg = QTextCharFormat()
        self._fmt_dup_bg.setBackground(QColor(SYNTAX_DUP_BG))

        # --- Незиветсные ---
        self._fmt_unknown_key = _fmt(SYNTAX_UNKNOWN_KEY)
        self._fmt_unknown_value = _fmt(SYNTAX_UNKNOWN_VALUE)

        self._duplicate_keys: set[str] = set()

        # Защита от рекурсии (чтобы rehighlight не вызывал сам себя)
        self._is_updating = False

        # Первичный расчёт
        self._recalc_duplicates()

        # Слушаем изменения
        document.contentsChange.connect(self._on_contents_change)

    def _on_contents_change(self, position: int, removed: int, added: int):
        """Вызывается при любом изменении текста."""
        if self._is_updating:
            return

        old_dups = self._duplicate_keys.copy()
        self._recalc_duplicates()

        # Если набор дублей изменился, принудительно перерисовываем весь текст
        if old_dups != self._duplicate_keys:
            self._is_updating = True
            self.rehighlight()
            self._is_updating = False

    def _recalc_duplicates(self):
        """Собирает ключи, встречающиеся больше одного раза."""
        text = self.document().toPlainText()
        seen = {}

        # Регулярка для быстрого поиска ключа
        key_re = re.compile(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=')

        for line in text.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith(("--", "//", "#")):
                continue
            m = key_re.match(line)
            if m:
                key = m.group(1)
                seen[key] = seen.get(key, 0) + 1

        self._duplicate_keys = {k for k, n in seen.items() if n > 1}

    def highlightBlock(self, text: str):
        # 1. комментарий
        it = self._re_comment.globalMatch(text)
        while it.hasNext():
            m = it.next()
            self.setFormat(m.capturedStart(), m.capturedLength(), self._fmt_comment)

        # 2. заголовок секции
        if self._re_section.match(text).hasMatch():
            self.setFormat(0, len(text), self._fmt_section)
            return

        # 3. key = value
        m = self._re_kv.match(text)
        if not m.hasMatch():
            return

        key = m.captured(1)
        is_dup = key in self._duplicate_keys
        is_unknown = self._known_keys and key not in self._known_keys

        key_start = m.capturedStart(1)
        key_len = m.capturedLength(1)
        eq_start = m.capturedStart(2)
        eq_len = m.capturedLength(2)
        val_start = m.capturedStart(3)
        val_len = m.capturedLength(3)

        # Фон: дубль важнее неизвестного
        if is_dup:
            self.setFormat(0, len(text), self._fmt_dup_bg)

        # Ключ: жёлтый (дубль) > красный (неизвестный) > золотой (известный)
        if is_dup:
            self.setFormat(key_start, key_len, self._fmt_dup_key)
        elif is_unknown:
            self.setFormat(key_start, key_len, self._fmt_unknown_key)
        else:
            self.setFormat(key_start, key_len, self._fmt_key)

        # Равно: серый (как было)
        self.setFormat(eq_start, eq_len, self._fmt_equals)

        # Значение
        if val_len > 0:
            # Если дубль - жёлтый, иначе белый (даже если неизвестный)
            self.setFormat(
                val_start, val_len,
                self._fmt_unknown_value if is_unknown else
                self._fmt_dup_value if is_dup else self._fmt_value
            )