"""Mini project - a command-line to-do list

Your job: finish the seven functions in Part 1. The menu loop in Part 2 is already
written and uses your functions, so once they work you can run this very file
and use your own app:

    python lessons/14_mini_project/exercises.py

Check your functions with:

    pytest tests/test_14_mini_project.py
"""

import json
from pathlib import Path

# Where tasks are saved between runs: a file called tasks.json next to this script.
TASKS_FILE = Path(__file__).parent / "tasks.json"

# A task is a dictionary:  {"title": "Buy milk", "done": False}
# The to-do list is a plain Python list of those dictionaries.


# =============================================================================
# Part 1: your code
# =============================================================================


def add_task(tasks, title):
    """Add a new task to the END of the `tasks` list and return the new task.

    - The task is a dictionary with a "title" and a "done" flag (False to start).
    - Remove spaces from both ends of the title before storing it.
    - If the title is empty (or only spaces), raise ValueError("A task needs a title.")
      and don't add anything.

    add_task(tasks, "  Buy milk ") -> {"title": "Buy milk", "done": False}
    """
    pass  # TODO


def complete_task(tasks, number):
    """Mark the task as done. `number` is what the user sees: the first task is 1.

    If there is no task with that number, raise IndexError. That includes 0 and
    negative numbers! (Careful: tasks[-1] would NOT raise an error on its own.)

    Hint: remove_task needs the same check, so a small helper function is a good idea.
    """
    pass  # TODO


def remove_task(tasks, number):
    """Remove the task with this number (the first task is 1) and return it.

    Raise IndexError if there is no such task, just like complete_task.
    """
    pass  # TODO


def count_remaining(tasks):
    """Return how many tasks are NOT done yet."""
    pass  # TODO


def format_tasks(tasks):
    """Return the tasks as numbered text, one per line, with [x] for done and [ ] for not:

        1. [ ] Buy milk
        2. [x] Write code

    There is no line break after the last line.
    If there are no tasks at all, return "No tasks yet!" instead.

    Hint: build a list of lines, then join them with "\\n".
    """
    pass  # TODO


def save_tasks(tasks, path):
    """Save the list of tasks to the file at `path` as JSON."""
    pass  # TODO


def load_tasks(path):
    """Read the list of tasks back from the JSON file at `path`.
    If the file doesn't exist yet, return an empty list.
    """
    pass  # TODO


# =============================================================================
# Part 2: already written. Read it, and see how it uses your functions.
# =============================================================================

HELP = "Commands: add <title> | list | done <number> | remove <number> | quit"


def parse_number(text):
    """Turn the text the user typed into a whole number, or raise a friendly error."""
    try:
        return int(text)
    except ValueError:
        raise ValueError("Please give a task number, like: done 1")


def main(path=TASKS_FILE):
    tasks = load_tasks(path)
    print("My To-Do List")
    print(HELP)

    while True:
        line = input("> ").strip()
        # partition splits at the first space: "done 2" -> ("done", " ", "2")
        command, _, argument = line.partition(" ")
        command = command.lower()

        try:
            if command == "add":
                task = add_task(tasks, argument)
                save_tasks(tasks, path)
                print(f"Added: {task['title']}")
            elif command == "list":
                print(format_tasks(tasks))
                if tasks:
                    print(f"({count_remaining(tasks)} left to do)")
            elif command == "done":
                complete_task(tasks, parse_number(argument))
                save_tasks(tasks, path)
                print("Nice work!")
            elif command == "remove":
                removed = remove_task(tasks, parse_number(argument))
                save_tasks(tasks, path)
                print(f"Removed: {removed['title']}")
            elif command == "quit":
                print("Goodbye!")
                break
            else:
                print(HELP)
        except ValueError as error:
            print(f"Oops: {error}")
        except IndexError:
            print("There is no task with that number.")


if __name__ == "__main__":
    main()
