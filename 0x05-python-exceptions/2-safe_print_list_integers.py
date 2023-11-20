#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        while count < x:
            value = my_list[count]
            print("{:d}".format(value), end="")
            count += 1
    except (ValueError, TypeError, IndexError):
        print("Error: list index out of range")
    finally:
        print()
        return count
