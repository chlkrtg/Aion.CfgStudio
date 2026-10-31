"""Генератор кодов раннего доступа (только для тебя).

Использование:
    python tools/generate_license.py <HWID> <days>

Пример:
    python tools/generate_license.py "12345678-1234-1234-1234-123456789abc" 1
"""
import sys
from pathlib import Path

# Добавляем корень проекта в sys.path, чтобы импортировать license
sys.path.insert(0, str(Path(__file__).parent.parent))

from logic.core.license import make_code


def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_license.py <HWID> <days>")
        print("Example: python generate_license.py 'a1b2c3d4-...' 7")
        sys.exit(1)

    hwid = sys.argv[1].strip()
    try:
        days = int(sys.argv[2])
    except ValueError:
        print("Error: <days> must be a number")
        sys.exit(1)

    if days <= 0:
        print("Error: <days> must be > 0")
        sys.exit(1)

    code = make_code(hwid, days)
    print(f"HWID:  {hwid}")
    print(f"Days:  {days}")
    print(f"Code:  {code}")


if __name__ == "__main__":
    main()