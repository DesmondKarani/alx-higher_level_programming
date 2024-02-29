#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument and displays the body of the response
# The script uses curl

# Check if the URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Store the URL in a variable
url=$1

# Use curl to send a DELETE request to the URL and display the body of the response
# The -s option suppresses the progress meter
# The -L option follows redirects
# The -X option specifies the request method
curl -s -L -X DELETE "$url"
