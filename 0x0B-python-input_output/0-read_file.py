#!/usr/bin/python3
"test"


def read_file(filename=""):
    "test2"
    with open(filename, encoding='utf-8') as file:
        data = file.read()
        print(data, end='')
