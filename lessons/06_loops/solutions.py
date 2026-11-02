"""Lesson 6 solutions - try the exercises yourself before reading this!"""


def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


def countdown(n):
    text = ""
    for i in range(n, 0, -1):
        text += f"{i} "
    return text + "Liftoff!"


def star_triangle(rows):
    lines = ""
    for i in range(1, rows + 1):
        lines += "*" * i
        if i < rows:
            lines += "\n"
    return lines


def smallest_power_of_two_above(limit):
    power = 1
    while power <= limit:
        power *= 2
    return power


def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
