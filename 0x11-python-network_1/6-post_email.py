#!/usr/bin/python3
"""a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to send in the POST request
    payload = {'email': email}

    # Send the POST request with the data
    response = requests.post(url, data=payload)

    # Display the body of the response
    print(response.text)
