import pytest


def test_describe_number(exercises):
    assert exercises.describe_number(5) == "positive"
    assert exercises.describe_number(-3) == "negative"
    assert exercises.describe_number(0) == "zero"


@pytest.mark.parametrize(
    "score, expected",
    [(100, "A"), (90, "A"), (89, "B"), (80, "B"), (79, "C"), (70, "C"), (65, "D"), (60, "D"), (59, "F"), (0, "F")],
)
def test_grade(exercises, score, expected):
    assert exercises.grade(score) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(15, "FizzBuzz"), (30, "FizzBuzz"), (9, "Fizz"), (10, "Buzz"), (7, "7"), (1, "1")],
)
def test_fizzbuzz(exercises, n, expected):
    assert exercises.fizzbuzz(n) == expected


@pytest.mark.parametrize(
    "age, expected",
    [(0, 0), (4, 0), (5, 8), (17, 8), (18, 12), (64, 12), (65, 9), (80, 9)],
)
def test_ticket_price(exercises, age, expected):
    assert exercises.ticket_price(age) == expected


@pytest.mark.parametrize(
    "weight, is_member, expected",
    [(0.5, False, 5), (1, False, 5), (3, False, 10), (5, False, 10), (5.1, False, 20), (50, True, 0), (0.1, True, 0)],
)
def test_shipping_cost(exercises, weight, is_member, expected):
    assert exercises.shipping_cost(weight, is_member) == expected


@pytest.mark.parametrize(
    "name, expected",
    [("ada99", True), ("abc", True), ("a" * 15, True), ("ab", False), ("a" * 16, False), ("ada_99", False), ("has space", False)],
)
def test_is_valid_username(exercises, name, expected):
    assert exercises.is_valid_username(name) is expected


@pytest.mark.parametrize(
    "day, expected",
    [("Saturday", "weekend"), ("sunday", "weekend"), ("Monday", "weekday"), ("FRIDAY", "weekday")],
)
def test_day_type(exercises, day, expected):
    assert exercises.day_type(day) == expected
