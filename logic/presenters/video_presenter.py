"""Presenter для страницы видео-руководства.

Логика: список глав, плеер, синхронизация глав с позицией,
перемотка, громкость.
"""
import os

from PyQt6.QtCore import QUrl, Qt
# from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput <- раскомментировать при возвращении плеера

from logic.presenters.base_presenter import BasePresenter


class VideoPresenter(BasePresenter):
    """Логика страницы видео."""

    def __init__(self, view, service):
        super().__init__(view)
        self.service = service  # CommandRepository

        self.player = None
        self.audio = None
        self._last_sync_ms = -10000

    # ============ инициализация плеера ============

    def init_player(self) -> bool:
        """Создаёт QMediaPlayer и QAudioOutput.

        Возвращает True при успехе, False если QtMultimedia недоступен.
        """
        try:
            from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput # убрать при возвращении плеера
            self.player = QMediaPlayer(self.view)
            self.audio = QAudioOutput(self.view)
            self.player.setAudioOutput(self.audio)
            self.player.setVideoOutput(self.view.videoWidget)

            self.player.positionChanged.connect(self.on_position)
            self.player.durationChanged.connect(self.on_duration)

            self.audio.setVolume(
                self.view.sliderVolume.value() / 100.0
            )
            return True
        except Exception:
            self.player = None
            self.audio = None
            return False

    # ============ жизненный цикл ============

    def on_enter(self):
        self.load_chapters()
        self.load_video_if_exists()

    def on_leave(self):
        if self.player is not None:
            self.player.pause()

    # ============ главы ============

    def load_chapters(self):
        """Загружает главы. Если уже загружены - не трогает."""
        view = self.view
        if view.listChapters.count() > 0:
            return

        view.listChapters.blockSignals(True)
        view.listChapters.clear()
        for row in self.service.video_chapters():
            item = view.make_chapter_item(
                row["title"],
                row["timestamp_ms"],
                row["description"] or "",
            )
            view.listChapters.addItem(item)
        view.listChapters.setCurrentRow(0)
        view.listChapters.blockSignals(False)

        self._update_chapter_desc(0)

    def _update_chapter_desc(self, row: int):
        view = self.view
        item = view.listChapters.item(row)
        if item is None:
            view.editChapterDesc.clear()
            return
        desc = item.data(Qt.ItemDataRole.UserRole + 1)
        view.editChapterDesc.setPlainText(desc or "")

    # ============ видео ============

    def load_video_if_exists(self):
        view = self.view
        if self.player is None:
            view.lblTime.setText("видео не найдено")
            return
        if self.player.source().isValid():
            return

        path = view.media_path()
        if os.path.isfile(path):
            self.player.setSource(QUrl.fromLocalFile(path))
            view.lblTime.setText("00:00 / 00:00")
        else:
            view.lblTime.setText("видео не найдено")

    # ============ обработка выбора главы ============

    def on_chapter_changed(self, current, _prev=None):
        """Пользователь кликнул по главе - перематываем и играем."""
        if current is None:
            return

        self._update_chapter_desc(self.view.listChapters.currentRow())

        if self.player is None:
            return

        ms = current.data(Qt.ItemDataRole.UserRole) or 0
        self.player.setPosition(int(ms))
        self.player.play()

    def sync_chapter_with_playback(self, ms: int):
        """Подсвечивает главу, соответствующую позиции видео.

        Блокирует сигналы, чтобы не запустить on_chapter_changed
        (иначе - рекурсивная перемотка).
        """
        view = self.view
        if view.listChapters.count() == 0:
            return

        target_row = 0
        for i in range(view.listChapters.count()):
            ts = view.listChapters.item(i).data(
                Qt.ItemDataRole.UserRole
            ) or 0
            if ts <= ms:
                target_row = i
            else:
                break

        if view.listChapters.currentRow() == target_row:
            return

        view.listChapters.blockSignals(True)
        view.listChapters.setCurrentRow(target_row)
        view.listChapters.blockSignals(False)

        self._update_chapter_desc(target_row)

    # ============ плеер ============

    def play_pause(self):
        if self.player is None:
            self.view.show_player_unavailable()
            return
        if self.player.playbackState().name == "PlayingState":
            self.player.pause()
        else:
            self.player.play()

    def stop(self):
        if self.player is not None:
            self.player.stop()

    def on_seek(self, value: int):
        """Пользователь тащит слайдер позиции."""
        if self.player is not None:
            self.player.setPosition(value)

    def on_position(self, ms: int):
        """Позиция изменилась - обновляем слайдер, время, главу."""
        view = self.view
        if not view.sliderPosition.isSliderDown():
            view.sliderPosition.setValue(ms)

        self._update_time_label(ms, self.player.duration())

        # синхронизация глав не чаще раза в секунду
        if abs(ms - self._last_sync_ms) >= 1000:
            self._last_sync_ms = ms
            self.sync_chapter_with_playback(ms)

    def on_duration(self, duration: int):
        self.view.sliderPosition.setRange(0, duration)
        self._update_time_label(self.player.position(), duration)

    def _update_time_label(self, ms: int, total: int):
        self.view.lblTime.setText(
            f"{self._fmt(ms)} / {self._fmt(total)}"
        )

    @staticmethod
    def _fmt(ms: int) -> str:
        s = max(0, ms) // 1000
        return f"{s // 60:02d}:{s % 60:02d}"

    def on_volume(self, value: int):
        if self.audio is not None:
            self.audio.setVolume(value / 100.0)

    # ============ перемотка / громкость ============

    def seek(self, delta_ms: int):
        """Перемотка на delta_ms миллисекунд."""
        if self.player is None:
            return
        new_pos = max(0, min(
            self.player.duration(),
            self.player.position() + delta_ms,
        ))
        self.player.setPosition(new_pos)

    def seek_back(self):
        self.seek(-5000)

    def seek_forward(self):
        self.seek(+5000)

    def seek_to(self, ms: int):
        if self.player:
            self.player.setPosition(ms)

    def seek_to_end(self):
        if self.player:
            self.player.setPosition(self.player.duration())

    def seek_to_percent(self, percent: int):
        """Перематывает на указанный процент длительности."""
        if self.player is None:
            return
        duration = self.player.duration()
        if duration <= 0:
            return
        self.player.setPosition(int(duration * percent / 100))

    def change_volume(self, delta: int):
        """Меняет громкость на delta (в процентах)."""
        self.view.sliderVolume.setValue(
            max(0, min(100, self.view.sliderVolume.value() + delta))
        )

    def toggle_mute(self):
        """Включает/выключает звук."""
        if self.audio is None:
            return
        self.audio.setMuted(not self.audio.isMuted())

    # ============ навигация ============

    def go_back(self):
        """Возвращает на страницу, откуда открыли видео."""
        window = self.view.window()
        if hasattr(window, "go_back_from_video"):
            window.go_back_from_video()
        else:
            if window.current_server_id:
                window.go_main(window.current_server_id)
            else:
                window.go_profile()