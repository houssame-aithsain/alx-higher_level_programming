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

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
