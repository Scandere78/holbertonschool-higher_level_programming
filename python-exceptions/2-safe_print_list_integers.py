#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    index2 = 0
    for index1 in range(x):
        try:
            print("{:d}".format(my_list[index1]), end="")
            index2 += 1
        except (ValueError, TypeError):
            continue
    print()
    return index2
