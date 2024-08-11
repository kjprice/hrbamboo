from product_match import match_product
from helpers.validation import _are_any_odd_indivisible, ProductException

from unittest import TestCase


class TestProductMatch(TestCase):
    def test_numbers_divisible(self):
        self.assertFalse(_are_any_odd_indivisible([3, 6]))
        self.assertFalse(_are_any_odd_indivisible([6, 3]))
        self.assertTrue(_are_any_odd_indivisible([2, 5]))
        self.assertTrue(_are_any_odd_indivisible([5, 2]))
