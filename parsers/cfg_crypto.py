"""XOR-шифрование .cfg-файлов Aion.

Алгоритм: каждый байт XOR-ится с 0xFF (побитовая инверсия).
Комментарии (строки, начинающиеся с --) НЕ шифруются.
Кодировка — latin1.

Источник алгоритма:
https://github.com/xan105/Aion-open-system-cfg-editor
"""

XOR_KEY = 0xFF
COMMENT_PREFIX = b"--"
ENCODING = "latin1"


def xor_byte(b: int) -> int:
    """XOR одного байта с 0xFF."""
    return b ^ XOR_KEY


def xor_bytes(data: bytes) -> bytes:
    """XOR всех байт с 0xFF."""
    return bytes(xor_byte(b) for b in data)


def decrypt(raw: bytes) -> str:
    """Расшифровывает .cfg из байтов в строку.

    - Разбивает по \r\n (CRLF).
    - Комментарии (начинаются с --) - как есть.
    - Остальные строки - XOR с 0xFF.
    """
    lines = raw.split(b"\r\n")

    result = []
    for line in lines:
        if not line:
            result.append(line)
            continue
        if line.startswith(COMMENT_PREFIX):
            result.append(line)  # комментарий как есть
        else:
            result.append(xor_bytes(line))

    # склеиваем через \n (единый формат)
    return b"\n".join(result).decode(ENCODING, errors="replace")


def encrypt(text: str) -> bytes:
    """Шифрует текст cfg в байты для записи в файл.

    - Разбивает по \n.
    - Комментарии - как есть.
    - Остальные строки - XOR с 0xFF.
    - Соединяет через \r\n (как в оригинале).
    """
    raw = text.encode(ENCODING, errors="replace")
    lines = raw.split(b"\n")

    result = []
    for line in lines:
        if not line:
            result.append(line)
            continue
        if line.startswith(COMMENT_PREFIX):
            result.append(line)
        else:
            result.append(xor_bytes(line))

    # соединяем через \r\n и добавляем завершающий \r\n
    joined = b"\r\n".join(result)
    if not joined.endswith(b"\r\n"):
        joined += b"\r\n"
    return joined


def looks_like_encrypted(raw: bytes) -> bool:
    """Эвристика: если много байт вне ASCII — вероятно, зашифровано."""
    if not raw:
        return False
    non_ascii = sum(1 for b in raw if b > 127 or b < 9)
    return non_ascii > len(raw) * 0.1  # больше 10% необычных