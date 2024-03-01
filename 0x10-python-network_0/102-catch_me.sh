#!/bin/bash

# Make a POST request with a specific header to the target URL
curl -s -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" "0.0.0.0:5000/catch_me"
