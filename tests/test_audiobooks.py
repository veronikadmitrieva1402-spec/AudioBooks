
from models import Audiobook
from models.audiobooks import (
    add_audiobook,
    delete_audiobook,
    filter_by_genre,
    find_audiobooks,
    get_statistics,
    sort_audiobooks,
)


def test_audiobook_creation():
    book = Audiobook(1, "Дюна", "Герберт", "Иванов",
                     "Фантастика", 10, 30, 1.0)
    assert book.id == 1
    assert book.title == "Дюна"
    assert book.hours == 10
    assert book.minutes == 30


def test_audiobook_normalizes_minutes():
    book = Audiobook(1, "Тест", "А", "N", "G", 1, 90, 1.0)
    assert book.hours == 2
    assert book.minutes == 30


def test_total_minutes_property():
    book = Audiobook(1, "Тест", "А", "N", "G", 10, 30, 1.0)
    assert book.total_minutes == 630


def test_real_minutes_with_speed():
    book = Audiobook(1, "Тест", "А", "N", "G", 10, 30, 2.0)
    assert book.real_minutes == 315.0


def test_format_duration():
    assert Audiobook.format_duration(630) == "10 ч 30 мин"
    assert Audiobook.format_duration(45) == "45 мин"


def test_check_speed():
    assert Audiobook.check_speed(1.0)[0] is True
    assert Audiobook.check_speed(0)[0] is False
    assert Audiobook.check_speed(5)[0] is False


def test_str_representation():
    book = Audiobook(1, "Дюна", "Герберт", "Иванов",
                     "Фантастика", 10, 30, 1.0)
    text = str(book)
    assert "Дюна" in text
    assert "[1]" in text


def test_mark_finished():
    book = Audiobook(1, "Дюна", "Герберт", "Иванов",
                     "Фантастика", 10, 30, 1.0)
    assert book.is_finished is False
    book.mark_finished()
    assert book.is_finished is True


def test_add_audiobook():
    books = []
    add_audiobook(books, "Дюна", "Герберт", "Иванов",
                  "Фантастика", 10, 30, 1.0)
    assert len(books) == 1
    assert isinstance(books[0], Audiobook)


def test_find_audiobooks():
    books = []
    add_audiobook(books, "Дюна", "Герберт", "Иванов",
                  "Фантастика", 10, 30, 1.0)
    add_audiobook(books, "1984", "Оруэлл", "Петров",
                  "Антиутопия", 8, 0, 1.0)
    assert len(find_audiobooks(books, "дюн")) == 1


def test_filter_by_genre():
    books = []
    add_audiobook(books, "Дюна", "Герберт", "Иванов",
                  "Фантастика", 10, 30, 1.0)
    add_audiobook(books, "1984", "Оруэлл", "Петров",
                  "Антиутопия", 8, 0, 1.0)
    assert len(filter_by_genre(books, "фантастика")) == 1


def test_sort_audiobooks():
    books = []
    add_audiobook(books, "Длинная", "A", "N", "G", 20, 0, 1.0)
    add_audiobook(books, "Короткая", "A", "N", "G", 2, 0, 1.0)
    assert sort_audiobooks(books)[0].title == "Короткая"


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
