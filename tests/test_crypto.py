"""Тесты шифрования cfg."""
from parsers.cfg_crypto import decrypt, encrypt, looks_like_encrypted


def test_encrypt_decrypt_roundtrip():
    original = 'e_beach = "0"\ng_maxfov = "60"'
    encrypted = encrypt(original)
    decrypted = decrypt(encrypted)
    # encrypt добавляет \n в конец (требование клиента Aion)
    assert decrypted.rstrip("\n") == original


def test_encrypt_empty():
    encrypted = encrypt("")
    # decrypt("") возвращает "\n"
    assert decrypt(encrypted).strip() == ""


def test_encrypt_latin1():
    # cfg в Aion хранится в Latin-1, кириллица не поддерживается
    original = 'e_beach = "0"\n-- comment'
    encrypted = encrypt(original)
    assert decrypt(encrypted).rstrip("\n") == original


def test_looks_like_encrypted():
    assert looks_like_encrypted(encrypt('key = "value"'))
    assert not looks_like_encrypted(b'key = "value"')