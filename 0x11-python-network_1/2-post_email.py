#!/usr/bin/python3
"""import modules"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    """ """
    url = sys.argv[1]
    email = sys.argv[2]

    query = parse.urlencode({'email' : email})
    query = query.encode('utf-8')

    with request.urlopen(url, query) as response:
        x = response.read().decode('utf-8')
        print(x)
