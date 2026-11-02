# Lesson 9: Functions

**Goal:** package code into reusable, named pieces, so you write it once and use it anywhere.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

You've been *calling* functions since Lesson 1 (`print`, `len`, `int`). Now you'll write your own. The exercises in every lesson so far were functions too, so this will look familiar.

## Defining and calling

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Ada")      # call it
print(message)              # Hello, Ada!
```

- `def` starts the definition, followed by the function's name, its **parameters** in brackets, and a colon.
- The indented block is the **body**.
- `return` hands a value back to the caller and ends the function.
- Defining a function doesn't run it. Calling it (`greet("Ada")`) does.

**Parameters** are the names in the definition (`name`). **Arguments** are the values you pass when calling (`"Ada"`).

## `return` vs `print`

This trips up almost everybody at first:

```python
def add_print(a, b):
    print(a + b)        # shows the answer, but gives nothing back

def add_return(a, b):
    return a + b        # gives the answer back to the caller

total = add_return(2, 3) * 10     # 50 -- we can use the result
total = add_print(2, 3) * 10      # prints 5, then crashes: None * 10
```

If a function has no `return` (or a bare `return`), it gives back `None`. As a rule, **functions that calculate should `return`; leave the printing to the code that calls them.**

## Several parameters, defaults and keyword arguments

```python
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

greet("Ada")                          # Hello, Ada!
greet("Ada", "Welcome")               # Welcome, Ada!
greet("Ada", punctuation="?")         # Hello, Ada?
greet(greeting="Hi", name="Bo")       # Hi, Bo!  (keyword arguments, any order)
```

- A **default** is used when the caller leaves the argument out.
- Parameters with defaults must come after the ones without.
- **Keyword arguments** (`name=value`) make calls self-explanatory, especially for functions with many parameters.

## Returning several values

Return a tuple, then unpack it:

```python
def min_and_max(numbers):
    return min(numbers), max(numbers)

low, high = min_and_max([4, 9, 2])
```

## Docstrings

A string on the first line of the body documents the function. VS Code shows it when you hover over a call.

```python
def area(width, height):
    """Return the area of a rectangle."""
    return width * height
```

## Scope: where variables live

Variables created inside a function are **local**: they only exist while it runs.

```python
def make_total():
    total = 10          # local to make_total

make_total()
print(total)            # NameError -- total doesn't exist out here
```

A function can *read* variables from outside, but it's cleaner to pass things in as arguments and get results out with `return`. Avoid the `global` keyword. It makes code hard to follow.

## Functions calling functions

Small functions that each do one thing can be combined:

```python
def is_even(n):
    return n % 2 == 0

def count_evens(numbers):
    count = 0
    for n in numbers:
        if is_even(n):
            count += 1
    return count
```

Good functions are short, have a clear name (usually a verb), and do one job.

## Functions are values too

You can pass a function to another function, just like a number:

```python
def apply_twice(func, value):
    return func(func(value))

def add_one(x):
    return x + 1

apply_twice(add_one, 5)       # 7
```

This idea powers things like `sorted(items, key=len)`. Note that we pass `len`, not `len()`. We're handing over the function itself, not calling it.

## Type hints (optional)

You can annotate what types a function expects. Python doesn't enforce them, but they help readers and VS Code:

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

## Gotchas

- **Forgetting `return`.** The function silently gives back `None`.
- **Forgetting to call it.** `greet` is the function; `greet("Ada")` runs it.
- **Mutable default arguments.** Never write `def add(item, items=[])`. That one list is shared by every call. Use `items=None` and create the list inside.
- **Modifying a list you were given.** The caller's list changes too (Lesson 7). Make a copy if you shouldn't touch the original.

## Try it yourself

1. Run [examples.py](examples.py) and use the debugger (Lesson 12, or `F5` now): set a breakpoint inside a function and step into it with `F11`.
2. Write a function `fahrenheit_to_celsius` and test it with a few values.
3. Do the exercises in [exercises.py](exercises.py).

```bash
pytest tests/test_09_functions.py
```

## Quick check

1. What does a function return if it has no `return` statement?
2. What's the difference between a parameter and an argument?
3. Why is `def f(items=[])` a bad idea?

<details>
<summary>Answers</summary>

1. `None`.
2. A parameter is the name in the `def` line. An argument is the actual value passed in a call.
3. The default list is created once and shared by every call that uses the default, so changes pile up between calls.

</details>

**Previous:** [Lesson 8](../08_dictionaries_and_sets/README.md) · **Next:** [Lesson 10: Modules and the Standard Library](../10_modules_and_stdlib/README.md)
