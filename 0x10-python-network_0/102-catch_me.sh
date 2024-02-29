#!/bin/bash
# This script makes a request to a specific URL that triggers a special server response
curl -sX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98" -L
