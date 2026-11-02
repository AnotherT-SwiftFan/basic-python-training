# Lesson 8: Dictionaries and Sets

**Goal:** look values up by name instead of by position, and work with collections of unique items.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## Dictionaries

A **dictionary** (`dict`) stores **key → value** pairs, like a real dictionary maps a word to its meaning. You look things up by key instead of by position.

```python
person = {
    "name": "Ada",
    "age": 36,
    "languages": ["English", "French"],
}
```

### Reading values

```python
person["name"]                    # "Ada"
person["email"]                   # KeyError: 'email'  <- the key doesn't exist
person.get("email")               # None               <- no error
person.get("email", "unknown")    # "unknown"          <- your own default
"name" in person                  # True  (`in` checks KEYS)
len(person)                       # 3
```

Use `[]` when the key must exist (a missing key is a bug you want to hear about). Use `.get()` when it might not.

### Adding, changing, removing

```python
person["email"] = "ada@example.com"   # adds a new key
person["age"] = 37                    # changes an existing one
del person["email"]                   # removes a key
age = person.pop("age")               # removes a key and returns its value
person.update({"city": "London"})     # merge in several pairs
```

### Looping

```python
for key in person:                    # keys
    print(key)

for value in person.values():         # values
    print(value)

for key, value in person.items():     # both together (the most useful)
    print(key, "->", value)
```

Dicts remember the order you added things in.

### Rules for keys

Keys must be **unique** and **unchangeable**: strings, numbers and tuples work; lists don't. Values can be anything.

### Counting with a dictionary

This is one of the most useful patterns in programming:

```python
counts = {}
for letter in "banana":
    counts[letter] = counts.get(letter, 0) + 1
print(counts)         # {'b': 1, 'a': 3, 'n': 2}
```

Read it as: "look up the current count (0 if we haven't seen it yet), add one, store it back."

### Records and nested data

Real data is usually a list of dictionaries, or dictionaries containing other dictionaries. This is exactly what JSON looks like (Lesson 11).

```python
students = [
    {"name": "Ada", "score": 92},
    {"name": "Bo", "score": 78},
]
for student in students:
    print(student["name"], student["score"])

inventory = {"apple": {"price": 0.5, "stock": 40}}
inventory["apple"]["stock"]        # 40
```

### Grouping with a dictionary

Dictionaries whose values are lists are good for grouping:

```python
groups = {}
for word in ["ant", "bee", "ape"]:
    first = word[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(word)
# {'a': ['ant', 'ape'], 'b': ['bee']}
```

## Sets

A **set** is an unordered collection of **unique** items. Adding something that's already there does nothing.

```python
tags = {"python", "code", "python"}   # {'python', 'code'}  duplicates vanish
empty = set()                         # NOT {} -- that makes an empty dict!
```

```python
tags.add("learning")
tags.discard("code")                  # remove if present, no error if absent
"python" in tags                      # True  (and very fast)
len(tags)
```

Sets have no order and no indexes, so `tags[0]` doesn't work.

### Set maths

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}
a | b       # union:        {1, 2, 3, 4, 5}  everything
a & b       # intersection: {3, 4}           in both
a - b       # difference:   {1, 2}           in a but not b
a ^ b       # symmetric:    {1, 2, 5}        in one but not both
```

### Removing duplicates

```python
list(set([3, 1, 3, 2, 1]))      # unique items, but the order is not guaranteed
```

If you need to keep the original order, use the loop approach from Lesson 7.

## Which collection do I use?

| I need to… | Use |
|------------|-----|
| keep things in order, allow repeats, change them | `list` |
| a fixed group of values that won't change | `tuple` |
| look something up by a name or ID | `dict` |
| keep only unique items or do overlap/difference | `set` |

## Common mistakes

- `KeyError` from `d["missing"]`: use `.get()` or check with `in`.
- Writing `{}` for an empty set. It's an empty dict. Use `set()`.
- Using a list as a key (`TypeError: unhashable type`). Use a tuple.
- Expecting `in` to check values. For a dict it checks keys. Use `value in d.values()`.
- Changing a dict's size while looping over it. Loop over a copy: `for k in list(d):`.

## Try it yourself

1. Run [examples.py](examples.py) and watch how the dictionaries are built up.
2. Make a dictionary of three friends and their ages. Loop over it with `.items()`.
3. Do the exercises in [exercises.py](exercises.py).

```bash
pytest tests/test_08_dictionaries_and_sets.py
```

## Quick check

1. If `d = {"a": 1}`, what do `d["b"]` and `d.get("b")` give?
2. What is `{1, 2, 3} & {2, 3, 4}`?
3. What does `{}` create?

<details>
<summary>Answers</summary>

1. `d["b"]` raises a `KeyError`. `d.get("b")` returns `None`.
2. `{2, 3}`: the items in both sets.
3. An empty dictionary. Use `set()` for an empty set.

</details>

**Previous:** [Lesson 7](../07_lists_and_tuples/README.md) · **Next:** [Lesson 9: Functions](../09_functions/README.md)
