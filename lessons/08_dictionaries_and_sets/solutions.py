"""Lesson 8 solutions - try the exercises yourself before reading this!"""


def get_phone(contacts, name):
    return contacts.get(name, "unknown")


def count_words(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def invert(d):
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted


def unique_letters(text):
    letters = set()
    for character in text.lower():
        if character.isalpha():
            letters.add(character)
    return len(letters)


def common_items(a, b):
    return sorted(set(a) & set(b))


def cart_total(prices, cart):
    total = 0
    for item, quantity in cart.items():
        total += prices[item] * quantity
    return total


def group_by_first_letter(words):
    groups = {}
    for word in words:
        first = word[0]
        if first not in groups:
            groups[first] = []
        groups[first].append(word)
    return groups
