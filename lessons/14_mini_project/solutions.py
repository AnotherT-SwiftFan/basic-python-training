"""Mini project solutions - try it yourself before reading this!

You can run this file to use the finished app:

    python lessons/14_mini_project/solutions.py
"""

import json
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"


# =============================================================================
# Part 1: the functions
# =============================================================================


def add_task(tasks, title):
    title = title.strip()
    if not title:
        raise ValueError("A task needs a title.")
    task = {"title": title, "done": False}
    tasks.append(task)
    return task


def check_number(tasks, number):
    """Shared by complete_task and remove_task. Rejects 0, negatives and too-big numbers."""
    if not 1 <= number <= len(tasks):
        raise IndexError(f"No task number {number}")


def complete_task(tasks, number):
    check_number(tasks, number)
    tasks[number - 1]["done"] = True


def remove_task(tasks, number):
    check_number(tasks, number)
    return tasks.pop(number - 1)


def count_remaining(tasks):
    remaining = 0
    for task in tasks:
        if not task["done"]:
            remaining += 1
    return remaining


def format_tasks(tasks):
    if not tasks:
        return "No tasks yet!"
    lines = []
    for number, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        lines.append(f"{number}. [{mark}] {task['title']}")
    return "\n".join(lines)


def save_tasks(tasks, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def load_tasks(path):
    if not Path(path).exists():
        return []
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


# =============================================================================
# Part 2: the menu loop (identical to exercises.py)
# =============================================================================

HELP = "Commands: add <title> | list | done <number> | remove <number> | quit"


def parse_number(text):
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
