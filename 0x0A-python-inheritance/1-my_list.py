#!/usr/bin/python3
"""Defines a subclass of list."""


class MyList(list):
    """A subclass of list."""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list, but sorted."""
        print(sorted(self))
