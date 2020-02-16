"""Tests for the programming.arrays.max_sum_contiguous_subarray module."""

from hypothesis import given
from hypothesis.strategies import integers, lists

from programming.arrays.max_sum_contiguous_subarray import (
    is_non_negative,
    is_non_positive,
    max_subarray
)

import pytest


@given(lists(integers(), min_size=1))
def test_is_non_positive(array):
    """is_non_positive() should return `True` when all elements are not greater than zero."""
    expected_result = not any(element > 0 for element in array)

    assert is_non_positive(array) == expected_result


@given(lists(integers(), min_size=1))
def test_is_non_negative(array):
    """is_non_negative() should return `True` when all elements are not less than zero."""
    expected_result = not any(element < 0 for element in array)

    assert is_non_negative(array) == expected_result


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ([1, 2, 3, 4, -10], (10, 0, 4)),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], (6, 3, 7)),
        ([1, 2, 3, 0, 3], (9, 0, 5)),
        ([-12, -2, -6, -9, -10, -21], (-2, 1, 2)),
        ([0, 0, 0, 0, 0], (0, 0, 1)),
        ([5, -2, -5, 2, -1, 3, 1], (5, 0, 1))
    ]
)
def test_max_subarray(mock_array, expected_result):
    """max_subarray() should return a tuple denoting max sum, start and end index of subarray."""
    assert max_subarray(mock_array) == expected_result
