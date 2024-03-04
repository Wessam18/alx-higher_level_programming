#!/usr/bin/python3
"""import modules"""

import requests
import sys

if __name__ == "__main__":
    """ """
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        x = response.text
        print(x)

    
