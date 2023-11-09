#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = a_dictionary.copy()
    for key, value in x.items():
        x[key] = value * 2
    return x
