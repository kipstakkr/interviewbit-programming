"""Tests for the programming.arrays.hotel_bookings module."""

from programming.arrays.hotel_bookings import check_bookings_possible

import pytest


@pytest.mark.parametrize(
    'mock_arrival, mock_departure, mock_num_rooms, expected_result',
    [
        ([4, 2, 8, 10], [6, 4, 10], 1, False),
        ([1, 3, 5], [2, 6, 8], 1, False),
        ([7, 2, 5], [10, 4, 6], 1, True),
        ([7, 2, 5], [10, 4, 7], 1, True),
        ([2, 5, 2], [10, 7, 4], 2, True)
    ]
)
def test_check_bookings_possible(mock_arrival, mock_departure, mock_num_rooms, expected_result):
    """check_bookings_possible() should return a boolean checking whether a booking is possible."""
    assert check_bookings_possible(mock_arrival, mock_departure, mock_num_rooms) == expected_result
