#!/usr/bin/python3
"""Module: 5-square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance."""
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to update the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#' to stdout."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
