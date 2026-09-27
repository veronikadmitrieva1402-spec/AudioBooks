"""Вспомогательные функции для безопасного ввода данных."""


def input_str(prompt: str) -> str:
    """Запросить непустую строку. Повторять запрос при пустом вводе."""
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Ошибка: строка не может быть пустой.")
            continue
        return value


def input_int(prompt: str, allow_negative: bool = False) -> int:
    """Запросить целое число. Повторять при ошибке ввода."""
    while True:
        try:
            value = int(input(prompt).strip())
            if not allow_negative and value < 0:
                print("Ошибка: число не может быть отрицательным.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите целое число.")


def input_float(prompt: str, min_value: float = 0.0) -> float:
    """Запросить дробное число. Повторять при ошибке ввода."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= min_value:
                print(f"Ошибка: число должно быть больше {min_value}.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите число (например, 1.5).")