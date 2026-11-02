"""Lesson 9 - Functions

Run this file. Then try the debugger: click left of a line number inside a function
to set a breakpoint, press F5, and step through with F10 (over) and F11 (into).
"""


# --- Defining and calling -----------------------------------------------------
def greet(name):
    return f"Hello, {name}!"


message = greet("Ada")
print(message)
print(greet("Grace"))


# --- return vs print ----------------------------------------------------------
def add_print(a, b):
    print(a + b)             # shows the answer but gives nothing back


def add_return(a, b):
    return a + b             # gives the answer back to the caller


total = add_return(2, 3) * 10
print("total:", total)       # 50

result = add_print(2, 3)     # prints 5
print("add_print returned:", result)   # None


# --- Defaults and keyword arguments -------------------------------------------
def greet_with(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


print(greet_with("Ada"))
print(greet_with("Ada", "Welcome"))
print(greet_with("Ada", punctuation="?"))
print(greet_with(greeting="Hi", name="Bo"))


# --- Returning several values -------------------------------------------------
def min_and_max(numbers):
    return min(numbers), max(numbers)       # a tuple


low, high = min_and_max([4, 9, 2, 7])
print("low:", low, "high:", high)


# --- Docstrings: hover over area() in VS Code to see this ---------------------
def area(width, height):
    """Return the area of a rectangle."""
    return width * height


print(area(3, 4))
print(area.__doc__)


# --- Scope --------------------------------------------------------------------
def make_total():
    local_total = 10          # only exists inside this function
    return local_total


print(make_total())
# print(local_total)          # <- uncomment: NameError, it doesn't exist out here


# --- Small functions working together -----------------------------------------
def is_even(n):
    return n % 2 == 0


def count_evens(numbers):
    count = 0
    for n in numbers:
        if is_even(n):
            count += 1
    return count


print(count_evens([1, 2, 3, 4, 5, 6]))     # 3


# --- Functions are values -----------------------------------------------------
def apply_twice(func, value):
    return func(func(value))


def add_one(x):
    return x + 1


print(apply_twice(add_one, 5))             # 7
print(sorted(["pear", "fig", "banana"], key=len))   # we pass len itself, not len()


# --- Type hints (optional, but nice) ------------------------------------------
def repeat_greeting(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()


print(repeat_greeting("Ada", 2))


# --- The mutable default argument trap ----------------------------------------
def add_item_bad(item, items=[]):          # DON'T do this
    items.append(item)
    return items


print(add_item_bad("a"))                   # ['a']
print(add_item_bad("b"))                   # ['a', 'b']  <- the same list again!


def add_item_good(item, items=None):       # do this instead
    if items is None:
        items = []
    items.append(item)
    return items


print(add_item_good("a"))                  # ['a']
print(add_item_good("b"))                  # ['b']
