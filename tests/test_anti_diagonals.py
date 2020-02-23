"""Tests for the programming.arrays.anti_diagonals module."""

from programming.arrays.anti_diagonals import get_anti_diagonal_matrix

import pytest


@pytest.mark.parametrize(
    'mock_matrix, expected_result',
    [
        ([[1]], [[1]]),
        (
            [
                [1, 2],
                [3, 4]
            ],
            [
                [1],
                [2, 3],
                [4]
            ]
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            [
                [1],
                [2, 4],
                [3, 5, 7],
                [6, 8],
                [9]
            ]
        ),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]
            ],
            [
                [1],
                [2, 6],
                [3, 7, 11],
                [4, 8, 12, 16],
                [5, 9, 13, 17, 21],
                [10, 14, 18, 22],
                [15, 19, 23],
                [20, 24],
                [25]
            ]
        )
    ]
)
def test_get_anti_diagonal_matrix(mock_matrix, expected_result):
    """get_anti_diagonal_matrix() should return the matrix containing anti-diagonal elements."""
    assert get_anti_diagonal_matrix(mock_matrix) == expected_result
