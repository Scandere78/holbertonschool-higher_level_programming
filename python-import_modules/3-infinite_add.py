#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arguments = argv[1:]
    somme = 0
    for arg in arguments:
        somme += int(arg)
    print(somme)

