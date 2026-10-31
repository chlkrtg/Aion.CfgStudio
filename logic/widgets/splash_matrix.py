"""Фоновый слой сплэша: случайные команды из БД."""
import random

from PyQt6.QtCore import (
    QEasingCurve,
    QVariantAnimation,
    QTimer,
    Qt,
    pyqtSignal,
)
from PyQt6.QtGui import QColor, QFont, QPainter
from PyQt6.QtWidgets import QLabel, QWidget

from logic.widgets.theme import ACCENT


SPLASH_COMMANDS = [
    "e_beach", "e_decals", "e_flocks",
    "e_maxdistance_ratio_entities", "e_maxdistance_terrain",
    "e_particles_fullfx", "e_particles_max_count",
    "e_shadow_maps", "e_water_render_distance",
    "e_weather_fx_enable", "e_vegetation_wind",
    "e_stencil_shadows", "e_voxel_realtime_light_update",
    "g_maxfov", "g_maxfps", "g_2dDamage",
    "g_char_manager", "g_ggAuth",
    "r_resolution", "r_fov", "r_farclip",
    "sys_debug_enable", "sys_log_level",
    "ca_HairAnim", "ca_DisplayInfo",
    "d3d9_VS30", "d3d9_PS30",
    "s_sound_volume", "s_music_volume",
    "log_level", "log_console",
]


class _FloatingCommand(QLabel):
    """Одна команда: плавно появляется, пульсирует, исчезает."""

    finished = pyqtSignal(object)  # сигнал: «я готов к удалению»

    def __init__(self, text: str, parent: QWidget):
        super().__init__(text, parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setFont(QFont("Consolas", 9))
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._opacity = 0.0

        # --- Fade-in (только для появления) ---
        self._fade_in_anim = QVariantAnimation(self)
        self._fade_in_anim.setDuration(600)
        self._fade_in_anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self._fade_in_anim.valueChanged.connect(self._set_opacity)

        # --- Fade-out (только для исчезновения) ---
        self._fade_out_anim = QVariantAnimation(self)
        self._fade_out_anim.setDuration(600)
        self._fade_out_anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self._fade_out_anim.valueChanged.connect(self._set_opacity)

        # --- Пульсация ---
        self._pulse_anim = QVariantAnimation(self)
        self._pulse_anim.setDuration(1500)
        self._pulse_anim.setEasingCurve(QEasingCurve.Type.InOutSine)
        self._pulse_anim.setLoopCount(-1)
        self._pulse_anim.valueChanged.connect(self._set_opacity)

        # --- Таймер жизни (привязан к lbl) ---
        self._life_timer = QTimer(self)
        self._life_timer.setSingleShot(True)
        self._life_timer.timeout.connect(self._on_life_end)

    # ============ отрисовка ============

    def _set_opacity(self, value):
        self._opacity = float(value)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(self._opacity)
        painter.setPen(QColor(ACCENT))
        painter.setFont(self.font())
        painter.drawText(self.rect(), self.alignment(), self.text())

    # ============ жизненный цикл ============

    def start_life(self, life_ms: int):
        self._life_timer.start(life_ms)

    def _on_life_end(self):
        self.fade_out()

    def fade_in(self, target_opacity: float):
        self._fade_in_anim.stop()
        self._fade_in_anim.setStartValue(self._opacity)
        self._fade_in_anim.setEndValue(target_opacity)
        self._fade_in_anim.start()

        # после появления — пульсация (один раз)
        try:
            self._fade_in_anim.finished.disconnect()
        except TypeError:
            pass
        self._fade_in_anim.finished.connect(
            lambda: self._start_pulse(target_opacity)
        )

    def _start_pulse(self, target_opacity: float):
        self._pulse_anim.stop()
        self._pulse_anim.setStartValue(target_opacity)
        self._pulse_anim.setEndValue(target_opacity * 0.5)
        self._pulse_anim.start()

    def fade_out(self):
        # остановить всё
        self._life_timer.stop()
        self._pulse_anim.stop()
        self._fade_in_anim.stop()
        self._fade_out_anim.stop()

        # отключить все коннекты от fade-in (чтобы _start_pulse не сработал)
        try:
            self._fade_in_anim.finished.disconnect()
        except TypeError:
            pass

        self._fade_out_anim.setStartValue(self._opacity)
        self._fade_out_anim.setEndValue(0.0)
        self._fade_out_anim.finished.connect(self._on_faded_out)
        self._fade_out_anim.start()

    def _on_faded_out(self):
        """Fade-out завершён: сообщаем родителю и удаляемся."""
        try:
            self._fade_out_anim.finished.disconnect(self._on_faded_out)
        except TypeError:
            pass
        self.finished.emit(self)
        self.deleteLater()


class SplashMatrix(QWidget):
    """Слой с плавающими командами."""

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self._active: list[_FloatingCommand] = []

        self._spawn_timer = QTimer(self)
        self._spawn_timer.setInterval(450)
        self._spawn_timer.timeout.connect(self._spawn)
        self._spawn_timer.start()

    def _spawn(self):
        # чистим мёртвые (на всякий случай)
        self._active = [l for l in self._active if l.isVisible()]

        if not SPLASH_COMMANDS:
            return
        if len(self._active) >= 25:
            return

        text = random.choice(SPLASH_COMMANDS)
        lbl = _FloatingCommand(text, self)

        x = random.randint(0, max(0, self.width() - 180))
        y = random.randint(0, max(0, self.height() - 14))
        lbl.move(x, y)
        lbl.adjustSize()
        lbl.show()

        lbl.finished.connect(self._on_command_finished)
        self._active.append(lbl)

        target_opacity = random.uniform(0.12, 0.17)
        lbl.fade_in(target_opacity)

        # таймер жизни (привязан к lbl)
        lbl.start_life(random.randint(2000, 4000))

    def _on_command_finished(self, lbl: _FloatingCommand):
        if lbl in self._active:
            self._active.remove(lbl)

    def stop(self):
        self._spawn_timer.stop()
        for lbl in self._active:
            try:
                lbl._life_timer.stop()
                lbl._fade_in_anim.stop()
                lbl._fade_out_anim.stop()
                lbl._pulse_anim.stop()
            except RuntimeError:
                pass
            lbl.deleteLater()
        self._active.clear()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # НЕ вызываем stop() — просто корректируем позиции
        for lbl in self._active:
            x = min(lbl.x(), max(0, self.width() - lbl.width()))
            y = min(lbl.y(), max(0, self.height() - lbl.height()))
            lbl.move(x, y)