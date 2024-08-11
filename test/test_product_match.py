from product_match import match_product

from unittest import TestCase

class TestProductMatch(TestCase):
    def test_diff_of_one(self):
        self.assertEqual(match_product([3,4]), -1)
    def test_all_even(self):
        self.assertEqual(match_product([2, 4, 6, 8]), -1)
    def test_support_includes_one_day(self):
        self.assertEqual(match_product([1, 10]), -1)
    def test_only_one_product(self):
        self.assertEqual(match_product([3]), -1)
