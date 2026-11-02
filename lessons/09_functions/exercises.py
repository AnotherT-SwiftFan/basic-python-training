"""Lesson 9 exercises - Functions

This time you'll write the whole function signature in a few places. Where a
`def` line is given, keep it exactly as it is and replace `pass`.

    pytest tests/test_09_functions.py
"""


def greet(name, greeting="Hello"):
    """Return "<greeting>, <name>!"
    greet("Ada") -> "Hello, Ada!"
    greet("Ada", "Welcome") -> "Welcome, Ada!"
    """
    pass  # TODO


def area_of_rectangle(width, height):
    """Return width times height. (Use return, don't print.)"""
    pass  # TODO


def divide_with_remainder(a, b):
    """Return BOTH the whole-number quotient and the remainder as a tuple.
    divide_with_remainder(10, 3) -> (3, 1)
    """
    pass  # TODO


def bmi(weight_kg, height_m):
    """Body mass index: weight divided by height squared, rounded to 1 decimal place.
    bmi(81, 1.8) -> 25.0
    The tests also call this with keyword arguments: bmi(height_m=1.8, weight_kg=81)
    """
    pass  # TODO


def format_name(first, last, title=""):
    """Join the parts of a name with spaces. Leave out the title if it's empty.
    format_name("Ada", "Lovelace") -> "Ada Lovelace"
    format_name("Ada", "Lovelace", title="Dr.") -> "Dr. Ada Lovelace"
    """
    pass  # TODO


def is_prime(n):
    """Return True if n is a prime number (a whole number above 1 that only
    divides evenly by 1 and itself).
    is_prime(7) -> True,  is_prime(8) -> False,  is_prime(1) -> False
    Hint: try dividing by 2, 3, ... up to n - 1. If any divide evenly, it's not prime.
    """
    pass  # TODO


def primes_up_to(n):
    """Return a list of all the prime numbers from 2 up to and including n.
    primes_up_to(10) -> [2, 3, 5, 7]
    Hint: reuse your is_prime function!
    """
    pass  # TODO


def apply_twice(func, value):
    """Call func on value, then call func on that result, and return it.
    If add_one(x) returns x + 1, then apply_twice(add_one, 5) -> 7
    """
    pass  # TODO
