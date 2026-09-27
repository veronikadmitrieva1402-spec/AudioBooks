"""Класс User и функции работы с пользователями."""


class User:
    """Пользователь сервиса учёта аудиокниг."""

    def __init__(self, user_id: int, name: str, email: str) -> None:
        """Создать объект пользователя."""
        self.id = user_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        """Строковое представление пользователя."""
        return f"[{self.id}] {self.name} <{self.email}>"

    def to_dict(self) -> dict:
        """Преобразовать в словарь для JSON."""
        return {"id": self.id, "name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Создать пользователя из словаря."""
        return cls(
            user_id=data["id"],
            name=data["name"],
            email=data["email"],
        )


def add_user(users: list[User], name: str, email: str) -> User:
    """Создать и добавить пользователя в коллекцию."""
    new_id = 1
    if users:
        new_id = max(u.id for u in users) + 1
    user = User(new_id, name, email)
    users.append(user)
    return user


def find_user(users: list[User], query: str) -> list[User]:
    """Найти пользователей по имени или email."""
    q = query.lower()
    return [u for u in users
            if q in u.name.lower() or q in u.email.lower()]
