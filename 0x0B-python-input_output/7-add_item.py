#!/usr/bin/python3
"""Add command-line arguments to a list and save it to a JSON file."""


import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_to_list_and_save(arguments):
    """Add command-line arguments to a list and save it to a JSON file."""
    filename = "add_item.json"
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(arguments)

    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_to_list_and_save(arguments)
