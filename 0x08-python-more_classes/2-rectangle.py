#!/usr/bin/python3

"""This module defines Rectangle"""


class Rectangle:
    """This is a Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        This method initializez the instance of Rectangle class

        Args:
            width (int): takes the width of the instance upon init
            height (int): takes the height of the instance upon init
        Raises:
            TypeError: if value entered isn't integer
            ValueError: if value entered is less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise TypeError("width must be >=0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("height must be >=0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        This method acts as the getter method

        Return: the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method sets the value of width

        Args:
            value (int): this value is assigned to the width

        Raises:
            TypeError: if value entered is not of type int
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """
        This method acts as the getter method

        Return: the value of heigth
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method sets the value of heigth

        Args:
            value (int): this value is assigned to the heigth

        Raises:
            TypeError: if value entered is not of type int
            ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >=0")
        self.__height = value

    def area(self):
        """
        This method checks for the area of the Rectangle

        Return: the area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        This method returns the perimeter of the Rectangle

        Return:
            if width or height = 0, return 0 and if otherwise, perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
