"""
Contains the solution to problem 13 of the array section.

Problem
-------
Given an array `A` of `N` real numbers greater than `zero` (in form of strings), find if there
exists a triplet `(a, b, c)` such that `1 < (a + b + c) < 2`. Return `1` for `True` and `0` for
`False`.

Note
----
1. The numbers in strings don’t overflow the primitive data type.
2. There are no leading zeroes in numbers.

Write a function to check whether a triplet exists based on the above condition.

Constraints
-----------
*   1 <= N <= 10 ** 7
*   -10 ** 4 <= A[i] <= 10 ** 4
*   0 <= i < N

"""


def check_triplet_exists(array):
    """Return an integer (`1` or `0`) by checking whether a triplet exists in the array or not."""
    # if there is no triplet possible in the array
    if len(array) < 3:
        return 0

    triplet = sorted(float(string) for string in array[:3])
    for index in range(3, len(array) + 1):

        triplet_sum = sum(triplet)
        if 1 < triplet_sum < 2:
            return 1
        elif index == len(array):
            return 0
        elif triplet_sum <= 1:
            triplet = sorted(triplet[1:] + [float(array[index])])
        elif triplet_sum >= 2:
            triplet = sorted(triplet[:2] + [float(array[index])])
