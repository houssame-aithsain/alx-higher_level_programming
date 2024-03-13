#!/usr/bin/python3
start = 0
for start in range(0, 100):
    if start == 99:
        print("{:02d}".format(start))
        break
    print("{:02d}".format(start), end=", ")
