#!/usr/bin/python3
"""
    write an empty class
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """function to determine the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
