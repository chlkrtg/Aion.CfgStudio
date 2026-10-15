"""Простейшая локализация: словарь + t().

Уровень 1: без Qt Linguist, без .ts/.qm.
Строки держим в STRINGS, текущий язык — в CURRENT.
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
        "dialog.about_text":         "Aion.CfgStudio v1.0  by @chealkrtengghnle\n\n"
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
        "shortcut.conflict": "Клавиша «{key}» уже занята действием «{title}».",

        # ================= ДИАЛОГИ ==============
        "dialog.input_hint":   "{label} (макс. {n}):",
        "dialog.error_title":  "Ошибка",
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
        "dialog.about_text":         "Aion.CfgStudio v1.0  by @chealkrtengghnle\n\n"
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
        "action.editor.cancel":        "Cancel and exit",
        "shortcut.conflict": "Key «{key}» is already used by «{title}».",

        # ============ DIALOGS ================
        "dialog.input_hint":   "{label} (max {n}):",
        "dialog.error_title":  "Error",
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