"""Tests for the programming.arrays.plus_one module."""

from hypothesis import given, settings
from hypothesis.strategies import integers, lists

from programming.arrays.plus_one import add_one_to_number, reverse


@given(lists(integers(min_value=0, max_value=9), min_size=1, max_size=10 ** 9))
@settings(max_examples=500)
def test_reverse(array):
    """reverse() should return the given array with values in reverse order."""
    assert reverse(array) == list(reversed(array))


@given(lists(integers(min_value=0, max_value=9), min_size=1, max_size=10 ** 9))
@settings(max_examples=500)
def test_add_one_to_number(digits):
    """add_one_to_number() should return the given digits after incrementing the number by 1."""
    # get the digits added by 1
    digit_str = ''.join([str(digit) for digit in digits])
    expected_result = list(map(int, str(int(digit_str) + 1)))

    assert add_one_to_number(digits) == expected_result
