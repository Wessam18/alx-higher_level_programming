#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for search in my_list:
        my_list.replace(search, replace)
    return my_list
