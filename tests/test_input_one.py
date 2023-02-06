from typing import Generator
import pytest

from certino_test.input_one import calc_sum


def test_calc_sum_with_fake(fake_numbers: Generator) -> None:
    calculated_sum = calc_sum(numbers=fake_numbers, required_value=2020, n_elements=2)
    assert calculated_sum == 514579


def test_calc_sum(numbers: Generator) -> None:
    calculated_sum = calc_sum(numbers=numbers, required_value=2020, n_elements=2)
    assert calculated_sum == 1013211


def test_calc_sum_raises(numbers: Generator) -> None:
    with pytest.raises(ValueError):
        calc_sum(numbers=numbers, required_value=1, n_elements=2)


def test_calc_sum_with_fake_and_three_elements(fake_numbers: Generator) -> None:
    calculated_sum = calc_sum(numbers=fake_numbers, required_value=2020, n_elements=3)
    assert calculated_sum == 241861950


def test_calc_sum_and_three_elements(numbers: Generator) -> None:
    calculated_sum = calc_sum(numbers=numbers, required_value=2020, n_elements=3)
    assert calculated_sum == 13891280

