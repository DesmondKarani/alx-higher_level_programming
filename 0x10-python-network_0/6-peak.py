#!/usr/bin/python3
""" This module contains the function find_peak """


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    Args:
    list_of_integers: A list of unsorted integers.

    Returns:
    The index of a peak in the list, or None if no peak is found.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] > list_of_integers[mid - 1]) and
        (mid == len(list_of_integers) - 1 or
         list_of_integers[mid] > list_of_integers[mid + 1]):
            return mid

        # Move to the larger half
        if list_of_integers[mid] < list_of_integers[right]:
            left = mid + 1
        else:
            right = mid - 1

            return None


# Test cases
print(find_peak([1, 2, 4, 6, 3]))  # Output: 3
print(find_peak([4, 2, 1, 2, 3, 1]))  # Output: 2
print(find_peak([2, 2, 2]))  # Output: 1
print(find_peak([]))  # Output: None
print(find_peak([-2, -4, 2, 1]))  # Output: 2
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 4
