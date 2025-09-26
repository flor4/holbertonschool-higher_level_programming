#!/usr/bin/python3
"""
Defines the BaseGeometry class with integer validation.
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    With size validated as a positive integer.
    """

    def __init__(self, size):
        """
        Initializes a square with given the size of the square.
        """
        self.integer_validator("size", size)  # Validation de 'size'
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size * self.__size
