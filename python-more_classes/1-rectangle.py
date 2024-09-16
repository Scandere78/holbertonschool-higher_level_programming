#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """
    class rectangle with width and height
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle


        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """
        Set width of rectangle

        Args:
            value (int): The width value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """
        Set height of rectangle

        Args:
            value (int): The height value to set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
