"""Lesson 6 exercises - Loops

Replace each `pass` with your code, then check:

    pytest tests/test_06_loops.py
"""


def sum_to(n):
    """Return 1 + 2 + 3 + ... + n.
    sum_to(4) -> 10
    sum_to(0) -> 0
    """
    pass  # TODO


def factorial(n):
    """Return n! (n factorial): 1 * 2 * 3 * ... * n.
    factorial(5) -> 120
    factorial(0) -> 1   (by definition)
    """
    pass  # TODO


def count_vowels(text):
    """Count the vowels (a, e, i, o, u) in the text, in any capitalisation.
    count_vowels("Hello World") -> 3
    """
    pass  # TODO


def countdown(n):
    """Return a countdown as one line of text.
    countdown(3) -> "3 2 1 Liftoff!"
    countdown(0) -> "Liftoff!"
    Hint: build the text up in a variable, one number at a time.
    """
    pass  # TODO


def star_triangle(rows):
    """Return a triangle of stars as one string with a line break between rows
    (no line break after the last row).
    star_triangle(3) -> "*\\n**\\n***"   which prints as:
        *
        **
        ***
    """
    pass  # TODO


def smallest_power_of_two_above(limit):
    """Return the smallest power of two (1, 2, 4, 8, 16, ...) that is strictly
    greater than `limit`.
    smallest_power_of_two_above(100) -> 128
    smallest_power_of_two_above(128) -> 256
    Hint: a while loop that keeps doubling.
    """
    pass  # TODO


def digit_sum(n):
    """Add up the digits of a whole number (0 or more).
    digit_sum(1234) -> 10
    Hint: n % 10 is the last digit, n // 10 removes it. Loop until n is 0.
    """
    pass  # TODO


def collatz_steps(n):
    """Count the steps for n to reach 1 under these rules (n is 1 or more):
      if n is even, halve it;  if n is odd, replace it with 3*n + 1.
    collatz_steps(6) -> 8   (6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1)
    collatz_steps(1) -> 0
    """
    pass  # TODO
