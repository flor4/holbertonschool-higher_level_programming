#!/usr/bin/python3
"""Class that defines a Rectangle"""


class Rectangle:
    """Represents a Rectangle with private width and height attributes"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle, validating width and height."""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):

        """that returns the rectangle area"""

        return self.width * self.height

    def perimeter(self):

        """that returns the rectangle perimeter:
        if width or height is equal to 0, perimeter is equal to 0"""

        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):

        """should print the rectangle with the character #,
        if width or height is equal to 0, return an empty string """

        if self.width == 0 or self.height == 0:
            return ""

        rows = ["#" * self.__width for _ in range(self.__height)]

        return "\n".join(rows)

    def __repr__(self):
        """Returns a string representation of the rectangle
         to be able to recreate a new instance"""

        return f"Rectangle({self.width}, {self.height})"
