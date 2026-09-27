"""Класс Audiobook и функции работы с коллекцией аудиокниг."""

import math


class Audiobook:
    """Аудиокнига в коллекции пользователя."""

    def __init__(
        self,
        book_id: int,
        title: str,
        author: str,
        narrator: str,
        genre: str,
        hours: int,
        minutes: int,
        speed: float = 1.0,
        is_finished: bool = False,
    ) -> None:
        """Создать объект аудиокниги."""
        if minutes >= 60:
            hours += minutes // 60
            minutes = minutes % 60

        self.id = book_id
        self.title = title
        self.author = author
        self.narrator = narrator
        self.genre = genre
        self.hours = hours
        self.minutes = minutes
        self.speed = speed
        self.is_finished = is_finished

    @property
    def total_minutes(self) -> int:
        """Полная длительность книги в минутах."""
        return self.hours * 60 + self.minutes

    @property
    def real_minutes(self) -> float:
        """Реальное время с учётом скорости."""
        if self.speed <= 0:
            return float(self.total_minutes)
        return self.total_minutes / self.speed

    @staticmethod
    def check_speed(speed: float) -> tuple[bool, str]:
        """Проверить корректность скорости."""
        if speed <= 0:
            return False, "Ошибка. Скорость некорректна!"
        if speed > 3:
            return False, "Ошибка. Слишком высокая скорость (макс. 3.0)!"
        return True, "Скорость корректна."

    @staticmethod
    def format_duration(total_minutes: float) -> str:
        """Преобразовать минуты в строку 'X ч Y мин'."""
        hours = int(total_minutes // 60)
        minutes = int(round(total_minutes % 60))
        if hours == 0:
            return f"{minutes} мин"
        return f"{hours} ч {minutes} мин"

    @staticmethod
    def count_days(total_minutes: float, per_day_hours: float) -> int:
        """Посчитать, за сколько дней будет прослушана книга."""
        if per_day_hours <= 0 or total_minutes <= 0:
            return -1
        return math.ceil(total_minutes / (per_day_hours * 60))

    def mark_finished(self) -> None:
        """Отметить книгу как прослушанную."""
        self.is_finished = True

    def days_to_listen(self, per_day_hours: float) -> int:
        """За сколько дней будет прослушана эта книга."""
        return self.count_days(self.real_minutes, per_day_hours)

    def __str__(self) -> str:
        """Строковое представление книги."""
        status = "прослушано" if self.is_finished else "в процессе"
        duration = self.format_duration(self.total_minutes)
        return (f"[{self.id}] «{self.title}» — {self.author} "
                f"({duration}, чтец: {self.narrator}, "
                f"жанр: {self.genre}) [{status}]")

    def to_dict(self) -> dict:
        """Преобразовать объект в словарь для JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "narrator": self.narrator,
            "genre": self.genre,
            "hours": self.hours,
            "minutes": self.minutes,
            "speed": self.speed,
            "is_finished": self.is_finished,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Audiobook":
        """Создать объект Audiobook из словаря."""
        return cls(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            narrator=data["narrator"],
            genre=data["genre"],
            hours=data["hours"],
            minutes=data["minutes"],
            speed=data.get("speed", 1.0),
            is_finished=data.get("is_finished", False),
        )


def add_audiobook(
    books: list[Audiobook],
    title: str,
    author: str,
    narrator: str,
    genre: str,
    hours: int,
    minutes: int,
    speed: float = 1.0,
) -> Audiobook:
    """Создать объект Audiobook и добавить его в коллекцию."""
    new_id = 1
    if books:
        new_id = max(b.id for b in books) + 1

    book = Audiobook(new_id, title, author, narrator,
                     genre, hours, minutes, speed)
    books.append(book)
    return book


def find_audiobooks(
    books: list[Audiobook], query: str
) -> list[Audiobook]:
    """Найти книги по подстроке в названии."""
    q = query.lower()
    return [b for b in books if q in b.title.lower()]


def filter_by_genre(
    books: list[Audiobook], genre: str
) -> list[Audiobook]:
    """Отобрать книги по жанру."""
    g = genre.lower()
    return [b for b in books if b.genre.lower() == g]


def sort_audiobooks(
    books: list[Audiobook]
) -> list[Audiobook]:
    """Отсортировать книги по длительности."""
    return sorted(books, key=lambda b: b.total_minutes)


def get_statistics(books: list[Audiobook]) -> dict:
    """Собрать статистику по коллекции."""
    if not books:
        return {"count": 0, "total_minutes": 0,
                "avg_minutes": 0, "finished": 0}
    total = sum(b.total_minutes for b in books)
    finished = sum(1 for b in books if b.is_finished)
    return {
        "count": len(books),
        "total_minutes": total,
        "avg_minutes": round(total / len(books)),
        "finished": finished,
    }


def delete_audiobook(
    books: list[Audiobook], book_id: int
) -> bool:
    """Удалить книгу по id."""
    for i, b in enumerate(books):
        if b.id == book_id:
            books.pop(i)
            return True
    return False
