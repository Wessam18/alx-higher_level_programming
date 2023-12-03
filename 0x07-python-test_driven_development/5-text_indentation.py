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
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    for char in text:
        result += char
        if char in ['.', '?', ':']:
            result += '\n\n'

    result = result.replace(': ', ':')
    print(result.strip(), end="")
