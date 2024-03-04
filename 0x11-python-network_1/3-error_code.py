#!/usr/bin/python3
"""import modules"""

from urllib import request, error
import sys

if __name__ == "__main__":
    """ """
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            x = response.read().decode('utf-8')
            print(x)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
