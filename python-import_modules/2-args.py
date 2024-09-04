#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print("Number of argument(s): 0.")
    elif num_args == 1:
        print(f"1 argument:")
    else:
        print(f"{num_args} arguments:")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")


