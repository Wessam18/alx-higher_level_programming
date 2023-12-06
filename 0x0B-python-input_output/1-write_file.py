#!/usr/bin/python3
"""write a function to write text file and 
    returns the number of characters written"""


def write_file(filename="", text=""):
    """function to write text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.read(text)
