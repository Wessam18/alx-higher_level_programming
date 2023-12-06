#!/usr/bin/python3
""" """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to append
        after the lines containing the search string.
    """
    with open(filename, 'r+', encoding="utf-8") as f:
        for line in f:
            if search_string in line:
                f.write(new_string + '\n')
