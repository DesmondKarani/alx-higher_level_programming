#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
# It only displays the body of a 200 status code response
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
# The -f option fails silently on server errors
# The -i option includes the HTTP headers in the output
# The output is piped to awk, which prints only the lines after the first empty line
curl -s -L -f -i "$url" | awk 'BEGIN {skip=1} /^$/ {skip=0; next} skip {next} {print}'
