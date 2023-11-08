#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Check if a_dictionary is a valid dictionary and key is a valid string
    if not isinstance(a_dictionary, dict) or not isinstance(key, str):
        return None
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Delete the key and the corresponding value from the dictionary
        del a_dictionary[key]
    # Return the updated dictionary
    return a_dictionary
