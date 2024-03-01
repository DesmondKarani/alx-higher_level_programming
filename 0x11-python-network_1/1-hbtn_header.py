#!/usr/bin/python3
""" a Python script that takes in a URL,
sends a request to the URL and displays the value of the X-Request-Id variable
found in the header of the response."""


import urllib.request
import sys

if __name__ == "__main__":
    # Take the URL from the first command-line argument
    url = sys.argv[1]

    # Use a `with` statement to open the URL and fetch the response
    with urllib.request.urlopen(url) as response:
        # The `info()` method of the response object returns the headers
        headers = response.info()
        # Print the value of the 'X-Request-Id' header
        print(headers.get('X-Request-Id'))
