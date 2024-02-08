#!/usr/bin/python3

"""This is a class that focuses on Rectangle and the str method"""


class Rectangle:
    """
    This class defines a ractangnd focuses on string representation
    """

    def __init__(self, width=0, height=0):
        """
        This initializes the class when an instance is created

        Args:
            width (int): value for width of Rectangle
            height (int): value for height of Rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        This acts as a getter for the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This sets the value for the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        This acts a getter for the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This sets the value for height

        Args:
            value (int): arg passed to change the value of height
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if self.__height < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        """
        This returns  the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        This method represents the str function which is used in print()
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        ash_print = []
        for counter in range(self.__height):
            ash_print.append("#" * self.__width)
            if counter < self.__height - 1:
                ash_print.append("\n")

        return "".join(ash_print)
