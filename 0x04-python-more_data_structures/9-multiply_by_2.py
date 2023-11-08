#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Check if a_dictionary is a valid dictionary
    if not isinstance(a_dictionary, dict):
        return None
    # Create a new dictionary to store the multiplied values
    new_dict = {}
    # Iterate over the items of the dictionary
    for key, value in a_dictionary.items():
        # Check if value is an integer
        if isinstance(value, int):
            # Multiply the value by 2 and assign
            # it to the same key in the new dictionary
            new_dict[key] = value * 2
        else:
            # Return None if value is not an integer
            return None
    # Return the new dictionary
    return new_dict
