#!/usr/bin/python3
def weight_average(my_list=[]):
    # Check if my_list is a valid list
    if not isinstance(my_list, list):
        return 0
    # Create variables to store the sum of the products
    # and the sum of the weights
    sum_products = 0
    sum_weights = 0
    # Iterate over the tuples in the list
    for score, weight in my_list:
        # Check if score and weight are valid integers
        if isinstance(score, int) and isinstance(weight, int):
            # Multiply the score and the weight and add
            # it to the sum of the products
            sum_products += score * weight
            # Add the weight to the sum of the weights
            sum_weights += weight
        else:
            # Return 0 if score or weight is not an integer
            return 0
    # Check if the sum of the weights is not zero
    if sum_weights != 0:
        # Divide the sum of the products by the sum
        # of the weights and return the result
        return sum_products / sum_weights
    else:
        # Return 0 if the sum of the weights is zero
        return 0
