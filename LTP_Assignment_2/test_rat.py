__author__ = 'sergej charskij'

from a2 import Rat
import unittest


class TestRat(unittest.TestCase):

    def setUp(self):
        self.rat = Rat('P', 1, 4)

    def test_rat_create(self):
        self.assertEqual(self.rat.symbol, 'P')
        self.assertEqual(self.rat.row, 1)
        self.assertEqual(self.rat.col, 4)
        self.assertEqual(self.rat.num_sprouts_eaten, 0)

    def test_set_location(self):
        self.rat.set_location(5,7)
        self.assertEqual(self.rat.row, 5)
        self.assertEqual(self.rat.col, 7)

    def test_num_sprouts_eaten(self):
        self.rat.eat_sprout()
        self.assertEqual(self.rat.num_sprouts_eaten, 1)
        self.rat.eat_sprout()
        self.assertEqual(self.rat.num_sprouts_eaten, 2)

    def test_print(self):
        rat = Rat('J', 4, 3)
        rat.eat_sprout()
        rat.eat_sprout()
        self.assertEqual(rat.__str__(), 'J at (4, 3) ate 2 sprouts.')



if __name__ == '__main__':
    unittest.main(exit=False)