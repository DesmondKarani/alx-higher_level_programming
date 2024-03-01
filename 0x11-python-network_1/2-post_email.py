#!/usr/bin/python3
""""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Data to be sent in the POST request
    values = {'email': email}

    # Encode the data to be sent
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # Data should be bytes

    # Create a request object
    req = urllib.request.Request(url, data)

    # Send the request and receive the response
    with urllib.request.urlopen(req) as response:
        # Read the response body and decode it
        body = response.read().decode('utf-8')
        print(body)
