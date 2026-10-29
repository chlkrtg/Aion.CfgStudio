"""Полная сборка Aion.CfgStudio.

Шаги:
    1. Очистка проекта (build/, dist/, *.spec, __pycache__)
    2. Версия из Git (setuptools-scm)
    3. PyInstaller → dist/AionCfgStudio/
    4. Очистка ненужных DLL из dist/AionCfgStudio/_internal
    5. Inno Setup → installer/Output/AionCfgStudio_Setup_vX.Y.Z.exe

Использование:
    python build.py
"""
import subprocess
import sys
from pathlib import Path


BASE = Path(__file__).parent
PY = sys.executable

# Путь к ISCC.exe (Inno Setup Compiler).
# Если iscc в PATH — можно оставить "iscc".
# Если нет — укажи полный путь, например:
# ISCC = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
ISCC = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"

ISS_FILE = BASE / "installer" / "AionCfgStudio.iss"
PYINSTALLER_NAME = "AionCfgStudio"


def run(cmd, cwd=None):
    """Запускает команду и падает, если она вернула ненулевой код."""
    print(f"\n[BUILD] {' '.join(str(c) for c in cmd)}")
    subprocess.run(cmd, cwd=cwd or BASE, check=True)


def get_version() -> str:
    """Версия из Git-тега (setuptools-scm)."""
    try:
        result = subprocess.check_output(
            [PY, "-m", "setuptools_scm"],
            cwd=BASE, text=True,
        )
        return result.strip()
    except subprocess.CalledProcessError:
        print("[BUILD] setuptools-scm не смог определить версию, "
              "использую 0.0.0")
        return "0.0.0"


def clean_project():
    """Удаляет build/, dist/, *.spec, __pycache__."""
    import shutil

    for path in (BASE / "build", BASE / "dist"):
        if path.exists():
            print(f"[CLEAN] Удаляю {path}")
            shutil.rmtree(path, ignore_errors=True)

    for spec in BASE.glob("*.spec"):
        print(f"[CLEAN] Удаляю {spec}")
        spec.unlink()

    for pycache in BASE.rglob("__pycache__"):
        shutil.rmtree(pycache, ignore_errors=True)

    out = BASE / "installer" / "Output"
    if out.exists():
        print(f"[CLEAN] Удаляю {out}")
        shutil.rmtree(out, ignore_errors=True)


def build_exe():
    """Сборка .exe через PyInstaller."""
    run([
        "PyInstaller",
        "AionCfgStudio.spec",
        "--clean",
        "--noconfirm",
    ])


def clean_dist():
    """Очистка ненужных DLL из dist/AionCfgStudio/_internal."""
    script = BASE / "clean_build.py"
    if not script.exists():
        print(f"[BUILD] Пропуск clean_dist: {script} не найден")
        return
    run([PY, str(script)])


def build_installer(version: str):
    """Сборка установщика через Inno Setup."""
    if not ISS_FILE.exists():
        print(f"[BUILD] Ошибка: {ISS_FILE} не найден")
        sys.exit(1)

    # Inno Setup требует версию вида X.Y.Z.W (4 числа).
    # Из "1.2.dev44+gd4f8aa637.d20261028" берём только "1.2" и добавляем ".0.0"
    import re
    m = re.match(r"(\d+)\.(\d+)(?:\.(\d+))?", version)
    if m:
        major = m.group(1)
        minor = m.group(2)
        patch = m.group(3) or "0"
        clean_version = f"{major}.{minor}.{patch}.0"
    else:
        clean_version = "0.0.0.0"

    print(f"[BUILD] Версия для Inno: {clean_version}")
    run([ISCC, f"/DMyAppVersion={clean_version}", str(ISS_FILE)])

def main():
    print("=" * 60)
    print("Aion.CfgStudio — сборка")
    print("=" * 60)

    # 1. Версия
    version = get_version()
    print(f"\n[BUILD] Версия: {version}")

    # 2. PyInstaller
    build_exe()

    # 3. Очистка DLL из dist
    clean_dist()

    # 4. Inno Setup
    build_installer(version)


if __name__ == "__main__":
    main()