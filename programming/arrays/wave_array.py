"""
Contains the solution to problem 15 of the array section.

Problem
-------
Given an array `A` of `N` integers, sort the array into a wave like array.
In other words, arrange the elements into a sequence such that:
    `A[0] >= A[1] <= A[2] >= A[3].....`

For example,
    Given [1, 2, 3, 4],
    One possible answer: [2, 1, 4, 3]
    Another possible answer: [4, 1, 3, 2]

Write a function to return the array sorted in a wave like manner as described above.

Note
----
1. If there are multiple answers possible, return the one that is lexicographically smallest.

Thus, in the example above we should return the first one as that is lexicographically smallest.

Constraints
-----------
*   1 <= N <= 10 ** 5
*   -10 ** 4 <= A[i] <= 10 ** 4
*   0 <= i < N

"""


def get_wave_array(array):  # T(n * log(n)), S(1)
    """Return the sorted array in a wave like manner."""
    array.sort()  # T(n * log(n))
    for index in range(0, len(array) - 1, 2):  # T(n)
        array[index], array[index + 1] = array[index + 1], array[index]

    return array
