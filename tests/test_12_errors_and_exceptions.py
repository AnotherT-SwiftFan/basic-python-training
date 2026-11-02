import pytest


def test_safe_int(exercises):
    assert exercises.safe_int("42") == 42
    assert exercises.safe_int("abc") == 0
    assert exercises.safe_int("abc", -1) == -1
    assert exercises.safe_int("") == 0
    assert exercises.safe_int("3.5") == 0


def test_safe_divide(exercises):
    assert exercises.safe_divide(10, 4) == 2.5
    assert exercises.safe_divide(1, 0) is None


def test_get_item(exercises):
    assert exercises.get_item(["a", "b"], 1) == "b"
    assert exercises.get_item(["a", "b"], 5) is None
    assert exercises.get_item(["a", "b"], 5, "none") == "none"
    assert exercises.get_item(["a", "b"], -1) == "b"


def test_read_int_file(exercises, tmp_path):
    good = tmp_path / "number.txt"
    good.write_text("42\n", encoding="utf-8")
    assert exercises.read_int_file(good) == 42
    assert exercises.read_int_file(tmp_path / "missing.txt") is None


def test_read_int_file_bad_content_raises(exercises, tmp_path):
    bad = tmp_path / "bad.txt"
    bad.write_text("not a number", encoding="utf-8")
    with pytest.raises(ValueError):
        exercises.read_int_file(bad)


def test_validate_age(exercises):
    assert exercises.validate_age(30) == 30
    assert exercises.validate_age(0) == 0
    assert exercises.validate_age(150) == 150
    for bad_age in (-1, 151, 1000):
        with pytest.raises(ValueError, match="age must be between 0 and 150"):
            exercises.validate_age(bad_age)


def test_parse_ints(exercises):
    assert exercises.parse_ints(["1", "two", "3", ""]) == [1, 3]
    assert exercises.parse_ints([]) == []
    assert exercises.parse_ints(["x", "y"]) == []


def test_withdraw(exercises):
    assert exercises.withdraw(100, 30) == 70
    assert exercises.withdraw(100, 100) == 0
    with pytest.raises(ValueError, match="insufficient funds"):
        exercises.withdraw(50, 80)
    with pytest.raises(ValueError, match="amount must be positive"):
        exercises.withdraw(50, 0)
    with pytest.raises(ValueError, match="amount must be positive"):
        exercises.withdraw(50, -5)
