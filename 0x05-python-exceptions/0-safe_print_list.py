#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # Initialize a counter for the number of printed elements
    count = 0
    # Use a try-except block to handle possible IndexError
    try:
        # Loop through the list from index 0 to x - 1
        for i in range(x):
            # Print the element at index i
            print(my_list[i], end="")
            # Increment the counter
            count += 1
        # Print a new line after the loop
        print()
    except IndexError:
        # If an IndexError occurs, print a new line
        print()
    # Return the number of printed elements
    return count

# Test the function with different values of x
my_list = [1, 2, 3, 4, 5]
x = 3
print("Output for x =", x)
safe_print_list(my_list, x)
x = 5
print("Output for x =", x)
safe_print_list(my_list, x)
x = 7
print("Output for x =", x)
safe_print_list(my_list, x)
