#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Check if set_1 and set_2 are valid sets
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        return None
    # Create a new set to store the common elements
    common_set = set()
    # Iterate over the elements of set_1
    for element in set_1:
        # Check if element is in set_2
        if element in set_2:
            # Add the element to the common set
            common_set.add(element)
    # Return the common set
    return common_set
