# Lesson 6: Loops

**Goal:** repeat work without repeating code, using `for` and `while`.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## Why loops?

Imagine printing the numbers 1 to 1000. You wouldn't write 1000 `print` lines. A **loop** runs the same block of code again and again.

Python has two kinds:

- **`for`**: do something for each item in a sequence, or a set number of times.
- **`while`**: keep going as long as a condition is true.

## `for` with `range()`

```python
for i in range(5):
    print(i)          # 0, 1, 2, 3, 4
```

`range()` produces numbers. Like slicing, it **stops before** the end value.

| Call | Numbers produced |
|------|------------------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

The variable after `for` (here `i`) takes each value in turn. Name it anything. If you don't need the value, the convention is `_`:

```python
for _ in range(3):
    print("Hip hip hooray!")
```

## `for` over text

A string is a sequence of characters, so you can loop straight over it:

```python
for letter in "Python":
    print(letter)
```

(Lesson 7 shows that the same works for lists.)

## The accumulator pattern

You'll write this pattern constantly: start with an empty starting value, update it inside the loop, use it after the loop.

```python
total = 0
for n in range(1, 6):
    total += n
print(total)          # 15
```

It works for text too. Start with `""` and add to it:

```python
shout = ""
for letter in "hey":
    shout += letter.upper() + "!"
print(shout)          # H!E!Y!
```

## `while`

```python
count = 3
while count > 0:
    print(count)
    count -= 1        # <- without this line the loop never ends!
print("Liftoff!")
```

Python checks the condition before each pass. When it becomes false, the loop stops. Use `while` when you don't know in advance how many repeats you need (keep asking until the answer is valid; keep halving until the number is small).

**Infinite loops:** if the condition never becomes false, the program runs forever. Press `Ctrl+C` in the terminal to stop it.

## `break` and `continue`

- `break` leaves the loop immediately.
- `continue` skips the rest of this pass and jumps to the next one.

```python
for n in range(1, 10):
    if n % 2 == 0:
        continue          # skip even numbers
    if n > 7:
        break             # stop completely
    print(n)              # 1, 3, 5, 7
```

A common idiom is `while True:` plus a `break`, for "repeat until something happens":

```python
while True:
    answer = input("Type 'quit' to stop: ")
    if answer == "quit":
        break
```

## Nested loops

A loop inside a loop runs the inner loop completely for every pass of the outer one:

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end=" ")
    print()               # new line after each row
```

## Which loop do I use?

| Situation | Use |
|-----------|-----|
| Do something N times | `for ... in range(N)` |
| Go through every item in a sequence | `for item in sequence` |
| Repeat until some condition changes | `while` |

## Common mistakes

- **Off by one:** `range(5)` gives 0 to 4, not 1 to 5. Use `range(1, 6)` for 1 to 5.
- **Forgetting to change the `while` variable:** infinite loop.
- **Wrong indentation:** a line that should be inside the loop isn't (or vice versa). Only indented lines repeat.
- **Changing the thing you are looping over.** More on that in Lesson 7.

## Try it yourself

1. Run [examples.py](examples.py) and read the loops against their output.
2. Change `range(1, 6)` to count backwards and by twos.
3. Do the exercises in [exercises.py](exercises.py).

```bash
pytest tests/test_06_loops.py
```

## Quick check

1. How many times does `for i in range(2, 7):` run, and what's the last value of `i`?
2. What's the difference between `break` and `continue`?
3. What happens if you forget `count -= 1` in a `while count > 0:` loop?

<details>
<summary>Answers</summary>

1. 5 times (2, 3, 4, 5, 6). The last value is 6.
2. `break` ends the whole loop. `continue` only skips to the next pass.
3. The condition never becomes false, so it loops forever. Press `Ctrl+C`.

</details>

**Previous:** [Lesson 5](../05_conditionals/README.md) · **Next:** [Lesson 7: Lists and Tuples](../07_lists_and_tuples/README.md)
