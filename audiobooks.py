"""Функции для работы с коллекцией аудиокниг."""

import math



def check_speed(speed: float) -> tuple[bool, str]:
    """Проверить корректность скорости прослушивания."""
    if speed <= 0:
        return False, "Ошибка. Скорость некорректна!"
    if speed > 3:
        return False, "Ошибка. Слишком высокая скорость (макс. 3.0)!"
    return True, "Скорость корректна."


def format_duration(total_minutes: float) -> str:
    """Преобразовать минуты в строку вида 'X ч Y мин'."""
    hours = int(total_minutes // 60)
    minutes = int(round(total_minutes % 60))
    if hours == 0:
        return f"{minutes} мин"
    return f"{hours} ч {minutes} мин"


def count_days(total_minutes: float, per_day_hours: float) -> int:
    """Посчитать, за сколько дней будет прослушана книга."""
    if per_day_hours <= 0 or total_minutes <= 0:
        return -1
    minutes_per_day = per_day_hours * 60
    return math.ceil(total_minutes / minutes_per_day)



def add_audiobook(
    books: list[dict],
    title: str,
    author: str,
    narrator: str,
    genre: str,
    hours: int,
    minutes: int,
    speed: float,
) -> dict:
    """Добавить аудиокнигу в список. Вернуть созданную запись."""
    if minutes >= 60:
        hours += minutes // 60
        minutes = minutes % 60

    new_id = 1
    if books:
        new_id = max(book["id"] for book in books) + 1

    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "narrator": narrator,
        "genre": genre,
        "hours": hours,
        "minutes": minutes,
        "speed": speed,
    }
    books.append(book)
    return book


def find_audiobooks(books: list[dict], query: str) -> list[dict]:
    """Найти книги, в названии которых есть подстрока query."""
    query_lower = query.lower()
    return [b for b in books if query_lower in b["title"].lower()]


def filter_by_genre(books: list[dict], genre: str) -> list[dict]:
    """Отобрать книги по жанру (без учёта регистра)."""
    genre_lower = genre.lower()
    return [b for b in books if b["genre"].lower() == genre_lower]


def sort_audiobooks(books: list[dict]) -> list[dict]:
    """Отсортировать книги по длительности (по возрастанию)."""
    return sorted(books, key=lambda b: b["hours"] * 60 + b["minutes"])


def get_statistics(books: list[dict]) -> dict:
    """Собрать статистику по коллекции."""
    if not books:
        return {"count": 0, "total_minutes": 0, "avg_minutes": 0}
    total = sum(b["hours"] * 60 + b["minutes"] for b in books)
    return {
        "count": len(books),
        "total_minutes": total,
        "avg_minutes": round(total / len(books)),
    }


def delete_audiobook(books: list[dict], book_id: int) -> bool:
    """Удалить книгу по id. Вернуть True, если удалено."""
    for i, b in enumerate(books):
        if b["id"] == book_id:
            books.pop(i)
            return True
    return False