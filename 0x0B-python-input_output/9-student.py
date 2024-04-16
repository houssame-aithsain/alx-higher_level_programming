#!/usr/bin/python3
"""Create a class Student that defines a student."""


class Student:
    """Create a class Student that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary description of a Student."""
        return self.__dict__.copy()
