#!/usr/bin/env python3

from typing import List

def _is_even(num: int) -> bool:
    return num % 2 == 0

def _are_all_even(nums: List[int]) -> bool:
    return len(list(filter(_is_even, nums))) == len(nums)

def _abs_diff(num1: int, num2: int) -> int:
    return abs(num2 - num1)

def match_product(product_supplies: List[int]) -> int:
    # TODO: If two numbers are odd and not divisible by each other, return good
    # TODO: If two numbers are odd and even, and not divisible by each other, return good
    
    # If any number is 1, impossible
    if [num for num in product_supplies if num == 1]:
        return -1
    # If only one number exists
    if len(product_supplies) == 1:
        return -1
    # If all numbers have a diff of 1, impossible
    if len(product_supplies) == 2 and _abs_diff(*product_supplies) == 1:
        return -1
    # If all numbers are even, impossible
    if _are_all_even(product_supplies):
        return -1
    return sum(product_supplies) + 1