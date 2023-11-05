#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        a = my_list.copy()
        a.sort()
        return a[-1]
