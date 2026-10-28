"""Единая палитра и QSS приложения.

Все цвета — здесь. Все стили — здесь.

Не импортирует ничего из проекта — только qdarktheme (внутри setup_theme,
чтобы не тянуть при простом import).
"""
from PyQt6.QtGui import QColor


# ==================== Палитра ====================

# accent (золото)
ACCENT = "#b38532"
ACCENT_HOVER = "#d1a95e"
ACCENT_PRESSED = "#b8904a"
ACCENT_DARK = "#a8823e"

# фон
BG_APP = "#1e2026"
BG_PANEL = "#23252e"
BG_INPUT = "#2a2a3a"
BG_INPUT_HOVER = "#3a3a4a"
BG_PRESSED = "#1a1c22"

# текст
TEXT = "#e0e0e0"
TEXT_MUTED = "#b0b0c0"
TEXT_DIM = "#888888"
TEXT_DISABLED = "#666666"

# границы
BORDER = "#444444"
BORDER_HOVER = "#5a5a6a"

# семантика
DANGER = "#e05a5a"
DANGER_BG_HOVER = "#3a2020"
SUCCESS = "#8ec07c"
INFO = "#7aa2f7"

# подсветка синтаксиса (для cfg_highlighter)
SYNTAX_COMMENT = "#6a6a7a"      # серый
SYNTAX_SECTION = INFO           # голубой
SYNTAX_EQUALS = TEXT_DIM        # тёмно-серый

# 1. Валидные (известные) — зелёные
SYNTAX_KEY = SUCCESS            # "#8ec07c"
SYNTAX_VALUE = SUCCESS          # "#8ec07c"

# 2. Дубликаты — жёлтые
SYNTAX_DUP_KEY = "#e5c07b"      # жёлтый
SYNTAX_DUP_VALUE = "#e5c07b"    # жёлтый
SYNTAX_DUP_BG = QColor(80, 30, 30, 40) # лёгкий красноватый фон (оставим)

# 3. Неизвестные — серые
SYNTAX_UNKNOWN_KEY = "#6e6968"  # серый
SYNTAX_UNKNOWN_VALUE = "#6e6968"

# 4. Ошибки — красные
SYNTAX_ERROR_KEY = DANGER       # "#e05a5a"
SYNTAX_ERROR_VALUE = DANGER

# 5. Перезаписи
SYNTAX_OVERRIDDEN_KEY = "#e67e22"      # оранжевый
SYNTAX_OVERRIDDEN_VALUE = "#e67e22"

# ==================== QSS ====================

ADDITIONAL_QSS = f"""
    /* ============ Тултипы ============ */
    QToolTip {{
        background-color: #1e2026; /* BG_APP */
        color: #e0e0e0;            /* TEXT */
        border: 1px solid #b38532; /* ACCENT */
        border-radius: 3px;
        padding: 6px;
        font-family: 'Segoe UI';
        font-size: 11pt;
        opacity: 240;              /* Немного прозрачности */
    }}
    QWidget {{
        font-family: 'Segoe UI';
        font-size: 12pt;
    }}
    QHeaderView::section {{
        font-size: 11pt;
        font-weight: 600;
        padding: 6px 8px;
    }}

    /* ============ Роли лейблов ============ */
    QLabel[role="page-title"] {{
        font-size: 16pt;
        font-weight: 700;
        color: {ACCENT};
    }}
    QLabel[role="section-title"] {{
        font-size: 12pt;
        font-weight: 700;
        color: {TEXT_MUTED};
    }}
    QLabel[role="hint"] {{
        color: {TEXT_DIM};
    }}

    /* ============ Поля ввода ============ */
    QComboBox:hover,
    QLineEdit:hover,
    QPlainTextEdit:hover,
    QTextEdit:hover {{
        border: 1px solid {BORDER_HOVER};
    }}
    QComboBox:focus,
    QLineEdit:focus,
    QPlainTextEdit:focus,
    QTextEdit:focus {{
        border: 1px solid {ACCENT};
    }}

    QPushButton:pressed {{
        background-color: {ACCENT};
        color: {BG_APP};
    }}

    /* ============ Скролл бары ============ */
    QScrollBar:vertical {{
        background: transparent;
        width: 10px;
        margin: 0;
        border: none;
    }}
    QScrollBar::handle:vertical {{
        background: {BG_INPUT_HOVER};
        border-radius: 5px;
        min-height: 20px;
        margin: 2px;
    }}
    QScrollBar::handle:vertical:hover {{
        background: {ACCENT};
    }}
    QScrollBar::handle:vertical:pressed {{
        background: {ACCENT_PRESSED};
    }}
    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical {{
        height: 0;
        background: none;
        border: none;
    }}
    QScrollBar::add-page:vertical,
    QScrollBar::sub-page:vertical {{
        background: transparent;
    }}

    QScrollBar:horizontal {{
        background: transparent;
        height: 10px;
        margin: 0;
        border: none;
    }}
    QScrollBar::handle:horizontal {{
        background: {BG_INPUT_HOVER};
        border-radius: 5px;
        min-width: 20px;
        margin: 2px;
    }}
    QScrollBar::handle:horizontal:hover {{
        background: {ACCENT};
    }}
    QScrollBar::handle:horizontal:pressed {{
        background: {ACCENT_PRESSED};
    }}
    QScrollBar::add-line:horizontal,
    QScrollBar::sub-line:horizontal {{
        width: 0;
        background: none;
        border: none;
    }}
    QScrollBar::add-page:horizontal,
    QScrollBar::sub-page:horizontal {{
        background: transparent;
    }}
"""


# ==================== Установка ====================

def setup_theme(app):
    """Применяет qdarktheme + наши кастомные QSS-правила.

    Вызывается один раз в main() после создания QApplication.
    """
    import qdarktheme

    qdarktheme.setup_theme(
        "dark",
        custom_colors={"primary": ACCENT},
        corner_shape="sharp",
        additional_qss=ADDITIONAL_QSS,
    )