"""Lesson 4 solutions - try the exercises yourself before reading this!"""


def circle_area(radius):
    return 3.14159 * radius ** 2


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def is_even(n):
    return n % 2 == 0


def hours_and_minutes(total_minutes):
    return f"{total_minutes // 60}h {total_minutes % 60}m"


def split_bill(total, people):
    return round(total / people, 2)


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def in_range(x, low, high):
    return low <= x <= high


def last_digit(n):
    return n % 10


def drop_last_digit(n):
    return n // 10
