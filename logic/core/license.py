"""Система раннего доступа: HWID + HMAC + срок действия.
"""
import base64
import hashlib
import hmac
import time
import os

from logic.core.i18n import t

SECRET = b'\xcd\x87o~^\x81\x7f\xf5\xbav\xe5\xb7\x8d\xf8\x0f\xc2\xc2Uf\xc3Ic\xf8\x89l\x06O>~T=\x0b'

# ==================== HWM (High-Water Mark) ====================

def _sign_payload(payload: str) -> str:
    return hmac.new(SECRET, payload.encode(), hashlib.sha256).hexdigest()[:16]


def _hwm_path(app_dir: str) -> str:
    return os.path.join(app_dir, ".aion_hwm")


def _serialize_hwm(timestamp: int) -> str:
    payload = str(timestamp)
    return f"{payload}|{_sign_payload(payload)}"


def _parse_hwm(raw: str) -> int | None:
    try:
        payload, sig = raw.rsplit("|", 1)
        if not hmac.compare_digest(sig, _sign_payload(payload)):
            return None
        return int(payload)
    except (ValueError, AttributeError):
        return None


def load_hwm(settings_repo, app_dir: str) -> int:
    """Загружает HWM из БД и файла. Берёт максимум валидных значений."""
    values = []

    # 1. Из БД
    db_raw = settings_repo.get("license.hwm", "") or ""
    db_val = _parse_hwm(db_raw)
    if db_val is not None:
        values.append(db_val)

    # 2. Из файла
    path = _hwm_path(app_dir)
    try:
        with open(path, "r", encoding="utf-8") as f:
            file_raw = f.read().strip()
        file_val = _parse_hwm(file_raw)
        if file_val is not None:
            values.append(file_val)
    except OSError:
        pass

    return max(values) if values else 0


def save_hwm(settings_repo, app_dir: str, timestamp: int):
    """Сохраняет HWM в БД и файл (с подписью)."""
    raw = _serialize_hwm(timestamp)

    # 1. В БД
    settings_repo.set("license.hwm", raw)

    # 2. В файл
    path = _hwm_path(app_dir)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(raw)
    except OSError:
        pass


def check_clock_rollback(
    settings_repo, app_dir: str, tolerance: int = 86400
) -> bool:
    """Проверяет, не переведены ли часы назад.

    tolerance — допустимое расхождение в секундах (5 минут).
    Возвращает True, если всё ок, False — если часы назад.
    """
    now = int(time.time())
    hwm = load_hwm(settings_repo, app_dir)

    if hwm == 0:
        # Первый запуск — сохраняем и пускаем
        save_hwm(settings_repo, app_dir, now)
        return True

    if now + tolerance < hwm:
        # Часы переведены назад
        return False

    # Обновляем HWM, если сейчас больше
    if now > hwm:
        save_hwm(settings_repo, app_dir, now)

    return True

# ==================== HWID ====================

def get_hwid() -> str:
    """Возвращает MachineGuid Windows (уникален для установки Windows)."""
    try:
        import winreg

        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Cryptography",
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_64KEY,
        )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")
        winreg.CloseKey(key)
        return value
    except OSError:
        return "unknown"


# ==================== Генерация (для tools/) ====================

def make_code(hwid: str, days: int) -> str:
    """Создаёт код активации для HWID на N дней."""
    expires = int(time.time()) + days * 86400
    payload = f"{hwid}|{expires}"
    sig = hmac.new(SECRET, payload.encode(), hashlib.sha256).hexdigest()[:16]
    raw = f"{payload}|{sig}"
    return base64.urlsafe_b64encode(raw.encode()).decode()


# ==================== Проверка (для приложения) ====================

def validate_code(code: str, hwm: int = 0) -> tuple[bool, str]:
    """Проверяет код. Возвращает (ok, reason)."""
    code = code.strip()
    if not code:
        return False, t("license.empty")

    try:
        raw = base64.urlsafe_b64decode(code.encode()).decode()
        hwid, expires_s, sig = raw.rsplit("|", 2)
        expires = int(expires_s)
    except Exception:
        return False, t("license.invalid_format")

    payload = f"{hwid}|{expires}"
    expected = hmac.new(
        SECRET, payload.encode(), hashlib.sha256
    ).hexdigest()[:16]

    if not hmac.compare_digest(sig, expected):
        return False, t("license.invalid_signature")

    if hwid != get_hwid():
        return False, t("license.wrong_machine")

    # Проверка срока с учётом HWM (защита от перевода часов)
    now = max(time.time(), hwm)
    if now > expires:
        return False, t("license.expired")

    return True, ""


def get_expires(code: str) -> int | None:
    """Возвращает timestamp истечения кода (или None)."""
    try:
        raw = base64.urlsafe_b64decode(code.encode()).decode()
        _, expires_s, _ = raw.rsplit("|", 2)
        return int(expires_s)
    except Exception:
        return None