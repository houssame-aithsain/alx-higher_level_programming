#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    resulte = 0
    for i in range(1, len(sys.argv)):
        resulte += int(sys.argv[i])
    print("{}".format(resulte))
