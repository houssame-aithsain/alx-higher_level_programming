#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    resulte = ()
    for i in (tuple_a, tuple_b):
        if not len(i):
            i = (0, 0)
        elif len(i) == 1:
            i = (i[0], 0)
        if resulte == ():
            resulte = i
    return i[0] + resulte[0], i[1] + resulte[1]
