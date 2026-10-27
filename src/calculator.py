def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b

def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b

def divide(a, b):
    """Возвращает частное от деления."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def power(a, b):
    """Возводит число a в степень b."""
    return a ** b

def modulo(a, b):
    return a % b
