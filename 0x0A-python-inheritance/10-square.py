#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using Rectangle."""
    def __init__(self, size):
        """Initialize a new square."""
        super().__init__(self.__size, self.__size)
        self.__size = size
