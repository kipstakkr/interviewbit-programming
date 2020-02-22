"""Tests for the programming.arrays.flip module."""

from programming.arrays.flip import max_flip_bits

import pytest


@pytest.mark.parametrize(
    'mock_string, expected_result',
    [
        ('010', (1, 1)),
        ('111', ()),
        ('11000111000', (3, 5)),
        ('111110011000001', (6, 14)),
        ('110010111', (3, 4))
    ]
)
def test_max_flip_bits(mock_string, expected_result):
    """max_flip_bits() should return the index pairs which contains the maximum number of 1's."""
    assert max_flip_bits(mock_string) == expected_result
