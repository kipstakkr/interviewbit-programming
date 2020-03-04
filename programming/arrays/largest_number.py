"""
Contains the solution to problem 14 of the array section.

Problem
-------
Given a list `A` of `N` non negative integers, arrange them such that they form the largest number.

For example,
    Given `[3, 30, 34, 5, 9]` as an input list, the largest formed number is `9534330`

Write a function to return a string representing a non-negative integer, which is the largest
number formed from a given array.

Note
----
1. The result may be very large, so you need to return a string instead of an integer.

Constraints
-----------
*   1 <= N <= 10 ** 5
*   0 <= A[i] <= 10 ** 5
*   0 <= i < N

"""

from functools import cmp_to_key


def combine_integers(integer_1, integer_2):  # T(1), S(1)
    """Combine the given two non-negative integers and return the combined integer."""
    return int(str(integer_1) + str(integer_2))


def comparision(num_1, num_2):  # T(1), S(1)
    """Compare the given numbers with respect to the combination of the given two numbers."""
    combination_1 = combine_integers(num_1, num_2)
    combination_2 = combine_integers(num_2, num_1)

    if combination_1 > combination_2:
        return -1
    elif combination_2 > combination_1:
        return 1

    return 0


def get_largest_number(array):  # T(n * log(n)), S(1)
    """Return a string representing a non-negative largest integer formed from the given array."""
    # if all the elements are zero
    if all(element == 0 for element in array):  # T(n)
        return '0'

    array.sort(key=cmp_to_key(comparision))  # T(n * log(n))

    return ''.join(str(integer) for integer in array)  # T(n)
