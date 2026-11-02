# Lesson 3: Strings

**Goal:** get comfortable with text: picking it apart, cleaning it up, and building messages from it.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## Creating strings

```python
a = "double quotes"
b = 'single quotes'
c = "It's easy with an apostrophe inside double quotes"
d = """Triple quotes can
span several lines."""
```

Inside a string, a backslash starts an *escape sequence*: `\n` (new line), `\t` (tab), `\"` (a quote mark), `\\` (a backslash).

`len(text)` gives the number of characters (spaces count too).

## Indexing: one character at a time

Each character has a position, starting from **0**. Negative numbers count back from the end.

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

```python
word = "Python"
word[0]     # "P"
word[3]     # "h"
word[-1]    # "n"   (the last character)
word[10]    # IndexError: string index out of range
```

## Slicing: a range of characters

`text[start:stop]` gives the characters from `start` up to, **but not including**, `stop`. Leave a side blank to mean "from the beginning" or "to the end". A third number is the step.

```python
word[0:2]     # "Py"
word[2:]      # "thon"
word[:3]      # "Pyt"
word[-3:]     # "hon"     the last three characters
word[::2]     # "Pto"     every second character
word[::-1]    # "nohtyP"  step backwards = reversed
```

A slice never raises an error for going past the end. It just stops there.

## Strings can't be changed

Strings are **immutable**: you can't edit one in place. `word[0] = "J"` is a `TypeError`. Instead you build a new string, such as `"J" + word[1:]`.

## Joining and repeating

```python
"Ada" + " " + "Lovelace"    # "Ada Lovelace"
"ha" * 3                     # "hahaha"
"-" * 20                     # a handy divider line
```

## String methods

A **method** is a function that belongs to a value, called with a dot: `text.upper()`. Because strings can't change, **methods return a new string and leave the original alone.**

```python
name = "ada"
name.upper()       # "ADA"
print(name)        # still "ada"  <- the original is unchanged
name = name.upper()  # to keep the result, assign it
```

| Method | What it does | Example → result |
|--------|--------------|------------------|
| `.upper()` / `.lower()` | change case | `"Hi".upper()` → `"HI"` |
| `.title()` | Capitalise Each Word | `"ada lovelace".title()` → `"Ada Lovelace"` |
| `.strip()` | trim whitespace from both ends | `"  hi ".strip()` → `"hi"` |
| `.replace(old, new)` | swap text | `"a-b".replace("-", "+")` → `"a+b"` |
| `.split()` | break into a list of words | `"a b c".split()` → `["a", "b", "c"]` |
| `.split(sep)` | break at a separator | `"1,2,3".split(",")` → `["1", "2", "3"]` |
| `sep.join(list)` | glue a list into one string | `"-".join(["a", "b"])` → `"a-b"` |
| `.startswith(x)` / `.endswith(x)` | check the start or end | `"Python".startswith("Py")` → `True` |
| `.find(x)` | index of first match, or `-1` | `"Python".find("th")` → `2` |
| `.count(x)` | how many times it appears | `"banana".count("a")` → `3` |
| `.isdigit()` / `.isalpha()` / `.isalnum()` | is it all digits / letters / letters-and-digits? | `"42".isdigit()` → `True` |

The `in` operator checks whether one string is inside another: `"th" in "Python"` is `True`.

Methods chain from left to right: `"  Ada  ".strip().upper()` gives `"ADA"`.

## f-strings: the best way to build text

Put an `f` in front of the quotes and write values or expressions inside `{}`:

```python
name = "Ada"
score = 92.456
print(f"{name} scored {score}")           # Ada scored 92.456
print(f"Next year: {score + 1}")          # any expression works
```

After a colon inside the braces you can control formatting:

| Format | Meaning | Example → result |
|--------|---------|------------------|
| `{x:.2f}` | 2 decimal places | `f"{3.14159:.2f}"` → `3.14` |
| `{x:,}` | thousands separators | `f"{1234567:,}"` → `1,234,567` |
| `{x:,.2f}` | both | `f"{1234.5:,.2f}"` → `1,234.50` |
| `{x:.1%}` | percentage | `f"{0.256:.1%}"` → `25.6%` |
| `{x:>8}` / `{x:<8}` / `{x:^8}` | right / left / centre in 8 spaces | `f"{'hi':>5}"` → `"   hi"` |
| `{x:05d}` | pad a whole number with zeros | `f"{42:05d}"` → `00042` |

Debugging trick: `f"{score=}"` prints `score=92.456`, showing the name and the value.

## Common mistakes

- Forgetting that methods return new strings: `name.upper()` on its own line does nothing useful.
- Off-by-one with slices: `text[0:3]` gives **three** characters, positions 0, 1 and 2.
- Mixing text and numbers with `+`: use an f-string instead.

## Try it yourself

1. Run [examples.py](examples.py) and match each line with its output.
2. Pick your full name and try slicing out your initials, reversing it, and shouting it.
3. Do the exercises in [exercises.py](exercises.py).

```bash
pytest tests/test_03_strings.py
```

## Quick check

1. What is `"Python"[1:4]`?
2. After `s = "hello"` and `s.upper()`, what is `s`?
3. What does `"a,b,c".split(",")` return?

<details>
<summary>Answers</summary>

1. `"yth"`: positions 1, 2 and 3.
2. Still `"hello"`. Methods return new strings and never change the original.
3. A list of three strings: `["a", "b", "c"]`.

</details>

**Previous:** [Lesson 2](../02_variables_and_types/README.md) · **Next:** [Lesson 4: Numbers and Operators](../04_numbers_and_operators/README.md)
