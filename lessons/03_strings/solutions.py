"""Lesson 3 solutions - try the exercises yourself before reading this!"""


def shout(text):
    return text.upper() + "!"


def first_and_last(text):
    return text[0] + text[-1]


def clean_name(raw):
    return raw.strip().title()


def reverse_text(text):
    return text[::-1]


def count_letter(text, letter):
    return text.lower().count(letter.lower())


def make_email(first, last):
    return f"{first.lower()}.{last.lower()}@example.com"


def format_price(amount):
    return f"${amount:,.2f}"


def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def initials(full_name):
    words = full_name.split()
    return (words[0][0] + words[-1][0]).upper()
