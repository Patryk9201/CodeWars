import unittest
from who_likes_it import likes


class TestList(unittest.TestCase):
    def test_one(self):
        self.assertEqual(likes(["Patryk"]), "Patryk likes this")

    def test_two(self):
        self.assertEqual(likes(["Patryk", "Kuba"]), "Patryk and Kuba like this")

    def test_three(self):
        self.assertEqual(likes(["Patryk", "Kuba", "Kasia"]), "Patryk, Kuba and Kasia like this")

    def test_others(self):
        self.assertEqual(likes(["Patryk", "Kuba", "Kasia", "Krzysiu"]), "Patryk, Kuba and 2 others like this")


if __name__ == '__main__':
    unittest.main()
