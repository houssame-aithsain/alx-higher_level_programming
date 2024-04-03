#!/usr/bin/python3
"""
Module: 3-square
Defines a class Square with private instance attribute size, size validation,
and a public instance method to calculate the area.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
