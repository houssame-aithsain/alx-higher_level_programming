#!/usr/bin/python3
"""Defines a function that prints a square."""


def print_square(size):
    """Print a square of a given size."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
