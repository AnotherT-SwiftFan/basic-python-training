"""Lesson 6 - Loops

Run this file and trace each loop by hand against its output.
"""

# --- for + range --------------------------------------------------------------
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()                                  # finish the line

print("range(1, 6):")
for i in range(1, 6):
    print(i, end=" ")
print()

print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

print("range(5, 0, -1):")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# _ is the convention for "I don't need this value"
for _ in range(3):
    print("Hip hip hooray!")

# --- for over a string --------------------------------------------------------
for letter in "Python":
    print(letter, end="-")
print()

# --- Accumulator pattern ------------------------------------------------------
total = 0
for n in range(1, 6):
    total += n
print("1 + 2 + 3 + 4 + 5 =", total)

shout = ""
for letter in "hey":
    shout += letter.upper() + "!"
print(shout)

# Counting things that match
vowels = 0
for letter in "Hello World":
    if letter.lower() in "aeiou":
        vowels += 1
print("vowels:", vowels)

# --- while --------------------------------------------------------------------
count = 3
while count > 0:
    print(count)
    count -= 1          # change the variable, or the loop never ends!
print("Liftoff!")

# while is great when you don't know how many repeats you need:
# how many times can we halve 100 before it drops below 1?
value = 100
halvings = 0
while value >= 1:
    value = value / 2
    halvings += 1
print("halvings:", halvings)

# --- break and continue -------------------------------------------------------
for n in range(1, 10):
    if n % 2 == 0:
        continue        # skip even numbers
    if n > 7:
        break           # stop the loop completely
    print("odd:", n)

# Finding the first match, then stopping
for n in range(1, 100):
    if n % 7 == 0 and n % 5 == 0:
        print("first multiple of both 5 and 7:", n)
        break

# --- while True with break ----------------------------------------------------
attempts = 0
while True:
    attempts += 1
    if attempts == 3:
        print("giving up after", attempts, "attempts")
        break

# --- Nested loops: a multiplication table -------------------------------------
for row in range(1, 4):
    for col in range(1, 5):
        print(f"{row * col:3}", end="")
    print()             # new line after each row

# A triangle of stars
for stars in range(1, 5):
    print("*" * stars)
