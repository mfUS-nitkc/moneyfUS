import hashlib


def hash_password(email: str, plain_password: str) -> str:
    data = f"{email}{plain_password}".encode("utf-8")
    return hashlib.sha256(data).hexdigest()
