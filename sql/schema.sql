CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS audiobooks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    narrator TEXT NOT NULL,
    genre TEXT NOT NULL,
    hours INTEGER NOT NULL,
    minutes INTEGER NOT NULL,
    speed REAL NOT NULL,
    is_finished INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS collection (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    audiobook_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    rating INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (audiobook_id) REFERENCES audiobooks(id)
);
