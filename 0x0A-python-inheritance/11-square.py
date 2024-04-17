#!/usr/bin/python3
"""Module for Square class."""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A subclass representing a square."""
    def __init__(self, size):
        """Initializes a new Square object."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns the printable representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
