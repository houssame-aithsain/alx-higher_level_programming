#!/usr/bin/python3
"""
Module: 1-square
Defines a class Square with a private instance attribute size.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square.

        Returns:
            None.
        """
        self.__size = size
