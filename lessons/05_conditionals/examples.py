"""Lesson 5 - Conditionals

Run this file, then change the starting values to make different branches run.
"""

# --- if / else ----------------------------------------------------------------
age = 20

if age >= 18:
    print("You can vote.")
else:
    print("Not yet.")

# --- if / elif / else (the first true branch wins) ----------------------------
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score {score} -> grade {grade}")

# --- Combining conditions -----------------------------------------------------
has_ticket = True

if has_ticket and age >= 18:
    print("Welcome to the show!")

name = "Ada"
if name == "Ada" or name == "Grace":
    print("A pioneer!")

# --- 'in' and 'not in' --------------------------------------------------------
day = "Saturday"
if day in ("Saturday", "Sunday"):
    print("It's the weekend.")

email = "ada.example.com"
if "@" not in email:
    print("That email address is missing an @")

# --- Truthiness: is there anything here? --------------------------------------
username = ""
if username:
    print(f"Hello, {username}")
else:
    print("Please enter a username")

shopping_cart = []
if not shopping_cart:
    print("Your cart is empty")

# --- Chained comparison -------------------------------------------------------
temperature = 22
if 18 <= temperature <= 25:
    print("Comfortable")

# --- Nested vs flat -----------------------------------------------------------
if has_ticket:
    if age >= 18:
        print("Nested check passed")

if has_ticket and age >= 18:
    print("Flat check passed (same result, easier to read)")

# --- Conditional expression (one-line choice) ---------------------------------
label = "adult" if age >= 18 else "minor"
print(label)

# --- Returning early from a function ------------------------------------------
def describe(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"


print(describe(-5), describe(0), describe(12))

# --- match (Python 3.10+) -----------------------------------------------------
command = "quit"
match command:
    case "start":
        print("Starting...")
    case "stop" | "quit":
        print("Stopping...")
    case _:
        print("Unknown command")

# --- The classic bug: "x == 1 or 2" is ALWAYS true ----------------------------
x = 5
print(bool(x == 1 or 2))        # True?! because "2" on its own is truthy
print(x == 1 or x == 2)         # False - this is what you meant
print(x in (1, 2))              # False - and this is even tidier
