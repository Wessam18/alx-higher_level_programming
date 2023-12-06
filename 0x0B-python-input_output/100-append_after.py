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
    index = 0
    with open(filename, "r", encoding="utf-8") as f:
	    read = f.readlines()

		while index < len(read):
			if search_string in read[index]:
				read[index:index + 1] = [read[index], new_string]
				index += 1
			index += 1

	with open(filename, "w", encoding="utf-8") as file:
            file.writelines(read)
