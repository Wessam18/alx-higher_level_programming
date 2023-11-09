#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = (sorted(a_dictionary.values()))
    for k in a_dictionary:
        if a_dictionary[k] == max[-1]:
            return k
