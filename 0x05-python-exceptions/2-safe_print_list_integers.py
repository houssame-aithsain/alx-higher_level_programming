#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            int_count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return int_count
