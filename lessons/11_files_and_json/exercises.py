"""Lesson 11 exercises - Files and JSON

The imports are done for you. Each function receives a `path` (a Path object or
a string). The tests use temporary files, so they won't touch your own.

    pytest tests/test_11_files_and_json.py
"""

import csv
import json
from pathlib import Path


def write_lines(path, lines):
    """Write each string in `lines` to the file on its own line (replacing any old content).
    write_lines("a.txt", ["one", "two"]) leaves a file containing:
        one
        two
    """
    pass  # TODO


def read_lines(path):
    """Return the lines of the file as a list of strings WITHOUT the line breaks.
    A file containing "one\\ntwo\\n" gives ["one", "two"]
    """
    pass  # TODO


def count_words_in_file(path):
    """Return the total number of words in the file (words are separated by whitespace)."""
    pass  # TODO


def append_line(path, line):
    """Add `line` to the END of the file on its own line, keeping the existing content.
    The file may not exist yet, in which case it should be created.
    """
    pass  # TODO


def save_json(path, data):
    """Write `data` (dicts, lists, strings, numbers...) to the file as JSON."""
    pass  # TODO


def load_json(path):
    """Read the JSON file and return the Python data inside it."""
    pass  # TODO


def load_or_default(path, default):
    """Like load_json, but if the file doesn't exist return `default` instead.
    Hint: Path(path).exists()
    """
    pass  # TODO


def read_csv_rows(path):
    """Read a CSV file that has a header row and return a list of dictionaries,
    one per data row.
    A file "name,age\\nAda,36\\n" gives [{"name": "Ada", "age": "36"}]
    (values stay as text).
    """
    pass  # TODO


def total_column(path, column):
    """Add up all the numbers in one column of a CSV file (with a header row).
    Return the total as a float. Reuse read_csv_rows if you like.
    """
    pass  # TODO
