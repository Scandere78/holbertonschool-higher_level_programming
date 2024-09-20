#!/usr/bin/python3
"""
Shebang to specify the Python 3 interpreter.
"""


class BaseGeometry:
    """
    A class BaseGeometry with a public instance method 'area' and
    'integer_validator' to validate values.
    """
    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer and greater than 0.
        Raises TypeError if 'value' is not an integer.
        Raises ValueError if 'value' is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
