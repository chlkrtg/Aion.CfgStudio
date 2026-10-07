"""Удаляет ненужные файлы из dist/ после PyInstaller.

Запуск ПОСЛЕ pyinstaller, ПЕРЕД Inno Setup:
    python clean_build.py

⚠️ После удаления запусти .exe и проверь, что всё работает.
"""
import shutil
from pathlib import Path


DIST = Path("dist/AionCfgStudio/_internal")


# === ПРИОРИТЕТ 1 точно безопасно ===

DIR_TARGETS = [
    "PyQt6/Qt6/qml",
    "PyQt6/Qt6/translations",
    "PyQt6/Qt6/plugins/networkinformation",
    "PyQt6/Qt6/plugins/tls",
    "PyQt6/Qt6/plugins/generic",
    "PyQt6/Qt6/plugins/qmltooling",
    "PyQt6/Qt6/plugins/assetimporters",
    "PyQt6/Qt6/plugins/sceneparsers",
    "PyQt6/Qt6/plugins/renderers",
    "PyQt6/Qt6/plugins/geometryloaders",
    "PyQt6/Qt6/plugins/position",
    "PyQt6/Qt6/plugins/multimedia",      # плеер скрыт
]

FILE_TARGETS = [
    "PyQt6/Qt6/bin/opengl32sw.dll",
    "PyQt6/Qt6/bin/avcodec-61.dll",
    "PyQt6/Qt6/bin/avformat-61.dll",
    "PyQt6/Qt6/bin/avutil-59.dll",
    "PyQt6/Qt6/bin/Qt6Pdf.dll",
    "PyQt6/Qt6/bin/Qt6Multimedia.dll",   # плеер скрыт
    "PyQt6/Qt6/bin/Qt6Network.dll",      # если нет сети
    "PyQt6/Qt6/bin/libcrypto-3.dll",     # если нет HTTPS
    "PyQt6/Qt6/bin/libssl-3.dll",
]


def main():
    if not DIST.exists():
        print(f"Не найдено: {DIST}")
        return

    total = 0

    for target in DIR_TARGETS:
        path = DIST / target
        if not path.exists():
            continue
        size = sum(
            f.stat().st_size for f in path.rglob("*") if f.is_file()
        )
        shutil.rmtree(path)
        total += size
        print(f"[DIR]  {target}  ({size / 1024 / 1024:.1f} МБ)")

    for target in FILE_TARGETS:
        path = DIST / target
        if not path.exists():
            continue
        size = path.stat().st_size
        path.unlink()
        total += size
        print(f"[FILE] {target}  ({size / 1024 / 1024:.1f} МБ)")

    print(f"\nИтого освобождено: {total / 1024 / 1024:.1f} МБ")


if __name__ == "__main__":
    main()