"""Lesson 5 solutions - try the exercises yourself before reading this!"""


def describe_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def ticket_price(age):
    if age < 5:
        return 0
    elif age < 18:
        return 8
    elif age < 65:
        return 12
    else:
        return 9


def shipping_cost(weight_kg, is_member):
    if is_member:
        return 0
    if weight_kg <= 1:
        return 5
    if weight_kg <= 5:
        return 10
    return 20


def is_valid_username(name):
    return 3 <= len(name) <= 15 and name.isalnum()


def day_type(day):
    if day.lower() in ("saturday", "sunday"):
        return "weekend"
    return "weekday"
