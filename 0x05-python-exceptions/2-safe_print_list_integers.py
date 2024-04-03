#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # This handles the case when the current element is not an integer
            continue
        except IndexError:
            # This handles the case when the index is out of range
            # It breaks the loop as we've gone beyond the list's bounds
            break
    print()  # Ensure we move to a new line after printing all integers
    return count
