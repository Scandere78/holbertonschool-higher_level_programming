#!/usr/bin/python3
"""
This module provides a function to print the first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    prints the first name and last name.
    first_name and last_name must be strings.
    raise a TypeError if first_name or last_name is not a string.
    print message with first_name and last_name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
