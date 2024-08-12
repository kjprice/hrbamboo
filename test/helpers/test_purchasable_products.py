from unittest import TestCase
from helpers.purchasable_products import _create_list_of_perfectly_purchasble_products, _find_last_missing_item, find_largest_order_volume_not_perfectly_purchasable


class TestPurchasableProducts(TestCase):
    def test_create_list_of_perfectly_purchasble_products(self):
        self.assertListEqual(
            _create_list_of_perfectly_purchasble_products([2, 5]), [2, 4, 5, 6, 7, 8, 9, 10]
        )
    def test_find_last_missing_item(self):
        self.assertEqual(_find_last_missing_item([2, 4, 5, 6, 7, 8, 9, 10]), 3)
