"""Tests for the programming.arrays.maximum_absolute_difference module."""

from programming.arrays.maximum_absolute_difference import max_abs_diff

import pytest


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ([1, 3, -1], 5),
        ([3, -2, 5, -4], 10),
        ([13880], 0),
        ([7, -12, 1334, 12321, -123, 8712, 12, 8132, 8162, -21234], 33561),
        ([21431, 12438, 18473, 18730, 99834, 16328, 12864,
          86323, 81326, 81653, 64355, 12635, 78623, 51325], 87399),
        ([-12343, -64352, -62324, -32554, -65232, -62355, -12543, -14532, -66834, -97934], 85600),
        ([87249] * 10 ** 4, 10 ** 4 - 1),
        ([0] * 10 ** 3, 10 ** 3 - 1)
    ]
)
def test_max_abs_diff(mock_array, expected_result):
    """max_abs_diff() should return the maximum value of the array based on the formula."""
    assert max_abs_diff(mock_array) == expected_result
