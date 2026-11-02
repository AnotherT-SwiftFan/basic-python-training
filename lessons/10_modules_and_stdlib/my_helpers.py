"""A tiny module of our own. examples.py imports it.

Try running THIS file directly (the play button) and compare with what you
see when examples.py imports it.
"""

GREETING = "Hello from my_helpers!"


def double(n):
    return n * 2


def shout(text):
    return text.upper() + "!"


def main():
    print("my_helpers was run directly")
    print("double(21) =", double(21))
    print(shout("it works"))


# This block only runs when the file is run directly, NOT when it is imported.
if __name__ == "__main__":
    main()
