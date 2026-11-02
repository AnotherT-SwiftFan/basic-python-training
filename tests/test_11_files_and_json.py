import pytest


def test_write_lines(exercises, tmp_path):
    path = tmp_path / "out.txt"
    path.write_text("old content that must disappear\n", encoding="utf-8")
    exercises.write_lines(path, ["one", "two", "three"])
    assert path.read_text(encoding="utf-8") == "one\ntwo\nthree\n"


def test_read_lines(exercises, tmp_path):
    path = tmp_path / "in.txt"
    path.write_text("one\ntwo\nthree\n", encoding="utf-8")
    assert exercises.read_lines(path) == ["one", "two", "three"]


def test_count_words_in_file(exercises, tmp_path):
    path = tmp_path / "words.txt"
    path.write_text("the quick brown fox\njumps  over\n\nthe lazy dog\n", encoding="utf-8")
    assert exercises.count_words_in_file(path) == 9


def test_append_line(exercises, tmp_path):
    path = tmp_path / "log.txt"
    path.write_text("first\n", encoding="utf-8")
    exercises.append_line(path, "second")
    exercises.append_line(path, "third")
    assert path.read_text(encoding="utf-8") == "first\nsecond\nthird\n"


def test_append_line_creates_file(exercises, tmp_path):
    path = tmp_path / "new.txt"
    exercises.append_line(path, "hello")
    assert path.read_text(encoding="utf-8") == "hello\n"


def test_save_and_load_json(exercises, tmp_path):
    path = tmp_path / "data.json"
    data = {"name": "Ada", "scores": [90, 85], "active": True, "nickname": None}
    exercises.save_json(path, data)
    assert exercises.load_json(path) == data


def test_load_json_reads_existing_file(exercises, tmp_path):
    path = tmp_path / "given.json"
    path.write_text('{"a": [1, 2, 3]}', encoding="utf-8")
    assert exercises.load_json(path) == {"a": [1, 2, 3]}


def test_load_or_default(exercises, tmp_path):
    missing = tmp_path / "missing.json"
    assert exercises.load_or_default(missing, {"x": 1}) == {"x": 1}

    present = tmp_path / "present.json"
    present.write_text('["a", "b"]', encoding="utf-8")
    assert exercises.load_or_default(present, []) == ["a", "b"]


def test_read_csv_rows(exercises, tmp_path):
    path = tmp_path / "people.csv"
    path.write_text("name,age\nAda,36\nBo,29\n", encoding="utf-8")
    assert exercises.read_csv_rows(path) == [
        {"name": "Ada", "age": "36"},
        {"name": "Bo", "age": "29"},
    ]


def test_total_column(exercises, tmp_path):
    path = tmp_path / "prices.csv"
    path.write_text("item,price\napple,1.5\nbread,2.25\n", encoding="utf-8")
    assert exercises.total_column(path, "price") == pytest.approx(3.75)
