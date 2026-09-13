import math

print("Сервис учета коллекции аудиокниг")
print("-" * 45)
print("Добавление новой аудиокниги")


def check_speed(speed):
    if speed <= 0:
        return False, "Ошибка. Скорость некорректна!"
    if speed > 3:
        return False, "Ошибка. Слишком высокая скорость!"
    return True, "Скорость корректна."


def format_duration(total_minutes):
    hours = int(total_minutes // 60)
    minutes = int(round(total_minutes % 60))
    if hours == 0:
        return f"{minutes} мин"
    return f"{hours} ч {minutes} мин"


def count_days(total_minutes, per_day_hours):
    if per_day_hours <= 0 or total_minutes <= 0:
        return -1
    minutes_per_day = per_day_hours * 60
    return math.ceil(total_minutes / minutes_per_day)


title = input("Название книги: ").strip()
author = input("Автор: ").strip()
narrator = input("Чтец: ").strip()
genre = input("Жанр: ").strip()

hours_str = input("Длительность (часы): ").strip()
minutes_str = input("Длительность (минуты): ").strip()
speed_str = input("Скорость прослушивания: ").strip()
per_day_str = input("Сколько часов в день слушаете? ").strip()

hours = int(hours_str)
minutes = int(minutes_str)
speed = float(speed_str)
per_day = float(per_day_str)

error = False

if title == "" or author == "":
    print("Ошибка. Пустая строка!")
    error = True

if hours < 0 or minutes < 0:
    print("Ошибка. Отрицательное значение!")
    error = True

if minutes >= 60:
    hours = hours + minutes // 60
    minutes = minutes % 60
    print(f"Время приведено к виду {hours} ч {minutes} мин.")

ok, msg = check_speed(speed)
print(msg)
if not ok:
    error = True

if error:
    print("\nЗапись не добавлена. Исправьте данные!")
else:
    total_minutes = hours * 60 + minutes
    real_minutes = total_minutes / speed

    duration_text = format_duration(total_minutes)
    real_time_text = format_duration(real_minutes)

    days = count_days(real_minutes, per_day)

    print()
    print("Карточка аудиокниги")
    print("-" * 45)
    print(f"Название: {title}")
    print(f"Автор: {author}")
    print(f"Чтец: {narrator}")
    print(f"Жанр: {genre}")
    print(f"Длительность: {duration_text} ({total_minutes} мин)")
    print(f"Скорость: x{speed}")
    print(f"Время прослушивания: {real_time_text}")
    print(f"При {per_day} ч в день: примерно {days} дн.")
    print("Запись успешно добавлена")