"""Простейшая локализация: словарь + t().

Уровень 1: без Qt Linguist, без .ts/.qm.
Строки держим в STRINGS, текущий язык - в CURRENT.
"""

CURRENT = "ru"

STRINGS = {
    "ru": {
        # ============ МЕНЮ (глобальное) ============
        "menu.file":         "Файл",
        "menu.settings":     "Настройки",
        "menu.help":         "Помощь",
        "menu.shortcuts":    "Горячие клавиши...",
        "menu.lang":         "Язык",
        "menu.lang.ru":      "Русский",
        "menu.lang.en":      "English",

        # ============ ПРОФИЛЬ ============
        "profile.window_title":  "Aion.CfgStudio — Выбор профиля",
        "profile.lbl_title":     "Выберите профиль",
        "profile.lbl_profiles":  "Профили",
        "profile.lbl_details":   "Информация",
        "profile.lbl_none":      "— профиль не выбран —",
        "profile.lbl_selected":  "Выбранный профиль: {name}",
        "profile.desc_placeholder": "Сохраняется автоматически (до {n} символов)...",
        "profile.stats":         "Серверов: {s} | Конфигураций: {c}",
        "profile.btn_new":       "Новый",
        "profile.btn_rename":    "Переименовать",
        "profile.btn_delete":    "Удалить",
        "profile.btn_enter":     "Войти",
        "profile.btn_video":     "Видео-руководство",
        "profile.btn_cancel":    "Выход",
        "profile.dialog.new.title":      "Новый профиль",
        "profile.dialog.new.label":      "Имя профиля",
        "profile.dialog.rename.title":   "Переименовать профиль",
        "profile.dialog.rename.label":   "Новое имя",
        "profile.dialog.dup.title":      "Дублировать профиль",
        "profile.dialog.dup.label":      "Имя нового профиля",
        "profile.dialog.delete.title":   "Удалить",
        "profile.confirm.delete":        "Удалить профиль «{name}» со всем содержимым?\n\n"
                                         "Будет удалено: серверов — {s}, конфигураций — {c}.",
        "profile.error.empty":           "Имя не может быть пустым.",
        "profile.error.too_long":        "Имя слишком длинное (макс. {n}).",
        "profile.error.exists":          "Профиль «{name}» уже существует.",
        "profile.error.not_found":       "Профиль не найден.",
        "profile.error.save_desc":       "Не удалось сохранить описание профиля:\n{exc}",
        "profile.copy_suffix": "(копия)",

        # ============ СЕРВЕР ============
        "server.window_title":   "Aion.CfgStudio — Выбор сервера",
        "server.title":          "Профиль: {name} / Выберите сервер",
        "server.lbl_servers":    "Серверы",
        "server.lbl_details":    "Информация",
        "server.lbl_none":       "— сервер не выбран —",
        "server.lbl_region":     "Регион:",
        "server.lbl_configs":    "Конфигураций:",
        "server.btn_new":        "Новый",
        "server.btn_rename":     "Переименовать",
        "server.btn_delete":     "Удалить",
        "server.btn_enter":      "Войти",
        "server.btn_video":      "Видео-руководство",
        "server.btn_back":       "← Назад к профилям",
        "server.lbl_selected":   "Выбранный сервер: {name}",
        "server.note_placeholder": "Сохраняется автоматически (до {n} символов)...",
        "server.dialog.new.title":      "Новый сервер",
        "server.dialog.new.label":      "Имя сервера",
        "server.dialog.rename.title":   "Переименовать сервер",
        "server.dialog.rename.label":   "Новое имя",
        "server.dialog.dup.title":      "Дублировать сервер",
        "server.dialog.dup.label":      "Имя нового сервера",
        "server.dialog.delete.title":   "Удалить",
        "server.dialog.enter.title":    "Вход",
        "server.confirm.delete":        "Удалить сервер «{name}» со всеми cfg?\n\n"
                                        "Будет удалено: конфигураций — {c}.",
        "server.error.empty":           "Имя не может быть пустым.",
        "server.error.too_long":        "Имя слишком длинное (макс. {n}).",
        "server.error.exists":          "Сервер «{name}» уже существует в этом профиле.",
        "server.error.not_found":       "Сервер не найден.",
        "server.error.save_note":       "Не удалось сохранить заметку:\n{exc}",
        "server.copy_suffix":           "(копия)",
        "server.lbl_export_path": "Экспорт по умолчанию:",
        "server.export_path_placeholder": "Путь не задан",
        "server.btn_browse": "Обзор...",
        "server.dialog.export_path.title": "Выберите папку сервера",
        "server.error.export_path_invalid": "Папка не найдена: {path}",
        "server.btn_clear": "Очистить",

        # ============ CFG ============
        "main.lbl_tree_title":   "Конфигурации",
        "main.lbl_preview_title": "Предпросмотр",
        "main.lbl_preview_none": "— файл не выбран —",
        "main.col_name":         "Название",
        "main.col_modified":     "Изменён",
        "main.filter_placeholder": "Поиск конфигурации...",
        "main.btn_new":          "Новый CFG",
        "main.btn_import":       "Импорт...",
        "main.btn_export":       "Экспорт...",
        "main.btn_rename":       "Переименовать",
        "main.btn_delete":       "Удалить",
        "main.btn_save":         "Сохранить",
        "main.btn_revert":       "Отменить",
        "main.btn_open_editor":  "Открыть редактор",
        "main.btn_show_logs":    "История изменений",
        "main.action_new_config":     "Новый CFG",
        "main.action_import_cfg":     "Импорт CFG...",
        "main.action_export_cfg":     "Экспорт CFG...",
        "main.action_change_profile": "Сменить профиль...",
        "main.action_change_server":  "Сменить сервер...",
        "main.action_video_help":     "Видео-руководство",
        "main.action_about":          "О программе",
        "main.dialog.import.title":     "Импорт cfg",
        "main.dialog.import.label":     "Имя",
        "main.dialog.export.format":    "Формат экспорта",
        "main.dialog.export.label":     "Выберите формат:",
        "main.dialog.export.encrypted": "Зашифрованный (для игры)",
        "main.dialog.export.plain":     "Plain-текст (для чтения)",
        "main.dialog.rename.title":     "Переименовать cfg",
        "main.dialog.rename.label":     "Новое имя",
        "main.dialog.dup.title":        "Дублировать cfg",
        "main.dialog.dup.label":        "Имя нового файла",
        "main.dialog.delete.title":     "Удалить",
        "main.dialog.logs.title":       "История",
        "main.dialog.export.filename_title": "Экспорт cfg",
        "main.dialog.import.filename_title": "Импорт cfg",

        "main.error.no_selection":      "Не выбран конфигурационный файл.",
        "main.error.read":              "Ошибка чтения",
        "main.error.write":             "Ошибка записи",

        "main.confirm.delete":          "Удалить cfg «{name}»?",
        "main.confirm.clear":           "Вы уверены, что хотите удалить всё содержимое cfg?",
        "main.info.exported":           "Сохранено в {path}",
        "main.info.done":               "Готово",
        "main.info.saved":              "Конфигурация сохранена.",
        "main.info.saved_with_details": "Конфигурация сохранена.\n\n{details}",
        "main.info.unknown_commands":   "Неизвестных команд (нет в БД): {n}",
        "main.info.duplicates":         "Дубликатов удалено: {n}",
        "main.info.no_logs":            "Изменений нет для файла «{name}».",
        "main.copy_suffix":             "(копия)",
        "main.dialog.clear.title":      "Очистить cfg?",

        "main.search": "Поиск:",
        "main.search.placeholder": "Введите текст...",
                "legend.title": "Справка по предпросмотру",
        "legend.header": "Цвета в предпросмотре",
        "legend.btn_close": "Понятно",

        "legend.color.green": "Зелёный — известные команды",
        "legend.color.gray": "Серый — неизвестные команды",
        "legend.color.yellow": "Жёлтый — дубликаты (будут удалены)",
        "legend.color.orange": "Оранжевый — сервер задаёт значение (SystemCfgLocal.cfg)",
        "legend.color.red": "Красный — синтаксические ошибки",

        "legend.search.header": "Поиск:",
        "legend.search.open": "— открыть строку поиска",
        "legend.search.hint": "Для перехода к следующему совпадению жмите Enter или ↓",

        "config.error.empty_name":      "Имя файла не может быть пустым.",
        "config.error.too_long_name":   "Имя слишком длинное (макс. {n}).",
        "config.error.not_found":       "Конфиг не найден.",
        "config.error.cannot_unlock": (
            "Не удалось снять атрибут «Только чтение» с файла:\n{path}\n\n"
            "Закройте игру (если она запущена) или запустите приложение "
            "от имени администратора."
        ),

        # ================= ЛОГИ ===================
        "logs.type.unknown":     "(неизвестная)",
        "logs.type.duplicate":   "(дубль)",
        "logs.value.removed":    "(удалено)",
        "logs.value.dup_removed": "(удалён)",
        "logs.window_title":       "История изменений — {name}",
        "logs.window_title_short": "История изменений",
        "logs.search_placeholder": "Поиск по команде / дате / старому / новому состоянию...",
        "logs.col_date":           "Дата",
        "logs.col_command":        "Команда",
        "logs.col_old":            "Было",
        "logs.col_new":            "Стало",
        "logs.btn_close":          "Закрыть",

        # ============ РЕДАКТОР КОМАНД ============
        "editor.window_title":   "Aion.CfgStudio — Редактор конфигурации",
        "editor.lbl_file":       "Файл: {name}",
        "editor.lbl_file_new":   "Файл: (новый)",
        "editor.lbl_file_none":  "Файл: —",
        "editor.lbl_mode":       "Режим:",
        "editor.mode.simple":    "Простые",
        "editor.mode.advanced":  "Расширенные",
        "editor.mode.all":       "Все (включая отладку)",
        "editor.search_placeholder": "Поиск команды...",
        "editor.btn_expand":     "Развернуть всё",
        "editor.btn_collapse":   "Свернуть всё",
        "editor.lbl_prefixes_title": "Категории команд",
        "editor.lbl_prefix_info":    "Выберите категорию для фильтрации",
        "editor.prefix_all":     "Все команды",
        "editor.col_use":        "Исп.",
        "editor.col_command":    "Команда",
        "editor.col_value":      "Значение",
        "editor.col_default":    "Дефолт",
        "editor.col_description": "Описание",
        "editor.btn_reset_all":  "Сбросить всё к стандартным",
        "editor.btn_cancel":     "Отмена",
        "editor.btn_apply":      "Применить",

        "editor.dialog.unsaved.title": "Несохранённые изменения",
        "editor.dialog.unsaved.text":  "В превью есть несохранённые правки.\n"
                                       "Сохранить перед выходом?",

        "editor.dialog.new.title":     "Несохранённый конфиг",
        "editor.dialog.new.text":      "Вы отметили команды, но не сохранили конфиг.\n"
                                      "Сохранить как system.cfg перед выходом?",
        "editor.dialog.save.title":    "Сохранить?",
        "editor.dialog.save.text":     "Конфигурация сохранена.",

        "editor.info.nothing":         "Нечего сохранять",
        "editor.info.nothing.text":    "Не отмечено ни одной команды.",
        "editor.error.save":           "Ошибка сохранения",
        "editor.error.save.text":      "Не удалось сохранить конфигурацию.",
        "editor.info.done":            "Готово",

        "editor.error.server_required": "server_id не задан для нового cfg.",
        "editor.error.no_config_service": "EditorService: config_service не задан, "
                                          "нельзя создать новый cfg.",

        "editor.btn_make_defaults":      "Сделать стандартными",
        "editor.make_defaults.title":    "Сделать стандартными?",
        "editor.make_defaults.text":     "Сделать значения {n} отмеченных команд "
                                         "стандартными?\n\n"
                                         "Это затронет все будущие cfg. "
                                         "Продолжить?",
        "editor.make_defaults.done":     "Готово. Стандартными стали значения "
                                         "{n} команд.",

        "editor.count.command.one":   "команда",
        "editor.count.command.few":   "команды",
        "editor.count.command.many":  "команд",

        "editor.reset_dialog.title":      "Сбросить к стандартным",
        "editor.reset_dialog.text":       "Будут затронуты <b>{n}</b> команд:<br>"
                                  "• видимые сейчас (префикс + поиск)<br>"
                                  "• у которых есть стандартное значение"
                                  "<br><br>"
                                  "Что сбросить?<br>"
                                  "• <b>Только значения</b> — оставить выбор, "
                                  "подставить стандартные значения<br>"
                                  "• <b>Значения и выбор</b> — отметить "
                                  "команды со стандартным значением и "
                                  "подставить дефолты",

        "editor.reset_dialog.btn_values": "Только значения",
        "editor.reset_dialog.btn_all":    "Значения и выбор",
        "editor.reset_dialog.nothing":    "Нет видимых команд со стандартным "
                                          "значением.",
        "editor.reset_dialog.done":       "Готово. Сброшено команд: {n}.",
        "editor.tooltip.overridden": (
            "Сервер задаёт это значение: {value}\n"
            "Ваши правки будут проигнорированы."
        ),

        # ============ РЕДАКТОР ХОТКЕЕВ ============
        "shortcuts.window_title":    "Горячие клавиши",
        "shortcuts.lbl_hint":        "Двойной клик по строке или кнопка «Изменить...» — назначить клавишу. Конфликты запрещены: сначала освободите занятую клавишу.",
        "shortcuts.col_action":      "Действие",
        "shortcuts.col_key":         "Клавиша",
        "shortcuts.col_default":     "Дефолт",
        "shortcuts.btn_change":      "Изменить...",
        "shortcuts.btn_reset":       "Сбросить",
        "shortcuts.btn_reset_all":   "Сбросить всё",
        "shortcuts.btn_close":       "Закрыть",
        "shortcuts.section.global":  "Глобальные",
        "shortcuts.section.profile": "Профили",
        "shortcuts.section.server":  "Серверы",
        "shortcuts.section.main":    "Cfg-файлы",
        "shortcuts.section.editor":  "Редактор",
        "shortcuts.capture.title":   "Назначить клавишу",
        "shortcuts.capture.action":  "Действие: {title}",
        "shortcuts.capture.hint":    "Нажмите нужную клавишу или комбинацию.\nEsc — отмена.",
        "shortcuts.capture.preview_empty": "—",

        # ============ ДИАЛОГИ ============
        "dialog.conflict_title":     "Конфликт",
        "dialog.reset_all_title":    "Сбросить все хоткеи?",
        "dialog.reset_all_text":     "Все переназначенные клавиши вернутся к значениям по умолчанию. Продолжить?",
        "dialog.about_title":        "О программе",
        "dialog.about_text":         "Aion.CfgStudio v{version}  by @chealkrtengghnle\n\n"
                                     "Редактор конфигурационного файла system.cfg для Aion.",

        # ============ КОНТЕКСТНЫЕ МЕНЮ ============
        "ctx.enter":         "Войти",
        "ctx.duplicate":     "Дублировать",
        "ctx.rename":        "Переименовать",
        "ctx.delete":        "Удалить",
        "ctx.edit":          "Редактировать",
        "ctx.export":        "Экспортировать",

        # ============ ХОТКЕИ ============
        "action.global.video":         "Видео-руководство",
        "action.profile.enter":        "Войти в профиль",
        "action.profile.create":       "Новый профиль",
        "action.profile.rename":       "Переименовать профиль",
        "action.profile.delete":       "Удалить профиль",
        "action.profile.quit":         "Закрыть приложение",
        "action.server.enter":         "Войти в сервер",
        "action.server.create":        "Новый сервер",
        "action.server.rename":        "Переименовать сервер",
        "action.server.delete":        "Удалить сервер",
        "action.server.quit":          "Назад к профилям",
        "action.main.open":            "Открыть редактор",
        "action.main.create":          "Новый cfg",
        "action.main.import":          "Импорт cfg",
        "action.main.export":          "Экспорт cfg",
        "action.main.rename":          "Переименовать cfg",
        "action.main.delete":          "Удалить cfg",
        "action.main.save":            "Сохранить изменения (предпросмотр)",
        "action.main.quit":            "Назад к серверам",
        "action.main.cancelandquit":   "Отменить и выйти",
        "action.main.find":            "Поиск в превью",
        "shortcut.conflict": "Клавиша «{key}» уже занята действием «{title}».",

        # ================= ДИАЛОГИ ==============
        "dialog.input_hint":   "{label} (макс. {n}):",
        "dialog.error_title":  "Ошибка",

        # ============= SPLASH =================
        "splash.loading": "Загрузка компонентов...",

        # ============== ДИАЛОГИ ================
        "dialog.yes":     "Да",
        "dialog.no":      "Нет",
        "dialog.cancel":  "Отмена",
        "dialog.ok":      "ОК",

        # ============== ХЕЛПЕРЫ ================
        "empty.profiles":   "Нет профилей.\nНажмите «Новый», чтобы создать.",
        "empty.servers":    "Нет серверов.\nНажмите «Новый», чтобы создать.",
        "empty.configs":    "Нет конфигураций.\nНажмите «Новый CFG», чтобы создать.",
        "empty.preview":    "Выберите конфигурацию для предпросмотра.",
    },

    "en": {
        # ============ МЕНЮ ============
        "menu.file":         "File",
        "menu.settings":     "Settings",
        "menu.help":         "Help",
        "menu.shortcuts":    "Hotkeys...",
        "menu.lang":         "Language",
        "menu.lang.ru":      "Русский",
        "menu.lang.en":      "English",

        # ============ PROFILE ============
        "profile.window_title":  "Aion.CfgStudio — Profile selection",
        "profile.lbl_title":     "Select profile",
        "profile.lbl_profiles":  "Profiles",
        "profile.lbl_details":   "Info",
        "profile.lbl_none":      "— no profile selected —",
        "profile.lbl_selected":  "Selected profile: {name}",
        "profile.desc_placeholder": "Auto-saved (up to {n} characters)...",
        "profile.stats":         "Servers: {s} | Configs: {c}",
        "profile.btn_new":       "New",
        "profile.btn_rename":    "Rename",
        "profile.btn_delete":    "Delete",
        "profile.btn_enter":     "Enter",
        "profile.btn_video":     "Video guide",
        "profile.btn_cancel":    "Exit",
        "profile.dialog.new.title":      "New profile",
        "profile.dialog.new.label":      "Profile name",
        "profile.dialog.rename.title":   "Rename profile",
        "profile.dialog.rename.label":   "New name",
        "profile.dialog.dup.title":      "Duplicate profile",
        "profile.dialog.dup.label":      "New profile name",
        "profile.dialog.delete.title":   "Delete",
        "profile.confirm.delete":        "Delete profile «{name}» with all content?\n\n"
                                         "Will be deleted: servers — {s}, configs — {c}.",
        "profile.error.empty":           "Name cannot be empty.",
        "profile.error.too_long":        "Name is too long (max {n}).",
        "profile.error.exists":          "Profile «{name}» already exists.",
        "profile.error.not_found":       "Profile not found.",
        "profile.error.save_desc":       "Failed to save profile description:\n{exc}",
        "profile.copy_suffix": "(copy)",

        # ============ SERVER ============
        "server.window_title":   "Aion.CfgStudio — Server selection",
        "server.title":          "Profile: {name} / Select server",
        "server.lbl_servers":    "Servers",
        "server.lbl_details":    "Info",
        "server.lbl_none":       "— no server selected —",
        "server.lbl_region":     "Region:",
        "server.lbl_configs":    "Configs:",
        "server.btn_new":        "New",
        "server.btn_rename":     "Rename",
        "server.btn_delete":     "Delete",
        "server.btn_enter":      "Enter",
        "server.btn_video":      "Video guide",
        "server.btn_back":       "← Back to profiles",
        "server.lbl_selected":   "Selected server: {name}",
        "server.note_placeholder": "Auto-saved (up to {n} characters)...",
        "server.dialog.new.title":      "New server",
        "server.dialog.new.label":      "Server name",
        "server.dialog.rename.title":   "Rename server",
        "server.dialog.rename.label":   "New name",
        "server.dialog.dup.title":      "Duplicate server",
        "server.dialog.dup.label":      "New server name",
        "server.dialog.delete.title":   "Delete",
        "server.dialog.enter.title":    "Enter",
        "server.confirm.delete":        "Delete server «{name}» with all configs?\n\n"
                                        "Will be deleted: configs — {c}.",
        "server.error.empty":           "Name cannot be empty.",
        "server.error.too_long":        "Name is too long (max {n}).",
        "server.error.exists":          "Server «{name}» already exists in this profile.",
        "server.error.not_found":       "Server not found.",
        "server.error.save_note":       "Failed to save note:\n{exc}",
        "server.copy_suffix":           "(copy)",
        "server.lbl_export_path": "Default export:",
        "server.export_path_placeholder": "Path not set",
        "server.btn_browse": "Browse...",
        "server.dialog.export_path.title": "Select server folder",
        "server.error.export_path_invalid": "Folder not found: {path}",
        "server.btn_clear": "Clear",

        # ============ CFG ============
        "main.lbl_tree_title":   "Configurations",
        "main.lbl_preview_title": "Preview",
        "main.lbl_preview_none": "— no file selected —",
        "main.col_name":         "Name",
        "main.col_modified":     "Modified",
        "main.filter_placeholder": "Search configuration...",
        "main.btn_new":          "New CFG",
        "main.btn_import":       "Import...",
        "main.btn_export":       "Export...",
        "main.btn_rename":       "Rename",
        "main.btn_delete":       "Delete",
        "main.btn_save":         "Save",
        "main.btn_revert":       "Revert",
        "main.btn_open_editor":  "Open editor",
        "main.btn_show_logs":    "Change history",
        "main.action_new_config":     "New CFG",
        "main.action_import_cfg":     "Import CFG...",
        "main.action_export_cfg":     "Export CFG...",
        "main.action_change_profile": "Change profile...",
        "main.action_change_server":  "Change server...",
        "main.action_video_help":     "Video guide",
        "main.action_about":          "About",
        "main.dialog.import.title":     "Import cfg",
        "main.dialog.import.label":     "Name",
        "main.dialog.export.format":    "Export format",
        "main.dialog.export.label":     "Choose format:",
        "main.dialog.export.encrypted": "Encrypted (for the game)",
        "main.dialog.export.plain":     "Plain text (for reading)",
        "main.dialog.rename.title":     "Rename cfg",
        "main.dialog.rename.label":     "New name",
        "main.dialog.dup.title":        "Duplicate cfg",
        "main.dialog.dup.label":        "New file name",
        "main.dialog.delete.title":     "Delete",
        "main.dialog.logs.title":       "History",
        "main.dialog.export.filename_title": "Export cfg",
        "main.dialog.import.filename_title": "Import cfg",

        "main.error.no_selection":      "No configuration file selected.",
        "main.error.read":              "Read error",
        "main.error.write":             "Write error",

        "main.confirm.delete":          "Delete cfg «{name}»?",
        "main.confirm.clear":           "Are you sure you want to delete all cfg content?",
        "main.info.exported":           "Saved to {path}",
        "main.info.done":               "Done",
        "main.info.saved":              "Configuration saved.",
        "main.info.saved_with_details": "Configuration saved.\n\n{details}",
        "main.info.unknown_commands":   "Unknown commands (not in DB): {n}",
        "main.info.duplicates":         "Duplicates removed: {n}",
        "main.info.no_logs":            "No changes for file «{name}».",
        "main.copy_suffix":             "(copy)",
        "main.dialog.clear.title":      "Clear cfg?",

        "main.search": "Search:",
        "main.search.placeholder": "Input text...",
                "legend.title": "Preview Help",
        "legend.header": "Preview Colors",
        "legend.btn_close": "Got it",

        "legend.color.green": "Green — known commands",
        "legend.color.gray": "Gray — unknown commands",
        "legend.color.yellow": "Yellow — duplicates (will be removed)",
        "legend.color.orange": "Orange — server overrides value (SystemCfgLocal.cfg)",
        "legend.color.red": "Red — syntax errors",

        "legend.search.header": "Search:",
        "legend.search.open": "— open search bar",
        "legend.search.hint": "Press Enter or ↓ to find next",

        "config.error.empty_name":      "File name cannot be empty.",
        "config.error.too_long_name":   "Name is too long (max {n}).",
        "config.error.not_found":       "Config not found.",
        "config.error.cannot_unlock": (
            "Failed to remove read-only attribute from:\n{path}\n\n"
            "Close the game (if running) or run the app as administrator."
        ),

        # ============ LOGS ============
        "logs.type.unknown":     "(unknown)",
        "logs.type.duplicate":   "(duplicate)",
        "logs.value.removed":    "(removed)",
        "logs.value.dup_removed": "(removed)",
        "logs.window_title":       "Change history — {name}",
        "logs.window_title_short": "Change history",
        "logs.search_placeholder": "Search by command / date / old / new state...",
        "logs.col_date":           "Date",
        "logs.col_command":        "Command",
        "logs.col_old":            "Old",
        "logs.col_new":            "New",
        "logs.btn_close":          "Close",

        # ============ EDITOR ============
        "editor.window_title":   "Aion.CfgStudio — Config editor",
        "editor.lbl_file":       "File: {name}",
        "editor.lbl_file_new":   "File: (new)",
        "editor.lbl_file_none":  "File: —",
        "editor.lbl_mode":       "Mode:",
        "editor.mode.simple":    "Simple",
        "editor.mode.advanced":  "Advanced",
        "editor.mode.all":       "All (including debug)",
        "editor.search_placeholder": "Search command...",
        "editor.btn_expand":     "Expand all",
        "editor.btn_collapse":   "Collapse all",
        "editor.lbl_prefixes_title": "Command categories",
        "editor.lbl_prefix_info":    "Select a category to filter",
        "editor.prefix_all":     "All commands",
        "editor.col_use":        "Use",
        "editor.col_command":    "Command",
        "editor.col_value":      "Value",
        "editor.col_default":    "Default",
        "editor.col_description": "Description",
        "editor.btn_reset_all":  "Reset all to defaults",
        "editor.btn_cancel":     "Cancel",
        "editor.btn_apply":      "Apply",

        "editor.dialog.unsaved.title": "Unsaved changes",
        "editor.dialog.unsaved.text":  "Preview has unsaved changes.\n"
                                       "Save before leaving?",

        "editor.dialog.new.title":     "Unsaved config",
        "editor.dialog.new.text":      "You have selected commands but haven't saved the config.\n"
                                      "Save as system.cfg before leaving?",
        "editor.dialog.save.title":    "Save?",
        "editor.dialog.save.text":     "Configuration saved.",

        "editor.info.nothing":         "Nothing to save",
        "editor.info.nothing.text":    "No commands selected.",
        "editor.error.save":           "Save error",
        "editor.error.save.text":      "Failed to save configuration.",
        "editor.info.done":            "Done",

        "editor.error.server_required": "server_id is not set for a new cfg.",
        "editor.error.no_config_service": "EditorService: config_service is not set, "
                                          "cannot create a new cfg.",

        "editor.btn_make_defaults":      "Make default",
        "editor.make_defaults.title":    "Make default?",
        "editor.make_defaults.text":     "Set values of {n} selected commands as "
                                         "defaults?\n\n"
                                         "This will affect all future cfgs. Continue?",
        "editor.make_defaults.done":     "Done. {n} commands are now default.",

        "editor.count.command.one":   "command",
        "editor.count.command.many":  "commands",

        "editor.reset_dialog.title":      "Reset to defaults",
        "editor.reset_dialog.text":       "<b>{n}</b> commands will be affected:<br>"
                                  "• currently visible (filter + search)<br>"
                                  "• with a default value"
                                  "<br><br>"
                                  "What to reset?<br>"
                                  "• <b>Values only</b> — keep selection, "
                                  "restore default values<br>"
                                  "• <b>Values and selection</b> — check "
                                  "commands with defaults and restore "
                                  "their values",

        "editor.reset_dialog.btn_values": "Values only",
        "editor.reset_dialog.btn_all":    "Values and selection",
        "editor.reset_dialog.nothing":    "No visible commands with a default value.",
        "editor.reset_dialog.done":       "Done. Commands reset: {n}.",
        "editor.tooltip.overridden": (
            "Server overrides this value: {value}\n"
            "Your changes will be ignored."
        ),

        # ============ SHORTCUTS EDITOR ============
        "shortcuts.window_title":    "Hotkeys",
        "shortcuts.lbl_hint":        "Double-click a row or use «Change...» to assign a key. Conflicts are forbidden: release the key first.",
        "shortcuts.col_action":      "Action",
        "shortcuts.col_key":         "Key",
        "shortcuts.col_default":     "Default",
        "shortcuts.btn_change":      "Change...",
        "shortcuts.btn_reset":       "Reset",
        "shortcuts.btn_reset_all":   "Reset all",
        "shortcuts.btn_close":       "Close",
        "shortcuts.section.global":  "Global",
        "shortcuts.section.profile": "Profiles",
        "shortcuts.section.server":  "Servers",
        "shortcuts.section.main":    "Cfg files",
        "shortcuts.section.editor":  "Editor",
        "shortcuts.capture.title":   "Assign a key",
        "shortcuts.capture.action":  "Action: {title}",
        "shortcuts.capture.hint":    "Press a key or combination.\nEsc — cancel.",
        "shortcuts.capture.preview_empty": "—",

        # ============ DIALOGS ============
        "dialog.conflict_title":     "Conflict",
        "dialog.reset_all_title":    "Reset all hotkeys?",
        "dialog.reset_all_text":     "All reassigned keys will return to defaults. Continue?",
        "dialog.about_title":        "About",
        "dialog.about_text":         "Aion.CfgStudio v{version}  by @chealkrtengghnle\n\n"
                                     "Aion system.cfg editor.",

        # ============ CONTEXT MENUS ============
        "ctx.enter":         "Enter",
        "ctx.duplicate":     "Duplicate",
        "ctx.rename":        "Rename",
        "ctx.delete":        "Delete",
        "ctx.edit":          "Edit",
        "ctx.export":        "Export",

        # ============ HOTKEYS ============
        "action.global.video":         "Video guide",
        "action.profile.enter":        "Enter profile",
        "action.profile.create":       "New profile",
        "action.profile.rename":       "Rename profile",
        "action.profile.delete":       "Delete profile",
        "action.profile.quit":         "Close application",
        "action.server.enter":         "Enter server",
        "action.server.create":        "New server",
        "action.server.rename":        "Rename server",
        "action.server.delete":        "Delete server",
        "action.server.quit":          "Back to profiles",
        "action.main.open":            "Open editor",
        "action.main.create":          "New cfg",
        "action.main.import":          "Import cfg",
        "action.main.export":          "Export cfg",
        "action.main.rename":          "Rename cfg",
        "action.main.delete":          "Delete cfg",
        "action.main.save":            "Save changes (preview)",
        "action.main.quit":            "Back to servers",
        "action.main.cancelandquit":   "Cancel and quit",
        "action.main.find":            "Search in preview",
        "action.editor.cancel":        "Cancel and exit",
        "shortcut.conflict": "Key «{key}» is already used by «{title}».",

        # ============ DIALOGS ================
        "dialog.input_hint":   "{label} (max {n}):",
        "dialog.error_title":  "Error",

        # ============= SPLASH =================
        "splash.loading": "Components loading...",

        # ============== ДИАЛОГИ ================
        "dialog.yes":     "Yes",
        "dialog.no":      "No",
        "dialog.cancel":  "Cancel",
        "dialog.ok":      "OK",

        # ============== HELPERS ================
        "empty.profiles":   "No profiles.\nClick «New» to create one.",
        "empty.servers":    "No servers.\nClick «New» to create one.",
        "empty.configs":    "No configs.\nClick «New CFG» to create one.",
        "empty.preview":    "Select a configuration to preview.",
    },
}

AVAILABLE_LANGUAGES = ("ru", "en")


def set_language(lang: str) -> None:
    """Меняет текущий язык. Молча игнорирует неизвестный код."""
    global CURRENT
    if lang in STRINGS:
        CURRENT = lang


def get_language() -> str:
    """Текущий код языка."""
    return CURRENT


def t(key: str) -> str:
    """Перевод по ключу.

    Если ключа нет — возвращает сам ключ (для отладки: сразу видно,
    какой строки не хватает).
    """
    return STRINGS.get(CURRENT, {}).get(key, key)

def plural_ru(n: int, one: str, few: str, many: str) -> str:
    """Русские склонения: 1 команда, 2 команды, 5 команд."""
    n10 = n % 10
    n100 = n % 100
    if n10 == 1 and n100 != 11:
        return one
    if 2 <= n10 <= 4 and not (12 <= n100 <= 14):
        return few
    return many