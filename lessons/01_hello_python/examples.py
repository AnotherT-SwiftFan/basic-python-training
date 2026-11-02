"""Lesson 1 - Hello, Python

Run this file with the play button (top right of VS Code) and read the output
next to the code. Then change things and run it again!
"""

# Lines that start with # are comments. Python skips them; they're notes for humans.

print("Hello, world!")

# print() can show text (in quotes) or numbers (no quotes).
print("I am learning Python")
print(2 + 3)
print("2 + 3")  # In quotes it's just text, so Python does NOT calculate it

# Give print() several things and it puts a space between them.
print("My lucky number is", 7)

# sep= changes what goes between the items.
print("a", "b", "c", sep="-")

# end= changes what goes at the end. Normally that's a new line.
print("No new line here...", end=" ")
print("...so this continues on the same line.")

# Single or double quotes both work. Pick one style and stick with it.
print('Single quotes work too')
print("Double quotes make it easy to write it's with an apostrophe")

# Special characters start with a backslash: \n is a new line, \t is a tab.
print("Line one\nLine two")
print("Name:\tAda")

# Triple quotes let a string span several lines.
print("""This text
spans several
lines.""")

# An empty print() gives a blank line.
print()

# Python is case sensitive and spelling matters.
# Uncomment the next line (remove the #) to see a SyntaxError, then fix it:
# print("Oops)

print("The end")
