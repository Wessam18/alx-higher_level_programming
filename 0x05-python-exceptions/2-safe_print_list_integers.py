def safe_print_list_integers(my_list=[], x=0):
    count = 0
    while count < x:
        try:
            value = my_list[count]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return count
