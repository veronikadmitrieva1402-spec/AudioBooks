"""Тесты сохранения и загрузки объектов."""

import os
import tempfile

from models import Audiobook, User
from storage import (
    load_audiobooks,
    load_users,
    save_audiobooks,
    save_users,
)


def test_save_and_load_audiobooks_roundtrip():
    with tempfile.TemporaryDirectory() as tmp:
        filename = os.path.join(tmp, "books.json")
        books = [Audiobook(1, "Дюна", "Герберт", "Иванов",
                           "Фантастика", 10, 30, 1.0)]
        save_audiobooks(books, filename)
        loaded = load_audiobooks(filename)

        assert len(loaded) == 1
        assert isinstance(loaded[0], Audiobook)
        assert loaded[0].title == "Дюна"


def test_save_and_load_users_roundtrip():
    with tempfile.TemporaryDirectory() as tmp:
        filename = os.path.join(tmp, "users.json")
        users = [User(1, "Иван", "ivan@example.com")]
        save_users(users, filename)
        loaded = load_users(filename)

        assert len(loaded) == 1
        assert isinstance(loaded[0], User)
        assert loaded[0].email == "ivan@example.com"


def test_load_missing_file_returns_empty():
    assert load_audiobooks("нет.json") == []


def test_load_corrupted_json_returns_empty():
    with tempfile.TemporaryDirectory() as tmp:
        filename = os.path.join(tmp, "broken.json")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("{ это не json")
        assert load_audiobooks(filename) == []
