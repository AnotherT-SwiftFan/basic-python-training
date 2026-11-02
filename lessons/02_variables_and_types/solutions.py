"""Lesson 2 solutions - try the exercises yourself before reading this!"""

language = "Python"
release_year = 1991
pi_approx = 3.14
is_fun = True

x = 5
y = 10
temp = x      # keep x's old value safe
x = y
y = temp
# Python also lets you do it in one line:  x, y = y, x


def add_number_strings(a, b):
    return int(a) + int(b)


def make_label(name, age):
    return f"{name} is {age} years old"


def is_truthy(value):
    return bool(value)
