def test_ends(exercises):
    assert exercises.ends([1, 2, 3, 4]) == [1, 4]
    assert exercises.ends(["a", "b"]) == ["a", "b"]


def test_average(exercises):
    assert exercises.average([2, 4, 9]) == 5.0
    assert exercises.average([10]) == 10
    assert exercises.average([]) == 0


def test_remove_negatives(exercises):
    original = [3, -1, 4, -5, 0]
    assert exercises.remove_negatives(original) == [3, 4, 0]
    assert original == [3, -1, 4, -5, 0], "the original list must not be changed"
    assert exercises.remove_negatives([-1, -2]) == []


def test_second_largest(exercises):
    assert exercises.second_largest([10, 40, 30, 20]) == 30
    assert exercises.second_largest([1, 2]) == 1


def test_squares(exercises):
    assert exercises.squares(4) == [1, 4, 9, 16]
    assert exercises.squares(1) == [1]
    assert exercises.squares(0) == []


def test_rotate_left(exercises):
    original = [1, 2, 3, 4]
    assert exercises.rotate_left(original) == [2, 3, 4, 1]
    assert original == [1, 2, 3, 4], "the original list must not be changed"
    assert exercises.rotate_left([]) == []
    assert exercises.rotate_left([7]) == [7]


def test_min_max(exercises):
    result = exercises.min_max([3, 9, 1, 7])
    assert result == (1, 9)
    assert isinstance(result, tuple)


def test_without_duplicates(exercises):
    original = [3, 1, 3, 2, 1]
    assert exercises.without_duplicates(original) == [3, 1, 2]
    assert original == [3, 1, 3, 2, 1], "the original list must not be changed"
    assert exercises.without_duplicates([]) == []
    assert exercises.without_duplicates(["a", "a", "a"]) == ["a"]


def test_lengths(exercises):
    assert exercises.lengths(["hi", "python"]) == [2, 6]
    assert exercises.lengths([]) == []
