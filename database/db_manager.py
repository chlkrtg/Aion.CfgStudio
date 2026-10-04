import os
import sys
import sqlite3

from contextlib import contextmanager


def get_base_dir() -> str:
    """Папка ресурсов: в .exe - _MEIPASS, иначе - корень проекта."""
    if getattr(sys, "frozen", False):
        return sys._MEIPASS
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_app_dir() -> str:
    """Папка для БД: в .exe - %APPDATA%, иначе - корень проекта."""
    if getattr(sys, "frozen", False):
        base = os.path.join(os.environ.get("APPDATA", ""), "AionCfgStudio")
        os.makedirs(base, exist_ok=True)
        return base
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


BASE_DIR = get_base_dir()
SCHEMA_PATH = os.path.join(BASE_DIR, "database", "schema.sql")
DEFAULT_DB_PATH = os.path.join(get_app_dir(), "aion_cfg_studio.db")


class DBManager:
    def __init__(self, db_path: str = DEFAULT_DB_PATH):
        self.db_path = db_path
        self._init_schema()
        self._ensure_seed()

    def _ensure_seed(self):
        """Загружает seed-файлы, если таблица Commands пуста."""
        with self._conn() as conn:
            row = conn.execute(
                "SELECT COUNT(*) AS c FROM Commands"
            ).fetchone()
            count = row["c"]

        if count > 0:
            print(f"[DB] Команды уже загружены: {count}")
            return

        print("[DB] Первый запуск — загрузка команд")

        seed_files = [
            "seed_commands.sql",
            "seed_updates.sql",
            "seed_modes.sql",
        ]

        for name in seed_files:
            path = os.path.join(BASE_DIR, "database", name)
            if not os.path.isfile(path):
                print(f"[DB] Пропуск (не найден): {name}")
                continue

            sql = open(path, "r", encoding="utf-8").read()
            with self._conn() as conn:
                conn.executescript(sql)
            print(f"[DB] Загружен: {name}")

        with self._conn() as conn:
            total = conn.execute(
                "SELECT COUNT(*) AS c FROM Commands"
            ).fetchone()["c"]
            print(f"[DB] Загружено команд: {total}")

    @contextmanager
    def _conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _init_schema(self):
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            sql = f.read()
        with self._conn() as conn:
            conn.executescript(sql)

    # ==================== ПРОФИЛИ ====================

    def create_profile(self, name: str, description: str = "") -> int:
        with self._conn() as conn:
            cur = conn.execute(
                "INSERT INTO Profiles (name, description) VALUES (?, ?)",
                (name, description),
            )
            return cur.lastrowid # для фокуса на элементе

    def list_profiles(self):
        with self._conn() as conn:
            return conn.execute("SELECT * FROM Profiles ORDER BY name").fetchall()

    def get_profile(self, profile_id: int):
        with self._conn() as conn:
            return conn.execute(
                "SELECT * FROM Profiles WHERE id = ?", (profile_id,)
            ).fetchone()

    def rename_profile(self, profile_id: int, new_name: str):
        with self._conn() as conn:
            conn.execute(
                "UPDATE Profiles SET name = ? WHERE id = ?",
                (new_name, profile_id),
            )

    def delete_profile(self, profile_id: int):
        with self._conn() as conn:
            conn.execute("DELETE FROM Profiles WHERE id = ?", (profile_id,))

    def update_profile_description(self, profile_id: int, description: str):
        with self._conn() as conn:
            conn.execute(
                "UPDATE Profiles SET description = ? WHERE id = ?",
                (description, profile_id),
            )

    def count_servers(self, profile_id: int) -> int:
        with self._conn() as conn:
            row = conn.execute(
                "SELECT COUNT(*) AS c FROM Servers WHERE profile_id = ?",
                (profile_id,),
            ).fetchone()
            return row["c"]

    def count_configs(self, profile_id: int) -> int:
        with self._conn() as conn:
            row = conn.execute(
                "SELECT COUNT(c.id) AS c FROM ConfigFiles c "
                "JOIN Servers s ON s.id = c.server_id "
                "WHERE s.profile_id = ?",
                (profile_id,),
            ).fetchone()
            return row["c"]

    # ==================== СЕРВЕРЫ ====================

    def create_server(self, profile_id: int, name: str,
                      region: str = "EU", note: str = "") -> int:
        with self._conn() as conn:
            cur = conn.execute(
                "INSERT INTO Servers (profile_id, name, region, note) "
                "VALUES (?, ?, ?, ?)",
                (profile_id, name, region, note),
            )
            return cur.lastrowid # для фокуса на элементе

    def list_servers(self, profile_id: int):
        with self._conn() as conn:
            return conn.execute(
                "SELECT * FROM Servers WHERE profile_id = ? ORDER BY name",
                (profile_id,),
            ).fetchall()

    def get_server(self, server_id: int):
        with self._conn() as conn:
            return conn.execute(
                "SELECT * FROM Servers WHERE id = ?", (server_id,)
            ).fetchone()

    def rename_server(self, server_id: int, new_name: str):
        with self._conn() as conn:
            conn.execute(
                "UPDATE Servers SET name = ? WHERE id = ?",
                (new_name, server_id),
            )

    def delete_server(self, server_id: int):
        with self._conn() as conn:
            conn.execute("DELETE FROM Servers WHERE id = ?", (server_id,))

    def update_server_note(self, server_id: int, note: str):
        """Обновляет заметку сервера."""
        with self._conn() as conn:
            conn.execute(
                "UPDATE Servers SET note = ? WHERE id = ?",
                (note, server_id),
            )

    def count_configs_in_server(self, server_id: int) -> int:
        with self._conn() as conn:
            row = conn.execute(
                "SELECT COUNT(*) AS c FROM ConfigFiles WHERE server_id = ?",
                (server_id,),
            ).fetchone()
            return row["c"]

    # ==================== ПРЕФИКСЫ ====================

    def list_prefixes(self):
        with self._conn() as conn:
            return conn.execute(
                "SELECT * FROM Prefixes ORDER BY display_order, code"
            ).fetchall()

    # ==================== КОМАНДЫ ====================

    def list_commands(self, mode: str = "advanced"):
        """mode: simple / advanced / debug."""
        filter_sql = {
            "simple": "WHERE mode = 'simple'",
            "advanced": "WHERE mode IN ('simple','advanced')",
            "debug": "",
        }.get(mode, "")
        with self._conn() as conn:
            return conn.execute(
                f"SELECT * FROM Commands {filter_sql} "
                f"ORDER BY prefix_id, key_name"
            ).fetchall()

    def get_command(self, command_id: int):
        with self._conn() as conn:
            return conn.execute(
                "SELECT * FROM Commands WHERE id = ?", (command_id,)
            ).fetchone()

    # ==================== ФАЙЛЫ КОНФИГУРАЦИЙ ====================

    def create_config(self, server_id: int, filename: str,
                      content: str = "") -> int:
        with self._conn() as conn:
            cur = conn.execute(
                "INSERT INTO ConfigFiles (server_id, filename, content) "
                "VALUES (?, ?, ?)",
                (server_id, filename, content),
            )
            return cur.lastrowid # для фокуса на элементе

    def list_configs(self, server_id: int):
        with self._conn() as conn:
            return conn.execute(
                "SELECT * FROM ConfigFiles WHERE server_id = ? ORDER BY filename",
                (server_id,),
            ).fetchall()

    def get_config(self, config_id: int):
        with self._conn() as conn:
            return conn.execute(
                "SELECT * FROM ConfigFiles WHERE id = ?", (config_id,)
            ).fetchone()

    def update_config(self, config_id: int, content: str):
        with self._conn() as conn:
            conn.execute(
                "UPDATE ConfigFiles SET content = ?, "
                "modified_at = CURRENT_TIMESTAMP WHERE id = ?",
                (content, config_id),
            )

    def delete_config(self, config_id: int):
        with self._conn() as conn:
            conn.execute("DELETE FROM ConfigFiles WHERE id = ?", (config_id,))

    def rename_config(self, config_id: int, new_name: str):
        with self._conn() as conn:
            conn.execute(
                "UPDATE ConfigFiles SET filename = ?, "
                "modified_at = CURRENT_TIMESTAMP WHERE id = ?",
                (new_name, config_id),
            )

    # ==================== ЗНАЧЕНИЯ КОМАНД ====================

    def upsert_config_value(self, config_id: int, command_id: int,
                            use_custom: int, custom_value):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO ConfigValues "
                "(config_id, command_id, use_custom, custom_value) "
                "VALUES (?, ?, ?, ?) "
                "ON CONFLICT(config_id, command_id) DO UPDATE SET "
                "use_custom = excluded.use_custom, "
                "custom_value = excluded.custom_value",
                (config_id, command_id, use_custom, custom_value),
            )

    def list_config_values(self, config_id: int):
        with self._conn() as conn:
            return conn.execute(
                "SELECT * FROM ConfigValues WHERE config_id = ?",
                (config_id,),
            ).fetchall()

    def save_config_values_bulk(self, config_id: int, values: list[tuple]):
        """Сохраняет много значений разом.
                values: список кортежей (command_id, use_custom, custom_value)
        """
        with self._conn() as conn:
            conn.executemany(
                "INSERT INTO ConfigValues "
                "(config_id, command_id, use_custom, custom_value) "
                "VALUES (?, ?, ?, ?) "
                "ON CONFLICT(config_id, command_id) DO UPDATE SET "
                "use_custom = excluded.use_custom, "
                "custom_value = excluded.custom_value",
                [(config_id, cmd_id, use, val) for cmd_id, use, val in values],
            )

    # ==================== ЛОГИ ====================

    def log_change(self, config_id: int, key: str, old: str, new: str):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO Logs (config_id, key_name, old_value, new_value) "
                "VALUES (?, ?, ?, ?)",
                (config_id, key, old, new),
            )

    def list_logs(self, config_id: int):
        with self._conn() as conn:
            return conn.execute(
                "SELECT * FROM Logs WHERE config_id = ? ORDER BY changed_at DESC",
                (config_id,),
            ).fetchall()

    # ==================== ВИДЕО ====================

    def list_video_chapters(self):
        with self._conn() as conn:
            return conn.execute(
                "SELECT * FROM VideoChapters ORDER BY timestamp_ms"
            ).fetchall()

    # ==================== ДУБЛИРОВАНИЕ ====================

    def duplicate_config(self, config_id: int, new_name: str) -> int:
        """Дублирует cfg-файл со всеми его ConfigValues."""
        with self._conn() as conn:
            # 1. читаем исходный cfg
            src = conn.execute(
                "SELECT * FROM ConfigFiles WHERE id = ?", (config_id,)
            ).fetchone()
            if not src:
                raise ValueError("Исходный cfg не найден")

            # 2. создаём копию
            cur = conn.execute(
                "INSERT INTO ConfigFiles (server_id, filename, content) "
                "VALUES (?, ?, ?)",
                (src["server_id"], new_name, src["content"]),
            )
            new_id = cur.lastrowid

            # 3. копируем ConfigValues
            conn.execute(
                "INSERT INTO ConfigValues (config_id, command_id, use_custom, custom_value) "
                "SELECT ?, command_id, use_custom, custom_value "
                "FROM ConfigValues WHERE config_id = ?",
                (new_id, config_id),
            )
            return new_id # для фокуса на элементе

    def duplicate_server(self, server_id: int, new_name: str) -> int:
        """Дублирует сервер вместе со всеми его cfg и ConfigValues."""
        with self._conn() as conn:
            src = conn.execute(
                "SELECT * FROM Servers WHERE id = ?", (server_id,)
            ).fetchone()
            if not src:
                raise ValueError("Исходный сервер не найден")

            # 1. создаём копию сервера
            cur = conn.execute(
                "INSERT INTO Servers (profile_id, name, region, note) "
                "VALUES (?, ?, ?, ?)",
                (src["profile_id"], new_name, src["region"], src["note"]),
            )
            new_server_id = cur.lastrowid

            # 2. копируем все cfg сервера
            configs = conn.execute(
                "SELECT * FROM ConfigFiles WHERE server_id = ?", (server_id,)
            ).fetchall()

            for cfg in configs:
                cur2 = conn.execute(
                    "INSERT INTO ConfigFiles (server_id, filename, content) "
                    "VALUES (?, ?, ?)",
                    (new_server_id, cfg["filename"], cfg["content"]),
                )
                new_cfg_id = cur2.lastrowid

                # копируем значения
                conn.execute(
                    "INSERT INTO ConfigValues (config_id, command_id, use_custom, custom_value) "
                    "SELECT ?, command_id, use_custom, custom_value "
                    "FROM ConfigValues WHERE config_id = ?",
                    (new_cfg_id, cfg["id"]),
                )
            return new_server_id # для фокуса на элементе

    def duplicate_profile(self, profile_id: int, new_name: str) -> int:
        """Дублирует профиль со всеми серверами, cfg и значениями."""
        with self._conn() as conn:
            src = conn.execute(
                "SELECT * FROM Profiles WHERE id = ?", (profile_id,)
            ).fetchone()
            if not src:
                raise ValueError("Исходный профиль не найден")

            # 1. создаём копию профиля
            cur = conn.execute(
                "INSERT INTO Profiles (name, description) VALUES (?, ?)",
                (new_name, src["description"]),
            )
            new_profile_id = cur.lastrowid

            # 2. копируем все серверы
            servers = conn.execute(
                "SELECT * FROM Servers WHERE profile_id = ?", (profile_id,)
            ).fetchall()

            for srv in servers:
                cur_srv = conn.execute(
                    "INSERT INTO Servers (profile_id, name, region, note) "
                    "VALUES (?, ?, ?, ?)",
                    (new_profile_id, srv["name"], srv["region"], srv["note"]),
                )
                new_server_id = cur_srv.lastrowid

                # копируем cfg каждого сервера
                configs = conn.execute(
                    "SELECT * FROM ConfigFiles WHERE server_id = ?", (srv["id"],)
                ).fetchall()

                for cfg in configs:
                    cur_cfg = conn.execute(
                        "INSERT INTO ConfigFiles (server_id, filename, content) "
                        "VALUES (?, ?, ?)",
                        (new_server_id, cfg["filename"], cfg["content"]),
                    )
                    new_cfg_id = cur_cfg.lastrowid

                    conn.execute(
                        "INSERT INTO ConfigValues (config_id, command_id, use_custom, custom_value) "
                        "SELECT ?, command_id, use_custom, custom_value "
                        "FROM ConfigValues WHERE config_id = ?",
                        (new_cfg_id, cfg["id"]),
                    )
            return new_profile_id # для фокуса на элементе
