#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_at_end(self):
        """Test with the max integer at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with the max integer at the beginning of the list"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_middle(self):
        """Test with the max integer in the middle of the list"""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_element(self):
        """Test with a single element in the list"""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_non_integers(self):
        """Test with a list that contains non-integer elements"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])


# This allows the test to be run from the command line
if __name__ == "__main__":
    unittest.main()
