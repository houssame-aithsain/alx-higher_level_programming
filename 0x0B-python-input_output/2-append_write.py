#!/usr/bin/python3
"""Append content to a file or create it if it doesn't exist."""


def append_write(filename="", text=""):
    """Append content to a file or create it if it doesn't exist."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
