#!/usr/bin/python3
"""_summary_."""
import sys

save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


args = list(sys.argv[1:])
list = []
try:
    list = load_from_json("add_item.json")
except Exception:
    list.extend(args)
    save_to_json(list, "add_item.json")
