import pytest


def make_tasks():
    return [
        {"title": "Buy milk", "done": False},
        {"title": "Write code", "done": True},
        {"title": "Walk dog", "done": False},
    ]


# --- Part 1: the functions ----------------------------------------------------


def test_add_task(exercises):
    tasks = []
    task = exercises.add_task(tasks, "  Buy milk  ")
    assert task == {"title": "Buy milk", "done": False}
    assert tasks == [task]
    exercises.add_task(tasks, "Write code")
    assert [t["title"] for t in tasks] == ["Buy milk", "Write code"]


@pytest.mark.parametrize("title", ["", "   "])
def test_add_task_rejects_blank_titles(exercises, title):
    tasks = []
    with pytest.raises(ValueError, match="needs a title"):
        exercises.add_task(tasks, title)
    assert tasks == []


def test_complete_task(exercises):
    tasks = make_tasks()
    exercises.complete_task(tasks, 1)
    exercises.complete_task(tasks, 3)
    assert [t["done"] for t in tasks] == [True, True, True]


@pytest.mark.parametrize("number", [0, -1, 4, 99])
def test_complete_task_rejects_bad_numbers(exercises, number):
    tasks = make_tasks()
    with pytest.raises(IndexError):
        exercises.complete_task(tasks, number)
    assert tasks == make_tasks(), "nothing should change when the number is bad"


def test_remove_task(exercises):
    tasks = make_tasks()
    removed = exercises.remove_task(tasks, 2)
    assert removed == {"title": "Write code", "done": True}
    assert [t["title"] for t in tasks] == ["Buy milk", "Walk dog"]


@pytest.mark.parametrize("number", [0, -1, 4, 99])
def test_remove_task_rejects_bad_numbers(exercises, number):
    tasks = make_tasks()
    with pytest.raises(IndexError):
        exercises.remove_task(tasks, number)
    assert tasks == make_tasks(), "nothing should change when the number is bad"


def test_count_remaining(exercises):
    assert exercises.count_remaining(make_tasks()) == 2
    assert exercises.count_remaining([]) == 0
    assert exercises.count_remaining([{"title": "x", "done": True}]) == 0


def test_format_tasks(exercises):
    assert exercises.format_tasks(make_tasks()) == (
        "1. [ ] Buy milk\n"
        "2. [x] Write code\n"
        "3. [ ] Walk dog"
    )


def test_format_tasks_when_empty(exercises):
    assert exercises.format_tasks([]) == "No tasks yet!"


def test_save_and_load_round_trip(exercises, tmp_path):
    path = tmp_path / "tasks.json"
    exercises.save_tasks(make_tasks(), path)
    assert path.exists()
    assert exercises.load_tasks(path) == make_tasks()


def test_load_tasks_when_file_is_missing(exercises, tmp_path):
    assert exercises.load_tasks(tmp_path / "nothing-here.json") == []


# --- Part 2: the whole app, driven by typed commands --------------------------


def run_app(exercises, monkeypatch, capsys, path, commands):
    typed = iter(commands)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(typed))
    exercises.main(path)
    return capsys.readouterr().out


def test_full_session(exercises, monkeypatch, capsys, tmp_path):
    path = tmp_path / "tasks.json"
    output = run_app(
        exercises, monkeypatch, capsys, path,
        ["add Buy milk", "add Write code", "done 1", "list", "quit"],
    )
    assert "Added: Buy milk" in output
    assert "1. [x] Buy milk" in output
    assert "2. [ ] Write code" in output
    assert "(1 left to do)" in output
    assert "Goodbye!" in output


def test_tasks_are_remembered_between_runs(exercises, monkeypatch, capsys, tmp_path):
    path = tmp_path / "tasks.json"
    run_app(exercises, monkeypatch, capsys, path, ["add Buy milk", "done 1", "quit"])
    output = run_app(exercises, monkeypatch, capsys, path, ["list", "remove 1", "list", "quit"])
    assert "1. [x] Buy milk" in output
    assert "Removed: Buy milk" in output
    assert "No tasks yet!" in output


def test_app_handles_mistakes_politely(exercises, monkeypatch, capsys, tmp_path):
    path = tmp_path / "tasks.json"
    output = run_app(
        exercises, monkeypatch, capsys, path,
        ["add", "done 7", "done abc", "remove 0", "dance", "quit"],
    )
    assert "A task needs a title." in output
    assert output.count("There is no task with that number.") == 2
    assert "Please give a task number" in output
    assert "Commands:" in output
