"""Tests for the programming.arrays.pascal_triangle module."""

from programming.arrays.pascal_triangle import generate_pascal_triangle

import pytest


@pytest.mark.parametrize(
    'mock_size, expected_result',
    [
        (0, []),
        (1, [[1]]),
        (4, [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1]
        ]),
        (5, [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]),
        (10, [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1],
            [1, 8, 28, 56, 70, 56, 28, 8, 1],
            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
        ])
    ]
)
def test_generate_pascal_triangle(mock_size, expected_result):
    """generate_pascal_triangle() should generate the first `size` rows of Pascal's triangle."""
    assert generate_pascal_triangle(mock_size) == expected_result
