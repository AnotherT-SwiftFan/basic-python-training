"""Lesson 3 exercises - Strings

Replace each `pass` with your code (use `return` to give the answer back), then check:

    pytest tests/test_03_strings.py
"""


def shout(text):
    """Return the text in capitals with an exclamation mark on the end.
    shout("hello") -> "HELLO!"
    """
    pass  # TODO


def first_and_last(text):
    """Return the first and last characters joined together.
    first_and_last("python") -> "pn"
    """
    pass  # TODO


def clean_name(raw):
    """Remove spaces from both ends and capitalise each word.
    clean_name("  ada LOVELACE ") -> "Ada Lovelace"
    """
    pass  # TODO


def reverse_text(text):
    """Return the text backwards.
    reverse_text("abc") -> "cba"
    """
    pass  # TODO


def count_letter(text, letter):
    """Count how many times `letter` appears in `text`, ignoring capitals.
    count_letter("Banana", "a") -> 3
    """
    pass  # TODO


def make_email(first, last):
    """Build a lowercase work email: first.last@example.com
    make_email("Ada", "Lovelace") -> "ada.lovelace@example.com"
    """
    pass  # TODO


def format_price(amount):
    """Format a number as a price with a $ sign, thousands separators and 2 decimals.
    format_price(1234.5) -> "$1,234.50"
    """
    pass  # TODO


def is_palindrome(text):
    """Return True if the text reads the same forwards and backwards,
    ignoring capitals and spaces.
    is_palindrome("level") -> True
    is_palindrome("A man a plan a canal Panama") -> True
    is_palindrome("Python") -> False

    Hint: `==` compares two values and gives back True or False.
    """
    pass  # TODO


def initials(full_name):
    """Return the capital initials of the FIRST and LAST word of a name.
    initials("Ada Lovelace") -> "AL"
    initials("grace brewster hopper") -> "GH"

    Hint: split() gives you a list of words, and lists have indexes like strings do.
    """
    pass  # TODO
