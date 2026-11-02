def test_shout(exercises):
    assert exercises.shout("hello") == "HELLO!"
    assert exercises.shout("Python rocks") == "PYTHON ROCKS!"


def test_first_and_last(exercises):
    assert exercises.first_and_last("python") == "pn"
    assert exercises.first_and_last("ab") == "ab"


def test_clean_name(exercises):
    assert exercises.clean_name("  ada LOVELACE ") == "Ada Lovelace"
    assert exercises.clean_name("GRACE hopper") == "Grace Hopper"


def test_reverse_text(exercises):
    assert exercises.reverse_text("abc") == "cba"
    assert exercises.reverse_text("") == ""


def test_count_letter(exercises):
    assert exercises.count_letter("Banana", "a") == 3
    assert exercises.count_letter("Banana", "A") == 3
    assert exercises.count_letter("Python", "z") == 0


def test_make_email(exercises):
    assert exercises.make_email("Ada", "Lovelace") == "ada.lovelace@example.com"
    assert exercises.make_email("LINUS", "Torvalds") == "linus.torvalds@example.com"


def test_format_price(exercises):
    assert exercises.format_price(1234.5) == "$1,234.50"
    assert exercises.format_price(5) == "$5.00"
    assert exercises.format_price(1000000) == "$1,000,000.00"


def test_is_palindrome(exercises):
    assert exercises.is_palindrome("level") is True
    assert exercises.is_palindrome("A man a plan a canal Panama") is True
    assert exercises.is_palindrome("Python") is False


def test_initials(exercises):
    assert exercises.initials("Ada Lovelace") == "AL"
    assert exercises.initials("grace brewster hopper") == "GH"
