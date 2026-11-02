# Lesson 1: Hello, Python

**Goal:** run your first program, show text on the screen, and learn to read Python's error messages without panic.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## What is a Python program?

A Python program is a plain text file ending in `.py` that holds a list of instructions. Python reads it from top to bottom, one line at a time, and does what each line says. There's no separate build step: you save the file and run it.

## Two ways to run Python

**1. Run a file** (what you'll do most of the time). Open [examples.py](examples.py) and click the **▶** button at the top right of VS Code, or type a command in the terminal (a window where you control the computer by typing; if that's new to you, read [TERMINAL.md](../../TERMINAL.md)):

```bash
python lessons/01_hello_python/examples.py
```

**2. The interactive prompt**, also called the REPL. Type `python` on its own in the terminal and you get a `>>>` prompt. Type a line, press Enter, and Python answers straight away. It's perfect for quick experiments. Type `exit()` to leave.

```pycon
>>> 2 + 2
4
>>> print("hi there")
hi there
```

## `print()`: showing things on screen

```python
print("Hello, world!")
```

- Text goes inside quotes. Python calls text a **string**. Single `'quotes'` and double `"quotes"` both work.
- Numbers don't need quotes: `print(42)`.
- Quotes matter: `print(2 + 3)` shows `5`, but `print("2 + 3")` shows the text `2 + 3`.
- Give `print()` several things separated by commas and it puts a space between them: `print("Score:", 10)` shows `Score: 10`.
- Two handy options:
  - `sep=` changes what goes between items: `print("a", "b", sep="-")` shows `a-b`.
  - `end=` changes what goes at the end (normally a new line): `print("Hi", end="!")`.
- Special characters inside a string start with a backslash: `\n` is a new line, `\t` is a tab.

## Comments

Anything after a `#` is ignored by Python. Use comments to explain *why* you did something.

```python
# This whole line is a comment
print("Hi")  # So is this part
```

## Two rules to remember early

- **Spelling and capital letters matter.** `print` works. `Print` and `prnt` don't.
- **Indentation matters.** Python uses leading spaces to group code together. For now every line starts at the left edge. You'll meet indentation properly in Lesson 5.

## Reading error messages

You will see lots of errors. That's normal at every level, and they're helpful once you know how to read them.

```text
Traceback (most recent call last):
  File "hello.py", line 3, in <module>
    prnt("Hello")
NameError: name 'prnt' is not defined
```

1. **Read the last line first.** It names the kind of error (`NameError`) and what went wrong (`'prnt' is not defined`).
2. The line above it shows the exact code. The `File ... line 3` part says where.
3. Fix it, save, run again.

The errors you'll meet first:

| Error | Usual cause |
|-------|-------------|
| `SyntaxError` | Broken grammar: a missing quote or bracket, a stray character |
| `NameError` | A typo in a name, or using something before creating it |
| `IndentationError` | Spaces at the start of a line where there shouldn't be (or vice versa) |
| `TypeError` | Mixing things that don't go together, such as adding text to a number |

## How the exercises work

Exercises in this course are small **functions**. Here's one:

```python
def say_goodbye():
    print("Goodbye!")
```

- `def` defines a named block of code, like a recipe. The indented lines underneath are what the recipe does.
- Running the file doesn't run the recipe. Something has to *call* it by writing `say_goodbye()`. The tests do that for you.
- **`print` and `return` are different.** `print(x)` shows `x` on screen. `return x` hands `x` back to whoever called the function, so they can use it. Some exercises ask for one, some for the other.

You'll learn functions properly in Lesson 9. For now: replace each `pass` with your own code, and keep the indentation.

Check your work with the tests. Type this in the terminal, opened in the top course folder (the one containing `README.md`):

```bash
pytest tests/test_01_hello_python.py
```

When a test fails, look for the lines starting with `E`. They show what the test expected and what your code produced.

## Try it yourself

1. Run [examples.py](examples.py). Read each line next to its output.
2. Change a message, save, and run again.
3. Uncomment the broken line near the bottom to see a `SyntaxError`, then fix it again.
4. Do the exercises in [exercises.py](exercises.py).

## Quick check

1. What's the difference between `print("5 + 5")` and `print(5 + 5)`?
2. Which line of an error message tells you what went wrong?
3. What does `print("a", "b", sep="")` show?

<details>
<summary>Answers</summary>

1. The first shows the text `5 + 5`. The second calculates and shows `10`.
2. The last line.
3. `ab`, because the separator is an empty string.

</details>

**Next:** [Lesson 2: Variables and Types](../02_variables_and_types/README.md)
