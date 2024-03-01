#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL
and displays the value of the variable X-Request-Id in the response header"""


import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    # Send a GET request to the URL
    response = requests.get(url)
    print("Body response:")
    # Print the type of the response text
    print("\t- type:", type(response.text))
    # Print the content of the response
    print("\t- content:", response.text)
