#!/usr/bin/python3
"""
    write a class inherit from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """ """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """function to determine the area"""
        return self.__size * self.__size

    def __str__(self):
        """ """
        return "[Square] {}/{}".format(
                self.__size, self.__size)
