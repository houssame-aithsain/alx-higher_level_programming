#!/usr/bin/python3
"""Defines a function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Print a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    print("\n".join([line.strip() for line in text.split("\n")]), end="")
