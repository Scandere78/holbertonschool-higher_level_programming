#!/usr/bin/python3
"""
    function to read a text file
"""


def read_file(filename=""):
    """
        Reads a text file (UTF8) and prints it to stdout.
        Arguments:
            filename (str): File to open.
    """
  
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
