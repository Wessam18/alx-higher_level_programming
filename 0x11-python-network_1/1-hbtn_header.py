#!/usr/bin/python3
"""import modules"""

from urllib import request
import sys

if __name__ == "__main__":
    """ """
    with request.urlopen(sys.argv[1]) as response:
        x = response.headers.get('X-Request-Id')
        print(x)
