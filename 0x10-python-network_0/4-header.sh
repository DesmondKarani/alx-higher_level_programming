#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
# A header variable X-School-User-Id must be sent with the value 98
# The script uses curl

# Check if the URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Store the URL in a variable
url=$1

# Use curl to send a GET request to the URL and display the body of the response
# The -s option suppresses the progress meter
# The -L option follows redirects
# The -H option adds a custom header
curl -s -L -H "X-School-User-Id: 98" "$url"
