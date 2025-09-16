#!/usr/bin/python3
"""Defines a Square class with a private size attribute"""


class Square:
    """A square with a private size representation"""

    def __init__(self, size=0):
        """Initialize a new Square with a
        private size attribute"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
