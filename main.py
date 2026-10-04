import os
import sys
import ctypes
import qdarktheme

from database.db_manager import DBManager
from logic.app_window import AppWindow
from PyQt6.QtCore import Qt, QTimer, QObject, QEvent
from PyQt6.QtWidgets import (
    QApplication, QSplashScreen, QLabel, QProgressBar,
    QMessageBox, QInputDialog, QFileDialog,
)
from PyQt6.QtGui import QColor, QPixmap, QIcon

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

        rect = window.geometry()
        window.resize(rect.width() + 1, rect.height())
        QTimer.singleShot(10, lambda: window.resize(rect.width(), rect.height()))
    except Exception:
        pass


class _DarkDialogsFilter(QObject):
    """Применяет единое оформление ко всем диалогам при их показе."""

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.Show:
            if isinstance(obj, (QMessageBox, QInputDialog, QFileDialog)):
                QTimer.singleShot(0, lambda o=obj: _style_window(o))
        return super().eventFilter(obj, event)


def _make_splash() -> QSplashScreen:
    """Сплэш-скрин в стиле приложения."""
    W, H = 460, 240

    pix = QPixmap(W, H)
    pix.fill(QColor("#1e2026"))

    splash = QSplashScreen(pix)

    # Заголовок
    title = QLabel("Aion.CfgStudio", splash)
    title.setGeometry(0, 50, W, 40)
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title.setStyleSheet(
        "color: #d4a95a;"
        "font-family: 'Segoe UI';"
        "font-size: 22pt;"
        "font-weight: bold;"
        "background: transparent;"
    )

    subtitle = QLabel("Configuration Editor", splash)
    subtitle.setGeometry(0, 90, W, 22)
    subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
    subtitle.setStyleSheet(
        "color: #7a7a8a;"
        "font-family: 'Segoe UI';"
        "font-size: 11pt;"
        "background: transparent;"
    )

    progress = QProgressBar(splash)
    progress.setGeometry(60, 160, W - 120, 4)
    progress.setRange(0, 0)
    progress.setTextVisible(False)
    progress.setStyleSheet("""
        QProgressBar {
            background: #2a2a3a;
            border: none;
            border-radius: 2px;
        }
        QProgressBar::chunk {
            background: #d4a95a;
            border-radius: 2px;
        }
    """)

    status = QLabel("Загрузка компонентов...", splash)
    status.setGeometry(0, 175, W, 22)
    status.setAlignment(Qt.AlignmentFlag.AlignCenter)
    status.setStyleSheet(
        "color: #7a7a8a;"
        "font-family: 'Segoe UI';"
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

    qdarktheme.setup_theme(
        "dark",
        custom_colors={"primary": "#d4a95a"},
        corner_shape="sharp",
        additional_qss="""
            QWidget { font-size: 12pt; }
            QTableWidget { font-size: 12pt; }
            QHeaderView::section { font-size: 12pt; }
            QComboBox { font-size: 12pt; }
            QPushButton { font-size: 12pt; }
            QLabel { font-size: 12pt; }
            QListWidget { font-size: 12pt; }
            QLineEdit { font-size: 12pt; }
        """,
    )

    splash = _make_splash()
    splash.show()
    app.processEvents()

    db = DBManager()
    if not db.list_profiles():
        db.create_profile("Demo", "Демонстрационный профиль")

    window = AppWindow(db)

    try:
        if not window.page_editor._built:
            window.page_editor._build_all_rows()
            window.page_editor._built = True
    except Exception as exc:
        print(f"[preload] Ошибка: {exc}")

    window.show()
    _style_window(window)
    splash.finish(window)

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
