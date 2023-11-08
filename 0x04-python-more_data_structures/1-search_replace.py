#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Check if my_list is a valid list
    if not isinstance(my_list, list):
        return None
    # Create a new list with the same size as the input list
    new_list = []
    for element in my_list:
        # Check if element is equal to the search value
        if element == search:
            # Replace the element with the replace value
            # and append it to the new list
            new_list.append(replace)
        else:
            # Keep the element as it is and append it to the new list
            new_list.append(element)
    # Return the new list
    return new_list
