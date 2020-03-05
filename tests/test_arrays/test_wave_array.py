"""Tests for the programming.arrays.wave_array module."""

from programming.arrays.wave_array import get_wave_array

import pytest


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ([4, 3, 1, 2], [2, 1, 4, 3]),
        ([1], [1]),
        ([1, 4, 3], [3, 1, 4]),
        ([1, 4, 3, 2, 4, 1, 2, 3], [1, 1, 2, 2, 3, 3, 4, 4]),
        ([4, 3, 2, 4, 1, 2, 3], [2, 1, 3, 2, 4, 3, 4])
    ]
)
def test_get_wave_array(mock_array, expected_result):
    """get_wave_array() should return the sorted array in a wave like manner."""
    assert get_wave_array(mock_array) == expected_result
