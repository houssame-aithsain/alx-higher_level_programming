#!/usr/bin/python3
"""Insert a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text"""
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        cd = []
        for line in range(len(lines)):
            cd.append(lines[line])
            if search_string in lines[line]:
                cd.append(new_string)
        file.truncate()
