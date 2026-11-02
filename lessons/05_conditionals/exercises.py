"""Lesson 5 exercises - Conditionals

Replace each `pass` with your code (use `return` to give the answer back), then check:

    pytest tests/test_05_conditionals.py
"""


def describe_number(n):
    """Return "positive", "negative" or "zero".
    describe_number(-3) -> "negative"
    """
    pass  # TODO


def grade(score):
    """Turn a score into a letter grade:
    90 or more -> "A", 80-89 -> "B", 70-79 -> "C", 60-69 -> "D", below 60 -> "F"
    """
    pass  # TODO


def fizzbuzz(n):
    """The classic. Return:
      "FizzBuzz" if n is divisible by both 3 and 5,
      "Fizz" if divisible by 3 only,
      "Buzz" if divisible by 5 only,
      otherwise the number itself as text, e.g. "7".
    Hint: check the "both" case first!
    """
    pass  # TODO


def ticket_price(age):
    """Return the ticket price in whole dollars:
      under 5      -> 0   (free)
      5 to 17      -> 8
      18 to 64     -> 12
      65 and over  -> 9
    """
    pass  # TODO


def shipping_cost(weight_kg, is_member):
    """Members ship free (0). Everyone else pays by weight:
      up to and including 1 kg  -> 5
      over 1 kg up to 5 kg      -> 10
      over 5 kg                 -> 20
    """
    pass  # TODO


def is_valid_username(name):
    """A valid username is 3 to 15 characters long (inclusive) and contains
    only letters and digits (no spaces or symbols).
    Hint: the string method .isalnum() checks the "letters and digits" part.
    """
    pass  # TODO


def day_type(day):
    """Return "weekend" for Saturday or Sunday (in any capitalisation),
    otherwise "weekday".
    day_type("sunday") -> "weekend"
    """
    pass  # TODO
