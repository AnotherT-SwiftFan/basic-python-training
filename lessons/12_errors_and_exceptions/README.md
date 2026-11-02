# Lesson 12: Errors and Exceptions

**Goal:** understand what goes wrong, handle expected problems gracefully, and find bugs methodically.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## Three kinds of problem

| Kind | When it shows up | Example |
|------|------------------|---------|
| **Syntax error** | Before the program even starts | a missing colon or bracket |
| **Exception** | While the program runs | `int("abc")`, a missing file, dividing by zero |
| **Logic bug** | Never as an error. The answer is just wrong | using `+` where you meant `-` |

This lesson is mostly about exceptions, and then about hunting down logic bugs.

## Reading a traceback

When an exception isn't handled, Python stops and prints a **traceback**:

```text
Traceback (most recent call last):
  File "shop.py", line 12, in <module>
    total = calculate_total(prices)
  File "shop.py", line 6, in calculate_total
    return sum(prices) / len(prices)
ZeroDivisionError: division by zero
```

1. **Start at the bottom.** `ZeroDivisionError: division by zero` is what happened.
2. The line just above shows the code that caused it: `shop.py`, line 6.
3. Lines further up show how you got there (the chain of calls). `<module>` means "top level of the file".
4. In VS Code, `Ctrl+Click` on a `File "…", line N` link in the terminal to jump straight to that line.

## Common exceptions

| Exception | Typical cause |
|-----------|---------------|
| `ValueError` | Right type, wrong value: `int("abc")` |
| `TypeError` | Wrong type: `"a" + 1`, or calling a function with the wrong arguments |
| `KeyError` | Missing dictionary key: `d["nope"]` |
| `IndexError` | List/string position out of range: `[1, 2][5]` |
| `NameError` | Using a name that doesn't exist (usually a typo) |
| `AttributeError` | Using a method/attribute that doesn't exist: `"abc".push("d")` |
| `ZeroDivisionError` | `5 / 0` |
| `FileNotFoundError` | Opening a file that isn't there |
| `ImportError` / `ModuleNotFoundError` | A module can't be found |

## `try` / `except`

Wrap code that might fail in `try`, and say what to do about it in `except`:

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("That wasn't a number.")
```

If nothing goes wrong, the `except` block is skipped. If a `ValueError` happens, Python jumps straight to it.

### The full form

```python
try:
    number = int(text)
except ValueError:                 # catch a specific exception
    print("Not a number")
except (TypeError, KeyError):      # or several at once
    print("Something else")
except Exception as error:         # catch anything else, keeping the details
    print("Unexpected:", error)
else:
    print("Worked!", number)       # runs only if NO exception happened
finally:
    print("Always runs")           # runs no matter what: good for cleanup
```

**Rules of thumb:**

- Catch the **most specific** exception you can. `except ValueError` is good; a bare `except:` hides every bug, even typos and `Ctrl+C`.
- Put as **little code** as possible inside `try`.
- Don't swallow errors silently. At the very least print or log what happened.
- Only catch exceptions you know how to handle. If you can't do anything useful, let it crash. A loud failure beats a silent wrong answer.

## `raise`: creating your own errors

Your functions can reject bad input too:

```python
def set_age(age):
    if age < 0:
        raise ValueError("age can't be negative")
    return age
```

The caller can then `try` / `except ValueError` just like with Python's own functions. Write messages that say what was wrong and, if you can, what would be right.

## Ask forgiveness or look first?

Two styles for the same problem:

```python
# Look before you leap
if key in data:
    value = data[key]

# Easier to ask forgiveness than permission
try:
    value = data[key]
except KeyError:
    value = None
```

Both are fine. Python programmers lean towards `try/except` when failure is rare, and checks like `in` or `.get()` when a miss is normal.

## Validating user input

The classic pattern is a loop that keeps asking until it gets something valid:

```python
while True:
    text = input("Pick a number from 1 to 10: ")
    try:
        number = int(text)
    except ValueError:
        print("Please type digits only.")
        continue
    if 1 <= number <= 10:
        break
    print("That's outside 1-10.")
```

## Debugging: finding logic bugs

The program runs but gives the wrong answer. Don't guess. Investigate.

1. **Reproduce it** with the smallest input that still shows the problem.
2. **Read the code aloud** (rubber-duck debugging): explain each line to a rubber duck, or a colleague. You will often find the bug yourself mid-sentence.
3. **Print the values.** `print(f"{total=}")` at key points shows what's really happening. Quick, but remember to remove the prints afterwards.
4. **Use the debugger**, which is much more powerful:
   - Click left of a line number to set a breakpoint (red dot), then press `F5`.
   - The program pauses on that line. Look at **Variables** in the side panel.
   - `F10` runs one line, `F11` steps into a function call, `F5` continues.
   - Right-click a breakpoint → **Edit Breakpoint → Expression** to pause only when, say, `i == 99`.
5. **Change one thing at a time**, then re-run.
6. **Search the exact error message** (without your file names). Someone has hit it before.

`assert condition, "message"` is a handy way to state something that must be true. If it isn't, the program stops right there with your message: `assert total >= 0, "total went negative"`.

## Try it yourself

1. Run [examples.py](examples.py). Each section shows one exception being handled. At the very end it asks you for a number.
2. Open [examples.py](examples.py), find the function `buggy_average`, set a breakpoint inside it, and step through it with the debugger to find the bug.
3. Do the exercises in [exercises.py](exercises.py).

```bash
pytest tests/test_12_errors_and_exceptions.py
```

## Quick check

1. Which line of a traceback tells you what went wrong?
2. Why is a bare `except:` a bad idea?
3. When does the `else` block of a `try` statement run?

<details>
<summary>Answers</summary>

1. The last line, which names the exception and gives its message.
2. It catches every error, including typos and `Ctrl+C`, and hides real bugs.
3. Only when the `try` block finished without raising an exception.

</details>

**Previous:** [Lesson 11](../11_files_and_json/README.md) · **Next:** [Lesson 13: Classes](../13_classes/README.md)
