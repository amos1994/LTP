import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.

    def test_num_buses_zero(self):
        """ to be sure that 0 not cause any error """
        actual = a1.num_buses(0)        
        self.assertEqual(actual, 0)

    def test_num_buses_equal_fifty(self):
        """ result must be precisely 1 to 50 """
        actual = a1.num_buses(50)
        self.assertEqual(actual, 1)

    def test_num_buses_more_than(self):
        """ check how function behaves for more than 50  """
        actual = a1.num_buses(75)        
        self.assertEqual(actual, 2)

if __name__ == '__main__':
    unittest.main(exit=False)
