#!/usr/bin/python3
"""Defines a function that finds the max integer in a list of integers."""


def max_integer(list=[]):
    """Find the max integer in a list of integers."""
    if not list:
        return None
    max = list[0]
    for item in list:
        if item > max:
            max = item
    return max
