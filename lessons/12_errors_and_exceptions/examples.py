"""Lesson 12 - Errors and Exceptions

Run this file. Each section triggers a problem on purpose and handles it.
The last section asks you to type a number.
"""

# --- Seeing exceptions (all caught, so the script keeps going) ----------------
def show_error(label, action):
    """Run `action` (a function that takes no arguments) and report what goes wrong."""
    try:
        action()
    except Exception as error:
        print(f"{label:<18} -> {type(error).__name__}: {error}")


# `lambda: ...` is a tiny nameless function, handy for passing a bit of code along.
show_error("int('abc')", lambda: int("abc"))
show_error("[1, 2][5]", lambda: [1, 2][5])
show_error("{'a': 1}['b']", lambda: {"a": 1}["b"])
show_error("5 / 0", lambda: 5 / 0)
show_error("'abc'.push('d')", lambda: "abc".push("d"))

# --- Basic try / except -------------------------------------------------------
text = "forty-two"
try:
    number = int(text)
except ValueError:
    print(f"'{text}' isn't a whole number")

# --- Several except blocks, plus else and finally -----------------------------
def describe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  can't divide by zero")
    except TypeError:
        print("  both values must be numbers")
    else:
        print(f"  {a} / {b} = {result}")      # only runs when nothing went wrong
    finally:
        print("  (done)")                      # always runs


describe_division(10, 2)
describe_division(10, 0)
describe_division(10, "x")


# --- Raising your own exceptions ----------------------------------------------
def set_age(age):
    if age < 0:
        raise ValueError(f"age can't be negative, got {age}")
    return age


try:
    set_age(-5)
except ValueError as error:
    print("Rejected:", error)


# --- Look before you leap vs ask forgiveness ----------------------------------
data = {"colour": "blue"}

if "size" in data:                       # LBYL
    print(data["size"])
else:
    print("no size set")

try:                                     # EAFP
    print(data["size"])
except KeyError:
    print("no size set (via KeyError)")

print(data.get("size", "no size set (via .get)"))   # often the tidiest


# --- Debugging practice: there is a bug in this function ----------------------
# Put a breakpoint on the line starting `total = 0`, press F5, and step through
# with F10. Watch `total` and `n` in the Variables panel. Can you spot the bug?
def buggy_average(numbers):
    total = 0
    for n in numbers[1:]:                # <-- the bug is on this line
        total += n
    return total / len(numbers)


print("average of [10, 20, 30] is", buggy_average([10, 20, 30]), "(should be 20.0)")


# --- Validating input with a loop ---------------------------------------------
while True:
    answer = input("Pick a number from 1 to 10: ")
    try:
        picked = int(answer)
    except ValueError:
        print("Please type digits only.")
        continue
    if 1 <= picked <= 10:
        break
    print("That's outside 1-10.")

print(f"You picked {picked}. Nice choice!")
