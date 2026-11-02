"""Lesson 9 solutions - try the exercises yourself before reading this!"""


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


def area_of_rectangle(width, height):
    return width * height


def divide_with_remainder(a, b):
    return a // b, a % b


def bmi(weight_kg, height_m):
    return round(weight_kg / height_m ** 2, 1)


def format_name(first, last, title=""):
    name = f"{first} {last}"
    if title:
        name = f"{title} {name}"
    return name


def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True


def primes_up_to(n):
    primes = []
    for candidate in range(2, n + 1):
        if is_prime(candidate):
            primes.append(candidate)
    return primes


def apply_twice(func, value):
    return func(func(value))
