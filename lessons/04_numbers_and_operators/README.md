# Lesson 4: Numbers and Operators

**Goal:** do maths in Python, compare values, and combine yes/no questions with `and`, `or` and `not`.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## Arithmetic

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | add | `7 + 2` | `9` |
| `-` | subtract | `7 - 2` | `5` |
| `*` | multiply | `7 * 2` | `14` |
| `/` | divide (always gives a `float`) | `7 / 2` | `3.5` |
| `//` | floor divide (whole-number part) | `7 // 2` | `3` |
| `%` | remainder ("modulo") | `7 % 2` | `1` |
| `**` | power | `2 ** 10` | `1024` |

Notice that `/` gives a float even when the answer is whole: `6 / 3` is `2.0`.

`//` and `%` work as a pair. `7 // 2` is "how many whole 2s fit in 7?" (3) and `7 % 2` is "what's left over?" (1). Together they split minutes into hours and minutes, or a number into its digits.

### Order of operations

Python follows the normal maths order: brackets, then `**`, then `* / // %`, then `+ -`. When in doubt, add brackets. They cost nothing and make code easier to read.

```python
2 + 3 * 4       # 14
(2 + 3) * 4     # 20
```

### Shorthand assignment

Updating a variable from its own value is so common it has a shortcut:

```python
score = 10
score += 5      # same as: score = score + 5   -> 15
score -= 3      # 12
score *= 2      # 24
score //= 5     # 4
```

## Integers and floats

- `int` has no size limit: `2 ** 200` works fine.
- Mix an `int` with a `float` and you get a `float`: `3 + 0.5` is `3.5`.
- Underscores make big numbers readable: `1_000_000`.

### Floats are approximate

Computers store decimals in binary, so some can't be stored exactly:

```python
0.1 + 0.2            # 0.30000000000000004
0.1 + 0.2 == 0.3     # False!
```

This isn't a Python bug. Every language does it. Never compare floats with `==`. Round them, or use `math.isclose()` (Lesson 10). For money, work in whole cents or use the `decimal` module.

### Handy built-in functions

```python
abs(-5)             # 5
round(3.14159, 2)   # 3.14
round(7.5)          # 8
round(2.5)          # 2   <- Python rounds .5 to the nearest EVEN number
min(3, 9, 1)        # 1
max(3, 9, 1)        # 9
divmod(17, 5)       # (3, 2)   quotient and remainder together
```

## Comparison operators

These ask a question and answer with a `bool`:

| Operator | Meaning |
|----------|---------|
| `==` | equal to |
| `!=` | not equal to |
| `<`  `>` | less than, greater than |
| `<=`  `>=` | less than or equal, greater than or equal |

**`=` stores a value. `==` asks a question.** Mixing them up is one of the most common beginner mistakes.

Python lets you chain comparisons the way you would in maths: `0 < x < 10` is `True` when `x` is between 0 and 10.

## Logical operators

Combine yes/no answers:

| Expression | Is `True` when… |
|------------|-----------------|
| `a and b` | both are true |
| `a or b` | at least one is true |
| `not a` | `a` is false |

```python
age = 25
has_ticket = True
age >= 18 and has_ticket      # True
age < 13 or age > 65          # False
not has_ticket                # False
```

Use brackets when mixing them: `not` goes first, then `and`, then `or`. So `a or b and c` means `a or (b and c)`.

## Useful patterns

- **Even or odd:** `n % 2 == 0` is `True` for even numbers.
- **Divisible by:** `n % 5 == 0` is `True` when `n` is a multiple of 5.
- **Last digit:** `n % 10`. **Drop the last digit:** `n // 10`.
- **Between two values:** `low <= x <= high`.

## Try it yourself

1. Run [examples.py](examples.py). Before each result appears, guess what it will be.
2. In the REPL (type `python` in the terminal), try `17 // 5`, `17 % 5`, `-17 // 5` and `-17 % 5`. Negative numbers are interesting!
3. Do the exercises in [exercises.py](exercises.py).

```bash
pytest tests/test_04_numbers_and_operators.py
```

## Quick check

1. What are `10 / 4`, `10 // 4` and `10 % 4`?
2. What does `3 > 2 > 1` give?
3. Why is `0.1 + 0.2 == 0.3` false?

<details>
<summary>Answers</summary>

1. `2.5`, `2` and `2`.
2. `True`: it's the same as `3 > 2 and 2 > 1`.
3. Decimal fractions like 0.1 can't be stored exactly in binary, so the sum is off by a tiny amount.

</details>

**Previous:** [Lesson 3](../03_strings/README.md) · **Next:** [Lesson 5: Conditionals](../05_conditionals/README.md)
