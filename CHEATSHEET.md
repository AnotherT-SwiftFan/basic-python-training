# Python Cheat Sheet

A one-page reminder of everything in the course. Lesson numbers show where to read more.

## Output, input, comments (1, 2)

```python
print("Hello", name, sep=", ", end="!\n")
answer = input("Question? ")        # always returns str
# a comment
```

## Types and conversion (2)

```python
42  3.14  "text"  True  None        # int  float  str  bool  NoneType
type(x)   int("7")   float("2.5")   str(9)   bool(0)
```

Falsy: `0`, `0.0`, `""`, `None`, `[]`, `{}`, `()`, `set()`. Everything else is truthy.

## Strings (3)

```python
s = "Python"
s[0]  s[-1]  s[1:4]  s[::-1]  len(s)
s.upper() s.lower() s.title() s.strip() s.replace("a", "b")
s.split(",")   ",".join(items)   s.startswith("Py")   s.find("th")   s.count("t")
"th" in s
f"{name} is {age + 1}"   f"{x:.2f}"   f"{n:,}"   f"{p:.1%}"   f"{x=}"
```

## Operators (4)

```python
+  -  *  /  //  %  **            # / is float division, // floors, % is remainder
==  !=  <  >  <=  >=   0 < x < 10
and  or  not
x += 1                           # also -=  *=  /=  //=
round(x, 2)  abs(x)  min(a, b)  max(a, b)  divmod(a, b)
```

## Conditionals (5)

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

label = "adult" if age >= 18 else "minor"
if day in ("Sat", "Sun"): ...
```

## Loops (6)

```python
for i in range(5): ...            # 0..4
for i in range(1, 6): ...         # 1..5
for i in range(10, 0, -2): ...    # 10, 8, 6, 4, 2
for ch in "text": ...
while condition: ...
break      # leave the loop
continue   # skip to the next pass
```

## Lists and tuples (7)

```python
items = [1, 2, 3]
items.append(4)  items.insert(0, 9)  items.extend([5, 6])
items.remove(2)  items.pop()  del items[0]
items[0]  items[-1]  items[1:3]  len(items)  sum(items)  min(items)
items.sort()  sorted(items, reverse=True)  items.reverse()
for i, item in enumerate(items, start=1): ...
for a, b in zip(list1, list2): ...
[n * n for n in items if n > 1]            # list comprehension
copy = items.copy()
point = (3, 4);  x, y = point               # tuple + unpacking
```

## Dictionaries and sets (8)

```python
d = {"name": "Ada", "age": 36}
d["name"]  d.get("email", "n/a")  d["email"] = "a@b.c"  del d["age"]
"name" in d     # checks keys
for key, value in d.items(): ...
counts[x] = counts.get(x, 0) + 1            # counting pattern

s = {1, 2, 3};  empty = set()
s.add(4)  s.discard(1)  2 in s
a | b   a & b   a - b   a ^ b                # union, both, difference, either-not-both
```

## Functions (9)

```python
def greet(name, greeting="Hello"):
    """Say hello."""
    return f"{greeting}, {name}!"

greet("Ada")   greet("Ada", greeting="Hi")
def min_max(nums): return min(nums), max(nums)
low, high = min_max([3, 1, 2])
```

`return` gives a value back. `print` only shows it. No `return` means `None`.

## Modules (10)

```python
import math                       # math.sqrt(9), math.pi, math.ceil(x)
from random import randint, choice
from datetime import date, timedelta
from collections import Counter
import my_file                    # your own my_file.py in the same folder

if __name__ == "__main__":
    main()
```

```bash
pip install package-name
pip freeze > requirements.txt
pip install -r requirements.txt
```

## Files and JSON (11)

```python
from pathlib import Path
import json

HERE = Path(__file__).parent                 # folder of this script
with open(HERE / "a.txt", "w", encoding="utf-8") as f:     # "r" read, "w" overwrite, "a" append
    f.write("line\n")
with open(HERE / "a.txt", encoding="utf-8") as f:
    for line in f: print(line.strip())

json.dump(data, f, indent=2)     data = json.load(f)
json.dumps(data)                 data = json.loads(text)
```

## Errors (12)

```python
try:
    n = int(text)
except ValueError:
    n = 0
except (KeyError, IndexError) as error:
    print(error)
else:
    ...                           # no exception happened
finally:
    ...                           # always runs

raise ValueError("what went wrong")
```

Common exceptions: `ValueError` `TypeError` `KeyError` `IndexError` `NameError` `AttributeError` `ZeroDivisionError` `FileNotFoundError`.

## Classes (13)

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"{self.owner}: {self.balance}"

class Savings(Account):                       # inheritance
    def add_interest(self):
        self.balance *= 1.02
```

## VS Code and terminal (SETUP.md)

| Task | How |
|------|-----|
| Run a file | ▶ button, or `python file.py` |
| Run tests | `pytest`, or the Testing (beaker) panel |
| Debug | click the margin for a breakpoint, `F5`, then `F10` / `F11` |
| Stop a runaway program | `Ctrl+C` in the terminal |
| Try code interactively | type `python` in the terminal, `exit()` to leave |
| Look around the terminal | `pwd` (where am I), `ls` (list files), `cd folder` / `cd ..` (move). See [TERMINAL.md](TERMINAL.md) |
| Get help | `help(len)`, hover in VS Code, [docs.python.org](https://docs.python.org/3/) |
