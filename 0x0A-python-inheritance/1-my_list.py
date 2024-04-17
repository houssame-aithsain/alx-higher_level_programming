#!/usr/bin/python3
"""Defines a subclass of list."""


class MyList(list):
    """A subclass of list."""

    def print_sorted(self):
        """Prints the list sorted."""
        print(sorted(self))
