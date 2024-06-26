#!/usr/bin/python3
""" Define a square"""


class Square:
    """Square class"""

    def area(self):
        return (self.__size**2)

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
