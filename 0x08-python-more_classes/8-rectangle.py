#!/usr/bin/python3
"""class Rectangle."""


class Rectangle:
    """Represents a rectangle with various properties and methods."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the rectangle's width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the rectangle's height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the rectangle's area."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the rectangle's perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a visual string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(self.print_symbol * self.width for _ in range(self.height))

    def __repr__(self):
        """Returns a string representation for recreating the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when a rectangle instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the one with a larger area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
