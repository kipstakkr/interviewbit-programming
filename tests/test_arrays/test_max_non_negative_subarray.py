"""Tests for the programming.arrays.max_non_negative_subarray module."""

from hypothesis import given
from hypothesis.strategies import integers, lists

from programming.arrays.max_non_negative_subarray import (
    get_max_non_negative_subarray_sum,
    is_negative
)

import pytest


@given(lists(integers(), min_size=1))
def test_is_negative(array):
    """is_negative() should return `True` when all elements are less than zero."""
    expected_result = not any(element >= 0 for element in array)

    assert is_negative(array) == expected_result


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ([1, 2, 5, -7, 2, 3], [1, 2, 5]),
        ([10, -1, 2, 3, -4, 100], [100]),
        ([-431, -1341, -3421, -5452], []),
        ([1232, 4531, 1245, 1243, 9327, 9474], [1232, 4531, 1245, 1243, 9327, 9474]),
        ([-432] + [10 ** 3] * 10 ** 3 + [-836, 10 ** 4], [10 ** 3] * 10 ** 3),
        ([20, 30, -45, 10, 10, 20, 10, -23, 50], [10, 10, 20, 10]),
        ([5, 10, 5, 4, 1, -5, 10, 2, 3, 6, 4, -4, 10, 15], [5, 10, 5, 4, 1])
    ]
)
def test_get_max_non_negative_subarray_sum(mock_array, expected_result):
    """get_max_non_negative_subarray_sum() should return the maximum non-negative subarray."""
    assert get_max_non_negative_subarray_sum(mock_array) == expected_result
