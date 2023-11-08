#!/usr/bin/python3
def number_keys(a_dictionary):
    # Check if a_dictionary is a valid dictionary
    if not isinstance(a_dictionary, dict):
        return None
    # Create a variable to store the number of keys
    count = 0
    # Iterate over the keys of the dictionary
    for key in a_dictionary:
        # Increment the count by one for each key
        count += 1
    # Return the count
    return count
