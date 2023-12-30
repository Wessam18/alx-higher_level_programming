#!/usr/bin/python3
"""
    write a class inherit from basegeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry class"""
    def __init__(self, width, height):
        """ """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """function to determine the area"""
        return self.__width * self.__height

    def __str__(self):
        """ """
        return f"[Rectangle] {self.__width}/{self.__height}"
