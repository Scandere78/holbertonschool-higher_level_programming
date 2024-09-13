#!/usr/bin/python3
"""
This function that prints a square with the character #
"""


def print_square(size):

    """
    Return: print # with number size
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 or (isinstance(size, float) and size < 0):
        raise ValueError("size must be >= 0")

    for index in range(size):
        print("#" * size)
