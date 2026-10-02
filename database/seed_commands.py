"""Загружает seed_commands.sql в БД. Запуск из корня проекта:

    python scripts/seed_commands.py
"""
import os
import sys

# корень проекта в sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database.db_manager import DBManager


SEED_PATH = os.path.join(BASE_DIR, "database", "seed_commands.sql")


def main() -> int:
    if not os.path.isfile(SEED_PATH):
        print(f"Файл не найден: {SEED_PATH}")
        return 1

    db = DBManager()
    sql = open(SEED_PATH, "r", encoding="utf-8").read()

    with db._conn() as conn:
        conn.executescript(sql)

    with db._conn() as conn:
        total = conn.execute("SELECT COUNT(*) AS c FROM Commands").fetchone()["c"]
        by_prefix = conn.execute(
            "SELECT p.code, COUNT(c.id) AS c "
            "FROM Prefixes p LEFT JOIN Commands c ON c.prefix_id = p.id "
            "GROUP BY p.id ORDER BY p.display_order"
        ).fetchall()

    print(f"Всего команд в БД: {total}")
    for row in by_prefix:
        print(f"  {row['code']:5s} {row['c']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())