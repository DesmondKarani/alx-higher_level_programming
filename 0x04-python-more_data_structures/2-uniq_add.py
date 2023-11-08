#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Check if my_list is a valid list
    if not isinstance(my_list, list):
        return None
    # Create a set to store the unique integers
    unique_set = set()
    # Create a variable to store the sum of the unique integers
    sum = 0
    for element in my_list:
        # Check if element is an integer
        if isinstance(element, int):
            # Add the element to the set if it is not already in it
            if element not in unique_set:
                unique_set.add(element)
                # Add the element to the sum
                sum += element
        else:
            # Return None if element is not an integer
            return None
    # Return the sum
    return sum
