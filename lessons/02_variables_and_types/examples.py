"""Lesson 2 - Variables and Types

Run this file. At the very end it asks you two questions, so answer them in the terminal.
"""

# --- Creating variables -------------------------------------------------------
name = "Ada"          # str
age = 36              # int
height_m = 1.65       # float
is_student = False    # bool
nickname = None       # NoneType: "nothing here yet"

print(name, age, height_m, is_student, nickname)

# --- Asking Python for a type -------------------------------------------------
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height_m))    # <class 'float'>
print(type(is_student))  # <class 'bool'>
print(type(nickname))    # <class 'NoneType'>

# --- Variables can change -----------------------------------------------------
score = 10
score = score + 5
print("score is now", score)

# A shorthand for "add to itself". More on this in Lesson 4.
score += 5
print("score is now", score)

# Several variables in one line
x, y = 3, 4
print(x, y)

# Swapping two variables (the Python way)
x, y = y, x
print("after swap:", x, y)

# --- Same-looking, different values -------------------------------------------
print(42 + 1)            # 43   (numbers add)
print("42" + "1")        # 421  (text joins together)
print(type(42), type("42"))

# --- Converting types ---------------------------------------------------------
print(int("42") + 1)     # 43
print(float("3.5") * 2)  # 7.0
print(str(42) + "!")     # 42!
print(int(3.9))          # 3  (the decimal part is chopped off, not rounded)
print(float(7))          # 7.0

# --- Truthiness: what does Python count as True or False? ---------------------
print(bool(0), bool(0.0), bool(""), bool(None))     # all False
print(bool(1), bool(-5), bool("hi"), bool("0"))     # all True (even the text "0")

# --- Constants (by convention, UPPER_CASE) ------------------------------------
MAX_ATTEMPTS = 3
print("You get", MAX_ATTEMPTS, "attempts")

# --- f-strings: the easy way to mix text and values ---------------------------
print(f"{name} is {age} years old and {height_m} m tall.")
print(f"Next year {name} will be {age + 1}.")

# --- Getting input (it's always text!) ----------------------------------------
your_name = input("What's your name? ")
age_text = input("How old are you? ")
your_age = int(age_text)    # input() gives text, so convert before doing maths
print(f"Hi {your_name}! In 10 years you'll be {your_age + 10}.")
