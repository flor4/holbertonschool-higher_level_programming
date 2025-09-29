#!/usr/bin/python3

"""
Read a txt file
"""


def read_file(filename=""):
    """
    read_file - Read a txt file
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
