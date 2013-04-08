import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_empty(self):
        """ Test that empty list not cause any error"""
        nums = []
        a1.swap_k(nums, 0)
        self.assertEqual(nums, [])

    def test_swap_k_one(self):
        """ Test with the smallest list possible """
        nums = [1]
        a1.swap_k(nums, 1)
        self.assertEqual(nums, [1])


    def test_swap_k_two(self):
        """ Test with two elements (even quantity) in the list """
        nums = [1,2]
        a1.swap_k(nums, 1)
        self.assertEqual(nums, [2,1])

    def test_swap_k_three(self):
        """ Test with three elements (odd quantity) in the list """
        nums = [1, 2, 3]
        a1.swap_k(nums, 1)
        self.assertEqual(nums, [3, 2, 1])

    def test_swap_k_actual(self):
        ''' Test with actual list'''
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)
        self.assertEqual(nums, [5, 6, 3, 4, 1, 2])



if __name__ == '__main__':
    unittest.main(exit=False)
