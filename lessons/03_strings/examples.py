"""Lesson 3 - Strings

Run this file and match every line of output to the code that made it.
"""

word = "Python"

# --- Length, indexing, slicing ------------------------------------------------
print(len(word))                 # 6
print(word[0], word[1], word[-1])  # P y n
print(word[0:2])                 # Py     (stop position is NOT included)
print(word[2:])                  # thon
print(word[:3])                  # Pyt
print(word[-3:])                 # hon
print(word[::2])                 # Pto    (every second character)
print(word[::-1])                # nohtyP (reversed)

# --- Strings can't be edited, but you can build a new one ---------------------
# word[0] = "J"                  # <- uncomment to see a TypeError
new_word = "J" + word[1:]
print(new_word)                  # Jython

# --- Joining and repeating ----------------------------------------------------
first = "Ada"
last = "Lovelace"
print(first + " " + last)
print("ha" * 3)
print("-" * 20)

# --- Methods return NEW strings -----------------------------------------------
shout = "hello"
print(shout.upper())             # HELLO
print(shout)                     # hello  <- unchanged!
shout = shout.upper()            # assign it back to keep the change
print(shout)                     # HELLO

messy = "   Hello, World!   "
print(f"[{messy}]")
print(f"[{messy.strip()}]")                 # whitespace trimmed
print(messy.strip().lower())                # chaining: strip, then lower

print("a-b-c".replace("-", "+"))            # a+b+c
print("ada lovelace".title())               # Ada Lovelace

# --- Splitting and joining ----------------------------------------------------
words = "the quick brown fox".split()
print(words)                                # ['the', 'quick', 'brown', 'fox']
print("-".join(words))                      # the-quick-brown-fox
print("1,2,3".split(","))                   # ['1', '2', '3']

# --- Searching and testing ----------------------------------------------------
print("Python".startswith("Py"), "Python".endswith("on"))   # True True
print("Python".find("th"))                  # 2
print("Python".find("z"))                   # -1  (not found)
print("banana".count("a"))                  # 3
print("42".isdigit(), "4x".isdigit())       # True False
print("abc".isalpha(), "abc123".isalnum())  # True True
print("th" in "Python")                     # True

# --- Escape sequences ---------------------------------------------------------
print("She said \"hi\"")
print("Column A\tColumn B")
print("C:\\Users\\ada")

# --- f-strings ----------------------------------------------------------------
name = "Ada"
score = 92.456
print(f"{name} scored {score}")
print(f"Next year: {score + 1}")
print(f"Rounded: {score:.1f}")

price = 1234.5
print(f"Price: ${price:,.2f}")             # Price: $1,234.50
print(f"Share: {0.256:.1%}")               # Share: 25.6%
print(f"[{'left':<10}] [{'right':>10}] [{'mid':^10}]")
print(f"Order #{42:05d}")                  # Order #00042
print(f"{score=}")                         # score=92.456  (handy for debugging)
