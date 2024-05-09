#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 argument.")
        print(".")
    else:
        print("{} argument{}:".format(
            len(argv) - 1, 's' if len(argv) > 2 else ''
        ))
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
