#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        while count < x:
            print("{:d:".format(my_list[count]), end="")
            count += 1
    except (IndexError, ValueError, TypeError):
        pass
    finally:
        print()
        return count
