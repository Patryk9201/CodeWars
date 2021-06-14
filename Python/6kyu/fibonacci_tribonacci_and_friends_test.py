import unittest
from fibonacci_tribonacci_and_friends import xbonacci


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(xbonacci([0, 5], 10), [0, 5, 5, 10, 15, 25, 40, 65, 105, 170])

    def test_two(self):
        self.assertEqual(xbonacci([1, 1], 10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


if __name__ == '__main__':
    unittest.main()
