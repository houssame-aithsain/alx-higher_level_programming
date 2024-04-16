#!/usr/bin/python3
"""Write content to a file or create it if it doesn't exist."""

def write_file(filename="", text=""):
    """Write content to a file or create it if it doesn't exist."""
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)
