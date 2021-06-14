import unittest
from dashatize_it import dashatize


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(dashatize(274), "2-7-4")
        self.assertEqual(dashatize(888), "888")


if __name__ == '__main__':
    unittest.main()