#!/usr/bin/python3

"""
    This module is to practice classes and objects in Python
    just by creating an empty class
"""


class Square:
    """This is the Square class

    Attributes:
        __size (int): Is a private attribute
        which is a field for the size of the square
    """

    def __init__(self, size):
        """This is a Constructor, it is used to initialize instances/field

        Args:
            size (int): Is the initializing value of the size attribute and
            it is passed upon the instantiation of the object.
        """
        self.__size = size
