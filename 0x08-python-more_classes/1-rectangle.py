#!/usr/bin/python3

"""This module contains a class Rectangle with the use @property"""


class Rectangle:
    """
    This class is of type Rectangle and contains attributes and properties
    """

    def __init__(self, width=0, height=0):
        """This method initializes the instance of this class

        Args:
            width (int): width of the class Ractangle with default val 0
            height (int): height of the class Rectangle with default val 0

        Raises:
            TypeError: if attributes not int
            ValueError: if arguments are less than 0

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This method is the width attribute getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets the value of width, hence acts as the setter

        Args:
            value (int): argument to be passed to width

        Raises:
            TypeError: if arg entered isn't int
            ValueError: if arg entered is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This method is the heigth attribute getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """This method sets the value of heigth, hence acts as the setter

        Args:
            value (int): argument to be passed to heigth

        Raises:
            TypeError: if arg entered isn't int
            ValueError: if arg entered is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
