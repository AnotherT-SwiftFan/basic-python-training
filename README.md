# Python Basics: A Hands-On Course

A friendly, practical introduction to Python for junior developers. You go from your first `print("Hello")` to building a small command-line app, with runnable examples and auto-checked exercises along the way.

- **No prior Python needed.** Some general programming familiarity helps, but isn't required.
- **Built for VS Code.** Run files with one click, check exercises in the Testing panel, debug with breakpoints.
- **Learn by doing.** Every lesson has examples to run and tinker with, plus exercises that tell you immediately whether you got them right.

## Quick start

1. **Get the course files** from GitHub by downloading the ZIP or cloning with Git. [Step 0 of SETUP.md](SETUP.md#0-get-the-course-files) shows how.
2. Install Python 3.10 or newer and VS Code. [SETUP.md](SETUP.md) walks through it (about 10 minutes).
3. Open the course folder in VS Code (**File → Open Folder…**) and accept the prompt to install the recommended extensions.
4. Open VS Code's terminal and create the course environment. (Never used a terminal? Read [TERMINAL.md](TERMINAL.md) first. It takes five minutes.) Full details are in [SETUP.md](SETUP.md):

   ```bash
   python -m venv .venv
   ```

   Activate it, then install the one dependency (`pytest`, used to check your exercises):

   ```bash
   pip install -r requirements.txt
   ```

5. Open [lessons/01_hello_python/README.md](lessons/01_hello_python/README.md) and press `Ctrl+Shift+V` to see it nicely formatted.

## Course outline

| # | Lesson | You'll learn |
|---|--------|--------------|
| 1 | [Hello, Python](lessons/01_hello_python/README.md) | Running scripts, `print()`, comments, reading error messages |
| 2 | [Variables & Types](lessons/02_variables_and_types/README.md) | `int`, `float`, `str`, `bool`, converting types, `input()` |
| 3 | [Strings](lessons/03_strings/README.md) | Indexing, slicing, string methods, f-strings |
| 4 | [Numbers & Operators](lessons/04_numbers_and_operators/README.md) | Arithmetic, comparisons, `and` / `or` / `not` |
| 5 | [Conditionals](lessons/05_conditionals/README.md) | `if` / `elif` / `else`, truthiness |
| 6 | [Loops](lessons/06_loops/README.md) | `for`, `while`, `range`, `break` / `continue` |
| 7 | [Lists & Tuples](lessons/07_lists_and_tuples/README.md) | Ordered collections, slicing, list methods, unpacking |
| 8 | [Dictionaries & Sets](lessons/08_dictionaries_and_sets/README.md) | Key/value data, counting, unique items, set maths |
| 9 | [Functions](lessons/09_functions/README.md) | `def`, parameters, `return`, scope, docstrings |
| 10 | [Modules & the Standard Library](lessons/10_modules_and_stdlib/README.md) | `import`, `math`, `random`, `datetime`, your own modules, `pip` |
| 11 | [Files & JSON](lessons/11_files_and_json/README.md) | Reading and writing text, JSON and CSV files |
| 12 | [Errors & Exceptions](lessons/12_errors_and_exceptions/README.md) | Reading tracebacks, `try` / `except`, `raise`, debugging |
| 13 | [Classes](lessons/13_classes/README.md) | Objects, methods, `__init__`, inheritance |
| 14 | [Mini Project: To-Do App](lessons/14_mini_project/README.md) | Put it all together in a working command-line app |

Allow roughly 45 to 90 minutes per lesson. Two to three weeks of part-time study is a comfortable pace. A one-page reference lives in [CHEATSHEET.md](CHEATSHEET.md).

## How each lesson works

Every lesson folder has these four files. (Lesson 10 adds one small helper module, and Lesson 14, the mini project, has no `examples.py` because the app itself is the example.)

| File | Purpose |
|------|---------|
| `README.md` | The lesson. Read this first. |
| `examples.py` | Runnable, commented examples. Run it, read the output, then **change things and run it again**. |
| `exercises.py` | Your turn. Replace each `pass` (or `None`) with real code. |
| `solutions.py` | Reference answers. Try each exercise properly before you peek. |

The loop for each lesson:

1. **Read** the lesson `README.md`.
2. **Run** `examples.py` (the ▶ button at the top right of VS Code) and tinker with it.
3. **Write** your answers in `exercises.py`.
4. **Check** them with the tests (below).
5. **Compare** with `solutions.py` once your tests pass, or if you're truly stuck.

## Checking your exercises

Each lesson has a matching test file in `tests/`. Type these in the VS Code terminal, with the terminal in the top course folder (the one containing this README; see [TERMINAL.md](TERMINAL.md) if you're unsure):

```bash
pytest tests/test_03_strings.py    # check one lesson
pytest                             # check everything
```

You can also click the beaker icon (Testing) in the VS Code sidebar and press ▶ next to a lesson.

Before you've written anything, **the tests fail. That's expected.** Your job is to turn them from red to green, one at a time. Each failure message tells you which exercise it was checking and what it expected.

## For mentors

- Ask the learner to explain each example out loud before running it. Predicting the output first is a great habit.
- Two or three lessons per sitting is plenty. The exercises are quick, so spend the time on the "why".
- To check that every `solutions.py` passes its tests, point the tests at the solutions instead of the exercises:

  ```bash
  # macOS / Linux / Git Bash
  CHECK_SOLUTIONS=1 pytest
  ```

  ```powershell
  # Windows PowerShell
  $env:CHECK_SOLUTIONS = "1"; pytest; Remove-Item Env:CHECK_SOLUTIONS
  ```

## Where to go next

- The official [Python tutorial](https://docs.python.org/3/tutorial/) is excellent once you know the basics.
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) for practical scripting projects.
- [Exercism's Python track](https://exercism.org/tracks/python) for more practice with mentor feedback.
- Topics that follow naturally: list/dict comprehensions, `dataclasses`, type hints, virtual environments in depth, `requests` for calling web APIs, writing your own tests, and Git.
