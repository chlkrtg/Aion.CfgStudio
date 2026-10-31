"""Сборка через Nuitka (standalone)."""
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent


def main():
    # Версия из setuptools-scm
    try:
        version = subprocess.check_output(
            [sys.executable, "-m", "setuptools_scm"],
            cwd=BASE, text=True,
        ).strip()
    except Exception:
        version = "0.0.0"
    print(f"[BUILD] Version: {version}")

    cmd = [
        sys.executable, "-m", "nuitka",
        "--standalone",
        "--enable-plugin=pyqt6",
        "--windows-disable-console",
        "--windows-icon-from-ico=resources/icons/aion.cfgstudio.ico",
        "--output-dir=dist_nuitka",
        "--output-filename=AionCfgStudio.exe",

        # Данные (SQL + иконки)
        "--include-data-dir=database=database",
        "--include-data-dir=resources=resources",

        # Секрет (обязательно!)
        "--include-module=logic.core.license_secret",

        # Исключения (из твоего .spec)
        "--nofollow-import-to=tkinter",
        "--nofollow-import-to=matplotlib",
        "--nofollow-import-to=numpy",
        "--nofollow-import-to=scipy",
        "--nofollow-import-to=pandas",
        "--nofollow-import-to=unittest",
        "--nofollow-import-to=pydoc",
        "--nofollow-import-to=pdb",
        "--nofollow-import-to=doctest",
        "--nofollow-import-to=PyQt6.QtWebEngineCore",
        "--nofollow-import-to=PyQt6.QtWebEngineWidgets",
        "--nofollow-import-to=PyQt6.QtMultimedia",
        "--nofollow-import-to=PyQt6.Qt3DCore",
        "--nofollow-import-to=PyQt6.QtCharts",
        "--nofollow-import-to=PyQt6.QtDataVisualization",
        "--nofollow-import-to=PyQt6.QtBluetooth",
        "--nofollow-import-to=PyQt6.QtNfc",
        "--nofollow-import-to=PyQt6.QtPositioning",
        "--nofollow-import-to=PyQt6.QtSerialPort",
        "--nofollow-import-to=PyQt6.QtSql",
        "--nofollow-import-to=PyQt6.QtTest",
        "--nofollow-import-to=PyQt6.QtDesigner",

        # Разрешаем Nuitka скачать MinGW (если MSVC нет)
        "--assume-yes-for-downloads",

        "main.py",
    ]

    print("[BUILD] Running Nuitka...")
    subprocess.run(cmd, cwd=BASE, check=True)
    print(f"[BUILD] Done: dist_nuitka/main.dist/AionCfgStudio.exe")


if __name__ == "__main__":
    main()