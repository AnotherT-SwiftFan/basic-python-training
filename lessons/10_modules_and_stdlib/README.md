# Lesson 10: Modules and the Standard Library

**Goal:** use code other people wrote, split your own code across files, and know where to look for help.

**Files in this lesson:** [examples.py](examples.py) · [my_helpers.py](my_helpers.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## What is a module?

A **module** is just a Python file full of functions and variables that other files can borrow with `import`. Python comes with a huge collection of ready-made modules called the **standard library** ("batteries included"), and you can add more from the internet.

## Ways to import

```python
import math                       # use as math.sqrt(16)
from math import sqrt, pi         # use as sqrt(16) and pi directly
import datetime as dt             # give it a shorter nickname: dt.date.today()
from collections import Counter  # import one specific thing
```

- `import math` is the safest default. When you read `math.sqrt`, you can see where `sqrt` came from.
- Avoid `from math import *`. It dumps every name into your file and hides where things come from.
- Put imports at the **top** of the file.

## A tour of the standard library

| Module | What it's for | Example |
|--------|---------------|---------|
| `math` | maths functions and constants | `math.sqrt(16)`, `math.pi`, `math.ceil(2.1)` |
| `random` | random numbers and choices | `random.randint(1, 6)`, `random.choice(items)` |
| `datetime` | dates, times and durations | `datetime.date.today()` |
| `collections` | extra containers | `Counter("banana")` counts items for you |
| `pathlib` | file paths (Lesson 11) | `Path("data") / "notes.txt"` |
| `json`, `csv` | reading and writing data files (Lesson 11) | `json.load(file)` |
| `os`, `sys` | talking to the operating system and interpreter | `os.getcwd()`, `sys.version` |
| `re` | regular expressions (pattern matching in text) | `re.findall(r"\d+", text)` |
| `time` | pausing and timing | `time.sleep(1)` |
| `argparse` | command-line options for your scripts | |
| `logging` | proper log messages instead of `print` | |
| `unittest` | a built-in testing framework | |

### `math`

```python
import math
math.sqrt(81)       # 9.0
math.pi             # 3.141592653589793
math.ceil(2.1)      # 3   round up
math.floor(2.9)     # 2   round down
math.isclose(0.1 + 0.2, 0.3)    # True -- the right way to compare floats
```

### `random`

```python
import random
random.randint(1, 6)               # a random whole number from 1 to 6 inclusive
random.choice(["rock", "paper"])   # a random item from a list
random.shuffle(my_list)            # shuffles a list in place
random.seed(42)                    # makes the "random" numbers repeatable (great for testing)
```

### `datetime`

```python
from datetime import date, timedelta

today = date.today()
christmas = date(2026, 12, 25)
print((christmas - today).days)          # days until Christmas
print(today + timedelta(days=30))        # 30 days from now
print(today.strftime("%A, %d %B %Y"))    # e.g. Monday, 02 November 2026
date.fromisoformat("2026-01-31")         # turn text into a date
```

### `collections.Counter`

```python
from collections import Counter
Counter("banana")                        # Counter({'a': 3, 'n': 2, 'b': 1})
Counter("a b a".split()).most_common(1)  # [('a', 2)]
```

## Your own modules

Any `.py` file is a module. This lesson's folder has [my_helpers.py](my_helpers.py), and [examples.py](examples.py) imports it:

```python
import my_helpers
print(my_helpers.double(21))
```

Python finds `my_helpers` because it looks in the folder of the script you ran.

### `if __name__ == "__main__":`

You'll see this at the bottom of lots of Python files. It means "only run this part when the file is run directly, not when it's imported":

```python
def main():
    print("Running as a program")

if __name__ == "__main__":
    main()
```

Run `my_helpers.py` directly and its `__main__` section runs. Import it from `examples.py` and that section is skipped.

## Third-party packages and `pip`

Beyond the standard library there are hundreds of thousands of packages on PyPI (the Python Package Index). Install them with `pip`, ideally inside your virtual environment:

```bash
pip install requests          # install a package
pip list                      # show what's installed
pip freeze > requirements.txt # save the exact versions for others
pip install -r requirements.txt   # install everything in that file
```

That's exactly how this course's `requirements.txt` installs `pytest`.

## Finding out more

- `help(math.sqrt)` in the REPL, or hover over a function in VS Code.
- `dir(math)` lists everything inside a module.
- The official docs at [docs.python.org](https://docs.python.org/3/library/) are excellent. Searching "python <module name>" always finds them.

## Gotcha: don't name your file after a module

If you create `random.py` or `math.py` in your project, then `import random` imports *your* file instead of the real one, and things break in confusing ways. Choose names like `dice_game.py` instead.

## Try it yourself

1. Run [examples.py](examples.py). Also run [my_helpers.py](my_helpers.py) directly and compare the output.
2. Use `random.choice` to build a "magic 8-ball" that answers a question with a random reply.
3. Do the exercises in [exercises.py](exercises.py). **Add the imports you need at the top of the file.**

```bash
pytest tests/test_10_modules_and_stdlib.py
```

## Quick check

1. What's the difference between `import math` and `from math import sqrt`?
2. Why does `if __name__ == "__main__":` exist?
3. Why shouldn't you save a file called `random.py`?

<details>
<summary>Answers</summary>

1. The first gives you the module, and you write `math.sqrt(...)`. The second pulls just `sqrt` into your file, so you write `sqrt(...)`.
2. So a file can be both a runnable program and an importable module. The block only runs when the file is run directly.
3. It would shadow Python's real `random` module, so `import random` would load your file instead.

</details>

**Previous:** [Lesson 9](../09_functions/README.md) · **Next:** [Lesson 11: Files and JSON](../11_files_and_json/README.md)
