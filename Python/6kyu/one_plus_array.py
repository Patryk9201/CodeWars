"""
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples

For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]
"""

import unittest


def up_array(arr):
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None
    else:
        return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]






if __name__ == '__main__':
    x = up_array([2, 3, 9])
    print(x)
    unittest.main()

