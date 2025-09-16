#!/usr/bin/python3
"""Defines a Square class with a private size attribute"""


class Square:
    """A square with a private size representation"""

    def __init__(self, size=0):

        """Initialize a new Square with
        private size attribute"""

        self.__size = size
