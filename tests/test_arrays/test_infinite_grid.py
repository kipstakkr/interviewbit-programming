"""Tests for the programming.arrays.infinite_grid module."""

from programming.arrays.infinite_grid import get_min_steps

import pytest


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ([(0, 0), (-1, 3)], 3),
        ([(1, 4), (-12, 16), (908, 13234)], 13231),
        ([(0, 0), (0, -1)], 1),
        ([(1288, 2189), (1232, -1223)], 3412),
        ([(98264, -12363), (-12421, 94321), (12571, -97364)], 302370)
    ]
)
def test_get_min_steps(mock_array, expected_result):
    """get_min_steps() should return the minimum steps to reach the end point from start point."""
    assert get_min_steps(mock_array) == expected_result
