#!/usr/bin/python3
"""
write a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a text file
    and returns the number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

    return len(text)
