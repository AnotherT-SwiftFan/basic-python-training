"""Lesson 12 exercises - Errors and Exceptions

Replace each `pass` with your code, then check:

    pytest tests/test_12_errors_and_exceptions.py
"""


def safe_int(text, default=0):
    """Convert text to an int. If it isn't a valid whole number, return `default`.
    safe_int("42") -> 42,  safe_int("abc") -> 0,  safe_int("abc", -1) -> -1
    """
    pass  # TODO


def safe_divide(a, b):
    """Return a / b, or None if b is zero. Use try/except (don't check b first)."""
    pass  # TODO


def get_item(items, index, default=None):
    """Return items[index], or `default` if that position doesn't exist.
    get_item(["a", "b"], 1) -> "b",  get_item(["a", "b"], 5) -> None
    """
    pass  # TODO


def read_int_file(path):
    """The file contains a single whole number, like "42". Return it as an int.
    If the file doesn't exist, return None.
    If the file exists but doesn't contain a valid number, DON'T catch the error:
    let the ValueError escape.
    """
    pass  # TODO


def validate_age(age):
    """Return `age` unchanged if it is from 0 to 150 inclusive.
    Otherwise raise a ValueError with the message "age must be between 0 and 150".
    """
    pass  # TODO


def parse_ints(texts):
    """Convert a list of strings to a list of ints, skipping any that aren't
    valid whole numbers.
    parse_ints(["1", "two", "3", ""]) -> [1, 3]
    """
    pass  # TODO


def withdraw(balance, amount):
    """Return the new balance after taking `amount` out of `balance`.
    Raise ValueError("amount must be positive") if amount is zero or negative.
    Raise ValueError("insufficient funds") if amount is more than the balance.
    """
    pass  # TODO
