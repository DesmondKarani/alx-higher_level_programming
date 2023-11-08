#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Check if a_dictionary is a valid dictionary and key is a valid string
    if not isinstance(a_dictionary, dict) or not isinstance(key, str):
        return None
    # Assign the value to the key in the dictionary
    a_dictionary[key] = value
    # Return the updated dictionary
    return a_dictionary
