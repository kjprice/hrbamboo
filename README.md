## Largest Number Not Perfectly Purchasable

Here we are given the task of finding the "largest number not perfectly purchasable" based on a set of available **product supplies** (a list of numbers where each number represents how many days of a product are provided).

An **order** (a number of days requested for product) is **purchasable** if we can use some combination of supplies to fulfill the order (combination is greater than or equal to order).

An order is **perfectly purchasable** if we can use some combination of supplies to exactly fulfill the order (combination is equal to order).

Our task is, provided an arbitrary list of product supplies (`[int]`), return the last number that is not perfectly purchasable.

### Methodology

To find the `largest number not perfectly purchasable`, we simply create a list of `perfectly purchasable orders` and then iterate backwards until we find a gap between the numbers (where `abs(prev - curr) > 1`). Then return the largest number in this gap.

It would be necessary to create a limit to the number of `perfectly purchasable orders` we would compute. It was discovered that the `largest number not perfectly purchasable` could be found in a list of `perfectly purchasable orders` with a max value. This max value would be computed by the input `product supplies` where we would take *smallest* and *second smallest* numbers and multiply them together (`max_number = sorted_product_supplies[0] * sorted_product_supplies[1]`).

### Validation and Caveats

We have created somewhat arbitrary restrictions on the input `product supplies`. An error would be thrown if any of these criteria are not met:

 - There must be at least two `product supplies`
 - All `product supplies` must be positive
 - All `product supplies` must be unique


We also found there are some sets of `product supplies` where we will never have a `largest number not perfectly purchasable`. In these cases we can iterate through combinations forever and still not find the `largest number not perfectly purchasable`. In these cases, we will return `-1`.

### To run

```
./product_match.py
```

### To test

```
python3 -m unittest discover
```
