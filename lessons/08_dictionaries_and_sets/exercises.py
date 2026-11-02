"""Lesson 8 exercises - Dictionaries and Sets

Replace each `pass` with your code, then check:

    pytest tests/test_08_dictionaries_and_sets.py
"""


def get_phone(contacts, name):
    """`contacts` maps names to phone numbers. Return the phone number for `name`,
    or the text "unknown" if the name isn't there.
    get_phone({"Ada": "555-1234"}, "Bo") -> "unknown"
    Hint: dict.get() takes a default value.
    """
    pass  # TODO


def count_words(text):
    """Return a dictionary of how many times each word appears. Ignore capitals.
    count_words("The cat and the hat") -> {"the": 2, "cat": 1, "and": 1, "hat": 1}
    """
    pass  # TODO


def invert(d):
    """Swap keys and values. All the values are different.
    invert({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
    """
    pass  # TODO


def unique_letters(text):
    """Return how many different letters appear in the text, ignoring capitals,
    spaces, digits and punctuation.
    unique_letters("Hello, World!") -> 7   (h, e, l, o, w, r, d)
    Hint: a set, and str.isalpha().
    """
    pass  # TODO


def common_items(a, b):
    """Return a sorted list of the items that appear in BOTH lists.
    common_items([1, 2, 3, 4], [3, 4, 5]) -> [3, 4]
    """
    pass  # TODO


def cart_total(prices, cart):
    """`prices` maps item names to the price of one. `cart` maps item names to
    how many were bought. Return the total cost.
    cart_total({"apple": 0.5, "bread": 2.0}, {"apple": 4, "bread": 1}) -> 4.0
    """
    pass  # TODO


def group_by_first_letter(words):
    """Group lowercase words by their first letter. Keep the original order of words.
    group_by_first_letter(["apple", "avocado", "banana"])
        -> {"a": ["apple", "avocado"], "b": ["banana"]}
    """
    pass  # TODO
