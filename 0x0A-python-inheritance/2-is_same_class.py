#!/usr/bin/python3
"""isinistance module"""


def is_same_class(obj, a_class):
    """
    function that return True if
    The obj is inistance of a_class
    or false if is not
    """

    return type(obj) is a_class
