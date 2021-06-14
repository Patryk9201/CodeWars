import unittest
from bouncing_balls import bouncing_ball


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(bouncing_ball(2, 0.5, 1), 1)


if __name__ == '__main__':
    unittest.main()