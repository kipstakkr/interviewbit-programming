"""Tests for the programming.arrays.triplet_sum_between_range module."""

from programming.arrays.triplet_sum_between_range import check_triplet_exists

import pytest


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ([1.4, 0.2], 0),
        ([0.4, 1.5, 0.6, 0.2, 0.7, 1.2], 1),
        ([0.1] * 9, 0)
    ]
)
def test_check_triplet_exists(mock_array, expected_result):
    """check_triplet_exists() should check whether triplet exists in the array or not."""
    assert check_triplet_exists(mock_array) == expected_result
