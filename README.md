# Aion.CfgStudio

Десктопное приложение для редактирования конфигурационных файлов клиента игры Aion. Написано на Python + PyQt6, использует SQLite, собирается в standalone `.exe`.

![Скриншот главного окна](docs/screenshots/main.png)

## Возможности

- Профили и серверы: несколько наборов конфигураций с описаниями и заметками.
- Импорт / экспорт `system.cfg` - с XOR-деобфускацией и обфускацией.
- Редактор 1100+ команд: фильтры по категории, режиму и поиску.
- История изменений: фиксируются только реально изменившиеся значения.
- Видео-руководство: встроенный плеер.

## Технологии

| **_Компонент_** | **_Технология_** |
|---|---|
| Язык | Python 3.12+ |
| GUI | PyQt6 |
| БД | SQLite |
| Сборка | PyInstaller (`--onedir`) |
| Установщик | Inno Setup 6 |
| Тема | qdarktheme |

## Установка

### Вариант 1 - готовая сборка

1. Скачай `AionCfgStudio_Setup_v1.0.exe` из [Releases](https://github.com/chlkrtg/Aion.CfgStudio/releases).
2. Запусти установщик.
3. Ярлык появится в меню "Пуск".

Требования: Windows 10/11.

### Вариант 2 - из исходников

```
git clone https://github.com/chlkrtg/Aion.CfgStudio.git
cd Aion.CfgStudio
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
## Для разработчиков

### Установка окружения

```bash
git clone https://github.com/chlkrtg/Aion.CfgStudio.git
cd Aion.CfgStudio
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
python main.py
```

### Видео-руководство

В репозитории видео **не хранится** (слишком большое). Оно поставляется **вместе с установщиком** из раздела [Releases](https://github.com/chlkrtg/Aion.CfgStudio/releases).

**Если вы собираете из исходников** - положите `tutorial.mp4` в папку `media/`. Без него приложение работает, но кнопка **F1** покажет "видео не найдено".

### Генерация озвучки

Скрипт `generate_voice.py` создаёт озвучку для видео-руководства через **Silero TTS v5_ru**.

**Требования:**
- Установленный `torch`, `soundfile`, `numpy` (входят в `requirements-dev.txt`).
- Файл модели `v5_ru.pt` в корне проекта.

**Скачать модель:**

```
https://models.silero.ai/models/tts/ru/v5_ru.pt
```

Положите `v5_ru.pt` рядом с `generate_voice.py`.

**Запуск:**

```bash
# все блоки, голос по умолчанию (aidar)
python generate_voice.py

# конкретный голос
python generate_voice.py --speaker xenia

# только один блок (для теста)
python generate_voice.py --only 01_title --speaker xenia

# список доступных голосов
python generate_voice.py --list
```

**Доступные голоса:** `aidar`, `baya`, `kseniya`, `xenia`, `eugene`.

**Результат:** файлы `voice/01_title.wav` … `voice/08_final.wav`.

**Дальше:**
1. Запишите экран (OBS, ShadowPlay).
2. Смонтируйте видео в Premiere Pro / DaVinci / CapCut.
3. Наложите `voice/*.wav` на видео.
4. Экспортируйте как `media/tutorial.mp4` (H.264, AAC, 1920×1080, 30 fps).
5. Обновите тайм-коды глав в `database/schema.sql` (таблица `VideoChapters`).

### Сборка `.exe`

```bash
pyinstaller AionCfgStudio.spec --clean --noconfirm
```

Результат - папка `dist/AionCfgStudio/` с `.exe` и `_internal/`.

**Почему `--onedir`, а не `--onefile`:**
Встроенный плеер использует `QMediaPlayer` и `QVideoWidget`, которым нужны плагины QtMultimedia. В режиме `--onefile` они распаковываются в `%TEMP%` и не всегда находятся вовремя. `--onedir` размещает плагины рядом с `.exe` - они находятся корректно.

**Проверка:** запустите `.exe` на чистой машине без Python.

### Установщик

```bash
ISCC.exe installer\AionCfgStudio.iss
```

Готовый установщик - `installer/Output/AionCfgStudio_Setup_v1.0.exe`.

## Структура проекта

```
Aion.CfgEditor/
├── main.py                     # точка входа
├── requirements.txt            # зависимости для запуска
├── requirements-dev.txt        # зависимости для разработки
├── AionCfgStudio.spec          # конфиг PyInstaller
├── README.md
├── LICENSE
├── .gitignore
├── logic/                      # логика приложения
│   ├── app_window.py           # главное окно + QStackedWidget
│   ├── base_page.py            # общий предок страниц
│   ├── constants.py            # ограничения длины, версия
│   ├── shortcuts.py            # хелперы для QShortcut
│   ├── context_menu.py         # построение контекстных меню
│   ├── page_profile.py         # страница профилей
│   ├── page_server.py          # страница серверов
│   ├── page_main.py            # дерево cfg-файлов
│   ├── page_editor.py          # редактор команд
│   └── page_video.py           # видео-руководство
├── ui/                         # формы Qt Designer
│   ├── command_editor.py/.ui
│   ├── main_window.py/.ui
│   ├── profile_select.py/.ui
│   ├── server_select.py/.ui
│   └── video_help.py/.ui
├── database/                   # работа с БД
│   ├── db_manager.py           # DBManager
│   ├── schema.sql              # схема
│   ├── seed_commands.sql
│   ├── seed_updates.sql
│   ├── seed_modes.sql
│   └── generate_seed.py        # скрипт генерации seed-файлов
├── parsers/                    # парсеры
│   └── cfg_crypto.py           # XOR-обработка
├── resources/                  # ресурсы
│   └── icons/
│       ├── aion.cfgstudio.ico
│       └── aion.cfgstudio_ico.png
├── media/                      # видео-руководство
│   └── tutorial.mp4            # не в Git - в Release
├── docs/                       # документация
│   └── screenshots/
│       ├── editor.png
│       ├── main.png
│       └── player.png
├── installer/                  # установщик
│   └── AionCfgStudio.iss       # Inno Setup
└── generate_voice.py           # генерация озвучки (dev)
```

## Горячие клавиши

| **_Клавиша_** | **_Действие_** |
|---|---|
| F1 | Видео-руководство |
| F2 | Переименовать |
| Delete | Удалить |
| Ctrl+N | Создать |
| Ctrl+O | Импорт cfg |
| Ctrl+S | Экспорт cfg / сохранить в редакторе |
| Ctrl+E | Открыть редактор |
| Ctrl+Q | Назад / выход |
| Space | Пауза (в плеере) |
| ← / → | Перемотка 5 сек |
| ↑ / ↓ | Громкость |
| 0–9 | Переход к % видео |
| Esc | Назад |

## Лицензия [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

MIT - см. [LICENSE](LICENSE).

## Благодарности

- [xan105/Aion-open-system-cfg-editor](https://github.com/xan105/Aion-open-system-cfg-editor) - алгоритм XOR-деобфускации.
- [Silero TTS](https://github.com/snakers4/silero-models) - озвучка видео-руководства.
- [qdarktheme](https://github.com/5yutan5/PyQtDarkTheme) - тёмная тема.

## Дисклеймер

Учебный проект. Не связан с NCSoft. Работает с локальными файлами конфигурации. Используется в образовательных целях.
