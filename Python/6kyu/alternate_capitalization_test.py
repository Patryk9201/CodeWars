import unittest
from alternate_capitalization import capitalizer


class TestList(unittest.TestCase):
    def test_capi(self):
        self.assertEqual(capitalizer("patryk"), ['PaTrYk', 'pAtRyK'])


if __name__ == '__main__':
    unittest.main()