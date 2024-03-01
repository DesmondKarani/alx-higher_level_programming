#!/usr/bin/python3
""" a Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


import requests
import sys

if __name__ == "__main__":
    # Check if a letter was provided as an argument; otherwise,
    # set q to an empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Prepare the data dictionary with the letter
    data = {'q': q}

    try:
        # Send the POST request with the data
        response = requests.post('http://0.0.0.0:5000/search_user', data=data)
        # Attempt to parse the JSON response
        json_response = response.json()

        # Check if the response contains data
        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        # Handle the exception if the response is not a valid JSON
        print("Not a valid JSON")
