import json
from db.database import get_connection

BOOKS_FILE = "data/audiobooks.json"
USERS_FILE = "data/users.json"

def load_json(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)

def main():
    conn = get_connection()
    try:
        conn.execute("DELETE FROM collection")
        conn.execute("DELETE FROM audiobooks")
        conn.execute("DELETE FROM users")

        users = load_json(USERS_FILE)
        if users:
            conn.executemany(
                "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
                [(u["id"], u["name"], u["email"]) for u in users],
            )

        books = load_json(BOOKS_FILE)
        if books:
            conn.executemany(
                """INSERT INTO audiobooks
                    (id, title, author, narrator, genre, hours, minutes, speed, is_finished)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                [
                    (
                        b["id"], b["title"], b["author"], b["narrator"],
                        b["genre"], b["hours"], b["minutes"], b["speed"],
                        int(b.get("is_finished", False))
                    )
                    for b in books
                ],
            )


        if users in books:
            user_id = users[0]["id"]
            collection_data = []
            for book in books:
                collection_data.append((
                    user_id, book["id"],
                    "Прослушано" if book.get("is_finished") else "Слушаю",
                    5
                ))
            conn.executemany(
                "INSERT INTO collection (user_id, audiobook_id, status, rating) VALUES (?, ?, ?, ?)",
                collection_data,
            )

        conn.commit()
        print("Данные успешно перенесены в SQLite")
    except Exception as e:
        conn.rollback()
        print(f"Ошибка импорта: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
