# -*- mode: python ; coding: utf-8 -*-
"""
Сборка Aion.CfgStudio (PyInstaller --onedir).

Сборка:
    pyinstaller AionCfgStudio.spec --clean --noconfirm
"""

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ui', 'ui'),
        ('database', 'database'),
        ('resources', 'resources'),
    ],
    hiddenimports=[
        'sqlite3',   # ← ЯВНО, чтобы PyInstaller точно включил
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Python-хлам
        'tkinter', 'matplotlib', 'numpy', 'scipy', 'pandas',
        'unittest', 'pydoc', 'pdb', 'doctest', 'test',
        'distutils', 'setuptools', 'pip', 'wheel',
        # НЕ исключать: sqlite3, os, sys, pathlib

        # PyQt6 — визуальные модули
        'PyQt6.QtWebEngineCore',
        'PyQt6.QtWebEngineWidgets',
        'PyQt6.QtWebEngineQuick',
        'PyQt6.QtWebChannel',
        'PyQt6.QtWebSockets',
        'PyQt6.QtQuick',
        'PyQt6.QtQuick3D',
        'PyQt6.QtQuickWidgets',
        'PyQt6.QtQml',

        # PyQt6 — 3D и графики
        'PyQt6.Qt3DCore',
        'PyQt6.Qt3DRender',
        'PyQt6.Qt3DInput',
        'PyQt6.Qt3DLogic',
        'PyQt6.Qt3DAnimation',
        'PyQt6.Qt3DExtras',
        'PyQt6.QtCharts',
        'PyQt6.QtDataVisualization',
        'PyQt6.QtGraphs',

        # PyQt6 — устройства
        'PyQt6.QtBluetooth',
        'PyQt6.QtNfc',
        'PyQt6.QtPositioning',
        'PyQt6.QtLocation',
        'PyQt6.QtSensors',
        'PyQt6.QtSerialPort',

        # PyQt6 — прочее
        'PyQt6.QtSql',
        'PyQt6.QtTest',
        'PyQt6.QtDesigner',
        'PyQt6.QtHelp',
        'PyQt6.QtPdf',
        'PyQt6.QtPdfWidgets',
        'PyQt6.QtNetworkAuth',
        'PyQt6.QtRemoteObjects',
        'PyQt6.QtScxml',
        'PyQt6.QtStateMachine',
        'PyQt6.QtTextToSpeech',
        'PyQt6.QtOpenGL',
        'PyQt6.QtOpenGLWidgets',
        # НЕ исключать PyQt6.QtSvg, если иконки .svg
    ],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AionCfgStudio',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    icon='resources/icons/aion.cfgstudio.ico',
    version='version_info.txt'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    name='AionCfgStudio',
)