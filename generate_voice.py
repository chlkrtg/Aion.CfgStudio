# generate_voice.py
"""
Генерация озвучки для видео-руководства Aion.CfgStudio.
Использует Silero TTS v5_ru (локальный файл v5_ru.pt).
Результат — voice/*.wav (48 kHz).

Установка:
    pip install torch soundfile numpy

Файл модели:
    v5_ru.pt должен лежать рядом с этим скриптом.

Запуск:
    python generate_voice.py
    python generate_voice.py --speaker xenia
    python generate_voice.py --list
    python generate_voice.py --only 01_title 02_profiles

Опции:
    --speaker aidar|baya|kseniya|xenia|eugene   голос (по умолчанию aidar)
    --out voice                                  папка для .wav
    --only 01_title 02_profiles ...              сгенерировать только указанные блоки
    --list                                       показать доступные голоса
"""

import argparse
import os
import sys
from database.db_manager import DBManager

try:
    import torch
    import soundfile as sf
    import numpy as np
except ImportError:
    print("❌ Не установлены зависимости.")
    print("   Выполни: pip install torch soundfile numpy")
    sys.exit(1)


def load_blocks_from_db() -> dict[str, str]:
    """Читает главы из БД. Ключ файла — NN_название."""
    db = DBManager()
    chapters = db.list_video_chapters()

    blocks = {}
    for ch in chapters:
        slug = ch["title"].lower().replace(" ", "_").replace("ё", "e")
        name = f"{ch['id']:02d}_{slug}"
        blocks[name] = ch["description"]
    return blocks


# ============ ТЕКСТЫ БЛОКОВ ============

BLOCKS = load_blocks_from_db()

# ============ ДОСТУПНЫЕ ГОЛОСА ============

AVAILABLE_SPEAKERS = {
    "aidar": "мужской, спокойный (рекомендуется)",
    "baya": "женский, мягкий",
    "kseniya": "женский, чёткий",
    "xenia": "женский, быстрый",
    "eugene": "мужской, размеренный",
}

# ============ КОНСТАНТЫ ============

SAMPLE_RATE = 48000
MODEL_FILE = "v5_ru.pt"  # файл лежит рядом со скриптом


# ============ ЗАГРУЗКА МОДЕЛИ ============

def load_model():
    """Загружает Silero TTS v5_ru из локального файла."""
    if not os.path.isfile(MODEL_FILE):
        print(f"❌ Файл {MODEL_FILE} не найден рядом с generate_voice.py.")
        print(f"   Положи его в: {os.path.abspath(MODEL_FILE)}")
        sys.exit(1)

    print(f"⏳ Загрузка модели {MODEL_FILE}...")
    try:
        model = torch.package.PackageImporter(MODEL_FILE).load_pickle(
            "tts_models", "model"
        )
        model.to(torch.device("cpu"))
        print("✅ Модель v5_ru загружена.")
        return model
    except Exception as exc:
        print(f"❌ Не удалось загрузить модель: {exc}")
        print("   Проверь, что файл действительно v5_ru.pt и не повреждён.")
        sys.exit(1)


# ============ ПОСТОБРАБОТКА ЗВУКА ============

def postprocess(data: np.ndarray) -> np.ndarray:
    """Обрезка тишины по RMS-окну + нормализация + fade in/out."""
    # 1. Нормализация
    max_val = np.abs(data).max()
    if max_val > 0:
        data = data / max_val * 0.9

    # 2. Обрезка тишины по RMS (скользящее окно)
    #    RMS видит "энергию" звука, а не одиночные пики
    window = int(0.02 * SAMPLE_RATE)  # 20 мс
    threshold = 0.008  # порог RMS (ниже = меньше режем)
    padding = int(0.08 * SAMPLE_RATE)  # запас 80 мс до/после речи

    if len(data) > window:
        # RMS по окну
        sq = data ** 2
        kernel = np.ones(window) / window
        rms = np.sqrt(np.convolve(sq, kernel, mode="same"))

        above = np.where(rms > threshold)[0]
        if len(above) > 0:
            start = max(0, above[0] - padding)
            end = min(len(data), above[-1] + padding)
            data = data[start:end]

    # 3. Мягкий fade in / out по 30 мс (только убирает щелчки)
    fade = int(0.03 * SAMPLE_RATE)
    if len(data) > fade * 2:
        data[:fade] *= np.linspace(0.0, 1.0, fade)
        data[-fade:] *= np.linspace(1.0, 0.0, fade)

    return data


# ============ ГЕНЕРАЦИЯ ============

def generate_block(model, name: str, text: str, speaker: str, out_dir: str) -> float:
    """Генерирует один .wav. Возвращает длительность в секундах (0 при ошибке)."""
    out_path = os.path.join(out_dir, f"{name}.wav")

    try:
        audio = model.apply_tts(
            text=text,
            speaker=speaker,
            sample_rate=SAMPLE_RATE,
            put_accent=True,  # ударения
            put_yo=True,  # буква ё
            put_stress_homo=True,  # ударения в омографах
            put_yo_homo=True,  # ё в омографах
        )
        data = audio.numpy()
        data = postprocess(data)
        sf.write(out_path, data, SAMPLE_RATE)

        duration = len(data) / SAMPLE_RATE
        print(f"  ✅ {name}.wav  ({duration:.1f} сек)")
        return duration
    except Exception as exc:
        print(f"  ❌ {name}: {exc}")
        return 0.0


# ============ MAIN ============

def main():
    parser = argparse.ArgumentParser(
        description="Генерация озвучки для Aion.CfgStudio (Silero TTS v5_ru)"
    )
    parser.add_argument(
        "--speaker",
        default="aidar",
        choices=list(AVAILABLE_SPEAKERS.keys()),
        help="Голос (по умолчанию aidar)",
    )
    parser.add_argument(
        "--out",
        default="voice",
        help="Папка для .wav файлов (по умолчанию voice)",
    )
    parser.add_argument(
        "--only",
        nargs="+",
        default=None,
        help="Сгенерировать только указанные блоки (например: --only 01_title 02_profiles)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Показать доступные голоса и выйти",
    )
    args = parser.parse_args()

    # --list
    if args.list:
        print("Доступные голоса Silero TTS (русский):")
        for name, desc in AVAILABLE_SPEAKERS.items():
            print(f"  {name:10} — {desc}")
        return

    # выбор блоков
    if args.only:
        unknown = [b for b in args.only if b not in BLOCKS]
        if unknown:
            print(f"❌ Неизвестные блоки: {', '.join(unknown)}")
            print(f"   Доступные: {', '.join(BLOCKS.keys())}")
            sys.exit(1)
        selected = {name: BLOCKS[name] for name in args.only}
    else:
        selected = BLOCKS

    os.makedirs(args.out, exist_ok=True)
    print(f"📁 Папка вывода: {os.path.abspath(args.out)}")
    print(f"🎙  Голос: {args.speaker} ({AVAILABLE_SPEAKERS[args.speaker]})")
    print(f"🧠 Модель: Silero TTS v5_ru (CC-NC-BY, образовательное использование)")
    print(f"📝 Блоков к генерации: {len(selected)}")
    print()

    model = load_model()
    print()

    total_duration = 0.0
    for i, (name, text) in enumerate(selected.items(), 1):
        print(f"[{i}/{len(selected)}] {name}")
        total_duration += generate_block(model, name, text, args.speaker, args.out)

    # итог
    print()
    print("─" * 50)
    print(f"✅ Готово. Суммарная длительность: {total_duration:.1f} сек "
          f"({total_duration / 60:.1f} мин)")
    print(f"📁 Файлы в: {os.path.abspath(args.out)}")
    print()
    print("Дальше:")
    print("  1. Прослушай каждый .wav — если что-то звучит плохо, поправь текст в BLOCKS")
    print("  2. Запиши экран молча, выполняя действия из сценария")
    print("  3. Смонтируй видео в DaVinci/Clipchamp: видео + аудио")
    print("  4. Экспортируй в media/tutorial.mp4")


if __name__ == "__main__":
    main()
