"""Tests for the programming.arrays.largest_number module."""

from programming.arrays.largest_number import combine_integers, comparision, get_largest_number

import pytest


@pytest.mark.parametrize(
    'mock_integer_1, mock_integer_2, expected_result',
    [
        (21, 45, 2145),
        (0, 23, 23),
        (23453, 0, 234530),
        (0, 0, 0)
    ]
)
def test_combine_integers(mock_integer_1, mock_integer_2, expected_result):
    """combine_integers() should combine the given integers and return the combined integer."""
    assert combine_integers(mock_integer_1, mock_integer_2) == expected_result


@pytest.mark.parametrize(
    'mock_num_1, mock_num_2, expected_result',
    [
        (35, 234, -1),
        (0, 42, 1),
        (55, 55, 0),
        (42, 0, -1)
    ]
)
def test_comparision(mock_num_1, mock_num_2, expected_result):
    """comparision() should compare the given numbers with respect to the combination of it."""
    assert comparision(mock_num_1, mock_num_2) == expected_result


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ([3, 30, 34, 5, 9], '9534330'),
        ([0] * 10 ** 5, '0'),
        ([43, 9074, 1324, 5423, 12345, 13463, 89456, 7, 65], '90748945676554234313463132412345')
    ]
)
def test_get_largest_number(mock_array, expected_result):
    """get_largest_number() should return the largest number formed from given integer array."""
    assert get_largest_number(mock_array) == expected_result
