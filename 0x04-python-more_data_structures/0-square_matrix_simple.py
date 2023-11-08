#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    res = map(lambda sub: list(map(lambda i: i ** 2, sub)), matrix)
    return list(res)
