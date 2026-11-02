import pytest


def test_greet(exercises):
    assert exercises.greet("Ada") == "Hello, Ada!"
    assert exercises.greet("Ada", "Welcome") == "Welcome, Ada!"
    assert exercises.greet(greeting="Hi", name="Bo") == "Hi, Bo!"


def test_area_of_rectangle(exercises):
    assert exercises.area_of_rectangle(3, 4) == 12
    assert exercises.area_of_rectangle(2.5, 2) == 5.0


def test_divide_with_remainder(exercises):
    assert exercises.divide_with_remainder(10, 3) == (3, 1)
    assert exercises.divide_with_remainder(20, 5) == (4, 0)


def test_bmi(exercises):
    assert exercises.bmi(81, 1.8) == 25.0
    assert exercises.bmi(height_m=1.8, weight_kg=81) == 25.0
    assert exercises.bmi(70, 1.75) == 22.9


def test_format_name(exercises):
    assert exercises.format_name("Ada", "Lovelace") == "Ada Lovelace"
    assert exercises.format_name("Ada", "Lovelace", title="Dr.") == "Dr. Ada Lovelace"


@pytest.mark.parametrize(
    "n, expected",
    [(0, False), (1, False), (2, True), (3, True), (4, False), (17, True), (25, False), (97, True)],
)
def test_is_prime(exercises, n, expected):
    assert exercises.is_prime(n) is expected


def test_primes_up_to(exercises):
    assert exercises.primes_up_to(10) == [2, 3, 5, 7]
    assert exercises.primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert exercises.primes_up_to(1) == []


def test_apply_twice(exercises):
    def double(x):
        return x * 2

    assert exercises.apply_twice(double, 3) == 12
    assert exercises.apply_twice(str.upper, "hi") == "HI"
    assert exercises.apply_twice(lambda s: s + "!", "wow") == "wow!!"
