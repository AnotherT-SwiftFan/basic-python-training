"""Lesson 7 solutions - try the exercises yourself before reading this!"""


def ends(items):
    return [items[0], items[-1]]


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def remove_negatives(numbers):
    kept = []
    for n in numbers:
        if n >= 0:
            kept.append(n)
    return kept


def second_largest(numbers):
    return sorted(numbers)[-2]


def squares(n):
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result


def rotate_left(items):
    return items[1:] + items[:1]


def min_max(numbers):
    return (min(numbers), max(numbers))


def without_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def lengths(words):
    return [len(word) for word in words]
