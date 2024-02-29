#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
# The size is displayed in bytes
# The script uses curl

# Check if the URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Store the URL in a variable
url=$1

# Use curl to send a request to the URL and get the size of the body
# The -s option suppresses the progress meter
# The -w option writes the output to a format string
# The %{size_download} variable contains the size of the downloaded content in bytes
# The -o option redirects the output to /dev/null
size=$(curl -s -w "%{size_download}" -o /dev/null "$url")

# Display the size
echo "$size"
