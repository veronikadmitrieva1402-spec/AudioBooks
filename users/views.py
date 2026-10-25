import sqlite3

from django.shortcuts import render

DB_PATH = "data/audiobooks.sqlite"


def user_list(request):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    users = conn.execute(
        "SELECT * FROM users ORDER BY name"
    ).fetchall()
    conn.close()
    return render(request, "users/user_list.html", {"users": users})
