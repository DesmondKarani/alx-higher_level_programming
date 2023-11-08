#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Check if set_1 and set_2 are valid sets
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        return None
    # Create a new set to store the only different elements
    diff_set = set()
    # Iterate over the elements of set_1
    for element in set_1:
        # Check if element is not in set_2
        if element not in set_2:
            # Add the element to the diff set
            diff_set.add(element)
    # Iterate over the elements of set_2
    for element in set_2:
        # Check if element is not in set_1
        if element not in set_1:
            # Add the element to the diff set
            diff_set.add(element)
    # Return the diff set
    return diff_set
