import ctypes
import os
import sys

from PyQt6.QtCore import QEvent, QObject, Qt, QTimer
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
from logic.widgets.theme import ACCENT, BG_APP, BG_INPUT, TEXT_DIM, setup_theme

WM_NCACTIVATE = 0x0086

def _force_titlebar_redraw(hwnd: int):
    """Форсирует перерисовку non-client area (заголовка) без ресайза."""
    try:
        user32 = ctypes.windll.user32
        # False → True: заставляет Windows перерисовать заголовок
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
    """Применяет единое оформление к окну (тёмный заголовок Windows).
            Работает для главного окна и диалогов.
    """
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
    """Применяет единое оформление ко всем диалогам при их показе."""

    def eventFilter(self, obj, event):
        if (event.type() == QEvent.Type.Show
            and isinstance(obj, (QMessageBox, QInputDialog, QFileDialog, QDialog))):
                QTimer.singleShot(0, lambda o=obj: _style_window(o))
        return super().eventFilter(obj, event)


def _make_splash() -> QSplashScreen:
    W, H = 460, 240

    pix = QPixmap(W, H)
    pix.fill(QColor(BG_APP))

    splash = QSplashScreen(pix)

    title = QLabel("Aion.CfgStudio", splash)
    title.setGeometry(0, 50, W, 40)
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title.setStyleSheet(
        f"color: {ACCENT};"
        "font-size: 22pt;"
        "font-weight: bold;"
        "background: transparent;"
    )

    subtitle = QLabel("Configuration Editor", splash)
    subtitle.setGeometry(0, 90, W, 22)
    subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
    subtitle.setStyleSheet(
        f"color: {TEXT_DIM};"
        "font-size: 11pt;"
        "background: transparent;"
    )

    progress = QProgressBar(splash)
    progress.setGeometry(60, 160, W - 120, 4)
    progress.setRange(0, 0)
    progress.setTextVisible(False)
    progress.setStyleSheet(f"""
        QProgressBar {{
            background: {BG_INPUT};
            border: none;
            border-radius: 2px;
        }}
        QProgressBar::chunk {{
            background: {ACCENT};
            border-radius: 2px;
        }}
    """)

    status = QLabel(t("splash.loading"), splash)
    status.setGeometry(0, 175, W, 22)
    status.setAlignment(Qt.AlignmentFlag.AlignCenter)
    status.setStyleSheet(
        f"color: {TEXT_DIM};"
        "font-size: 10pt;"
        "background: transparent;"
    )

    return splash


def main() -> int:
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(resource_path("resources/icons/aion.cfgstudio.ico")))
    _filter = _DarkDialogsFilter()
    app.installEventFilter(_filter)
    app.setApplicationName("Aion.CfgStudio")
    app.setApplicationDisplayName("Aion.CfgStudio")

    setup_theme(app)

    splash = _make_splash()
    splash.show()
    app.processEvents()

    db = DBManager()
    if not db.list_profiles():
        db.create_profile("Demo", "Демонстрационный профиль")

    window = AppWindow(db)

    window.show()
    _style_window(window)
    splash.finish(window)

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
