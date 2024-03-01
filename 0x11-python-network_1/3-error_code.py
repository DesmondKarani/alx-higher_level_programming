#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in utf-8)."""


import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Use a `with` statement to open the URL and fetch the response
        with urllib.request.urlopen(url) as response:
            # Read the response body and decode it
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Print the error code if an HTTPError exception is caught
        print("Error code:", e.code)
