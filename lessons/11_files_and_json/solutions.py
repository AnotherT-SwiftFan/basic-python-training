"""Lesson 11 solutions - try the exercises yourself before reading this!"""

import csv
import json
from pathlib import Path


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read().splitlines()


def count_words_in_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return len(file.read().split())


def append_line(path, line):
    with open(path, "a", encoding="utf-8") as file:
        file.write(line + "\n")


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_or_default(path, default):
    if not Path(path).exists():
        return default
    return load_json(path)


def read_csv_rows(path):
    with open(path, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def total_column(path, column):
    total = 0.0
    for row in read_csv_rows(path):
        total += float(row[column])
    return total
