#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if a_dictionary is a valid dictionary
    if not isinstance(a_dictionary, dict):
        return None
    # Create a variable to store the best score
    best_score = None
    # Create a variable to store the best key
    best_key = None
    # Iterate over the items of the dictionary
    for key, value in a_dictionary.items():
        # Check if value is an integer
        if isinstance(value, int):
            # Check if value is greater than the current best score
            if best_score is None or value > best_score:
                # Update the best score and the best key
                best_score = value
                best_key = key
        else:
            # Return None if value is not an integer
            return None
    # Return the best key
    return best_key
