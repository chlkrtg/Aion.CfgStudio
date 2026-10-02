"""Страница видео-руководства: список глав + плеер."""
import os
import sys

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl, Qt, QTimer, QEvent
from PyQt6.QtWidgets import (
    QListWidgetItem, QFileDialog, QMessageBox, QStyle, QSizePolicy,
)

from logic.base_page import BasePage
from logic.shortcuts import bind_shortcuts, WITH_CHILDREN, bind_shortcut
from ui.video_help import Ui_VideoHelpDialog


def _media_path() -> str:
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, "media", "tutorial.mp4")


class PageVideo(BasePage, Ui_VideoHelpDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # растягиваем область видео, а не заголовок
        self.videoLayout.setStretch(0, 0)  # lblVideoTitle
        self.videoLayout.setStretch(1, 1)  # videoWidget

        self.videoWidget.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )

        self._last_sync_ms = -10000

        self._resize_timer = QTimer(self)
        self._resize_timer.setSingleShot(True)
        self._resize_timer.setInterval(50)
        self._resize_timer.timeout.connect(self._fit_video_to_width)

        self.videoWidget.installEventFilter(self)
        self._fit_video_to_width()

        self.player = None
        self.audio = None
        self._init_multimedia()
        self._connect_signals()
        self._setup_shortcuts()
        self._apply_icons()

        self.gbChapters.setMinimumWidth(300)
        self.gbChapters.setMaximumWidth(420)
        self.chaptersLayout.setStretch(0, 0)  # lblChaptersTitle
        self.chaptersLayout.setStretch(1, 2)  # listChapters
        self.chaptersLayout.setStretch(2, 1)  # editChapterDesc
        self.editChapterDesc.setMinimumHeight(80)

        self.rootLayout.setStretch(0, 0)  # gbChapters
        self.rootLayout.setStretch(1, 1)  # gbVideo

        self.btnOpenFile.hide()
        self.lblVideoTitle.hide()

    def _init_multimedia(self):
        try:
            self.player = QMediaPlayer(self)
            self.audio = QAudioOutput(self)
            self.player.setAudioOutput(self.audio)
            self.player.setVideoOutput(self.videoWidget)
            self.player.positionChanged.connect(self._on_position)
            self.player.durationChanged.connect(self._on_duration)
            self.audio.setVolume(self.sliderVolume.value() / 100.0)

        except Exception:
            self.player = None
            self.audio = None

    def _fit_video_to_width(self):
        """Высота videoWidget = 16:9 от ширины. Не трогает размер, если не изменился."""
        w = self.videoWidget.width()
        if w <= 0:
            return

        new_h = int(w * 9 / 16)

        # ограничение по высоте gbVideo
        max_h = self.gbVideo.height() - 150
        if max_h > 0 and new_h > max_h:
            new_h = max_h

        # если высота уже такая - выходим (иначе мерцание)
        if self.videoWidget.height() == new_h:
            return

        # отключаем перерисовку на время ресайза
        self.videoWidget.setUpdatesEnabled(False)
        self.videoWidget.setFixedHeight(new_h)
        self.videoWidget.setUpdatesEnabled(True)

    def eventFilter(self, obj, event):
        """Пересчитывает высоту videoWidget с дебаунсом 50 мс."""
        if obj is self.videoWidget and event.type() in (
                QEvent.Type.Resize,
                QEvent.Type.Show,
        ):
            # дебаунс - пересчёт через 50 мс после последнего события
            self._resize_timer.start()
        return super().eventFilter(obj, event)

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

    def _connect_signals(self):
        self.btnClose.clicked.connect(self._on_back)
        # self.btnOpenFile.clicked.connect(self._on_open_file)
        self.listChapters.currentItemChanged.connect(self._on_chapter_changed)
        self.btnPlay.clicked.connect(self._on_play_pause)
        self.btnStop.clicked.connect(self._on_stop)
        self.sliderPosition.sliderMoved.connect(self._on_seek)
        self.sliderVolume.valueChanged.connect(self._on_volume)

    def on_enter(self):
        self._load_chapters()
        self._load_video_if_exists()

    def on_leave(self):
        """Останавливает воспроизведение при уходе со страницы."""
        if self.player is not None:
            self.player.pause()

    def refresh(self):
        """Вызывается при каждом открытии страницы."""
        self._load_chapters()
        self._load_video_if_exists()

    def _load_chapters(self):
        """Загружает главы. Если уже загружены - не трогает выделение."""
        if self.listChapters.count() > 0:
            return  # уже загружено - не пересоздаём

        self.listChapters.blockSignals(True)
        self.listChapters.clear()
        for row in self.db.list_video_chapters():
            item = QListWidgetItem(row["title"])
            item.setData(Qt.ItemDataRole.UserRole, row["timestamp_ms"])
            item.setData(Qt.ItemDataRole.UserRole + 1, row["description"] or "")
            self.listChapters.addItem(item)
        self.listChapters.setCurrentRow(0)
        self.listChapters.blockSignals(False)

        # обновляем описание вручную (сигналы заблокированы)
        self._update_chapter_desc(0)

    def _load_video_if_exists(self):
        """Загружает видео. Если уже загружено - не трогает."""
        if self.player is None:
            self.lblTime.setText("видео не найдено")
            return

        # если источник уже установлен — не перезагружаем
        if self.player.source().isValid():
            return

        path = _media_path()
        if os.path.isfile(path):
            self.player.setSource(QUrl.fromLocalFile(path))
            self.lblTime.setText("00:00 / 00:00")
        else:
            self.lblTime.setText("видео не найдено")

    # ============== главы ==============

    def _update_chapter_desc(self, row: int):
        """Обновляет поле описания главы."""
        item = self.listChapters.item(row)
        if item is None:
            self.editChapterDesc.clear()
            return
        desc = item.data(Qt.ItemDataRole.UserRole + 1)
        self.editChapterDesc.setPlainText(desc or "")

    def _on_chapter_changed(self, current, _prev=None):
        if current is None:
            return
        self._update_chapter_desc(self.listChapters.currentRow())
        if self.player is None:
            return

        ms = current.data(Qt.ItemDataRole.UserRole) or 0
        self.player.setPosition(int(ms))

        # клик пользователя — всегда запускаем
        self.player.play()

    def _sync_chapter_with_playback(self, ms: int):
        """Подсвечивает главу, соответствующую текущей позиции видео.

        Вызывается из _on_position при каждом изменении позиции.
        Блокирует сигналы listChapters, чтобы не запустить _on_chapter_changed
        (иначе рекурсивная перемотка).
        """
        if self.listChapters.count() == 0:
            return

        # ищем последнюю главу с timestamp_ms <= ms
        target_row = 0
        for i in range(self.listChapters.count()):
            ts = self.listChapters.item(i).data(Qt.ItemDataRole.UserRole) or 0
            if ts <= ms:
                target_row = i
            else:
                break

        # не трогаем, если уже выбрано
        if self.listChapters.currentRow() == target_row:
            return

        # переключаем без эмита currentItemChanged,
        # чтобы не запускать _on_chapter_changed (перемотку)
        self.listChapters.blockSignals(True)
        self.listChapters.setCurrentRow(target_row)
        self.listChapters.blockSignals(False)

        # но описание обновить надо - вручную
        self._update_chapter_desc(target_row)

    # ============== плеер ==============

    def _on_play_pause(self):
        if self.player is None:
            QMessageBox.information(
                self, "Плеер недоступен",
                "PyQt6.QtMultimedia не установлен или видео не найдено."
            )
            return
        if self.player.playbackState().name == "PlayingState":
            self.player.pause()
        else:
            self.player.play()

    def _on_stop(self):
        if self.player is None:
            return
        self.player.stop()

    def _on_seek(self, value: int):
        if self.player is None:
            return
        self.player.setPosition(value)

    def _on_position(self, ms: int):
        if not self.sliderPosition.isSliderDown():
            self.sliderPosition.setValue(ms)
        self._update_time_label(ms, self.player.duration())

        # синхронизация глав не чаще раза в секунду
        if abs(ms - self._last_sync_ms) >= 1000:
            self._last_sync_ms = ms
            self._sync_chapter_with_playback(ms)

    def _on_duration(self, duration: int):
        self.sliderPosition.setRange(0, duration)
        self._update_time_label(self.player.position(), duration)

    def _update_time_label(self, ms: int, total: int):
        self.lblTime.setText(
            f"{self._fmt(ms)} / {self._fmt(total)}"
        )

    @staticmethod
    def _fmt(ms: int) -> str:
        s = max(0, ms) // 1000
        return f"{s // 60:02d}:{s % 60:02d}"

    def _on_volume(self, value: int):
        if self.audio is not None:
            self.audio.setVolume(value / 100.0)

    def _seek(self, delta_ms: int):
        """Перемотка на delta_ms миллисекунд."""
        if self.player is None:
            return
        new_pos = max(0, min(
            self.player.duration(),
            self.player.position() + delta_ms
        ))
        self.player.setPosition(new_pos)

    def _seek_back(self):
        self._seek(-5000)

    def _seek_forward(self):
        self._seek(+5000)

    def _seek_to(self, ms: int):
        if self.player:
            self.player.setPosition(ms)

    def _seek_to_end(self):
        if self.player:
            self.player.setPosition(self.player.duration())

    def _change_volume(self, delta: int):
        """Меняет громкость на delta (в процентах)."""
        self.sliderVolume.setValue(
            max(0, min(100, self.sliderVolume.value() + delta))
        )

    def _toggle_mute(self):
        """Включает / выключает звук."""
        if self.audio is None:
            return
        self.audio.setMuted(not self.audio.isMuted())

    def _seek_to_percent(self, percent: int):
        """Перематывает видео на указанный процент длительности."""
        if self.player is None:
            return

        duration = self.player.duration()
        if duration <= 0:
            return  # видео ещё не загрузилось

        position = int(duration * percent / 100)
        self.player.setPosition(position)

    # ============== файл ==============

    def _on_open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Выбрать видео", "", "Видео (*.mp4 *.avi *.mkv *.mov)"
        )
        if not path or self.player is None:
            return
        self.player.setSource(QUrl.fromLocalFile(path))

    # ============== навигация ==============

    def _on_back(self):
        """Возвращает на страницу, откуда открыли видео."""
        window = self.window()
        if hasattr(window, "go_back_from_video"):
            window.go_back_from_video()
        else:
            if window.current_server_id:
                window.go_main(window.current_server_id)
            else:
                window.go_profile()

    # ============== клавиатура ==============

    def _setup_shortcuts(self):
        """Хоткеи плеера: работают при фокусе на любом виджете страницы."""
        bind_shortcuts(self, {
            "Space": self._on_play_pause,
            "Left": self._seek_back,
            "Right": self._seek_forward,
            "Shift+Left": lambda: self._seek(-30000),
            "Shift+Right": lambda: self._seek(+30000),
            "Up": lambda: self._change_volume(+5),
            "Down": lambda: self._change_volume(-5),
            "M": self._toggle_mute,
            "Home": lambda: self._seek_to(0),
            "End": self._seek_to_end,
            "Escape": self._on_back,
        }, WITH_CHILDREN)

        # 0–9 — переход к проценту видео
        for digit in range(10):
            bind_shortcut(
                self,
                str(digit),
                lambda _checked=False, d=digit: self._seek_to_percent(d * 10),
                WITH_CHILDREN,
            )