import pytest


def test_hypotenuse(exercises):
    assert exercises.hypotenuse(3, 4) == pytest.approx(5.0)
    assert exercises.hypotenuse(5, 12) == pytest.approx(13.0)
    assert exercises.hypotenuse(1, 1) == pytest.approx(2 ** 0.5)


def test_round_up(exercises):
    assert exercises.round_up(2.1) == 3
    assert exercises.round_up(5) == 5
    assert exercises.round_up(-1.5) == -1


def test_days_between(exercises):
    assert exercises.days_between("2024-01-01", "2024-03-01") == 60
    assert exercises.days_between("2024-03-01", "2024-01-01") == 60
    assert exercises.days_between("2023-12-31", "2024-01-01") == 1
    assert exercises.days_between("2025-05-05", "2025-05-05") == 0


def test_weekday_name(exercises):
    assert exercises.weekday_name("2024-01-01") == "Monday"
    assert exercises.weekday_name("2000-01-01") == "Saturday"


def test_roll_dice(exercises):
    rolls = exercises.roll_dice(6, 200)
    assert len(rolls) == 200
    assert all(1 <= roll <= 6 for roll in rolls)
    assert len(set(rolls)) > 1, "200 rolls of a d6 should not all be the same number"
    assert exercises.roll_dice(1, 5) == [1, 1, 1, 1, 1]
    assert exercises.roll_dice(6, 0) == []


def test_most_common_word(exercises):
    assert exercises.most_common_word("the cat and the dog and the bird") == "the"
    assert exercises.most_common_word("Go go GO stop") == "go"
