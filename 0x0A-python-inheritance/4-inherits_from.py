#!/usr/bin/python3
"""
    A function determine the object is
    exactly an instance of the specified class
Args:
        obj: the object to test
        a_class: the parent
Return:
        true or false
"""


def inherits_from(obj, a_class):
    """"
    function determine the object is exactly an instance of the specified class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
