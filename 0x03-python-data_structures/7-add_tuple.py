#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Start with two elements initialized to zero
    sum_1, sum_2 = 0, 0

    # Add the first element of each tuple if it exists
    if len(tuple_a) > 0:
        sum_1 += tuple_a[0]
    if len(tuple_b) > 0:
        sum_1 += tuple_b[0]

    # Add the second element of each tuple if it exists
    if len(tuple_a) > 1:
        sum_2 += tuple_a[1]
    if len(tuple_b) > 1:
        sum_2 += tuple_b[1]

    return (sum_1, sum_2)
