from unittest import TestCase
from helpers.purchasable_products import _get_numbers_less_than_max


class TestPurchasableProducts(TestCase):
    def test_get_numbers_less_than_max(self):
        self.assertListEqual(
            _get_numbers_less_than_max([2, 5], 10), [2, 4, 5, 6, 7, 8, 9, 10]
        )
