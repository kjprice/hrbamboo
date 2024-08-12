#!/usr/bin/env python3

from typing import List
from helpers.validation import can_answer_be_found, prevalidation
from helpers.purchasable_products import find_largest_order_volume_not_perfectly_purchasable


def match_product(product_supplies: List[int]) -> int:
    prevalidation(product_supplies)

    if not can_answer_be_found(product_supplies):
        return -1

    return find_largest_order_volume_not_perfectly_purchasable(product_supplies)
