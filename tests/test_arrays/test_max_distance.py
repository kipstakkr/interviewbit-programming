"""Tests for the programming.arrays.max_distance module."""

from programming.arrays.max_distance import get_max_distance

import pytest


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ([], -1),
        ([3, 4, 5, 2], 2),
        ([9, 6, 3, 2], 0),
        ([1, 2, 4, 6], 3),
        ([6, -2, 9, 132, -523, -5621, 234], 6),
        ([10 ** 4] * 10 ** 5, 10 ** 5 - 1)
    ]
)
def test_get_max_distance(mock_array, expected_result):
    """get_max_distance() should return the maximum distance between indices."""
    assert get_max_distance(mock_array) == expected_result
