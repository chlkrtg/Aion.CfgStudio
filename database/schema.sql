PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Profiles (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL UNIQUE,
    description TEXT    DEFAULT '',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Servers (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    name       TEXT    NOT NULL,
    region     TEXT    DEFAULT 'EU',
    note       TEXT    DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (profile_id) REFERENCES Profiles(id) ON DELETE CASCADE,
    UNIQUE (profile_id, name)
);

CREATE TABLE IF NOT EXISTS Prefixes (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    code          TEXT    NOT NULL UNIQUE,
    name          TEXT    NOT NULL,
    description   TEXT    DEFAULT '',
    display_order INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS Commands (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    key_name        TEXT    NOT NULL UNIQUE,
    prefix_id       INTEGER,
    value_type      TEXT    DEFAULT 'string',
    default_value   TEXT,
    possible_values TEXT,
    min_value       TEXT,
    max_value       TEXT,
    description     TEXT    DEFAULT '',
    mode            TEXT    DEFAULT 'advanced',
    FOREIGN KEY (prefix_id) REFERENCES Prefixes(id)
);

CREATE TABLE IF NOT EXISTS ConfigFiles (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    server_id   INTEGER NOT NULL,
    filename    TEXT    NOT NULL,
    content     TEXT    DEFAULT '',
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (server_id) REFERENCES Servers(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ConfigValues (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    config_id    INTEGER NOT NULL,
    command_id   INTEGER NOT NULL,
    use_custom   INTEGER DEFAULT 0,
    custom_value TEXT,
    FOREIGN KEY (config_id) REFERENCES ConfigFiles(id) ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES Commands(id),
    UNIQUE (config_id, command_id)
);

CREATE TABLE IF NOT EXISTS Logs (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    config_id  INTEGER,
    key_name   TEXT,
    old_value  TEXT,
    new_value  TEXT,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (config_id) REFERENCES ConfigFiles(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS VideoChapters (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    title        TEXT    NOT NULL,
    timestamp_ms INTEGER NOT NULL,
    description  TEXT    DEFAULT ''
);

-- ==================== ПРЕФИКСЫ ====================
INSERT OR IGNORE INTO Prefixes (code, name, description, display_order) VALUES
('g_',      'Общие игровые',       'Камера, UI, персонаж, бой, сеть', 1),
('r_',      'Render / графика',    'Разрешение, сглаживание, качество', 2),
('e_',      'Engine / мир',        'Тени, LOD, дальность, погода, вода', 3),
('p_',      'Physics',             'Физика, коллизии, покачивание камеры', 4),
('es_',     'Entity System',       'Сущности, камера, обновления', 5),
('a_',      'Audio / Area',        'Звук и зоны', 6),
('ca_',     'Character / Animation', 'Анимации, скелеты, cloth', 7),
('con_',    'Console',             'Консоль и логи', 8),
('CV_',     'Debug Visualization', 'Отладочная визуализация', 9),
('d3d9_',   'DirectX 9',           'Рендерер D3D9', 10),
('s_',      'Sound',               'Звук', 11),
('sys_',    'System',              'Системные и движковые', 12),
('i_',      'Input',               'Ввод', 13),
('log_',    'Logging',             'Логирование', 14),
('mov_',    'Movies',              'Видео и катсцены', 15),
('profile', 'Profiling',           'Профилирование', 16),
('Mem',     'Memory',              'Память', 17),
('misc',    'Прочее',              'Команды без префикса', 18);

-- ==================== ВИДЕО ====================
INSERT OR IGNORE INTO VideoChapters (id, title, timestamp_ms, description) VALUES
(1, 'Введение', 8000,
 'Добро пожаловать в Aion.CfgStudio. Это редактор одноимённого конфигурационного файла игры Айон. За три минуты мы разберём, как им пользоваться.'),

(2, 'Профили', 20600,
 'Начнём с профилей. Профиль — это отдельный набор серверов и конфигураций. Чтобы создать профиль, нажмите кнопку «Новый профиль» или выберите готовый демонстрационный профиль. Описание профиля сохраняется автоматически, через секунду после того, как вы закончите печатать. Нажав по профилю правой кнопкой мыши, можно вызвать контекстное меню. С его помощью можно войти, дублировать, переименовать или удалить профиль.'),

(3, 'Серверы', 51600,
 'Внутри профиля находятся серверы. Чтобы добавить сервер, нажмите «Новый сервер». Как и профиль, сервер обладает заметкой, которая сохраняется автоматически. Нажав по серверу правой кнопкой мыши, можно вызвать контекстное меню. С его помощью можно войти, дублировать, переименовать или удалить сервер.'),

(4, 'Конфигурации', 74500,
 'Перед вами список конфигурационных файлов сервера. Каждый файл — это отдельный конфиг. Чтобы импортировать существующий файл, нажмите кнопку Импорт или используйте соответствующее сочетание клавиш. Фильтр сверху помогает найти нужный файл по имени или дате. Для экспорта выберите файл и нажмите кнопку Экспорт или используйте соответствующее сочетание клавиш. Можно сохранить как в зашифрованном виде для игры, так и в виде обычного текста для чтения.'),

(5, 'Редактор', 109000,
 'Главная часть приложения — редактор команд. Здесь больше тысячи команд, разбитых на группы. Слева — список префиксов. Выберите нужную группу, чтобы видеть только её команды. Сверху — режим отображения. Простой режим показывает только основные команды. Расширенный режим — все доступные. В поле поиска введите название команды. Таблица отфильтруется мгновенно. Слева у каждой команды находится чекбокс. Отметьте те, которые хотите применить. Для отмеченных команд станет активным поле значения, которое можно выбрать из списка или ввести вручную. Если нужно отметить всю группу сразу — нажмите групповой чекбокс в заголовке. Он автоматически показывает частичное выделение, если отмечена только часть команд. Когда всё готово, нажмите кнопку Сохранить. Конфигурация сохранится, а все изменения попадут в историю.'),

(6, 'Логирование', 171000,
 'История изменений показывает, какие команды менялись, старые и новые значения, и когда это произошло. Записываются только реальные изменения, чтобы не засорять журнал.'),

(7, 'Горячие клавиши', 186000,
 'Напоследок — горячие клавиши. Рядом с каждой кнопкой указано сочетание клавиш, нажав которые можно выполнять те или иные действия.'),

(8, 'Заключение', 196500,
 'Приятной настройки. Спасибо за выбор Aion.CfgStudio!');