#!/usr/bin/python3

"""This module is aimed at practicing testing
   This module contains add_integer function
"""

def add_integer(a, b=98):
    """This function adds 2 integer values (a, b) even when it takes a float

    Args:
        a (int or float): this is the first arg to be added
        b (int or float): this is the second arg to be added, with a default val of 98

    Return:
        The result of the addition of both arg of int type
    Raises:
        TypeError: if the arg entered are not int or float
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = float(b)

    return a + b
