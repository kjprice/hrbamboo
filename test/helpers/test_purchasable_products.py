from unittest import TestCase
from helpers.purchasable_products import _create_list_of_perfectly_purchasble_products, _find_last_missing_item, find_largest_order_volume_not_perfectly_purchasable


class TestPurchasableProducts(TestCase):
    def test_create_list_of_perfectly_purchasble_products(self):
        self.assertListEqual(
            _create_list_of_perfectly_purchasble_products([2, 5]), [2, 4, 5, 6, 7, 8, 9]
        )
        self.assertListEqual(
            _create_list_of_perfectly_purchasble_products([3, 7]), [3, 6, 7, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        )

    def test_find_last_missing_item(self):
        self.assertEqual(_find_last_missing_item([2, 4, 5, 6, 7, 8, 9, 10]), 3)

    def test_find_largest_order_volume_not_perfectly_purchasable(self):
        self.assertEqual(find_largest_order_volume_not_perfectly_purchasable([2, 5]), 3)
        self.assertEqual(find_largest_order_volume_not_perfectly_purchasable([3, 5]), 7)
        self.assertEqual(find_largest_order_volume_not_perfectly_purchasable([3, 7]), 11)
        self.assertEqual(find_largest_order_volume_not_perfectly_purchasable([4, 7]), 17)
        