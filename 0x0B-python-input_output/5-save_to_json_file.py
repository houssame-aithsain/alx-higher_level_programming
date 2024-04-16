#!/usr/bin/python3
"""Save an object to a file in JSON format."""


import json


def save_to_json_file(my_obj, filename):
    """Save an object to a file in JSON format."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
