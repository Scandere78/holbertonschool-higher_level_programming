#!/usr/bin/python3
"""
This function adds two numbers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    - a must be an integer or a float.
    - b must be an integer or a float (default value is b = 98).
    - If a or b is a float, it will be cast to an integer.
    - Raises a TypeError if a or b is neither an integer nor a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
