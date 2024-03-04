#!/usr/bin/python3
"""import modules"""

import requests
import sys

if __name__ == "__main__":
    """ """
    url = sys.argv[1]
    email = sys.argv[2]

    query = {'email': email}

    response = requests.post(url, data=query)
    x = response.text()
    print(x)
