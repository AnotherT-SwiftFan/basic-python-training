"""Lesson 7 - Lists and Tuples

Run this file and follow how the list changes after each step.
"""

# --- Creating and reading lists -----------------------------------------------
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0], fruits[-1])        # apple cherry
print(fruits[1:])                   # ['banana', 'cherry']
print(fruits[::-1])                 # reversed copy
print(len(fruits))                  # 3

# --- Changing a list (unlike strings, lists are mutable) ----------------------
fruits[1] = "blueberry"
print(fruits)

fruits.append("date")
print("after append:", fruits)

fruits.insert(0, "avocado")
print("after insert:", fruits)

fruits.extend(["elderberry", "fig"])
print("after extend:", fruits)

fruits.remove("cherry")
print("after remove:", fruits)

last = fruits.pop()                 # removes AND returns the last item
print("popped:", last, "->", fruits)

del fruits[0]
print("after del:", fruits)

# --- Searching and measuring --------------------------------------------------
numbers = [4, 8, 15, 16, 23, 42]
print("blueberry" in fruits)        # True
print(numbers.index(15))            # 2
print(sum(numbers), min(numbers), max(numbers))
print("average:", sum(numbers) / len(numbers))

# --- Sorting ------------------------------------------------------------------
messy = [3, 1, 2]
print(sorted(messy))                # new sorted list: [1, 2, 3]
print(messy)                        # original untouched: [3, 1, 2]
messy.sort()                         # in-place; returns None
print(messy)                        # [1, 2, 3]
print(sorted(["pear", "fig", "apple"], reverse=True))
print(sorted(["pear", "fig", "apple"], key=len))   # sort by length

# --- Splitting and joining text -----------------------------------------------
words = "the quick brown fox".split()
print(words)
print(" ".join(words))

# --- Looping ------------------------------------------------------------------
for fruit in ["apple", "banana", "cherry"]:
    print("I like", fruit)

for position, fruit in enumerate(["apple", "banana", "cherry"], start=1):
    print(position, fruit)

for name, score in zip(["Ada", "Bo", "Cy"], [90, 85, 77]):
    print(f"{name}: {score}")

# Building a new list with a loop...
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)

# ...and the same thing as a list comprehension (a preview)
print([n for n in numbers if n % 2 == 0])
print([n * n for n in range(1, 6)])

# --- Two names, one list ------------------------------------------------------
a = [1, 2, 3]
b = a                  # NOT a copy - both names point at the same list
b.append(4)
print("a is now", a)   # [1, 2, 3, 4]

c = a.copy()           # a real, independent copy
c.append(5)
print("a:", a, " c:", c)

# --- Lists of lists -----------------------------------------------------------
grid = [[1, 2, 3],
        [4, 5, 6]]
print(grid[1][2])      # 6
for row in grid:
    print(row)

# --- Tuples: like lists, but fixed --------------------------------------------
point = (3, 4)
print(point[0], point[1])
# point[0] = 9          # <- uncomment to see a TypeError

x, y = point            # unpacking
print("x =", x, "y =", y)

name, age = ("Ada", 36)
print(name, age)

first, *rest = [1, 2, 3, 4]
print(first, rest)

single = (5,)           # the comma is what makes it a tuple
print(type(single), type((5)))
