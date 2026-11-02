# Lesson 2: Variables and Types

**Goal:** store values under names, know the basic kinds of data (called *types*), and convert between them.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## Variables

A **variable** is a name that points at a value. You create one with `=`, the *assignment* operator:

```python
name = "Ada"
age = 36
```

Read `age = 36` as "`age` *becomes* 36", not "age equals 36". The right side is worked out first, then the name is attached to the result. Use the variable by writing its name:

```python
print(name, "is", age)    # Ada is 36
```

Variables can change. That's why they're called variables:

```python
age = age + 1             # take the old age, add 1, store it back
print(age)                # 37
```

### Naming rules

- Letters, digits and underscores only, and it can't start with a digit. `score2` is fine; `2score` isn't.
- No spaces: use `total_price`, not `total price`.
- Names are **case sensitive**: `age`, `Age` and `AGE` are three different variables.
- You can't use Python's reserved words (`if`, `for`, `class`, `True`, …) as names.

### Naming style

- Use `snake_case`: lowercase words joined with underscores.
- Make names say what's inside: `total_price`, not `tp` or `x`.
- A value that never changes (a *constant*) is written in `UPPER_CASE`, like `MAX_ATTEMPTS = 3`. It's only a convention. Python won't stop you from changing it.

## The basic types

Every value has a **type**. These five cover most of what you'll do at first:

| Type | Meaning | Examples |
|------|---------|----------|
| `int` | whole number | `42`, `-7`, `1_000_000` |
| `float` | number with a decimal point | `3.14`, `-0.5`, `2.0` |
| `str` | text ("string") | `"hello"`, `'hi'`, `""` |
| `bool` | yes/no value | `True`, `False` (capital first letter!) |
| `NoneType` | "no value here" | `None` |

Ask Python for a value's type with `type()`:

```python
print(type(42))        # <class 'int'>
print(type("42"))      # <class 'str'>
```

`42` and `"42"` look alike but behave very differently. One is a number you can calculate with; the other is two characters of text.

## Converting between types

Use the type's own name as a function:

```python
int("42")      # 42      text to whole number
float("3.5")   # 3.5     text to decimal number
str(42)        # "42"    anything to text
int(3.9)       # 3       drops the decimal part, does NOT round
```

A conversion that can't work stops the program with a `ValueError`:

```python
int("hello")   # ValueError: invalid literal for int() with base 10: 'hello'
```

### Truthiness

`bool(x)` tells you whether Python treats `x` as true or false. These are **falsy**: `0`, `0.0`, `""` (empty text), `None`, and empty collections (you'll meet those in Lesson 7). Everything else is **truthy**, including the text `"0"` and `"False"`.

## Getting input from the user

`input("question")` shows a prompt, waits for the user to type and press Enter, and gives back what they typed. **It always gives back a `str`**, even if they type digits.

```python
age_text = input("How old are you? ")   # the user types 30 -> "30" (text!)
age = int(age_text)                     # now it's the number 30
print(age + 1)                          # 31
```

## A quick look at f-strings

An **f-string** puts values straight into text. Put an `f` before the opening quote and wrap the values in `{}`:

```python
print(f"{name} will be {age + 1} next year.")
```

You can put whole expressions inside the braces. Lesson 3 covers f-strings in depth.

## Common mistakes

| You wrote | What happens | Fix |
|-----------|--------------|-----|
| `"Age: " + 36` | `TypeError`: can't add text and a number | `"Age: " + str(36)` or `f"Age: {36}"` |
| `input("n? ") + 1` | `TypeError`: `input` gives text | `int(input("n? ")) + 1` |
| `"3" + "4"` | gives `"34"`, not `7` | `int("3") + int("4")` |
| `nmae` instead of `name` | `NameError` | Check your spelling |
| `true` instead of `True` | `NameError` | Capital `T` |

## Try it yourself

1. Run [examples.py](examples.py). At the end it asks you two questions. Click in the terminal panel, type your answers, and press Enter after each.
2. Change the values and predict the output before you run it.
3. Do the exercises in [exercises.py](exercises.py). The first ones are plain variables, not functions.

```bash
pytest tests/test_02_variables_and_types.py
```

## Quick check

1. What's the type of `3.0`? Of `"3.0"`? Of `3 > 2`?
2. What does `int("7") + int("8")` give? And `"7" + "8"`?
3. A user types `25` at an `input()` prompt. What type do you get back?

<details>
<summary>Answers</summary>

1. `float`, `str`, `bool` (the comparison gives `True`).
2. `15`, and `"78"` (the text joined together).
3. `str`. `input()` always returns text, so convert it with `int()` if you need a number.

</details>

**Previous:** [Lesson 1](../01_hello_python/README.md) · **Next:** [Lesson 3: Strings](../03_strings/README.md)
