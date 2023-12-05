#!/usr/bin/python3
""" 
    A function that returns the list of available attributes
    and methods of an object.
Args:
        obj: the object to get it is attributes
Return:
        a list object.
    
"""


def lookup(obj):
    """function that returns the list of available attributes"""
    return list(dir(obj))
