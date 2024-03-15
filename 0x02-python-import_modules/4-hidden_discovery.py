#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for st in names:
        if st[:2] != "__":
            print(st)
