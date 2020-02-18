"""Tests for the programming.arrays.repeat_and_missing_number module."""

import random

from programming.arrays.repeat_and_missing_number import (
    repeat_and_missing_number_using_constant_space,
    repeat_and_missing_number_using_linear_space
)

import pytest


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ((3, 1, 2, 5, 3), (3, 4)),
        ((1, 2, 5, 3, 3, 6), (3, 4)),
        ((4, 2, 1, 2), (2, 3)),
        ((3, 5, 4, 2, 4), (4, 1)),
        (tuple(random.sample(range(1, 10 ** 7), 10 ** 7 - 1)) + (10 ** 4,), (10 ** 4, 10 ** 7))
    ]
)
def test_repeat_and_missing_number_common(mock_array, expected_result):
    """repeat_and_missing_number() should return the repeated and missing number from array."""
    assert repeat_and_missing_number_using_linear_space(mock_array) == expected_result
    assert repeat_and_missing_number_using_constant_space(mock_array) == expected_result
