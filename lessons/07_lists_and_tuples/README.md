# Lesson 7: Lists and Tuples

**Goal:** store many values in one variable, and learn to add, remove, search and loop over them.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## Lists

A **list** is an ordered collection of values in square brackets. The items can be any type, and you can change the list after you create it.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [4, 8, 15, 16, 23, 42]
mixed = ["Ada", 36, True]
empty = []
```

### Indexing and slicing

Lists use the same indexes and slices as strings (Lesson 3), starting at 0:

```python
fruits[0]       # "apple"
fruits[-1]      # "cherry"
fruits[1:]      # ["banana", "cherry"]
fruits[::-1]    # ["cherry", "banana", "apple"]
len(fruits)     # 3
```

Unlike strings, lists can be **changed in place**:

```python
fruits[1] = "blueberry"
```

### Adding and removing

| Code | What it does |
|------|--------------|
| `items.append(x)` | add `x` to the end |
| `items.insert(i, x)` | add `x` at position `i` |
| `items.extend(other)` | add every item of `other` to the end |
| `items.remove(x)` | remove the first `x` (error if it isn't there) |
| `items.pop()` | remove and return the last item |
| `items.pop(i)` | remove and return the item at position `i` |
| `del items[i]` | remove the item at position `i` |
| `items.clear()` | remove everything |

### Searching and measuring

```python
"banana" in fruits        # True
fruits.index("cherry")    # 2   (position of the first match)
fruits.count("apple")     # 1
len(numbers)              # 6
sum(numbers)              # 108
min(numbers), max(numbers)
```

### Sorting

```python
numbers.sort()                      # sorts the list in place, returns None
sorted(numbers)                     # returns a NEW sorted list
sorted(numbers, reverse=True)       # biggest first
numbers.reverse()                   # reverses in place
```

Classic trap: `numbers = numbers.sort()` sets `numbers` to `None`, because `.sort()` changes the list and returns nothing.

### Joining lists and text

```python
"a b c".split()          # ["a", "b", "c"]
", ".join(["a", "b"])    # "a, b"   (the items must be strings)
[1, 2] + [3]             # [1, 2, 3]
[0] * 3                  # [0, 0, 0]
```

## Looping over a list

```python
for fruit in fruits:
    print(fruit)
```

If you also need the position, use `enumerate()`. To walk two lists side by side, use `zip()`:

```python
for position, fruit in enumerate(fruits, start=1):
    print(position, fruit)        # 1 apple, 2 banana, ...

for name, score in zip(["Ada", "Bo"], [90, 85]):
    print(name, score)
```

**Don't add or remove items from a list while looping over it.** The loop skips items. Build a new list instead:

```python
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
```

### List comprehensions (a preview)

The "build a new list" loop above is so common that Python has a one-line form. You'll see it in other people's code, so it's good to recognise:

```python
evens = [n for n in numbers if n % 2 == 0]
squares = [n * n for n in range(1, 6)]      # [1, 4, 9, 16, 25]
```

Read it as "n squared, for each n in range 1 to 5". Use the longer loop version until it feels natural.

## Two names, one list

Assigning a list to another variable doesn't copy it. Both names point at the same list:

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)               # [1, 2, 3, 4]  <- a changed too!

c = a.copy()           # or a[:] or list(a): a real, separate copy
```

This catches everyone out at least once. The same thing happens when you pass a list into a function that modifies it.

## Lists of lists

```python
grid = [[1, 2, 3],
        [4, 5, 6]]
grid[1][2]             # 6   (row 1, column 2)
```

## Tuples

A **tuple** is like a list that can't be changed. It's written with round brackets (or just commas):

```python
point = (3, 4)
point[0]               # 3
point[0] = 9           # TypeError: tuples are immutable
```

Use a tuple for a small, fixed group of related values: coordinates, an RGB colour, a function returning two things. The big trick is **unpacking**:

```python
x, y = point                    # x = 3, y = 4
name, age = ("Ada", 36)
first, *rest = [1, 2, 3, 4]     # first = 1, rest = [2, 3, 4]
```

A one-item tuple needs a trailing comma: `(5,)`. Without it, `(5)` is just the number 5.

## Try it yourself

1. Run [examples.py](examples.py) and follow how the list changes after each step.
2. Make a list of your five favourite films. Sort it, reverse it, and print the third one.
3. Do the exercises in [exercises.py](exercises.py).

```bash
pytest tests/test_07_lists_and_tuples.py
```

## Quick check

1. What does `[10, 20, 30, 40][1:3]` give?
2. After `a = [1, 2]` and `b = a`, then `b.append(3)`, what is `a`?
3. What does `x = [3, 1, 2].sort()` store in `x`?

<details>
<summary>Answers</summary>

1. `[20, 30]`.
2. `[1, 2, 3]`, because `a` and `b` are the same list.
3. `None`. Use `sorted([3, 1, 2])` if you want the sorted list back.

</details>

**Previous:** [Lesson 6](../06_loops/README.md) · **Next:** [Lesson 8: Dictionaries and Sets](../08_dictionaries_and_sets/README.md)
