"""Lesson 10 - Modules and the Standard Library

Run this file. It also imports my_helpers.py from the same folder.
"""

import math
import random
from collections import Counter
from datetime import date, timedelta

import my_helpers       # our own module: see my_helpers.py

# --- math ---------------------------------------------------------------------
print(math.sqrt(81))                    # 9.0
print(math.pi)
print(math.ceil(2.1), math.floor(2.9))  # 3 2
print(0.1 + 0.2 == 0.3)                 # False
print(math.isclose(0.1 + 0.2, 0.3))     # True: the right way to compare floats

# --- random -------------------------------------------------------------------
print(random.randint(1, 6))             # changes every run
print(random.choice(["rock", "paper", "scissors"]))

cards = ["A", "K", "Q", "J"]
random.shuffle(cards)                   # shuffles in place
print(cards)

random.seed(42)                         # same seed -> same "random" numbers
first = [random.randint(1, 100) for _ in range(3)]
random.seed(42)
second = [random.randint(1, 100) for _ in range(3)]
print(first == second)                  # True

# --- datetime -----------------------------------------------------------------
today = date.today()
print("today is", today)
print("in 30 days:", today + timedelta(days=30))
print(today.strftime("%A, %d %B %Y"))

new_year = date(2030, 1, 1)
print("days until 2030:", (new_year - today).days)

d = date.fromisoformat("2024-02-29")    # text -> date
print(d.year, d.month, d.day, d.strftime("%A"))

# --- collections.Counter ------------------------------------------------------
print(Counter("banana"))
print(Counter("the cat and the hat".split()).most_common(1))   # [('the', 2)]

# --- our own module -----------------------------------------------------------
print(my_helpers.GREETING)
print(my_helpers.double(21))
print(my_helpers.shout("modules are great"))

# __name__ is "__main__" when you run this file, and the file's name when imported
print("this file's __name__ is:", __name__)
print("my_helpers' __name__ is:", my_helpers.__name__)

# --- exploring a module -------------------------------------------------------
print(math.sqrt.__doc__)                # the same text help(math.sqrt) shows
print([name for name in dir(math) if name.startswith("c")])
