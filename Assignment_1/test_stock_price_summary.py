import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_empty_list(self):
        """ Test with empty list """
        actual = a1.stock_price_summary([])
        self.assertEqual(actual, (0,0))

    def test_stock_price_summary_negative(self):
        """ Test with one negative value """
        actual = a1.stock_price_summary([-1])
        self.assertEqual(actual, (0, -1))

    def test_stock_price_summary_big_negative_numbers(self):
        """ Test with big floating point numbers (precise calculation)"""
        negative_given = -0.184357
        (positive_calc, negative_calc) = a1.stock_price_summary([0.010126, 0.03894, -0.02, -0.144827, 0, 0, 0.10, -0.01953])
        self.assertAlmostEqual(negative_calc, negative_given, places=7, msg=None, delta=None)

    def test_stock_price_summary_positive(self):
        """ Test with one positive value """
        actual = a1.stock_price_summary([1])
        self.assertEqual(actual, (1, 0))

    def test_stock_price_summary_big_positive_numbers(self):
        """ Test with big floating point numbers (precise calculation)"""
        positive_given =  0.149066
        (positive_calc, negative_calc) = a1.stock_price_summary([0.010126, 0.03894, -0.02, -0.144827, 0, 0, 0.10, -0.01953])
        self.assertAlmostEqual(positive_calc, positive_given, places=7, msg=None, delta=None)

    def test_stock_price_summary_zero(self):
        """ Test with zero """
        actual = a1.stock_price_summary([0])
        self.assertEqual(actual, (0, 0))

    def test_stock_price_summary_actual(self):
        """ Test with actual values """
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        self.assertEqual(actual, (0.14, -0.17))

if __name__ == '__main__':
    unittest.main(exit=False)
