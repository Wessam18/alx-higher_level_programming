#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1

if num_args == 0:
    print("0 arguments.")
else:
    print("{} {'argument' if num_args == 1 else 'arguments'}:" .format(num_args))
    for i, arg in enumerate(sys.argv[1:], 1):
        print("{}: {}" .format(i, arg))
