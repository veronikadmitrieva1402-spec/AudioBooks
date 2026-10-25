import sqlite3

from django.shortcuts import render

DB_PATH = "data/audiobooks.sqlite"


def book_list(request):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    books = conn.execute(
        "SELECT * FROM audiobooks ORDER BY title"
    ).fetchall()
    conn.close()
    return render(request, "audiobooks/book_list.html", {"books": books})


def book_detail(request, book_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    book = conn.execute(
        "SELECT * FROM audiobooks WHERE id = ?", [book_id]
    ).fetchone()
    conn.close()

    if book is None:
        return render(
            request,
            "audiobooks/book_detail.html",
            {"book": None},
            status=404,
        )

    return render(request, "audiobooks/book_detail.html", {"book": book})


def statistics(request):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    stats = conn.execute(
        "SELECT genre, COUNT(*) AS count_books "
        "FROM audiobooks "
        "GROUP BY genre ORDER BY count_books DESC"
    ).fetchall()
    total = conn.execute(
        "SELECT COUNT(*) AS total FROM audiobooks"
    ).fetchone()
    conn.close()

    return render(
        request,
        "audiobooks/statistics.html",
        {"stats": stats, "total": total},
    )
