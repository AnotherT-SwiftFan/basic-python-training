def test_language(exercises):
    assert exercises.language == "Python"


def test_release_year(exercises):
    assert exercises.release_year == 1991
    assert type(exercises.release_year) is int


def test_pi_approx(exercises):
    assert exercises.pi_approx == 3.14
    assert type(exercises.pi_approx) is float


def test_is_fun(exercises):
    assert exercises.is_fun is True


def test_swap(exercises):
    assert exercises.x == 10
    assert exercises.y == 5


def test_add_number_strings(exercises):
    assert exercises.add_number_strings("3", "4") == 7
    assert exercises.add_number_strings("10", "25") == 35


def test_make_label(exercises):
    assert exercises.make_label("Ada", 36) == "Ada is 36 years old"
    assert exercises.make_label("Linus", 9) == "Linus is 9 years old"


def test_is_truthy(exercises):
    assert exercises.is_truthy("hello") is True
    assert exercises.is_truthy("0") is True
    assert exercises.is_truthy(42) is True
    assert exercises.is_truthy(0) is False
    assert exercises.is_truthy("") is False
    assert exercises.is_truthy(None) is False
