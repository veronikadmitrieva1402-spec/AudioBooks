"""Точка входа: меню сервиса учёта коллекции аудиокниг."""

from models import Audiobook, User
from models.audiobooks import (
    add_audiobook,
    delete_audiobook,
    filter_by_genre,
    find_audiobooks,
    get_statistics,
    sort_audiobooks,
)
from models.users import add_user, find_user
from storage import (
    load_audiobooks,
    load_users,
    save_audiobooks,
    save_users,
)
from utils import input_float, input_int, input_str


def show_audiobooks(books: list[Audiobook]) -> None:
    """Вывести список книг."""
    if not books:
        print("Коллекция пуста.")
        return
    print("-" * 60)
    for b in books:
        print(b)


def show_users(users: list[User]) -> None:
    """Вывести список пользователей."""
    if not users:
        print("Пользователей нет.")
        return
    print("-" * 40)
    for u in users:
        print(u)


def cmd_add_book(books: list[Audiobook]) -> None:
    """Добавить книгу в коллекцию."""
    title = input_str("Название: ")
    author = input_str("Автор: ")
    narrator = input_str("Чтец: ")
    genre = input_str("Жанр: ")
    hours = input_int("Часы: ")
    minutes = input_int("Минуты: ")
    speed = input_float("Скорость прослушивания: ", min_value=0.0)

    ok, msg = Audiobook.check_speed(speed)
    print(msg)
    if not ok:
        print("Запись не добавлена.")
        return

    book = add_audiobook(books, title, author, narrator,
                         genre, hours, minutes, speed)
    save_audiobooks(books)
    print(f"Книга «{book.title}» добавлена (ID {book.id}).")


def cmd_find(books: list[Audiobook]) -> None:
    """Найти книги по подстроке."""
    query = input_str("Что искать: ")
    show_audiobooks(find_audiobooks(books, query))


def cmd_filter(books: list[Audiobook]) -> None:
    """Фильтр по жанру."""
    genre = input_str("Жанр: ")
    show_audiobooks(filter_by_genre(books, genre))


def cmd_sort(books: list[Audiobook]) -> None:
    """Сортировка по длительности."""
    show_audiobooks(sort_audiobooks(books))


def cmd_stats(books: list[Audiobook]) -> None:
    """Статистика коллекции."""
    stats = get_statistics(books)
    print(f"Всего книг: {stats['count']}")
    print(f"Прослушано: {stats['finished']}")
    print("Общее время: "
          f"{Audiobook.format_duration(stats['total_minutes'])}")
    print("Средняя длительность: "
          f"{Audiobook.format_duration(stats['avg_minutes'])}")


def cmd_delete(books: list[Audiobook]) -> None:
    """Удалить книгу по ID."""
    book_id = input_int("ID книги для удаления: ")
    if delete_audiobook(books, book_id):
        save_audiobooks(books)
        print("Удалено.")
    else:
        print("Книга с таким ID не найдена.")


def cmd_mark_finished(books: list[Audiobook]) -> None:
    """Отметить книгу как прослушанную."""
    book_id = input_int("ID книги: ")
    for b in books:
        if b.id == book_id:
            b.mark_finished()
            save_audiobooks(books)
            print(f"Книга «{b.title}» отмечена как прослушанная.")
            return
    print("Книга не найдена.")


def cmd_plan(books: list[Audiobook]) -> None:
    """Посчитать дни прослушивания."""
    book_id = input_int("ID книги: ")
    per_day = input_float("Сколько часов в день слушаете: ",
                          min_value=0.0)
    for b in books:
        if b.id == book_id:
            real = Audiobook.format_duration(b.real_minutes)
            print(f"Реальное время: {real}")
            print(f"При {per_day} ч/день: примерно "
                  f"{b.days_to_listen(per_day)} дн.")
            return
    print("Книга не найдена.")


def cmd_add_user(users: list[User]) -> None:
    """Добавить пользователя."""
    name = input_str("Имя: ")
    email = input_str("Email: ")
    user = add_user(users, name, email)
    save_users(users)
    print(f"Пользователь {user} добавлен.")


def cmd_find_user(users: list[User]) -> None:
    """Найти пользователя."""
    query = input_str("Что искать: ")
    show_users(find_user(users, query))


def print_menu() -> None:
    """Главное меню."""
    print()
    print("=" * 45)
    print("  СЕРВИС УЧЁТА КОЛЛЕКЦИИ АУДИОКНИГ")
    print("=" * 45)
    print("1. Показать все книги")
    print("2. Добавить книгу")
    print("3. Найти по названию")
    print("4. Фильтр по жанру")
    print("5. Сортировка по длительности")
    print("6. Статистика")
    print("7. Посчитать дни прослушивания")
    print("8. Отметить как прослушанную")
    print("9. Удалить книгу")
    print("--- Пользователи ---")
    print("10. Показать пользователей")
    print("11. Добавить пользователя")
    print("12. Найти пользователя")
    print("0. Выход")


def main() -> None:
    """Главный цикл меню."""
    books = load_audiobooks()
    users = load_users()
    print(f"Загружено книг: {len(books)}, "
          f"пользователей: {len(users)}")

    actions = {
        "1": lambda: show_audiobooks(books),
        "2": lambda: cmd_add_book(books),
        "3": lambda: cmd_find(books),
        "4": lambda: cmd_filter(books),
        "5": lambda: cmd_sort(books),
        "6": lambda: cmd_stats(books),
        "7": lambda: cmd_plan(books),
        "8": lambda: cmd_mark_finished(books),
        "9": lambda: cmd_delete(books),
        "10": lambda: show_users(users),
        "11": lambda: cmd_add_user(users),
        "12": lambda: cmd_find_user(users),
    }

    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "0":
            print("До встречи!")
            break

        action = actions.get(choice)
        if action is None:
            print("Неизвестная команда.")
            continue

        try:
            action()
        except Exception as e:
            print(f"Ошибка выполнения: {e}")


if __name__ == "__main__":
    main()
