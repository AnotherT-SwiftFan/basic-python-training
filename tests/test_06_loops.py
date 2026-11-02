import pytest


@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (4, 10), (10, 55), (100, 5050)])
def test_sum_to(exercises, n, expected):
    assert exercises.sum_to(n) == expected


@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (5, 120), (10, 3628800)])
def test_factorial(exercises, n, expected):
    assert exercises.factorial(n) == expected


@pytest.mark.parametrize(
    "text, expected",
    [("Hello World", 3), ("PYTHON", 1), ("rhythm", 0), ("AEIOU", 5), ("", 0)],
)
def test_count_vowels(exercises, text, expected):
    assert exercises.count_vowels(text) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(3, "3 2 1 Liftoff!"), (1, "1 Liftoff!"), (0, "Liftoff!")],
)
def test_countdown(exercises, n, expected):
    assert exercises.countdown(n) == expected


@pytest.mark.parametrize(
    "rows, expected",
    [(3, "*\n**\n***"), (1, "*"), (0, ""), (4, "*\n**\n***\n****")],
)
def test_star_triangle(exercises, rows, expected):
    assert exercises.star_triangle(rows) == expected


@pytest.mark.parametrize(
    "limit, expected",
    [(0, 1), (1, 2), (100, 128), (127, 128), (128, 256)],
)
def test_smallest_power_of_two_above(exercises, limit, expected):
    assert exercises.smallest_power_of_two_above(limit) == expected


@pytest.mark.parametrize("n, expected", [(0, 0), (9, 9), (1234, 10), (999, 27)])
def test_digit_sum(exercises, n, expected):
    assert exercises.digit_sum(n) == expected


@pytest.mark.parametrize("n, expected", [(1, 0), (6, 8), (7, 16), (27, 111)])
def test_collatz_steps(exercises, n, expected):
    assert exercises.collatz_steps(n) == expected
