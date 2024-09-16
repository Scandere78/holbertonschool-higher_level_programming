#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """
    Class that defines a rectangle by its width and height.
    Tracks the number of instances of the class.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """
        Set width of rectangle

        Args:
            value (int): The width value to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """
        Set height of rectangle

        Args:
            value (int): The height value to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for _ in range(self.height):
            rect_str += str(self.print_symbol) * self.width + '\n'
        return rect_str[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): First rectangle to compare.
            rect_2 (Rectangle): Second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the larger area.
                      If both have the same area, return rect_1.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Return a new Rectangle instance with width == height == size.

        Args:
            size (int): The size of the square sides.

        Returns:
            Rectangle: A new Rectangle instance with equal width and height.
        """
        return cls(size, size)
