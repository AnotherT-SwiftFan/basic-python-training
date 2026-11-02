"""Lesson 11 - Files and JSON

Run this file. It creates an `output/` folder next to this script and writes
some files into it. Open them in VS Code to see what was written.
"""

import csv
import json
from pathlib import Path

# Anchor paths to THIS file so the script works wherever it's run from.
HERE = Path(__file__).parent
OUTPUT = HERE / "output"
OUTPUT.mkdir(exist_ok=True)            # no error if the folder already exists

# --- Paths --------------------------------------------------------------------
notes_path = OUTPUT / "notes.txt"
print("name:  ", notes_path.name)
print("suffix:", notes_path.suffix)
print("folder:", notes_path.parent.name)

# --- Writing text ("w" creates the file, or ERASES it if it exists) -----------
with open(notes_path, "w", encoding="utf-8") as file:
    file.write("First line\n")             # write() does NOT add a new line
    file.write("Second line\n")
    print("Third line", file=file)         # print() does

# --- Appending ("a" adds to the end) ------------------------------------------
with open(notes_path, "a", encoding="utf-8") as file:
    file.write("Fourth line (appended)\n")

# --- Reading ------------------------------------------------------------------
with open(notes_path, "r", encoding="utf-8") as file:
    text = file.read()                     # whole file as one string
print("--- whole file ---")
print(text)

with open(notes_path, "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):   # one line at a time
        print(number, line.strip())                  # strip() removes the "\n"

print(text.splitlines())                   # a list of lines without "\n"

# --- The shortcut for small files ---------------------------------------------
quick = OUTPUT / "quick.txt"
quick.write_text("Hello from write_text!\n", encoding="utf-8")
print(quick.read_text(encoding="utf-8").strip())
print("exists?", quick.exists(), "| missing exists?", (OUTPUT / "nope.txt").exists())

# --- JSON ---------------------------------------------------------------------
person = {
    "name": "Ada",
    "scores": [90, 85],
    "active": True,
    "nickname": None,
    "address": {"city": "London"},
}

json_path = OUTPUT / "ada.json"
with open(json_path, "w", encoding="utf-8") as file:
    json.dump(person, file, indent=2)      # Python data -> JSON file

with open(json_path, "r", encoding="utf-8") as file:
    loaded = json.load(file)               # JSON file -> Python data

print(loaded == person)                    # True: a perfect round trip
print(loaded["address"]["city"])

# dumps / loads work on strings instead of files
as_text = json.dumps({"a": 1, "b": [1, 2]})
print(as_text, type(as_text))
print(json.loads(as_text), type(json.loads(as_text)))

# Gotchas: keys become text, tuples become lists
print(json.loads(json.dumps({1: "one", 2: (3, 4)})))     # {'1': 'one', '2': [3, 4]}

# --- CSV ----------------------------------------------------------------------
csv_path = OUTPUT / "people.csv"
people = [
    {"name": "Ada", "age": 36},
    {"name": "Bo", "age": 29},
]
with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(people)

with open(csv_path, "r", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        # every value comes back as text, so convert numbers yourself
        print(row["name"], int(row["age"]) + 1)

print("\nDone! Look inside the output/ folder next to this file.")
