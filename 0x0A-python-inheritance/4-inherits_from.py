#!/usr/bin/python3
"""Defines a function that returns True if the object is an instance"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited from a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
