"""Полная сборка: Nuitka → Inno Setup."""
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
PY = sys.executable
ISCC = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
ISS_FILE = BASE / "installer" / "AionCfgStudio.iss"


def run(cmd, cwd=None):
    print(f"\n[BUILD] {' '.join(str(c) for c in cmd)}")
    subprocess.run(cmd, cwd=cwd or BASE, check=True)


def get_version() -> str:
    try:
        return subprocess.check_output(
            [PY, "-m", "setuptools_scm"], cwd=BASE, text=True,
        ).strip()
    except subprocess.CalledProcessError:
        return "0.0.0"


def main():
    print("=" * 60)
    print("Aion.CfgStudio — сборка (Nuitka)")
    print("=" * 60)

    version = get_version()
    print(f"[BUILD] Version: {version}")

    # 1. Nuitka
    run([PY, str(BASE / "build_nuitka.py")])

    # 2. Inno Setup (версия → X.Y.Z.W)
    import re
    m = re.match(r"(\d+)\.(\d+)(?:\.(\d+))?", version)
    if m:
        clean = f"{m.group(1)}.{m.group(2)}.{m.group(3) or '0'}.0"
    else:
        clean = "0.0.0.0"

    print(f"[BUILD] Inno version: {clean}")
    run([ISCC, f"/DMyAppVersion={clean}", str(ISS_FILE)])

    # 3. Итог
    setup = BASE / "installer" / "Output" / f"AionCfgStudio_Setup_v{clean}.exe"
    if setup.exists():
        print(f"\n[BUILD] Готово: {setup}")
        print(f"[BUILD] Размер: {setup.stat().st_size / 1024 / 1024:.1f} МБ")


if __name__ == "__main__":
    main()