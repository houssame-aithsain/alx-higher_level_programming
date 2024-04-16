#!/usr/bin/python3
"""Insert a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text"""
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
        file.truncate()
