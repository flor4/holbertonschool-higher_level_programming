#!/usr/bin/python3
""" defines the Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height
        as parameter
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
