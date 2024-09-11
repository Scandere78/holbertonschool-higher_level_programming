#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for index in range(x):
            print(my_list[index], end="")
            i += 1
    except IndexError:
        pass
    print()
    return i
