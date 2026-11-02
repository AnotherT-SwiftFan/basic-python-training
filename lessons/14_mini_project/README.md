# Lesson 14: Mini Project: A To-Do App

**Goal:** combine everything from the course into one small, working command-line program.

**Files in this lesson:** [exercises.py](exercises.py) (the app, with some functions for you to write) · [solutions.py](solutions.py)

There's no separate `examples.py` this time. The app *is* the example.

## What you're building

A to-do list you control by typing commands. It remembers your tasks between runs by saving them to a JSON file.

```text
My To-Do List
Commands: add <title> | list | done <number> | remove <number> | quit
> add Buy milk
Added: Buy milk
> add Write some Python
Added: Write some Python
> list
1. [ ] Buy milk
2. [ ] Write some Python
(2 left to do)
> done 1
Nice work!
> list
1. [x] Buy milk
2. [ ] Write some Python
(1 left to do)
> done 9
There is no task with that number.
> quit
Goodbye!
```

Run it again later and your tasks are still there.

## How the code is organised

Open [exercises.py](exercises.py). It has two parts:

- **Part 1: your code.** Seven small functions that each do one job. This is what the tests check.
- **Part 2: already written.** The menu loop (`main`) that reads commands and calls your functions. Read it carefully. It uses nearly everything you've learned, and the way it handles errors is a good example of Lesson 12.

A task is a dictionary: `{"title": "Buy milk", "done": False}`. The to-do list is a plain list of those dictionaries.

## Build it in this order

Run the tests after each step with:

```bash
pytest tests/test_14_mini_project.py
```

(Tests for functions you haven't written yet will fail. Focus on the one you're working on, or run a single test: `pytest tests/test_14_mini_project.py -k add_task`.)

| Step | Function | You'll use |
|------|----------|------------|
| 1 | `add_task` | strings (`strip`), dictionaries, lists, `raise ValueError` |
| 2 | `format_tasks` | `for` + `enumerate`, f-strings, `"\n".join(...)` |
| 3 | `count_remaining` | loops, conditions, the accumulator pattern |
| 4 | `complete_task` | list indexing (careful with numbering!), `raise IndexError` |
| 5 | `remove_task` | `list.pop`, reusing a check from step 4 |
| 6 | `save_tasks` | `open`, `json.dump` |
| 7 | `load_tasks` | `Path.exists`, `json.load` |

After step 2 you could already run the app and `add` / `list` tasks, but nothing is saved until steps 6 and 7 are done.

### Watch out for this

The user sees tasks numbered from **1**, but Python lists start at **0**. So task number 1 lives at `tasks[0]`. And be careful: `tasks[-1]` is a valid way to get the *last* item, so a user typing `done 0` would quietly complete the last task if you only subtract 1 and don't check the number first. The tests check for it.

## Run your app

When the tests pass, run the app for real:

```bash
python lessons/14_mini_project/exercises.py
```

Or press **▶** with `exercises.py` open. A `tasks.json` file appears next to it (Git ignores it, so it won't be committed).

Try to break it: type nonsense, an empty `add`, `done abc`, `remove 99`. Does it always respond politely?

## Stretch goals

Pick any of these to push yourself further:

1. **Clear completed.** Add a `clear` command that removes every finished task.
2. **Edit.** Add `rename <number> <new title>`.
3. **Priorities or due dates.** Store a `"priority"` or `"due"` key on each task, show it in the list, and sort by it.
4. **Search.** Add `find <word>` that lists tasks whose title contains the word (ignore capitals).
5. **Your own tests.** Write extra tests in `tests/` for your new features.
6. **Refactor into a class.** Create a `TodoList` class that owns the list of tasks and has `add`, `complete`, `remove`, `save` and `load` methods.
7. **Command-line options.** Use the standard `argparse` module so you can run `python todo.py add "Buy milk"` without the menu.

## You made it!

If you've worked through all 14 lessons, you can read and write real Python programs. Where next?

- Write something you'd actually use: a script that renames files, summarises a CSV, or reminds you of things.
- Learn about calling web APIs with the `requests` library.
- Read through [the official tutorial](https://docs.python.org/3/tutorial/) and notice how much of it you now understand.
- Learn Git properly, and put your own projects on GitHub.
- Keep [CHEATSHEET.md](../../CHEATSHEET.md) handy.

**Previous:** [Lesson 13](../13_classes/README.md)
