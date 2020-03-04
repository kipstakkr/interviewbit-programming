"""Tests for the programming.arrays.noble_integer module."""

from programming.arrays.noble_integer import check_noble_integer_exists

import pytest


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ([2], -1),
        ([0], 1),
        ([3, 2, 4, 1], 1),
        ([6, 7, 4, 2, 6, 5, 2, 1, 7, 3, 6], 1),
        ([6, 7, 4, 2, 6, 5, 2, 1, 7, 3], -1)
    ]
)
def test_check_noble_integer_exists(mock_array, expected_result):
    """check_noble_integer_exists() should check whether noble integer exists in array or not."""
    assert check_noble_integer_exists(mock_array) == expected_result
