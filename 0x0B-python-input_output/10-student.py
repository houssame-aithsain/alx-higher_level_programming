#!/usr/bin/python3
"""Define a Student class."""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of a Student."""
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            res = {}
            for i in attrs:
                if i in self.__dict__:
                    res[i] = self.__dict__[i]
            return res
        return self.__dict__
