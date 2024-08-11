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
