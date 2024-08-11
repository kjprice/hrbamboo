#!/usr/bin/env python3

from typing import List
from helpers.validation import abs_diff, can_answer_be_found, prevalidation


def _find_largest_order_volume_not_perfectly_purchasable(product_supplies: List[int]):
    smallest = min(product_supplies)
    # TODO: Continuously add numbers together (for now max of ten times but should be improved)
    # TODO: Sort numbers (should be auto sorted)
    # TODO: from the end, go towards beginning, return the first gap (prev - curr > 2), return the largest number in gap

def match_product(product_supplies: List[int]) -> int:
    prevalidation(product_supplies)

    if not can_answer_be_found(product_supplies):
        return -1

    # If all numbers have a diff of 1, return (lowest value - 1)
    if len(product_supplies) == 2 and abs_diff(*product_supplies) == 1:
        return min(product_supplies) - 1

    # TODO: Test [10, 5, 6]
    return sum(product_supplies) + 1
