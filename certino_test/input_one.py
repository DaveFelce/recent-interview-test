from itertools import combinations
from math import prod
from typing import Generator


def calc_sum(numbers: Generator, required_value: int, n_elements: int) -> int:
    try:
        combination: tuple = list(
            filter(lambda t: True if sum(t) == required_value else False, combinations(numbers, n_elements))
        )[0]
    except IndexError as e:
        raise ValueError("No combination found that meets the criteria")

    return prod(combination)
