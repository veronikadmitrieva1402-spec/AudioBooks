"""Загрузка и сохранение данных в JSON-файлах."""

import json
import os

from models import Audiobook, User


DATA_DIR = "data"
BOOKS_FILE = os.path.join(DATA_DIR, "audiobooks.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")


def load_audiobooks(filename: str = BOOKS_FILE) -> list[Audiobook]:
    """Загрузить список аудиокниг из JSON и вернуть объекты."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Audiobook.from_dict(item) for item in data]
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создана пустая коллекция.")
        return []
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Ошибка чтения {filename}: {e}")
        return []


def save_audiobooks(
    books: list[Audiobook], filename: str = BOOKS_FILE
) -> None:
    """Сохранить коллекцию объектов Audiobook в JSON."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in books],
                      f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"Ошибка сохранения: {e}")


def load_users(filename: str = USERS_FILE) -> list[User]:
    """Загрузить пользователей из JSON."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [User.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Ошибка чтения {filename}: {e}")
        return []


def save_users(
    users: list[User], filename: str = USERS_FILE
) -> None:
    """Сохранить пользователей в JSON."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([u.to_dict() for u in users],
                      f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"Ошибка сохранения: {e}")
        