#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]  # No need to use sys.argv, just argv
    num_args = len(args)

    if num_args == 0:
        print("Number of argument(s): 0.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")
