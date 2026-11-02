"""Lesson 2 exercises - Variables and Types

Replace each `None` or `pass` with real code, then check your work:

    pytest tests/test_02_variables_and_types.py
"""

# --- Part 1: create variables -------------------------------------------------

# 1. Set `language` to the text "Python".
language = None  # TODO

# 2. Python was first released in 1991. Set `release_year` to that whole number.
release_year = None  # TODO

# 3. Set `pi_approx` to the decimal number 3.14.
pi_approx = None  # TODO

# 4. Python is fun! Set `is_fun` to the boolean value True.
is_fun = None  # TODO

# 5. Swap the values of x and y so that x ends up as 10 and y ends up as 5.
#    Write your code on the lines below the two assignments.
#    Hint: you can use a third variable to hold one value while you swap.
x = 5
y = 10
# TODO: your swap code here


# --- Part 2: convert between types --------------------------------------------

def add_number_strings(a, b):
    """a and b are text containing whole numbers, like "3" and "4".
    Return their sum as an int (so "3" and "4" give 7, not "34").
    """
    pass  # TODO


def make_label(name, age):
    """Return text like  "Ada is 36 years old"  built from a name (str) and an age (int).
    Hint: you'll need str(), or an f-string.
    """
    pass  # TODO


def is_truthy(value):
    """Return True if Python treats `value` as true, otherwise False.
    Hint: there's a built-in for this. Look at the "Truthiness" part of the lesson.
    """
    pass  # TODO
