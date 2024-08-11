#!/usr/bin/env python3

from typing import Iterable, List

class ProductException(Exception):
    pass

def _is_even(num: int) -> bool:
    return num % 2 == 0
def _is_odd(num: int) -> bool:
    return not _is_even(num)

def _get_odd_numbers(nums: List[int]) -> List[int]:
    return list(filter(_is_odd, nums))

def _even_count(nums: List[int]) -> int:
    return len(list(filter(_is_even, nums)))

def _are_all_even(nums: List[int]) -> bool:
    return _even_count(nums) == len(nums)

def _abs_diff(num1: int, num2: int) -> int:
    return abs(num2 - num1)

def _is_divisible(num1: int, num2: int):
    return num1 % num2 == 0 or num2 % num1 == 0

def _are_any_indivisible(num: int, nums: Iterable[int]) -> bool:
    for other in nums:
        if not _is_divisible(num, other):
            return True
    return False

def _are_any_odd_indivisible(nums: List[int]) -> bool:
    """
    For the algorithm to work, we must have at least one odd number that:
    - is not divisible by one other number AND
    - other number is not divisible by same odd number
    """
    nums_set = set(nums)
    odd_nums = _get_odd_numbers(nums)
    for odd_num in odd_nums:
        other_nums = nums_set - set([odd_num])
        if _are_any_indivisible(odd_num, other_nums):
            return True
    return False

def _prevalidation(nums: List[int]) -> None:
    for num in nums:
        if num < 1:
            raise ProductException("All products must be positive")
    
    if len(nums) != len(set(nums)):
        raise ProductException("All products must be unique")

def match_product(product_supplies: List[int]) -> int:
    # TODO: If two numbers are odd and not divisible by each other, return good
    # TODO: If two numbers are odd and even, and not divisible by each other, return good

    _prevalidation(product_supplies)
    
    # If any number is 1, impossible
    if [num for num in product_supplies if num == 1]:
        return -1
    # If only one number exists
    if len(product_supplies) == 1:
        return -1
    # If all numbers are even, impossible
    if _are_all_even(product_supplies):
        return -1
    # If all numbers have a diff of 1, return (lowest value - 1)
    if len(product_supplies) == 2 and _abs_diff(*product_supplies) == 1:
        return min(product_supplies) - 1
    
    # At least one odd number must exist that is not divisible by another number
    if not _are_any_odd_indivisible(product_supplies):
        return -1
    return sum(product_supplies) + 1