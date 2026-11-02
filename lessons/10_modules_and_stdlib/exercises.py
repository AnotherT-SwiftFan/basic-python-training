"""Lesson 10 exercises - Modules and the Standard Library

ADD THE IMPORTS YOU NEED at the top of this file (just below this comment),
then fill in each function:

    pytest tests/test_10_modules_and_stdlib.py
"""

# TODO: add your imports here


def hypotenuse(a, b):
    """Return the length of the longest side of a right-angled triangle
    with shorter sides a and b (Pythagoras: square root of a*a + b*b).
    hypotenuse(3, 4) -> 5.0
    Hint: the math module.
    """
    pass  # TODO


def round_up(x):
    """Round a number UP to the next whole number.
    round_up(2.1) -> 3,  round_up(5) -> 5,  round_up(-1.5) -> -1
    Hint: the math module.
    """
    pass  # TODO


def days_between(date_a, date_b):
    """Both dates are text like "2024-01-31" (year-month-day). Return how many days
    apart they are, as a positive whole number whichever way round they are given.
    days_between("2024-01-01", "2024-03-01") -> 60
    Hint: datetime.date.fromisoformat(), then subtract and use .days
    """
    pass  # TODO


def weekday_name(iso_date):
    """Return the name of the weekday for a date given as "YYYY-MM-DD".
    weekday_name("2024-01-01") -> "Monday"
    Hint: strftime("%A")
    """
    pass  # TODO


def roll_dice(sides, rolls):
    """Roll a die with `sides` sides `rolls` times and return the results as a list.
    Each roll is a random whole number from 1 to `sides` inclusive.
    roll_dice(6, 3) -> e.g. [4, 1, 6]
    Hint: the random module.
    """
    pass  # TODO


def most_common_word(text):
    """Return the word that appears most often (ignore capitals).
    most_common_word("the cat and the dog and the bird") -> "the"
    Hint: collections.Counter has a .most_common() method.
    """
    pass  # TODO
