#!/usr/bin/python3
import sys

# Get the number of command-line arguments
num_args = len(sys.argv) - 1

# Determine the pluralization of "argument(s)"
arg_plural = "arguments" if num_args != 1 else "argument"

# Print the number of argument(s)
print("Number of {}{}:".format(num_args, " " + arg_plural))

# Iterate over the arguments and print them with their position
for i, arg in enumerate(sys.argv[1:], 1):
    print("{}: {}".format(i, arg))
