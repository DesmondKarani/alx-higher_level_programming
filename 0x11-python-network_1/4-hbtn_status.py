#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""


import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    # Send a GET request to the URL
    response = requests.get(url)
    # Extract the content of the response
    content = response.text
    # `text` attribute will give you the content as a str

    print("Body response:")
    # Print the type of the content
    print("\t- type:", type(content))
    # Print the content itself
    print("\t- content:", content)
