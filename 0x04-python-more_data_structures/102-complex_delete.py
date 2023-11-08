#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Check if a_dictionary is a valid dictionary
    if not isinstance(a_dictionary, dict):
        return None
    # Create a list to store the keys to be deleted
    keys_to_delete = []
    # Iterate over the items of the dictionary
    for key, val in a_dictionary.items():
        # Check if val is equal to the value parameter
        if val == value:
            # Append the key to the list of keys to be deleted
            keys_to_delete.append(key)
    # Iterate over the keys to be deleted
    for key in keys_to_delete:
        # Delete the key and the corresponding value from the dictionary
        del a_dictionary[key]
    # Return the updated dictionary
    return a_dictionary
