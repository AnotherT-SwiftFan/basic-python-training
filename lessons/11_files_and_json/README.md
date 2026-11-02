# Lesson 11: Files and JSON

**Goal:** make your programs remember things by reading and writing files, including the JSON and CSV formats that real projects use all the time.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## Paths: telling Python which file

A **path** is a file's address. Python's `pathlib` module treats paths as objects:

```python
from pathlib import Path

folder = Path("data")                # a relative path
notes = folder / "notes.txt"         # `/` joins path pieces: data/notes.txt
notes.name                           # "notes.txt"
notes.suffix                         # ".txt"
notes.exists()                       # True or False
folder.mkdir(exist_ok=True)          # create the folder (no error if it exists)
```

### Relative paths depend on where you run from

`Path("notes.txt")` means "a file called notes.txt in the **current working directory**", which is wherever the terminal was when you ran the program. That changes between machines and tools, which causes the dreaded "it works on my computer".

To refer to files **next to your script**, anchor the path to the script itself:

```python
HERE = Path(__file__).parent         # the folder this .py file lives in
notes = HERE / "notes.txt"
```

`__file__` is a built-in variable holding the path of the current file. Use this pattern and your script works wherever it's run from. Don't hard-code paths like `C:\Users\ada\...`. They break on every other computer.

## Reading and writing text

The standard way is `open()` inside a `with` block:

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("First line\n")
    file.write("Second line\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

- `with` closes the file for you when the block ends, even if something goes wrong. Always use it.
- `encoding="utf-8"` makes sure accents, emoji and non-English text work on every system.
- The **mode** says what you want to do:

| Mode | Meaning |
|------|---------|
| `"r"` | read (the default). The file must exist. |
| `"w"` | write. **Creates the file, or erases it if it exists!** |
| `"a"` | append. Adds to the end, creating the file if needed. |

### Ways to read

```python
text = file.read()               # the whole file as one string
lines = file.readlines()         # a list of lines (each ends with "\n")
for line in file:                # one line at a time (best for big files)
    print(line.strip())          # strip() removes the trailing "\n"
```

`text.splitlines()` splits a string into lines without the `\n` characters.

### Writing

`file.write(...)` writes exactly what you give it. **It doesn't add a new line**, so add `"\n"` yourself. `print("text", file=file)` does add one.

### The shortcut for small files

```python
notes.write_text("Hello\n", encoding="utf-8")
text = notes.read_text(encoding="utf-8")
```

## JSON: saving structured data

**JSON** is a text format for dictionaries, lists, strings, numbers, booleans and null. Nearly every web API and config file uses it, and it looks almost exactly like the Python data you already know:

```json
{"name": "Ada", "scores": [90, 85], "active": true, "nickname": null}
```

```python
import json

data = {"name": "Ada", "scores": [90, 85], "active": True, "nickname": None}

with open("ada.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)          # write Python data as JSON

with open("ada.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)                 # read JSON back into Python data
```

| Python | JSON |
|--------|------|
| `dict` | object `{}` |
| `list`, `tuple` | array `[]` |
| `str` | string |
| `int`, `float` | number |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

Things to remember:

- `indent=2` makes the file easy for humans to read.
- `json.dumps(data)` and `json.loads(text)` (with an **s**) work on strings rather than files.
- JSON object keys are always text, so `{1: "a"}` comes back as `{"1": "a"}`.
- Tuples come back as lists. Custom objects and sets can't be saved directly.

## CSV: spreadsheet-style data

CSV files hold rows of comma-separated values. `csv.DictReader` turns each row into a dictionary using the header row for the keys:

```python
import csv

with open("people.csv", "r", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row["name"], row["age"])         # every value is a str!
```

- Open CSV files with `newline=""`. The `csv` module handles line endings itself.
- Everything comes in as text, so convert numbers yourself: `int(row["age"])`.
- Write with `csv.DictWriter(file, fieldnames=[...])`, then `writeheader()` and `writerow({...})`.

## When the file isn't there

Reading a file that doesn't exist raises `FileNotFoundError`. Lesson 12 shows how to handle that gracefully. For now you can check first with `Path.exists()`.

## Try it yourself

1. Run [examples.py](examples.py). It creates an `output/` folder next to the script. Open the files it made in VS Code.
2. Run it a second time. Which files changed and which just grew?
3. Do the exercises in [exercises.py](exercises.py). The tests use temporary folders, so they won't touch your own files.

```bash
pytest tests/test_11_files_and_json.py
```

## Quick check

1. What happens if you open an existing file with mode `"w"`?
2. Why use `with open(...)`?
3. Does `json.load` take a file or a string? What about `json.loads`?

<details>
<summary>Answers</summary>

1. Its contents are erased immediately. Use `"a"` to add to the end instead.
2. It closes the file automatically, even if an error happens inside the block.
3. `json.load` takes an open file; `json.loads` takes a string.

</details>

**Previous:** [Lesson 10](../10_modules_and_stdlib/README.md) · **Next:** [Lesson 12: Errors and Exceptions](../12_errors_and_exceptions/README.md)
