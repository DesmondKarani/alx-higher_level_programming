#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL, and displays the body of the response
# A variable email must be sent with the value test@gmail.com
# A variable subject must be sent with the value I will always be here for PLD
# The script uses curl

# Check if the URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Store the URL in a variable
url=$1

# Use curl to send a POST request to the URL and display the body of the response
# The -s option suppresses the progress meter
# The -L option follows redirects
# The -d option sends data in the request body
curl -s -L -d "email=test@gmail.com&subject=I will always be here for PLD" "$url"
