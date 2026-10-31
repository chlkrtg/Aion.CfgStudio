"""Фоновый слой сплэша: случайные команды из БД."""
import random

from PyQt6.QtCore import QEasingCurve, QPropertyAnimation, QTimer, Qt
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtWidgets import QGraphicsOpacityEffect, QLabel, QWidget

from logic.widgets.theme import TEXT_DIM, ACCENT

# Фиксированный набор команд (БД может ещё не быть при показе сплэша)
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
    """Одна команда, которая плавно появляется, пульсирует и исчезает."""

    def __init__(self, text: str, parent: QWidget):
        super().__init__(text, parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        # Золотой цвет (ACCENT) — как акцент приложения
        self.setStyleSheet(f"color: {ACCENT}; font-style: italic; background: transparent;")
        font = QFont("Consolas", 9)
        self.setFont(font)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Эффект прозрачности
        self._effect = QGraphicsOpacityEffect(self)
        self._effect.setOpacity(0.0)
        self.setGraphicsEffect(self._effect)

        # Анимация появления/исчезновения
        self._fade_anim = QPropertyAnimation(self._effect, b"opacity", self)
        self._fade_anim.setDuration(600)
        self._fade_anim.setEasingCurve(QEasingCurve.Type.InOutQuad)

        # Пульсация (перелив) — отдельная анимация
        self._pulse_anim = QPropertyAnimation(self._effect, b"opacity", self)
        self._pulse_anim.setDuration(1500)
        self._pulse_anim.setEasingCurve(QEasingCurve.Type.InOutSine)

    def fade_in(self, target_opacity: float, on_finished=None):
        self._fade_anim.stop()
        self._fade_anim.setStartValue(self._effect.opacity())
        self._fade_anim.setEndValue(target_opacity)
        if on_finished:
            self._fade_anim.finished.connect(on_finished)
        self._fade_anim.start()

        # После появления — запускаем пульсацию
        def _start_pulse():
            self._pulse_anim.stop()
            self._pulse_anim.setStartValue(target_opacity)
            self._pulse_anim.setEndValue(target_opacity * 0.5)
            self._pulse_anim.setLoopCount(-1)  # бесконечно
            # Туда-сюда
            self._pulse_anim.setDirection(
                QPropertyAnimation.Direction.Forward
            )
            self._pulse_anim.start()

        self._fade_anim.finished.connect(_start_pulse)

    def fade_out(self, on_finished=None):
        self._pulse_anim.stop()
        self._fade_anim.stop()
        self._fade_anim.setStartValue(self._effect.opacity())
        self._fade_anim.setEndValue(0.0)
        if on_finished:
            self._fade_anim.finished.connect(on_finished)
        self._fade_anim.start()


class SplashMatrix(QWidget):
    """Слой с плавающими командами на фоне сплэша."""

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self._active: list[_FloatingCommand] = []

        self._spawn_timer = QTimer(self)
        self._spawn_timer.setInterval(450)
        self._spawn_timer.timeout.connect(self._spawn)
        self._spawn_timer.start()

    def _spawn(self):
        if not SPLASH_COMMANDS:
            return
        if len(self._active) > 25:
            return

        text = random.choice(SPLASH_COMMANDS)
        lbl = _FloatingCommand(text, self)

        x = random.randint(0, max(0, self.width() - 180))
        y = random.randint(0, max(0, self.height() - 14))
        lbl.move(x, y)
        lbl.adjustSize()
        lbl.show()

        self._active.append(lbl)

        # Плавное появление до 0.15 (полупрозрачность)
        target_opacity = random.uniform(0.12, 0.17)
        lbl.fade_in(target_opacity)

        # Через 2–4 секунды — плавное исчезновение и удаление
        life_ms = random.randint(2000, 4000)
        QTimer.singleShot(
            life_ms,
            lambda l=lbl: self._fade_and_remove(l),
        )

    def _fade_and_remove(self, lbl: _FloatingCommand):
        def _remove():
            if lbl in self._active:
                self._active.remove(lbl)
            lbl.deleteLater()

        lbl.fade_out(on_finished=_remove)

    def stop(self):
        """Останавливает таймер и удаляет все команды."""
        self._spawn_timer.stop()
        for lbl in self._active:
            lbl.deleteLater()
        self._active.clear()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        for lbl in self._active:
            lbl.deleteLater()
        self._active.clear()