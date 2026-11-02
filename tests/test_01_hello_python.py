def printed_lines(capsys):
    return capsys.readouterr().out.splitlines()


def test_say_hello(exercises, capsys):
    exercises.say_hello()
    assert printed_lines(capsys) == ["Hello, world!"]


def test_three_lines(exercises, capsys):
    exercises.three_lines()
    assert printed_lines(capsys) == ["Python", "is", "fun"]


def test_fruit_list(exercises, capsys):
    exercises.fruit_list()
    assert printed_lines(capsys) == ["apples, bananas, cherries"]


def test_print_the_sum(exercises, capsys):
    exercises.print_the_sum()
    assert printed_lines(capsys) == ["42"]


def test_print_a_box(exercises, capsys):
    exercises.print_a_box()
    assert printed_lines(capsys) == ["+------+", "| Done |", "+------+"]


def test_return_greeting(exercises, capsys):
    assert exercises.return_greeting() == "Hello from Python"
    assert printed_lines(capsys) == [], "return_greeting should return the text, not print it"
