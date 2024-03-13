#!/usr/bin/python3
start = 0
end = 0
for start in range(0, 9):
    for end in range(start + 1, 10):
        if start == 8 and end == 9:
            print("{}{}".format(start, end))
            break
        print("{}{}".format(start, end), end=", ")
