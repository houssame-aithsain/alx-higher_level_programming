#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lent = len(sys.argv) - 1
    print("{} ".format(lent), end='')
    if lent == 0 or lent > 1:
        print("arguments", end='')
        if lent == 0:
            print(".")
        else:
            print(":")
    else:
        print("argument:")
    for i in range(1, lent + 1):
        print("{}: {}".format(i, sys.argv[i]))
