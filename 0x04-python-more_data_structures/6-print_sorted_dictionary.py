#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Check if a_dictionary is a valid dictionary
    if not isinstance(a_dictionary, dict):
        return None
    # Create a list of the keys of the dictionary
    keys = list(a_dictionary.keys())
    # Sort the keys in alphabetic order
    keys.sort()
    # Iterate over the sorted keys
    for key in keys:
        # Print the key and the corresponding value
        print("{}: {}".format(key, a_dictionary[key]))
