#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        while count < x:
            value = my_list[count]
            if not isinstance(value, int):
                raise ValueError("Element is not an integer")
            
            print("{:d}".format(value), end="")
            count += 1
    except (ValueError, IndexError):
        pass
    finally:
        print()
        return count
