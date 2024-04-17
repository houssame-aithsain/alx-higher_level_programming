#!/usr/bin/python3
"""Defines a class BaseGeometry."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle."""
    def __init__(self, width, height):
        """Initializes a new rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the printable representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
