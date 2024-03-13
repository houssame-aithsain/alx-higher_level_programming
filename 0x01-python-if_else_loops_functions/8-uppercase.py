#!/usr/bin/python3
def uppercase(str):
    for c in range(str):
        if ord(c) >= 97 and ord(c) <= 122:
            print("{}".format(c))
        else:
            print("{}".format(chr(ord(c) - 32)))
