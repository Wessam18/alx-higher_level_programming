#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """instance constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """return the printable representation of the object"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str

        for i in range(self.__height):
            str += ("#" * self.__width) + "\n"
        return str.rstrip()

    def __repr__(self):
        """return the string representation of the object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
