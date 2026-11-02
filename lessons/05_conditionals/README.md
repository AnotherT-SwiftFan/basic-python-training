# Lesson 5: Conditionals

**Goal:** make your programs choose between different actions using `if`, `elif` and `else`.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## `if` and `else`

```python
age = 20

if age >= 18:
    print("You can vote.")
else:
    print("Not yet.")
```

Three things to notice:

1. The condition is followed by a **colon** `:`.
2. The code that belongs to the `if` is **indented** (4 spaces). That indentation is how Python knows where the block starts and ends.
3. `else` has no condition. It runs when none of the earlier ones did.

In VS Code, press `Tab` to indent. Never mix tabs and spaces in one file.

## `elif`: more than two choices

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

Python checks from the top and runs the **first** block whose condition is true, then skips the rest. So the order matters. If you tested `score >= 70` first, an 85 would get a "C".

## What counts as a condition?

Anything that is `True` or `False`: comparisons (`x > 5`), combinations (`a and b`), `in` checks, or a function that returns a bool.

```python
if name == "Ada" or name == "Grace":      # combine with or / and / not
    ...
if day in ("Saturday", "Sunday"):         # is the value in this group?
    ...
if "@" not in email:                      # not in
    ...
if 13 <= age <= 19:                       # chained comparison
    ...
```

(`("Saturday", "Sunday")` is a *tuple*, a fixed group of values. You'll meet tuples in Lesson 7.)

### Truthiness

Any value can be used as a condition. The falsy values from Lesson 2 (`0`, `""`, `None`, empty collections) count as false, everything else as true. This gives you a tidy way to check "is there anything here?":

```python
if name:                  # instead of:  if name != "":
    print(f"Hello, {name}")
else:
    print("Please enter a name")
```

## Nested conditions

You can put an `if` inside an `if`, but flat code is easier to read. Often `and` does the job:

```python
# Nested
if has_ticket:
    if age >= 18:
        print("Welcome")

# Flat (same meaning)
if has_ticket and age >= 18:
    print("Welcome")
```

## Returning early from a function

Inside a function, `return` ends the function straight away. That lets you skip `else` and keep the code flat:

```python
def describe(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
```

## One-line choice: the conditional expression

```python
label = "adult" if age >= 18 else "minor"
```

Great for simple choices. If it gets complicated, use a normal `if`.

## `match` (a taste)

Python 3.10 added `match` for choosing between many specific values:

```python
match command:
    case "start":
        print("Starting...")
    case "stop" | "quit":
        print("Stopping...")
    case _:
        print("Unknown command")
```

`_` means "anything else". An `if`/`elif` chain does the same job and works everywhere, so you don't need `match` yet.

## Common mistakes

| Mistake | Problem |
|---------|---------|
| `if x = 5:` | `=` assigns; you want `==` to compare (this one is a `SyntaxError`) |
| `if x > 5` (no colon) | `SyntaxError: expected ':'` |
| Wrong indentation | `IndentationError`, or code that runs when it shouldn't |
| `if x == 1 or 2:` | Always true! Python reads it as `(x == 1) or 2`, and `2` is truthy. Write `x == 1 or x == 2`, or `x in (1, 2)` |
| Checking the wide case first | `elif` chains stop at the first match, so test the most specific condition first |

## Try it yourself

1. Run [examples.py](examples.py) and change the starting values to see each branch run.
2. Write an `if`/`elif`/`else` chain that prints "cold", "mild" or "hot" for a temperature.
3. Do the exercises in [exercises.py](exercises.py).

```bash
pytest tests/test_05_conditionals.py
```

## Quick check

1. In an `if`/`elif`/`else` chain, how many blocks can run?
2. What does `bool("")` give, and why does that matter for `if name:`?
3. What's wrong with `if color == "red" or "blue":`?

<details>
<summary>Answers</summary>

1. At most one: the first block whose condition is true (or the `else` if none are).
2. `False`. An empty string is falsy, so `if name:` only runs when the user typed something.
3. `"blue"` on its own is truthy, so the condition is always true. Write `color == "red" or color == "blue"` or `color in ("red", "blue")`.

</details>

**Previous:** [Lesson 4](../04_numbers_and_operators/README.md) · **Next:** [Lesson 6: Loops](../06_loops/README.md)
