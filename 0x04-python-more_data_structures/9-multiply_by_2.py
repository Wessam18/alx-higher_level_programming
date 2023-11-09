#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = a_dictionary.copy()
    for key in x:
         x[key] = a_dictionary[key] * 2
    return x
