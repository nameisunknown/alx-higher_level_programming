#!/usr/bin/python3

"""This module helps us prevents the user from dynamically creating
    new instance attributes, except if the new instance attribute
    is already defined
"""


class LockedClass:
    """This is a class name LockedClass, with only 1 attribute
        and you can't add an extra attribute to it, due to the
        presence of the __slots__ magic method, and defining what the
        attributes the class will carry in it.
        Hence, it prevents the user from dynamically creating new instance
        attributes except the ones already defined, which is first_name
    """
    __slots__ = ["first_name"]
