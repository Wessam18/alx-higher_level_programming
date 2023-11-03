#!/usr/bin/python3
if __name__ == "__main__":
    import sys

args = len(sys.argv) - 1

if args == 0:
    print("0 arguments.")
elif args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(args))


for y in range(1, args + 1):
    print("{}: {}".format(y, sys.argv[y]))
