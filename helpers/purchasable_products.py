from typing import List


def _get_numbers_less_than_max(nums: List[int], max_number: int) -> List[int]:
    output = nums.copy()
    nums_added = set()
    i = 0
    while output[i] <= max_number:
        num = output[i]
        for curr in nums:
            add = curr + num
            if not add in nums_added:
                nums_added.add(add)
                output.append(add)
        i += 1
    output.sort()
    while output[-1] > max_number:
        output.pop()
    return output


def _create_list_of_perfectly_purchasble_products(
    product_supplies: List[int],
) -> List[int]:
    nums = sorted(product_supplies)
    max_number = nums[0] * nums[1]

    return _get_numbers_less_than_max(product_supplies, max_number)

def _find_last_missing_item(nums: List[int]) -> int:
    curr = nums[-1]
    for prev in nums[:-1][::-1]:
        if abs(curr - prev) > 1:
            return curr - 1
        curr = prev
    return -1

def find_largest_order_volume_not_perfectly_purchasable(
    product_supplies: List[int],
) -> int:
    perfectly_purchasble_products = _create_list_of_perfectly_purchasble_products(product_supplies)

    return _find_last_missing_item(perfectly_purchasble_products)
