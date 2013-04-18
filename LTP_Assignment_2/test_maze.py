__author__ = 'sergej charskij'

from a2 import Rat, LEFT, NO_CHANGE, RIGHT, DOWN
from a2 import Maze
import unittest

class TestMaze(unittest.TestCase):

    def setUp(self):
        self.maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
                          ['#', '.', '.', '.', '.', '.', '#'],
                          ['#', '.', '#', '#', '#', '.', '#'],
                          ['#', '.', '.', '@', '#', '.', '#'],
                          ['#', '@', '#', '.', '@', '.', '#'],
                          ['#', '#', '#', '#', '#', '#', '#']],
                         Rat('J', 1, 1),
                         Rat('P', 1, 4))

    def test_maze_create(self):
        tmp = [['#', '#', '#', '#', '#', '#', '#'],
               ['#', '.', '.', '.', '.', '.', '#'],
               ['#', '.', '#', '#', '#', '.', '#'],
               ['#', '.', '.', '@', '#', '.', '#'],
               ['#', '@', '#', '.', '@', '.', '#'],
               ['#', '#', '#', '#', '#', '#', '#']]
        self.assertListEqual(tmp, self.maze.maze)
        self.assertEqual(self.maze.rat_1.symbol, 'J')
        self.assertEqual(self.maze.rat_1.row, 1)
        self.assertEqual(self.maze.rat_1.col, 1)

        self.assertEqual(self.maze.rat_2.symbol, 'P')
        self.assertEqual(self.maze.rat_2.row, 1)
        self.assertEqual(self.maze.rat_2.col, 4)

    def test_is_wall(self):
        self.assertTrue(self.maze.is_wall(0,0))
        self.assertTrue(self.maze.is_wall(0,6))
        self.assertTrue(self.maze.is_wall(2,2))
        self.assertFalse(self.maze.is_wall(1,1))
        self.assertFalse(self.maze.is_wall(4,1))

    def test_get_character(self):
        self.assertEqual(self.maze.get_character(0,0), '#')
        self.assertEqual(self.maze.get_character(1,1), 'J')
        self.assertEqual(self.maze.get_character(1,4), 'P')
        self.assertEqual(self.maze.get_character(3,3), '@')

    def test_move(self):
        # original position for J (1,1)
        self.assertTrue(self.maze.move(self.maze.rat_1, NO_CHANGE, NO_CHANGE))
        self.assertTrue(self.maze.move(self.maze.rat_1, NO_CHANGE, RIGHT))
        self.assertFalse(self.maze.move(self.maze.rat_1, DOWN, NO_CHANGE))
        # position 1, 2
        self.assertTrue(self.maze.move(self.maze.rat_1, NO_CHANGE, LEFT))
        self.maze.move(self.maze.rat_1, DOWN, NO_CHANGE)
        self.assertTrue(self.maze.move(self.maze.rat_1, DOWN, NO_CHANGE))

if __name__ == '__main__':
    unittest.main(exit=False)