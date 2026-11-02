# Lesson 13: Classes

**Goal:** bundle data and the code that works on it into your own types, called classes.

**Files in this lesson:** [examples.py](examples.py) · [exercises.py](exercises.py) · [solutions.py](solutions.py)

## You've been using objects all along

Strings, lists and dictionaries are **objects**. Each one holds some data and comes with **methods** that work on it: `"hi".upper()`, `[3, 1].sort()`, `{}.get("a")`. A **class** is the blueprint for a kind of object, and writing your own lets you create types that fit your problem: a `BankAccount`, a `Task`, a `Player`.

Each object made from a class is called an **instance**.

## Your first class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1


rex = Dog("Rex", 3)          # create an instance
print(rex.name)              # Rex          (an attribute)
print(rex.bark())            # Rex says Woof!   (a method)
rex.birthday()
print(rex.age)               # 4
```

Piece by piece:

- `class Dog:` starts the blueprint. Class names use `CapitalisedWords`.
- `__init__` is the **initialiser**. Python calls it automatically when you write `Dog("Rex", 3)`. It sets up the new object's starting data.
- **`self`** is the instance the method is working on. It's always the first parameter of a method, but you don't pass it when calling: `rex.bark()` passes `rex` as `self` for you.
- `self.name = name` stores a value on the object. Those stored values are **attributes**.
- Methods are just functions defined inside the class.

Every instance has its own data:

```python
fido = Dog("Fido", 5)
rex.birthday()
print(rex.age, fido.age)     # 5 5  -> rex is 5 now; fido was already 5
```

## Making objects printable: `__str__`

By default, `print(rex)` shows something unhelpful like `<__main__.Dog object at 0x…>`. Define `__str__` to control it:

```python
class Dog:
    ...
    def __str__(self):
        return f"{self.name} ({self.age})"

print(rex)                   # Rex (5)
```

Methods with double underscores on both sides are called **special methods**. You don't call them yourself. Python calls them for you: `__str__` for `print()` and `str()`, `__len__` for `len()`, `__eq__` for `==`, and so on.

## Keeping data valid

Classes are a good place to protect rules, such as "a balance can't go negative":

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
```

By convention, a name that starts with an underscore (`self._cache`) means "internal, please don't touch from outside". Python doesn't enforce it.

## Inheritance

A class can build on another class, getting all its attributes and methods for free, and then add to them or override them:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.speak()}"


class Dog(Animal):                 # Dog is an Animal
    def speak(self):               # override
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


for pet in [Dog("Rex"), Cat("Tom"), Animal("Thing")]:
    print(pet.describe())
```

`describe` is written once in `Animal`, but calls whichever `speak` belongs to the actual object. That's **polymorphism**. Use `super().__init__(...)` when a subclass needs its own `__init__` but still wants the parent's setup to run.

`isinstance(rex, Animal)` is `True` for a `Dog` instance.

Inheritance is powerful but easy to overuse. Prefer a simple class that *holds* other objects (composition) unless the "is a" relationship is really true.

## Data classes (a shortcut)

For classes that mostly just hold data, `dataclass` writes `__init__`, `__repr__` and `==` for you:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

p = Point(3, 4)
print(p)                     # Point(x=3, y=4)
print(p == Point(3, 4))      # True
```

## When should I write a class?

- You have data and several functions that always travel together.
- You need many independent copies, each with their own state (many accounts, many tasks).
- Plain functions and dictionaries are still great for lots of jobs. Don't reach for a class unless it makes the code clearer.

## Common mistakes

| Mistake | Result |
|---------|--------|
| Forgetting `self` as the first parameter | `TypeError: … takes 1 positional argument but 2 were given` |
| Writing `name = name` instead of `self.name = name` | The value is thrown away when `__init__` ends |
| Using `age` instead of `self.age` inside a method | `NameError`: the attribute lives on `self` |
| Forgetting the brackets: `rex.bark` | You get the method itself, not its result |
| A list as a class-level attribute (`items = []` in the class body) | Shared by every instance. Create it in `__init__` instead |

## Try it yourself

1. Run [examples.py](examples.py) and read the classes next to the output.
2. Add a `Dog.rename(new_name)` method and a `__str__` of your own.
3. Do the exercises in [exercises.py](exercises.py).

```bash
pytest tests/test_13_classes.py
```

## Quick check

1. What is `self`?
2. When does Python run `__init__`?
3. If `Dog` inherits from `Animal` and doesn't define `describe`, what happens on `Dog("Rex").describe()`?

<details>
<summary>Answers</summary>

1. The instance the method is being called on. Python passes it automatically as the first argument.
2. Every time you create an instance, e.g. `Dog("Rex", 3)`.
3. It uses `Animal.describe`, because `Dog` inherits it.

</details>

**Previous:** [Lesson 12](../12_errors_and_exceptions/README.md) · **Next:** [Lesson 14: Mini Project](../14_mini_project/README.md)
