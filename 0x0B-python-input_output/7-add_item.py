#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
and then save them to a file"""
from sys import argv
from os import path

save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

# Load existing data from the file if it exists
if path.exists(filename):
    my_list = load_from_json(filename)
else:
    my_list = []

# Add new arguments to the list
my_list.extend(argv[1:])

# Save the updated list to the file
save_to_json(my_list, filename)
