"""Точка входа: меню сервиса учёта коллекции аудиокниг."""

from audiobooks import (
    add_audiobook,
    check_speed,
    count_days,
    delete_audiobook,
    filter_by_genre,
    find_audiobooks,
    format_duration,
    get_statistics,
    sort_audiobooks,
)
from storage import load_audiobooks, save_audiobooks
from utils import input_float, input_int, input_str


def show_audiobooks(books: list[dict]) -> None:
    """Вывести список книг в виде таблицы."""
    if not books:
        print("Коллекция пуста.")
        return
    print("-" * 60)
    print(f"{'ID':<4}{'Название':<25}{'Автор':<20}{'Жанр':<15}")
    print("-" * 60)
    for b in books:
        duration = format_duration(b["hours"] * 60 + b["minutes"])
        print(f"{b['id']:<4}{b['title'][:23]:<25}{b['author'][:18]:<20}"
              f"{b['genre'][:13]:<15}")
        print(f"    {duration}, чтец: {b['narrator']}")


def cmd_add(books: list[dict]) -> None:
    """Обработать команду добавления книги."""
    title = input_str("Название: ")
    author = input_str("Автор: ")
    narrator = input_str("Чтец: ")
    genre = input_str("Жанр: ")
    hours = input_int("Часы: ")
    minutes = input_int("Минуты: ")
    speed = input_float("Скорость прослушивания: ", min_value=0.0)

    ok, msg = check_speed(speed)
    print(msg)
    if not ok:
        print("Запись не добавлена.")
        return

    book = add_audiobook(books, title, author, narrator, genre,
                         hours, minutes, speed)
    save_audiobooks(books)
    print(f"Книга «{book['title']}» добавлена (ID {book['id']}).")


def cmd_find(books: list[dict]) -> None:
    """Найти книги по подстроке."""
    query = input_str("Что искать: ")
    found = find_audiobooks(books, query)
    show_audiobooks(found)


def cmd_filter(books: list[dict]) -> None:
    """Фильтр по жанру."""
    genre = input_str("Жанр: ")
    found = filter_by_genre(books, genre)
    show_audiobooks(found)


def cmd_sort(books: list[dict]) -> None:
    """Показать книги, отсортированные по длительности."""
    show_audiobooks(sort_audiobooks(books))


def cmd_stats(books: list[dict]) -> None:
    """Показать статистику коллекции."""
    stats = get_statistics(books)
    print(f"Всего книг: {stats['count']}")
    print(f"Общее время: {format_duration(stats['total_minutes'])}")
    print(f"Средняя длительность: {format_duration(stats['avg_minutes'])}")


def cmd_delete(books: list[dict]) -> None:
    """Удалить книгу по ID."""
    book_id = input_int("ID книги для удаления: ")
    if delete_audiobook(books, book_id):
        save_audiobooks(books)
        print("Удалено.")
    else:
        print("Книга с таким ID не найдена.")


def cmd_plan(books: list[dict]) -> None:
    """Посчитать дни прослушивания для выбранной книги."""
    book_id = input_int("ID книги: ")
    per_day = input_float("Сколько часов в день слушаете: ", min_value=0.0)
    for b in books:
        if b["id"] == book_id:
            total = b["hours"] * 60 + b["minutes"]
            real = total / b["speed"]
            days = count_days(real, per_day)
            print(f"Реальное время: {format_duration(real)}")
            print(f"При {per_day} ч/день: примерно {days} дн.")
            return
    print("Книга не найдена.")


def print_menu() -> None:
    """Вывести главное меню."""
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
    print("8. Удалить книгу")
    print("0. Выход")


def main() -> None:
    """Главный цикл меню."""
    books = load_audiobooks()
    print(f"Загружено книг: {len(books)}")

    actions = {
        "1": lambda: show_audiobooks(books),
        "2": lambda: cmd_add(books),
        "3": lambda: cmd_find(books),
        "4": lambda: cmd_filter(books),
        "5": lambda: cmd_sort(books),
        "6": lambda: cmd_stats(books),
        "7": lambda: cmd_plan(books),
        "8": lambda: cmd_delete(books),
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