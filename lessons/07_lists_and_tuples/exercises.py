"""Lesson 7 exercises - Lists and Tuples

Replace each `pass` with your code, then check:

    pytest tests/test_07_lists_and_tuples.py
"""


def ends(items):
    """Return a NEW list containing just the first and last items.
    ends([1, 2, 3, 4]) -> [1, 4]
    (The list will have at least two items.)
    """
    pass  # TODO


def average(numbers):
    """Return the average (mean) of a list of numbers, or 0 if the list is empty.
    average([2, 4, 9]) -> 5.0
    """
    pass  # TODO


def remove_negatives(numbers):
    """Return a NEW list with the negative numbers left out (keep the order).
    remove_negatives([3, -1, 4, -5, 0]) -> [3, 4, 0]
    The original list must not be changed.
    """
    pass  # TODO


def second_largest(numbers):
    """Return the second-largest number. The list has at least 2 items, all different.
    second_largest([10, 40, 30, 20]) -> 30
    """
    pass  # TODO


def squares(n):
    """Return a list of the squares of 1 to n.
    squares(4) -> [1, 4, 9, 16]
    squares(0) -> []
    """
    pass  # TODO


def rotate_left(items):
    """Return a NEW list with the first item moved to the end.
    rotate_left([1, 2, 3, 4]) -> [2, 3, 4, 1]
    rotate_left([]) -> []
    Hint: slicing.
    """
    pass  # TODO


def min_max(numbers):
    """Return a tuple of (smallest, largest).
    min_max([3, 9, 1, 7]) -> (1, 9)
    """
    pass  # TODO


def without_duplicates(items):
    """Return a NEW list with repeated items removed, keeping the first of each
    and the original order.
    without_duplicates([3, 1, 3, 2, 1]) -> [3, 1, 2]
    Hint: build a result list, and only append items that aren't already in it.
    """
    pass  # TODO


def lengths(words):
    """Return a list with the length of each word.
    lengths(["hi", "python"]) -> [2, 6]
    """
    pass  # TODO
