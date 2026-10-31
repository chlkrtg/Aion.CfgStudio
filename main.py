import ctypes
import os
import re
import sys

from PyQt6.QtCore import QEvent, QObject, QTimer, Qt
from PyQt6.QtGui import QColor, QIcon, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QInputDialog,
    QLabel,
    QMessageBox,
    QProgressBar,
    QSplashScreen,
)

from database.db_manager import DBManager
from logic.app_window import AppWindow
from logic.core.i18n import t
from logic.core.license import (
    check_clock_rollback,
    load_hwm,
    validate_code,
)
from logic.widgets.activation_dialog import ActivationDialog
from logic.widgets.dialogs import warn
from logic.widgets.theme import ACCENT, BG_APP, BG_INPUT, TEXT_DIM, setup_theme


# ==================== ЛИЦЕНЗИЯ ====================

def ensure_license(window) -> bool:
    from database.db_manager import get_app_dir

    repo = window.settings_repo
    app_dir = get_app_dir()

    if not check_clock_rollback(repo, app_dir):
        warn(window, t("license.title"), t("license.clock_rollback"))
        return False

    saved = repo.get("license.code", "") or ""
    if saved:
        hwm = load_hwm(repo, app_dir)
        ok, _ = validate_code(saved, hwm=hwm)
        if ok:
            return True

    window._activation_dlg = ActivationDialog(window)
    result = window._activation_dlg.exec()

    if result != QDialog.DialogCode.Accepted:
        window._activation_dlg = None
        return False

    code = window._activation_dlg.code
    window._activation_dlg = None
    repo.set("license.code", code)
    return True


# ==================== WINDOWS-ЗАГОЛОВОК ====================

WM_NCACTIVATE = 0x0086


def _force_titlebar_redraw(hwnd: int):
    try:
        user32 = ctypes.windll.user32
        user32.SendMessageW(hwnd, WM_NCACTIVATE, 0, 0)
        user32.SendMessageW(hwnd, WM_NCACTIVATE, 1, 0)
    except Exception:
        pass


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


def resource_path(relative: str) -> str:
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)


def _style_window(window):
    try:
        hwnd = int(window.winId())
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd, 20,
            ctypes.byref(ctypes.c_int(1)),
            ctypes.sizeof(ctypes.c_int),
        )
        _force_titlebar_redraw(hwnd)
    except Exception:
        pass


class _DarkDialogsFilter(QObject):
    def eventFilter(self, obj, event):
        if (event.type() == QEvent.Type.Show
            and isinstance(obj, (QMessageBox, QInputDialog, QFileDialog, QDialog))):
                QTimer.singleShot(0, lambda o=obj: _style_window(o))
        return super().eventFilter(obj, event)


# ==================== СПЛЭШ ====================

def _short_version(v: str) -> str:
    if not v:
        return "?"
    m = re.match(r"^(\d+(?:\.\d+)*)", str(v))
    return m.group(1) if m else str(v)


def _make_splash() -> QSplashScreen:
    from logic.core.constants import APP_VERSION
    from logic.widgets.splash_matrix import SplashMatrix
    from PyQt6.QtGui import QLinearGradient, QPainter
    from PyQt6.QtWidgets import QFrame

    W, H = 520, 320

    # --- Фон с градиентом ---
    pix = QPixmap(W, H)
    painter = QPainter(pix)
    gradient = QLinearGradient(0, 0, 0, H)
    gradient.setColorAt(0.0, QColor(BG_APP))
    gradient.setColorAt(1.0, QColor("#14161c"))
    painter.fillRect(pix.rect(), gradient)
    painter.end()

    splash = QSplashScreen(pix)

    # --- Слой с командами ---
    matrix = SplashMatrix(splash)
    matrix.setGeometry(0, 0, W, H)
    matrix.lower()
    matrix.show()
    splash._matrix = matrix

    # --- Логотип ---
    logo = QLabel("{A}", splash)
    logo.setGeometry(W // 2 - 40, 30, 80, 80)
    logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet(f"""
        QLabel {{
            background-color: {ACCENT};
            color: {BG_APP};
            border-radius: 40px;
            font-size: 28pt;
            font-weight: bold;
            font-family: 'Consolas', monospace;
        }}
    """)

    # --- Заголовок ---
    title = QLabel("Aion.CfgStudio", splash)
    title.setGeometry(0, 115, W, 40)
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title.setStyleSheet(f"""
        color: {ACCENT};
        font-size: 24pt;
        font-weight: bold;
        background: transparent;
    """)

    # --- Линия ---
    line = QFrame(splash)
    line.setGeometry(80, 165, W - 160, 1)
    line.setStyleSheet(f"""
        QFrame {{
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:0,
                stop:0 transparent,
                stop:0.5 {ACCENT},
                stop:1 transparent
            );
            border: none;
        }}
    """)

    # --- Подзаголовок ---
    subtitle = QLabel("Configuration Editor", splash)
    subtitle.setGeometry(0, 175, W, 22)
    subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
    subtitle.setStyleSheet(f"""
        color: {TEXT_DIM};
        font-size: 11pt;
        font-style: italic;
        background: transparent;
    """)

    # --- Прогресс ---
    progress = QProgressBar(splash)
    progress.setGeometry(80, 240, W - 160, 6)
    progress.setRange(0, 0)
    progress.setTextVisible(False)
    progress.setStyleSheet(f"""
        QProgressBar {{
            background: {BG_INPUT};
            border: none;
            border-radius: 3px;
        }}
        QProgressBar::chunk {{
            background: {ACCENT};
            border-radius: 3px;
        }}
    """)

    # --- Статус ---
    status = QLabel(t("splash.loading"), splash)
    status.setGeometry(0, 260, W, 22)
    status.setAlignment(Qt.AlignmentFlag.AlignCenter)
    status.setStyleSheet(f"""
        color: {TEXT_DIM};
        font-size: 10pt;
        background: transparent;
    """)

    dots_timer = QTimer(splash)
    dots_state = {"n": 0}

    def _update_dots():
        dots_state["n"] = (dots_state["n"] + 1) % 4
        status.setText(t("splash.loading") + "." * dots_state["n"])

    dots_timer.timeout.connect(_update_dots)
    dots_timer.start(400)
    splash._dots_timer = dots_timer

    # --- Версия ---
    version = QLabel(f"v{_short_version(APP_VERSION)}", splash)
    version.setGeometry(W - 80, H - 25, 70, 20)
    version.setAlignment(Qt.AlignmentFlag.AlignRight)
    version.setStyleSheet(f"""
        color: {TEXT_DIM};
        font-size: 9pt;
        background: transparent;
    """)

    return splash


# ==================== MAIN ====================

def main() -> int:
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(resource_path("resources/icons/aion.cfgstudio.ico")))
    _filter = _DarkDialogsFilter()
    app.installEventFilter(_filter)
    app.setApplicationName("Aion.CfgStudio")
    app.setApplicationDisplayName("Aion.CfgStudio")

    setup_theme(app)

    def _startup():
        splash = _make_splash()
        splash.show()

        def _load():
            db = DBManager()
            window = AppWindow(db)

            if not ensure_license(window):
                if hasattr(splash, "_matrix"):
                    splash._matrix.stop()
                splash.deleteLater()
                app.quit()
                return

            window.show()
            _style_window(window)

            if hasattr(splash, "_matrix"):
                splash._matrix.stop()
            splash.finish(window)
            splash.deleteLater()

        QTimer.singleShot(1500, _load)

    QTimer.singleShot(0, _startup)

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())