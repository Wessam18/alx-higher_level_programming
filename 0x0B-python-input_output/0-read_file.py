#!/usr/bin/python3
"""write a function to read text file and prints it to stdout."""


def read_file(filename=""):
    """function to read text file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
