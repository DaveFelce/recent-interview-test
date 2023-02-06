from typing import Generator

from certino_test.input_two import calc_valid_positions, calc_valid_strings


def test_calc_valid_strings_with_fake(input_two_fake_lines: Generator):
    valid_strings = calc_valid_strings(input_two_fake_lines)
    assert valid_strings == 2


def test_calc_valid_strings(input_two_lines: Generator):
    valid_strings = calc_valid_strings(input_two_lines)
    assert valid_strings == 666


def test_calc_valid_positions_with_fake(input_two_fake_lines: Generator):
    valid_strings = calc_valid_positions(input_two_fake_lines)
    assert valid_strings == 1


def test_calc_valid_positions(input_two_lines: Generator):
    valid_strings = calc_valid_positions(input_two_lines)
    assert valid_strings == 29
