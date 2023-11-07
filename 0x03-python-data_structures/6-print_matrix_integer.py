#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            if len(row) == 0:
                print()
            for i, column in enumerate(row):
                if i == len(row) - 1:
                    print("{:d}".format(column), end="\n")
                else:
                    print("{:d}".format(column), end=" ")
