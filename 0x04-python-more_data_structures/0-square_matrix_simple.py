#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        sub = list(map(lambda i: i ** 2, row))
        new_list.append(sub)
    return new_list
