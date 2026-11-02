"""Lesson 8 - Dictionaries and Sets

Run this file and watch how the dictionaries are built up and changed.
"""

# --- Creating and reading a dictionary ----------------------------------------
person = {
    "name": "Ada",
    "age": 36,
    "languages": ["English", "French"],
}

print(person["name"])                    # Ada
print(person["languages"][0])            # English
print(person.get("email"))               # None (no error)
print(person.get("email", "unknown"))    # unknown
print("name" in person, "email" in person)   # True False
print(len(person))                       # 3

# person["email"]  # <- uncomment to see a KeyError

# --- Adding, changing, removing -----------------------------------------------
person["email"] = "ada@example.com"      # add
person["age"] = 37                       # change
print(person)

del person["email"]
age = person.pop("age")                  # remove AND get the value back
print("popped age:", age)
person.update({"city": "London", "job": "mathematician"})
print(person)

# --- Looping ------------------------------------------------------------------
for key in person:
    print("key:", key)

for key, value in person.items():
    print(f"{key} -> {value}")

# --- Counting with a dictionary -----------------------------------------------
counts = {}
for letter in "banana":
    counts[letter] = counts.get(letter, 0) + 1
print(counts)                            # {'b': 1, 'a': 3, 'n': 2}

word_counts = {}
for word in "the cat and the hat and the bat".split():
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)

# Sorting a dictionary's items by value (biggest first).
# `lambda pair: pair[1]` is a tiny nameless function that picks out the count.
# You'll learn how to write functions properly in Lesson 9.
for word, n in sorted(word_counts.items(), key=lambda pair: pair[1], reverse=True):
    print(word, n)

# --- Lists of dictionaries (records) ------------------------------------------
students = [
    {"name": "Ada", "score": 92},
    {"name": "Bo", "score": 78},
    {"name": "Cy", "score": 85},
]
for student in students:
    print(f"{student['name']}: {student['score']}")

best = max(students, key=lambda s: s["score"])   # "the student with the biggest score"
print("top student:", best["name"])

# Nested dictionaries
inventory = {
    "apple": {"price": 0.5, "stock": 40},
    "bread": {"price": 2.0, "stock": 5},
}
inventory["apple"]["stock"] -= 3
print(inventory["apple"]["stock"])       # 37

# --- Grouping: a dict whose values are lists ----------------------------------
groups = {}
for word in ["ant", "bee", "ape", "bat", "cow"]:
    first = word[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(word)
print(groups)

# --- Sets ---------------------------------------------------------------------
tags = {"python", "code", "python"}      # duplicates vanish
print(tags)

tags.add("learning")
tags.discard("code")
print(tags, "python" in tags)

empty_set = set()                        # {} would make an empty DICT
print(type(empty_set), type({}))

# Set maths
a = {1, 2, 3, 4}
b = {3, 4, 5}
print("union:       ", a | b)
print("intersection:", a & b)
print("difference:  ", a - b)
print("symmetric:   ", a ^ b)

# Removing duplicates (order is not guaranteed)
print(sorted(set([3, 1, 3, 2, 1])))      # sorted() puts them back in order

# How many different letters are in a word?
print(len(set("mississippi")))           # 4
