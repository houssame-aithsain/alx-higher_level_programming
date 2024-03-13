#!/usr/bin/python3
start = ord('a')
end = ord('z')
for start in range(start, end + 1):
    if (chr(start) != 'q' and chr(start) != 'e'):
        print("{}".format(chr(start)), end="")
