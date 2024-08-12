from product_match import match_product
from helpers.validation import _are_any_odd_indivisible, ProductException

from unittest import TestCase

class TestProductMatch(TestCase):
    def test_prevalidation(self):
        # only positive numbers allowed
        self.assertRaises(ProductException, match_product, [-1])
        # numbers must be unique
        self.assertRaises(ProductException, match_product, [1, 1])
    def test_all_even(self):
        self.assertEqual(match_product([2, 4, 6, 8]), -1)
    def test_support_includes_one_day(self):
        self.assertEqual(match_product([1, 10]), -1)
    def test_only_one_product(self):
        self.assertEqual(match_product([3]), -1)
    def test_diff_of_one(self):
        self.assertEqual(match_product([3,4]), 5)

    def test_find_largest_order_volume_not_perfectly_purchasable(self):
        self.assertEqual(match_product([2, 5]), 3)
        self.assertEqual(match_product([3, 5]), 7)
        self.assertEqual(match_product([3, 7]), 11)
        self.assertEqual(match_product([4, 7]), 17)
        self.assertEqual(match_product([2, 4, 7]), 5)
        self.assertEqual(match_product([2, 4, 7]), 5)
        self.assertEqual(match_product([3, 10]), 17)
        self.assertEqual(match_product([10, 5, 6]), 19)
        