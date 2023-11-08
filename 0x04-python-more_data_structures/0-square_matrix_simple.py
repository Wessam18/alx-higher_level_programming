#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for col in matrix:
            res = map(lambda sub: list(map(lambda i: i ** 2, sub)), matrix)
    print(list(res))
