#!/usr/bin/python3
"""Module: 3-square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
