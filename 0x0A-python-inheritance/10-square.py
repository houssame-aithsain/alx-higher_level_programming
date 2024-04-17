#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using Rectangle."""
    def __init__(self, size):
        """Initialize a new square."""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the printable representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
