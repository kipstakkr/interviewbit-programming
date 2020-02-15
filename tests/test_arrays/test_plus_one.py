"""Tests for the programming.arrays.plus_one module."""

from hypothesis import given, settings
from hypothesis.strategies import integers, lists

from programming.arrays.plus_one import add_one_to_number, reverse

import pytest


@given(lists(integers(min_value=0, max_value=9), min_size=1, max_size=10 ** 7))
@settings(max_examples=500)
def test_reverse(array):
    """reverse() should return the given array with values in reverse order."""
    assert reverse(array) == list(reversed(array))


@pytest.mark.parametrize(
    'mock_digits, expected_result',
    [
        ([0], [1]),
        ([7, 9, 8, 7], [7, 9, 8, 8]),
        ([0, 0, 1, 3, 2, 9], [1, 3, 3, 0]),
        ([9, 9, 9, 9, 9], [1, 0, 0, 0, 0, 0]),
        ([0, 9, 2, 9, 9, 9], [9, 3, 0, 0, 0]),
        ([0] * 100 + [9] * (10 ** 6), [1] + [0] * (10 ** 6))
    ]
)
def test_add_one_to_number(mock_digits, expected_result):
    """add_one_to_number() should return the given digits after incrementing the number by 1."""
    assert add_one_to_number(mock_digits) == expected_result
