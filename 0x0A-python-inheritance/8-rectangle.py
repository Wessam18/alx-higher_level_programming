#!/usr/bin/python3
"""
    write a class inherit from basegeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry class"""
    def __init__(self, width, height):
        """ """
        super().integer_validator(width, height)
        self.__width = width
        self.__height = height
