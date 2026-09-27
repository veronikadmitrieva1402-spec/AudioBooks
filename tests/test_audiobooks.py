"""Тесты функций работы с аудиокнигами."""

from audiobooks import (
    add_audiobook,
    delete_audiobook,
    filter_by_genre,
    find_audiobooks,
    format_duration,
    get_statistics,
    sort_audiobooks,
)


def test_format_duration():
    assert format_duration(630) == "10 ч 30 мин"
    assert format_duration(45) == "45 мин"
    assert format_duration(60) == "1 ч 0 мин"


def test_add_audiobook():
    books = []
    add_audiobook(books, "Дюна", "Герберт", "Иванов", "Фантастика", 10, 30, 1.0)
    assert len(books) == 1
    assert books[0]["title"] == "Дюна"
    assert books[0]["id"] == 1


def test_add_normalizes_minutes():
    books = []
    add_audiobook(books, "Тест", "Автор", "Чтец", "Жанр", 1, 90, 1.0)
    assert books[0]["hours"] == 2
    assert books[0]["minutes"] == 30


def test_find_audiobooks():
    books = []
    add_audiobook(books, "Дюна", "Герберт", "Иванов", "Фантастика", 10, 30, 1.0)
    add_audiobook(books, "1984", "Оруэлл", "Петров", "Антиутопия", 8, 0, 1.0)
    assert len(find_audiobooks(books, "дюн")) == 1
    assert len(find_audiobooks(books, "о")) == 2


def test_filter_by_genre():
    books = []
    add_audiobook(books, "Дюна", "Герберт", "Иванов", "Фантастика", 10, 30, 1.0)
    add_audiobook(books, "1984", "Оруэлл", "Петров", "Антиутопия", 8, 0, 1.0)
    assert len(filter_by_genre(books, "фантастика")) == 1


def test_sort_audiobooks():
    books = []
    add_audiobook(books, "Длинная", "A", "N", "G", 20, 0, 1.0)
    add_audiobook(books, "Короткая", "A", "N", "G", 2, 0, 1.0)
    sorted_books = sort_audiobooks(books)
    assert sorted_books[0]["title"] == "Короткая"


def test_statistics():
    books = []
    add_audiobook(books, "A", "A", "N", "G", 1, 0, 1.0)
    add_audiobook(books, "B", "A", "N", "G", 2, 0, 1.0)
    stats = get_statistics(books)
    assert stats["count"] == 2
    assert stats["total_minutes"] == 180


def test_delete_audiobook():
    books = []
    add_audiobook(books, "A", "A", "N", "G", 1, 0, 1.0)
    assert delete_audiobook(books, 1) is True
    assert len(books) == 0
    assert delete_audiobook(books, 99) is False