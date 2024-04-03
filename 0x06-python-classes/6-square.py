#!/usr/bin/python3
"""
Module: 6-square
Defines a class Square with private instance attributes size and position, size and position validation,
getter and setter methods for size and position, a public instance method to calculate the area,
and a public instance method to print the square with respect to position.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square (default 0).
            position (tuple): The position of the square (default (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or position does not contain 2 positive integers.

        Returns:
            None.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to update the size of the square.

        Parameters:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Returns:
            None.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to update the position of the square.

        Parameters:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value does not contain 2 positive integers.

        Returns:
            None.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.

        Returns:
            None.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
