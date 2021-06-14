import unittest
from one_plus_array import up_array

class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(up_array([2, 3, 9]), [2, 4, 0])

    def test_false(self):
        self.assertFalse(up_array([2, 3, 10]), None)

if __name__ == '__main__':
    unittest.main()