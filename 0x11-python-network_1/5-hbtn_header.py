#!/usr/bin/python3
"""import modules"""

import requests
import sys

if __name__ == "__main__":
    """ """
    response =  requests.get(sys.argv[1])
    x = response.headers['X-Request-Id']
    print(x)
