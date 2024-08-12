#!/usr/bin/env python3

import argparse
from typing import List

from helpers.validation import can_answer_be_found, prevalidation
from helpers.purchasable_products import find_largest_order_volume_not_perfectly_purchasable


def match_product(product_supplies: List[int]) -> int:
    prevalidation(product_supplies)

    if not can_answer_be_found(product_supplies):
        return -1

    return find_largest_order_volume_not_perfectly_purchasable(product_supplies)

def _main():
    def get_args():
        parser = argparse.ArgumentParser(
                        prog='./product_match.py',
                        description='Largest Number Not Perfectly Purchasable'
                        )
        
        parser.add_argument('supplies', metavar="N", type=int, nargs="+", help="supplies")
        return parser.parse_args()
    args = get_args()
    print(f'Given the supplies: "{args.supplies}"')
    output = match_product(args.supplies)
    if output == -1:
        print("We could not find the largest number not perfectly purchasable")
    else:
        print(f"We found the following largest number not perfectly purchasable: {output}")


if __name__ == "__main__":
    _main()