"""Загрузка и сохранение данных в JSON-файлах."""

import json
import os


DATA_FILE = os.path.join("data", "audiobooks.json")


def load_audiobooks(filename: str = DATA_FILE) -> list[dict]:
    """Загрузить список аудиокниг из JSON-файла."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создана пустая коллекция.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка чтения {filename}: файл повреждён.")
        return []


def save_audiobooks(books: list[dict], filename: str = DATA_FILE) -> None:
    """Сохранить список аудиокниг в JSON-файл."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(books, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"Ошибка сохранения: {e}")