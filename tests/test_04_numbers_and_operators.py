import pytest


def test_circle_area(exercises):
    assert exercises.circle_area(1) == pytest.approx(3.14159)
    assert exercises.circle_area(10) == pytest.approx(314.159)
    assert exercises.circle_area(0) == 0


def test_celsius_to_fahrenheit(exercises):
    assert exercises.celsius_to_fahrenheit(0) == pytest.approx(32)
    assert exercises.celsius_to_fahrenheit(100) == pytest.approx(212)
    assert exercises.celsius_to_fahrenheit(-40) == pytest.approx(-40)
    assert exercises.celsius_to_fahrenheit(37) == pytest.approx(98.6)


def test_is_even(exercises):
    assert exercises.is_even(4) is True
    assert exercises.is_even(7) is False
    assert exercises.is_even(0) is True
    assert exercises.is_even(-3) is False


def test_hours_and_minutes(exercises):
    assert exercises.hours_and_minutes(135) == "2h 15m"
    assert exercises.hours_and_minutes(45) == "0h 45m"
    assert exercises.hours_and_minutes(60) == "1h 0m"


def test_split_bill(exercises):
    assert exercises.split_bill(100, 3) == 33.33
    assert exercises.split_bill(50, 2) == 25.0
    assert exercises.split_bill(10, 4) == 2.5


@pytest.mark.parametrize(
    "year, expected",
    [(2000, True), (1900, False), (2024, True), (2023, False), (2100, False), (1996, True)],
)
def test_is_leap_year(exercises, year, expected):
    assert exercises.is_leap_year(year) is expected


@pytest.mark.parametrize(
    "x, expected",
    [(5, True), (1, True), (10, True), (11, False), (0, False)],
)
def test_in_range(exercises, x, expected):
    assert exercises.in_range(x, 1, 10) is expected


def test_last_digit(exercises):
    assert exercises.last_digit(1234) == 4
    assert exercises.last_digit(7) == 7
    assert exercises.last_digit(50) == 0


def test_drop_last_digit(exercises):
    assert exercises.drop_last_digit(1234) == 123
    assert exercises.drop_last_digit(7) == 0
