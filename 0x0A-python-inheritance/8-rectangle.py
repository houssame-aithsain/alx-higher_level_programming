#!/usr/bin/python3
"""Defines a class BaseGeometry."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle."""
    def __init__(self, width, height):
        """Initializes a new rectangle."""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns the printable representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height
