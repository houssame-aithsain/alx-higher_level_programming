#!/usr/bin/python3
"""Add command-line arguments to a list and save it to a JSON file."""


import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

items = []
if os.path.exists('add_item.json'):
    items = load_from_json_file('add_item.json')

items.extend(sys.argv[1:])
save_to_json_file(items, 'add_item.json')
