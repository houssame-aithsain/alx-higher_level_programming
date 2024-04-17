#!/usr/bin/python3
"""Defines a function that returns True"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
