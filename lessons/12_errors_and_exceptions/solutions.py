"""Lesson 12 solutions - try the exercises yourself before reading this!"""


def safe_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def get_item(items, index, default=None):
    try:
        return items[index]
    except IndexError:
        return default


def read_int_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        return None
    return int(text)          # a bad number raises ValueError, as the exercise asks


def validate_age(age):
    if not 0 <= age <= 150:
        raise ValueError("age must be between 0 and 150")
    return age


def parse_ints(texts):
    numbers = []
    for text in texts:
        try:
            numbers.append(int(text))
        except ValueError:
            continue
    return numbers


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount
