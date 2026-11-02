"""Lesson 4 - Numbers and Operators

Run this file. Before each line prints, try to predict what it will show.
"""

# --- Arithmetic ---------------------------------------------------------------
print(7 + 2)       # 9
print(7 - 2)       # 5
print(7 * 2)       # 14
print(7 / 2)       # 3.5   <- "/" always gives a float
print(6 / 3)       # 2.0   <- even when the answer is whole
print(7 // 2)      # 3     <- floor division: how many whole 2s fit in 7?
print(7 % 2)       # 1     <- remainder
print(2 ** 10)     # 1024  <- power

# Negative numbers and // and % behave "mathematically" (rounding down)
print(-7 // 2)     # -4
print(-7 % 2)      # 1

# --- Order of operations ------------------------------------------------------
print(2 + 3 * 4)       # 14
print((2 + 3) * 4)     # 20
print(2 ** 3 ** 2)     # 512  (powers go right to left: 2 ** 9)

# --- Shorthand assignment -----------------------------------------------------
score = 10
score += 5
print(score)       # 15
score -= 3
print(score)       # 12
score *= 2
print(score)       # 24
score //= 5
print(score)       # 4

# --- ints and floats ----------------------------------------------------------
print(3 + 0.5)             # 3.5 (int + float = float)
print(2 ** 200)            # ints can be huge
print(1_000_000 + 1)       # underscores make big numbers easier to read

# --- Floats are approximate ---------------------------------------------------
print(0.1 + 0.2)               # 0.30000000000000004
print(0.1 + 0.2 == 0.3)        # False!
print(round(0.1 + 0.2, 2) == 0.3)  # True: round before comparing

# --- Built-in helpers ---------------------------------------------------------
print(abs(-5))                 # 5
print(round(3.14159, 2))       # 3.14
print(round(7.5), round(2.5))  # 8 2  (halves round to the nearest even number)
print(min(3, 9, 1), max(3, 9, 1))   # 1 9
print(divmod(17, 5))           # (3, 2)

# --- Comparisons --------------------------------------------------------------
x = 7
print(x == 7)          # True
print(x != 7)          # False
print(x > 5, x < 5)    # True False
print(x >= 7, x <= 6)  # True False
print(0 < x < 10)      # True (chained comparison)

# --- and / or / not -----------------------------------------------------------
age = 25
has_ticket = True
print(age >= 18 and has_ticket)    # True
print(age < 13 or age > 65)        # False
print(not has_ticket)              # False

# not goes first, then and, then or. Brackets make your intent obvious.
print(True or False and False)     # True   (and goes first)
print((True or False) and False)   # False

# --- Everyday patterns --------------------------------------------------------
n = 1234
print(n % 2 == 0)      # is it even?        True
print(n % 5 == 0)      # divisible by 5?    False
print(n % 10)          # last digit         4
print(n // 10)         # drop last digit    123

minutes = 135
print(f"{minutes} minutes = {minutes // 60}h {minutes % 60}m")
