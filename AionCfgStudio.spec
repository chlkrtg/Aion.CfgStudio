# -*- mode: python ; coding: utf-8 -*-
"""
Сборка Aion.CfgStudio (PyInstaller --onedir).

Сборка:
    pyinstaller AionCfgStudio.spec --clean --noconfirm

Результат:
    dist/AionCfgStudio/AionCfgStudio.exe

Почему --onedir, а не --onefile:
    QtMultimedia не подгружает плагины из временной распаковки --onefile.
    --onedir кладёт плагины рядом с exe, и они находятся корректно.
"""

import os
import PyQt6

# Папка установленного PyQt6 (там лежат Qt6/plugins/multimedia)
PYQT6_DIR = os.path.dirname(PyQt6.__file__)

# Путь к multimedia-плагину Qt
MULTIMEDIA_PLUGIN_SRC = os.path.join(PYQT6_DIR, 'Qt6', 'plugins', 'multimedia')

# === Analysis ===

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        # формы Qt Designer
        ('ui', 'ui'),
        # schema.sql + seed-файлы
        ('database', 'database'),
        # video tutorial.mp4
        ('media', 'media'),
        # иконки и прочие ресурсы
        ('resources', 'resources'),
        # multimedia-плагин Qt - кладём по тому же пути,
        # по которому PyQt6 ищет плагины внутри бандла
        (MULTIMEDIA_PLUGIN_SRC, 'PyQt6/Qt6/plugins/multimedia'),
    ],
    hiddenimports=[
        'PyQt6.QtMultimedia',
        'PyQt6.QtMultimediaWidgets',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # лишние тяжёлые библиотеки - уменьшают размер
        'tkinter',
        'matplotlib',
        'numpy',
        # неиспользуемые модули Qt
        'PyQt6.QtWebEngineCore',
        'PyQt6.QtWebEngineWidgets',
        'PyQt6.QtQuick',
        'PyQt6.QtQml',
    ],
    noarchive=False,
)

# === PYZ ===

pyz = PYZ(a.pure)

# === EXE (лаунчер) ===

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,   # обязательно для --onedir
    name='AionCfgStudio',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,               # UPX ломает Qt DLL - не включать
    console=False,           # окно без консоли
    disable_windowed_traceback=False,
    icon='resources/icons/aion.cfgstudio.ico',
)

# === COLLECT (собирает всё в dist/AionCfgStudio/) ===

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    name='AionCfgStudio',
)