#!/usr/bin/python3

"""
    A function that print text.
Args:
        text: the text will be print

Raises:
        TypeError: If text is not a string.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.
    """
    if type(text) is not str:
            raise TypeError("text must be a string")
    after_new_line = False
    for c in text:
        if after_new_line:
            if c == " ":
                continue
            after_new_line = False
        if c == '.' or c == '?' or c == ':':
            print(c)
            #print("")
            after_new_line = True
        else:
            print(c, end="")
