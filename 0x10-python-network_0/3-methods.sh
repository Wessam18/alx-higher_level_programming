#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -sX OPTIONS -I "$1" | grep -i "Allow:" | cut -d ' ' -f 2-
