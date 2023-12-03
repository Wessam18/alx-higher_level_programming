#!/usr/bin/python3
"""
    A function that print squre.
Args:
        size: the size length of the square

Raises:
        TypeError: if size is a float and is less than 0
                size must be an integer,
        ValueError: if size is less than 0
"""


def print_square(size):
    """
    Prints a square of a specified size using the character '#'.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        print(int(size) * "#")
