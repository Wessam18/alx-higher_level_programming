#!/usr/bin/python3
import sys

args = len(sys.argv) - 1

if args == 0:
    print("0 arguments.")
elif args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(args))

for i, s in enumerate(sys.argv[1:], 1):
    print("{}: {}".format(i, s))
