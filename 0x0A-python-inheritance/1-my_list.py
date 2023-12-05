#!/usr/bin/python3
""" 
    Write a class MyList that inherits from list
Args:
        list: the parent class to inhert from
"""


class MyList(list):
    """child class """
    def print_sorted(self):
        """function to sort list"""
        print(sorted(self))
