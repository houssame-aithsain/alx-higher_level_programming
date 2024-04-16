#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import json


def add_item(args, filename):
    """Add all arguments to a Python list and save them to a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            my_list = json.load(file)
    except FileNotFoundError:
        my_list = []
    my_list.extend(args)
    with open (filename, 'w', encoding='utf-8') as file:
        json.dump(my_list, file)
