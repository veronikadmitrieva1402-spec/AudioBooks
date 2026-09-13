import math 

print(" Сервис учета коллекции аудиокниг")
print("-" * 45)
print("Добавление новой аудиокниги")

title = input("Название книги: ").strip()
author = input("Автор: ").strip()
narrator = input("Чтец: ").strip()
genre = input("Жанр: ").strip()

hours_str = input("Длительность (часы): ").strip()
minutes_str = input("Длительность (минуты): ").strip()
speed_str = input("Скорость прослушивания: ").strip()

hours = int(hours_str)
minutes = int(minutes_str)
speed = float(speed_str)

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
    print("Время имеет вид {hours} ч {minutes} мин.")

if speed <= 0:
    print("Ошибка. Скорость некорректна!")
    error = True

if error:
    print("\nЗапись не добавлена. Исправьте данные!")
else:
    total_minutes = hours * 60 + minutes
    real_minutes = total_minutes / speed
    real_hours = real_minutes // 60
    real_min = round(real_minutes % 60)

    print()
    print("Карточка аудиокниги")
    print("-" * 45)
    print(f"Название: {title}")
    print(f"Автор: {author}")
    print(f"Чтец: {narrator}")
    print(f"Жанр: {genre}")
    print(f"Длительность: {hours} ч {minutes} мин"
          f"({total_minutes} мин)")
    print(f"Скорость: x{speed}")
    print(f"Время прослушивания: {int(real_hours)} ч {real_min} мин")
    print("Запись успешно добавлена")

