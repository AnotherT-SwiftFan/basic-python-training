"""Lesson 10 solutions - try the exercises yourself before reading this!"""

import math
import random
from collections import Counter
from datetime import date


def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def round_up(x):
    return math.ceil(x)


def days_between(date_a, date_b):
    difference = date.fromisoformat(date_a) - date.fromisoformat(date_b)
    return abs(difference.days)


def weekday_name(iso_date):
    return date.fromisoformat(iso_date).strftime("%A")


def roll_dice(sides, rolls):
    results = []
    for _ in range(rolls):
        results.append(random.randint(1, sides))
    return results


def most_common_word(text):
    counts = Counter(text.lower().split())
    return counts.most_common(1)[0][0]
