#!/usr/bin/python3
"""write a function to append text file and 
    returns the number of characters added"""


def append_write(filename="", text=""):
    """function to append text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.read(text)
