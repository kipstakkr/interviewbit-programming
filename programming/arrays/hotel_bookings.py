"""
Contains the solution to problem 16 of the array section.

Problem
-------
A hotel manager has to process `N` advance bookings of rooms for the next season. His hotel has
`K` rooms. Bookings contain an arrival date `A` and a departure date `D`. He wants to find out
whether there are enough rooms in the hotel to satisfy the demand.

Write a function to return a boolean which tells whether all the bookings are possible or not.

Constraints
-----------
*   1 <= N <= 10 ** 5
*   1 <= A[i] <= D[i] <= 10 ** 5
*   0 <= i < N
*   1 <= k <= 10 ** 7

"""

from operator import itemgetter


def check_bookings_possible(arrival, departure, num_rooms):  # T(n * log(n)), S(n)
    """Return a boolean by checking whether whether all the bookings are possible or not."""
    if len(arrival) != len(departure):
        return False

    # `S` for Start and `E` for end
    arrival = [(date, 'S') for date in arrival]  # T(n), S(n)
    departure = [(date, 'E') for date in departure]  # T(n), S(n)

    booking_list = arrival + departure  # T(n), S(n)
    booking_list.sort(key=itemgetter(0, 1))  # T(n * log(n))

    active_guests = 0
    for index in range(len(booking_list)):  # T(n)
        if booking_list[index][1] == 'S':
            active_guests += 1
        elif booking_list[index][1] == 'E':
            active_guests -= 1

        if active_guests > num_rooms:
            return False

    return True
