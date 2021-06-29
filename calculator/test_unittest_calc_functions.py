import pytest
import unittest

import calculator.calc_functions as calc

class Cacltest(unittest.TestCase):


    def test_add(self):  # naming convention is essential as 'test' is the word we need to use when naming tests so
        # python interpreter recog nised it to run the test
        self.assertEqual(calc.add(4, 4), 8)

    def test_subtract(self):
        self.assertEqual(calc.subtract(2, 2), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(4, 10), 40)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
