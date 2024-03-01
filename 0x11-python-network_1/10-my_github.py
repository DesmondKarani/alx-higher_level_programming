#!/usr/bin/python3
"""a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""


import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # Set the URL for the GitHub API endpoint for user details
    url = 'https://api.github.com/user'

    # Make a request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=(username, token))

    # Try to retrieve the user ID from the JSON response
    try:
        print(response.json().get('id'))
    except ValueError:
        print("None")
