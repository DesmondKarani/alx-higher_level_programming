#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    # Use a `with` statement to open the URL and fetch the response
    with urllib.request.urlopen(url) as response:
        # Read the response body
        body = response.read()
        print("Body response:")
        # Print the type of the body
        print("\t- type:", type(body))
        # Print the content of the body
        print("\t- content:", body)
        # Print the UTF-8 decoded content of the body
        print("\t- utf8 content:", body.decode('utf-8'))
