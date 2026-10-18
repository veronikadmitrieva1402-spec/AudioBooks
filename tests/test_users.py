
from models import User
from models.users import add_user, find_user


def test_user_creation():
    user = User(1, "Иван Петров", "ivan@example.com")
    assert user.id == 1
    assert user.name == "Иван Петров"
    assert user.email == "ivan@example.com"


def test_user_str():
    user = User(1, "Иван Петров", "ivan@example.com")
    assert "Иван Петров" in str(user)
    assert "ivan@example.com" in str(user)


def test_add_user():
    users = []
    user = add_user(users, "Анна", "anna@example.com")
    assert len(users) == 1
    assert user.name == "Анна"
    assert user.id == 1


def test_find_user():
    users = []
    add_user(users, "Иван Петров", "ivan@example.com")
    add_user(users, "Анна Смирнова", "anna@example.com")
    assert len(find_user(users, "иван")) == 1
    assert len(find_user(users, "anna")) == 1