#!/usr/bin/python3
"""
    write a class inherit from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """ """
        super().integer_validator("size", size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """function to determine the area"""
        return self.__size * self.__size

    def __str__(self):
        """printable string """
        return f"[Square] {self.__size}/{self.__size}"
