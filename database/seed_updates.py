"""Запускает database/seed_updates.sql на текущей БД.
Запуск из корня проекта: python scripts/seed_updates.py
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database.db_manager import DBManager

SQL_PATH = os.path.join(BASE_DIR, "database", "seed_updates.sql")
MODES_PATH = os.path.join(BASE_DIR, "database", "seed_modes.sql")


def main() -> int:
    db = DBManager()

    # 1. основной seed_updates.sql
    if os.path.isfile(SQL_PATH):
        sql = open(SQL_PATH, "r", encoding="utf-8").read()
        with db._conn() as conn:
            conn.executescript(sql)
        print(f"Применён: {os.path.basename(SQL_PATH)}")

    # 2. seed_modes.sql — пометка команд из стандартного cfg
    if os.path.isfile(MODES_PATH):
        sql = open(MODES_PATH, "r", encoding="utf-8").read()
        with db._conn() as conn:
            conn.executescript(sql)
        print(f"Применён: {os.path.basename(MODES_PATH)}")

    # 3. проверка
    with db._conn() as conn:
        total_simple = conn.execute(
            "SELECT COUNT(*) FROM Commands WHERE mode='simple'"
        ).fetchone()[0]
        total_advanced = conn.execute(
            "SELECT COUNT(*) FROM Commands WHERE mode='advanced'"
        ).fetchone()[0]
        total_possible = conn.execute(
            "SELECT COUNT(*) FROM Commands WHERE possible_values IS NOT NULL"
        ).fetchone()[0]

    print(f"Команд 'simple':   {total_simple}")
    print(f"Команд 'advanced': {total_advanced}")
    print(f"С possible_values: {total_possible}")
    return 0


if __name__ == "__main__":
    sys.exit(main())