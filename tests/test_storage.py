"""Тесты сохранения и загрузки данных."""

import json
import os
import tempfile

from storage import load_audiobooks, save_audiobooks


def test_save_and_load_roundtrip():
    with tempfile.TemporaryDirectory() as tmp:
        filename = os.path.join(tmp, "test.json")
        books = [{"id": 1, "title": "Дюна", "hours": 10, "minutes": 30}]

        save_audiobooks(books, filename)
        loaded = load_audiobooks(filename)

        assert loaded == books


def test_load_missing_file_returns_empty():
    result = load_audiobooks("несуществующий_файл.json")
    assert result == []


def test_load_corrupted_json_returns_empty():
    with tempfile.TemporaryDirectory() as tmp:
        filename = os.path.join(tmp, "broken.json")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("{ это не валидный json")

        result = load_audiobooks(filename)
        assert result == []