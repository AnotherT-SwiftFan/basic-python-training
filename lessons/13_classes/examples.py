"""Lesson 13 - Classes

Run this file and read each class next to the output it produces.
"""

from dataclasses import dataclass


# --- A first class ------------------------------------------------------------
class Dog:
    def __init__(self, name, age):       # runs automatically when you create a Dog
        self.name = name                 # attributes live on `self`
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1

    def __str__(self):                   # controls what print() shows
        return f"{self.name} ({self.age})"


rex = Dog("Rex", 3)
fido = Dog("Fido", 5)

print(rex.name, rex.age)
print(rex.bark())
rex.birthday()
print(rex, "and", fido)                  # each instance keeps its OWN data
print(rex.age, fido.age)


# --- A class that protects its own rules --------------------------------------
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

    def __str__(self):
        return f"{self.owner}: ${self.balance:,.2f}"


account = BankAccount("Ada", 100)
account.deposit(50)
account.withdraw(30)
print(account)

try:
    account.withdraw(1000)
except ValueError as error:
    print("Refused:", error)


# --- Inheritance and polymorphism ---------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.speak()}"      # calls the right speak()


class Cow(Animal):                       # Cow IS an Animal
    def speak(self):                     # override just the part that differs
        return "Moo!"


class Duck(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name)           # let Animal set up `name` first
        self.can_fly = can_fly

    def speak(self):
        return "Quack!"


for animal in [Animal("Thing"), Cow("Daisy"), Duck("Donald")]:
    print(animal.describe())

print(isinstance(Cow("Daisy"), Animal))   # True: a Cow is an Animal
print(isinstance(Animal("Thing"), Cow))   # False


# --- Two instances really are independent -------------------------------------
class Counter:
    def __init__(self):
        self.count = 0

    def click(self):
        self.count += 1


first, second = Counter(), Counter()
first.click()
first.click()
second.click()
print(first.count, second.count)          # 2 1


# --- A data class: the shortcut for classes that mostly hold data -------------
@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


p = Point(3, 4)
print(p)                                  # Point(x=3, y=4)
print(p == Point(3, 4))                   # True
print(p.distance_from_origin())           # 5.0
