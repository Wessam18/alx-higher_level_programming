#!/usr/bin/python3
"""
    A function that divides all elements of a matrix.
Args:
        matrix:  (list of lists): The matrix of integers or floats.
        div:  (int or float): The divisor.

Returns:
        new matrix
Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   if each row of the matrix doesn't have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
"""


def matrix_divided(matrix, div):
    """
    Module for matrix division

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not (isinstance(row, list)):
            raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    new = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        new.append(new_row)

    return new
