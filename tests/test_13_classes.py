import pytest


def test_rectangle(exercises):
    r = exercises.Rectangle(3, 4)
    assert r.width == 3
    assert r.height == 4
    assert r.area() == 12
    assert r.perimeter() == 14
    assert r.is_square() is False
    assert exercises.Rectangle(5, 5).is_square() is True


def test_click_counter(exercises):
    c = exercises.ClickCounter()
    assert c.count == 0
    c.click()
    c.click()
    assert c.count == 2
    c.reset()
    assert c.count == 0


def test_click_counters_are_independent(exercises):
    a, b = exercises.ClickCounter(), exercises.ClickCounter()
    a.click()
    assert a.count == 1
    assert b.count == 0


def test_bank_account_basics(exercises):
    account = exercises.BankAccount("Ada", 100)
    assert account.owner == "Ada"
    assert account.balance == 100
    account.deposit(50)
    assert account.balance == 150
    account.withdraw(30)
    assert account.balance == 120
    assert exercises.BankAccount("Bo").balance == 0


def test_bank_account_rules(exercises):
    account = exercises.BankAccount("Ada", 100)
    with pytest.raises(ValueError, match="deposit must be positive"):
        account.deposit(0)
    with pytest.raises(ValueError, match="withdrawal must be positive"):
        account.withdraw(-5)
    with pytest.raises(ValueError, match="insufficient funds"):
        account.withdraw(500)
    assert account.balance == 100, "failed operations must not change the balance"


def test_bank_account_str(exercises):
    assert str(exercises.BankAccount("Ada", 100)) == "Ada: $100.00"
    assert str(exercises.BankAccount("Bo")) == "Bo: $0.00"
    assert str(exercises.BankAccount("Cy", 1234.5)) == "Cy: $1,234.50"


def test_animal(exercises):
    animal = exercises.Animal("Thing")
    assert animal.name == "Thing"
    assert animal.speak() == "..."
    assert animal.describe() == "Thing says ..."


def test_dog_and_cat(exercises):
    assert exercises.Dog("Rex").describe() == "Rex says Woof!"
    assert exercises.Cat("Tom").describe() == "Tom says Meow!"
    assert exercises.Dog("Rex").name == "Rex"


def test_stack(exercises):
    s = exercises.Stack()
    assert s.is_empty() is True
    assert len(s) == 0
    s.push("a")
    s.push("b")
    assert s.is_empty() is False
    assert len(s) == 2
    assert s.peek() == "b"
    assert len(s) == 2
    assert s.pop() == "b"
    assert s.pop() == "a"
    assert s.is_empty() is True


def test_stack_empty_errors(exercises):
    s = exercises.Stack()
    with pytest.raises(IndexError, match="stack is empty"):
        s.pop()
    with pytest.raises(IndexError, match="stack is empty"):
        s.peek()
