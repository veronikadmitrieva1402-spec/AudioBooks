-- 1. Все аудиокниги
SELECT id, title, author, genre FROM audiobooks ORDER BY title;

-- 2. Все пользователи
SELECT id, name, email FROM users ORDER BY name;

-- 3. Книги "Фантастика"
SELECT title, author FROM audiobooks WHERE genre = 'Фантастика';

-- 4. Книги больше 10 ч
SELECT title, hours FROM audiobooks WHERE hours >= 10;

-- 5. Книги и статус из коллекции пользователя
SELECT users.name AS user_name, audiobooks.title AS book_title, collection.status
FROM collection
JOIN users ON collection.user_id = users.id
JOIN audiobooks ON collection.audiobook_id = audiobooks.id;

-- 6. Прослушаные с оценками
SELECT audiobooks.title, collection.rating
FROM collection
JOIN audiobooks ON collection.audiobook_id = audiobooks.id
WHERE collection.status = 'Прослушано';

-- 7. Общее кол-во книг в базе
SELECT COUNT(*) AS total_books FROM audiobooks;

-- 8. Средняя оценка всех прослушанных книг
SELECT AVG(rating) AS average_rating FROM collection WHERE status = 'Прослушано';

-- 9. Сколько книг в каждом жанре
SELECT genre, COUNT(*) AS count_books
FROM audiobooks
GROUP BY genre;

-- 10. Жанры, в которых больше 1 книги
SELECT genre, COUNT(*) AS count_books
FROM audiobooks
GROUP BY genre
HAVING COUNT(*) > 1;
