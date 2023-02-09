from itertools import combinations
from math import prod
from typing import Generator


def calc_prod(numbers: Generator, required_value: int, n_elements: int) -> int:
    combination = tuple()
    found_combination = False
    for combination in combinations(numbers, n_elements):
        if sum(combination) == required_value:
            found_combination = True
            break

    if not found_combination:
        raise ValueError("No combination found that meets the criteria")

    return prod(combination)
