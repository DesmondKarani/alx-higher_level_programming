#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept
# The script uses curl

# Check if the URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Store the URL in a variable
url=$1

# Use curl to send an OPTIONS request to the URL and display the Allow header
# The -s option suppresses the progress meter
# The -L option follows redirects
# The -X option specifies the request method
# The -I option shows only the HTTP headers
# The output is piped to grep, which filters only the line that starts with Allow
curl -s -L -X OPTIONS -I "$url" | grep "^Allow"
