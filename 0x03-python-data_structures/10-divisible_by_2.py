#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        new = []
        for i in my_list:
            if i % 2 == 0:
                my_list.append(True)
            else:
                my_list.append(False)
        return new
