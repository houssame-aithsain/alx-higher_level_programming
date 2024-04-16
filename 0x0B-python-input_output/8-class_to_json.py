#!/usr/bin/python3
"""Return the dictionary description with simple data structure for JSON"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure for JSON"""
    return obj.__dict__
