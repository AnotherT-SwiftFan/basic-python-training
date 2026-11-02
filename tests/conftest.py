"""Shared setup for the course tests.

Each test file is named test_<NN>_<topic>.py and checks the matching
lessons/<NN>_<topic>/exercises.py. The `exercises` fixture below loads that file
and hands it to the test, so tests can write `exercises.some_function(...)`.

Mentors: set CHECK_SOLUTIONS=1 to load solutions.py instead of exercises.py.
"""

import importlib.util
import os
from pathlib import Path

import pytest

LESSONS_DIR = Path(__file__).resolve().parent.parent / "lessons"
FILENAME = "solutions.py" if os.environ.get("CHECK_SOLUTIONS") == "1" else "exercises.py"


@pytest.fixture
def exercises(request):
    topic = Path(request.module.__file__).stem.removeprefix("test_")  # e.g. "03_strings"
    path = LESSONS_DIR / topic / FILENAME
    spec = importlib.util.spec_from_file_location(f"{topic}_{path.stem}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
