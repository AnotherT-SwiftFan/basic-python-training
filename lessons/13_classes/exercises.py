"""Lesson 13 exercises - Classes

Each exercise is a class with `pass` placeholders. Replace them with real code.
Remember: store data on `self` in __init__, and give every method `self` as its
first parameter.

    pytest tests/test_13_classes.py
"""


class Rectangle:
    """A rectangle with a width and a height."""

    def __init__(self, width, height):
        pass  # TODO: store width and height on self

    def area(self):
        """Return width * height."""
        pass  # TODO

    def perimeter(self):
        """Return the total length around the rectangle."""
        pass  # TODO

    def is_square(self):
        """Return True if width equals height."""
        pass  # TODO


class ClickCounter:
    """A counter that starts at 0."""

    def __init__(self):
        pass  # TODO: start self.count at 0

    def click(self):
        """Add 1 to the count."""
        pass  # TODO

    def reset(self):
        """Put the count back to 0."""
        pass  # TODO


class BankAccount:
    """A bank account with an owner and a balance (which starts at 0 unless given)."""

    def __init__(self, owner, balance=0):
        pass  # TODO: store owner and balance

    def deposit(self, amount):
        """Add money. Raise ValueError("deposit must be positive") if amount <= 0."""
        pass  # TODO

    def withdraw(self, amount):
        """Take money out.
        Raise ValueError("withdrawal must be positive") if amount <= 0.
        Raise ValueError("insufficient funds") if amount is more than the balance.
        """
        pass  # TODO

    def __str__(self):
        """Return text like "Ada: $100.00" (2 decimals, thousands separators)."""
        pass  # TODO


class Animal:
    """Any animal. It has a name and makes a sound."""

    def __init__(self, name):
        pass  # TODO: store name

    def speak(self):
        """The generic sound is "..." """
        pass  # TODO

    def describe(self):
        """Return text like "Rex says Woof!" using this animal's name and its speak()."""
        pass  # TODO


class Dog(Animal):
    """A dog. Only speak() needs to change: it should return "Woof!" """

    pass  # TODO: override speak (replace this `pass`)


class Cat(Animal):
    """A cat. Its speak() should return "Meow!" """

    pass  # TODO: override speak (replace this `pass`)


class Stack:
    """A stack: last in, first out (like a pile of plates).
    Keep the items in a list stored on self.
    """

    def __init__(self):
        pass  # TODO

    def push(self, item):
        """Put an item on top of the stack."""
        pass  # TODO

    def pop(self):
        """Remove and return the top item. Raise IndexError("stack is empty") if empty."""
        pass  # TODO

    def peek(self):
        """Return the top item WITHOUT removing it. Raise IndexError("stack is empty") if empty."""
        pass  # TODO

    def is_empty(self):
        """Return True if there are no items."""
        pass  # TODO

    def __len__(self):
        """Make len(stack) work: return the number of items."""
        pass  # TODO
