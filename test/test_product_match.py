from product_match import match_product

from unittest import TestCase

class TestProductMatch(TestCase):
    def test_match_product(self):
        self.assertEqual(match_product([1,2]), 4)