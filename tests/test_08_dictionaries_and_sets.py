import pytest


def test_get_phone(exercises):
    contacts = {"Ada": "555-1234", "Bo": "555-9876"}
    assert exercises.get_phone(contacts, "Ada") == "555-1234"
    assert exercises.get_phone(contacts, "Cy") == "unknown"


def test_count_words(exercises):
    assert exercises.count_words("The cat and the hat") == {"the": 2, "cat": 1, "and": 1, "hat": 1}
    assert exercises.count_words("go GO Go") == {"go": 3}
    assert exercises.count_words("") == {}


def test_invert(exercises):
    assert exercises.invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert exercises.invert({}) == {}


def test_unique_letters(exercises):
    assert exercises.unique_letters("Hello, World!") == 7
    assert exercises.unique_letters("aAa") == 1
    assert exercises.unique_letters("123 !?") == 0


def test_common_items(exercises):
    assert exercises.common_items([1, 2, 3, 4], [3, 4, 5]) == [3, 4]
    assert exercises.common_items(["b", "a"], ["a", "b", "c"]) == ["a", "b"]
    assert exercises.common_items([1, 2], [3, 4]) == []


def test_cart_total(exercises):
    prices = {"apple": 0.5, "bread": 2.0, "milk": 1.25}
    assert exercises.cart_total(prices, {"apple": 4, "bread": 1}) == pytest.approx(4.0)
    assert exercises.cart_total(prices, {"apple": 4, "bread": 1, "milk": 2}) == pytest.approx(6.5)
    assert exercises.cart_total(prices, {}) == 0


def test_group_by_first_letter(exercises):
    words = ["apple", "avocado", "banana", "blueberry", "cherry"]
    assert exercises.group_by_first_letter(words) == {
        "a": ["apple", "avocado"],
        "b": ["banana", "blueberry"],
        "c": ["cherry"],
    }
    assert exercises.group_by_first_letter([]) == {}
