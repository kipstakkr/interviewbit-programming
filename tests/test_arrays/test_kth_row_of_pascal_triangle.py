"""Tests for the programming.arrays.kth_row_of_pascal_triangle module."""

from hypothesis import given
from hypothesis.strategies import integers

from programming.arrays.kth_row_of_pascal_triangle import get_row_elements

import pytest


class TestGetRowElements:
    """get_row_elements() should return the given indexed row elements of Pascal's triangle."""

    @given(integers(min_value=0, max_value=10 ** 4))
    def test_get_row_elements_for_the_row_sum(self, row_index):
        """Test whether the row elements satisfy the Pascal's triangle sum property."""
        assert sum(get_row_elements(row_index)) == 2 ** row_index

    @pytest.mark.parametrize(
        'mock_row_index, expected_result',
        [
            (0, [1]),
            (4, [1, 4, 6, 4, 1]),
            (10, [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1])
        ]
    )
    def test_get_row_elements(self, mock_row_index, expected_result):
        """Test whether the row elements the given index of Pascal's triangle is returned."""
        assert get_row_elements(mock_row_index) == expected_result
