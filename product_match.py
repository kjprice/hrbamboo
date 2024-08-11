#!/usr/bin/env python3

from typing import List
from helpers.validation import abs_diff, can_answer_be_found, prevalidation


def match_product(product_supplies: List[int]) -> int:
    prevalidation(product_supplies)

    if not can_answer_be_found(product_supplies):
        return -1

    # If all numbers have a diff of 1, return (lowest value - 1)
    if len(product_supplies) == 2 and abs_diff(*product_supplies) == 1:
        return min(product_supplies) - 1

    # TODO: Test [10, 5, 6]
    return sum(product_supplies) + 1
