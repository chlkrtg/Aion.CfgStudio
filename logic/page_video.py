"""Страница видео-руководства: список глав + плеер.

Вся логика - в VideoPresenter.
"""
import os
import sys

from PyQt6.QtCore import Qt, QTimer, QEvent
from PyQt6.QtWidgets import (
    QListWidgetItem, QMessageBox, QStyle, QSizePolicy,
)

from logic.base_page import BasePage
from logic.shortcuts import bind_shortcut, bind_shortcuts, WITH_CHILDREN
from logic.repositories import CommandRepository
from logic.presenters import VideoPresenter
from ui.video_help import Ui_VideoHelpDialog


class PageVideo(BasePage, Ui_VideoHelpDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # ================== презентер ==================
        command_repo = CommandRepository(self.db)
        self.presenter = VideoPresenter(self, command_repo)
        self.presenter.init_player()

        # ================== UI: видео растягивается, а не заголовок ==================
        self.videoLayout.setStretch(0, 0)
        self.videoLayout.setStretch(1, 1)

        self.videoWidget.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )

        # пересчёт высоты видео с debounce
        self._resize_timer = QTimer(self)
        self._resize_timer.setSingleShot(True)
        self._resize_timer.setInterval(50)
        self._resize_timer.timeout.connect(self._fit_video_to_width)

        self.videoWidget.installEventFilter(self)
        self._fit_video_to_width()

        # главы
        self.gbChapters.setMinimumWidth(300)
        self.gbChapters.setMaximumWidth(420)
        self.chaptersLayout.setStretch(0, 0)
        self.chaptersLayout.setStretch(1, 2)
        self.chaptersLayout.setStretch(2, 1)
        self.editChapterDesc.setMinimumHeight(80)

        self.rootLayout.setStretch(0, 0)
        self.rootLayout.setStretch(1, 1)

        # скрыть ненужное
        self.btnOpenFile.hide()
        self.lblVideoTitle.hide()

        self._connect_signals()
        self._apply_icons()
        self._setup_shortcuts()

    # ============== сигналы ==============

    def _connect_signals(self):
        self.btnClose.clicked.connect(self.presenter.go_back)
        self.listChapters.currentItemChanged.connect(
            self.presenter.on_chapter_changed
        )
        self.btnPlay.clicked.connect(self.presenter.play_pause)
        self.btnStop.clicked.connect(self.presenter.stop)
        self.sliderPosition.sliderMoved.connect(self.presenter.on_seek)
        self.sliderVolume.valueChanged.connect(self.presenter.on_volume)

    def _apply_icons(self):
        style = self.style()
        self.btnPlay.setIcon(
            style.standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        )
        self.btnStop.setIcon(
            style.standardIcon(QStyle.StandardPixmap.SP_MediaStop)
        )
        self.btnPlay.setText("")
        self.btnStop.setText("")

    # ============== хоткеи ==============

    def _setup_shortcuts(self):
        """Хоткеи плеера: работают при фокусе на любом виджете страницы."""
        bind_shortcuts(self, {
            "Space": self.presenter.play_pause,
            "Left": self.presenter.seek_back,
            "Right": self.presenter.seek_forward,
            "Shift+Left": lambda: self.presenter.seek(-30000),
            "Shift+Right": lambda: self.presenter.seek(+30000),
            "Up": lambda: self.presenter.change_volume(+5),
            "Down": lambda: self.presenter.change_volume(-5),
            "M": self.presenter.toggle_mute,
            "Home": lambda: self.presenter.seek_to(0),
            "End": self.presenter.seek_to_end,
            "Escape": self.presenter.go_back,
        }, WITH_CHILDREN)

        # 0–9 - переход к проценту видео
        for digit in range(10):
            bind_shortcut(
                self,
                str(digit),
                lambda _checked=False, d=digit:
                    self.presenter.seek_to_percent(d * 10),
                WITH_CHILDREN,
            )

    # ============== жизненный цикл ==============

    def on_enter(self):
        self.presenter.on_enter()

    def on_leave(self):
        self.presenter.on_leave()

    # ============== UI-хелперы (зовёт презентер) ==============

    def make_chapter_item(self, title: str, ts: int, desc: str):
        """Создаёт QListWidgetItem для главы."""
        item = QListWidgetItem(title)
        item.setData(Qt.ItemDataRole.UserRole, ts)
        item.setData(Qt.ItemDataRole.UserRole + 1, desc or "")
        return item

    def show_player_unavailable(self):
        """Сообщает, что плеер недоступен."""
        QMessageBox.information(
            self, "Плеер недоступен",
            "PyQt6.QtMultimedia не установлен или видео не найдено."
        )

    # ============== пересчёт высоты видео ==============

    def _fit_video_to_width(self):
        """Высота videoWidget = 16:9 от ширины."""
        w = self.videoWidget.width()
        if w <= 0:
            return

        new_h = int(w * 9 / 16)

        max_h = self.gbVideo.height() - 150
        if max_h > 0 and new_h > max_h:
            new_h = max_h

        if self.videoWidget.height() == new_h:
            return

        self.videoWidget.setUpdatesEnabled(False)
        self.videoWidget.setFixedHeight(new_h)
        self.videoWidget.setUpdatesEnabled(True)

    def eventFilter(self, obj, event):
        """Пересчитывает высоту videoWidget с дебаунсом 50 мс."""
        if obj is self.videoWidget and event.type() in (
                QEvent.Type.Resize,
                QEvent.Type.Show,
        ):
            self._resize_timer.start()
        return super().eventFilter(obj, event)

    # ============== поиск видео ==============
    def media_path(self) -> str:
        """Путь к встроенному видео."""
        if getattr(sys, "frozen", False):
            base = sys._MEIPASS
        else:
            base = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
        return os.path.join(base, "media", "tutorial.mp4")