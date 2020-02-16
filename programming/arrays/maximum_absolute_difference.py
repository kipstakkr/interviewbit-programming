"""
Contains the solution to problem 4 of the array section.

Problem
-------
Given an array `a` of `n` integers, return the maximum value of f(i, j) for all 0 <= i, j < n,
where
    f(i, j) = |a[i] - a[j]| + |i - j|, where |x| denotes absolute value of x.

Write a method to return the maximum value for the above function.

Constraints
-----------
*   1 <= n <= 10 ** 7
*   -10 ** 5 <= a[i] <= 10 ** 5

"""


def max_abs_diff(array):
    """
    Return the maximum absolute difference value for the given array based on the formula.

    Formula
    -------
        f(i, j) = |a[i] - a[j]| + |i - j|, for all 0 <= i, j < n.

    """
    # if there is only one element in the array, then the formula will return 0
    if len(array) == 1:
        return 0

    max_add, min_add = float('-Inf'), float('Inf')  # for the case of array[i] + i
    max_sub, min_sub = float('-Inf'), float('Inf')  # for the case of array[i] - i
    for index in range(len(array)):

        max_add = max(max_add, array[index] + index)
        min_add = min(min_add, array[index] + index)

        max_sub = max(max_sub, array[index] - index)
        min_sub = min(min_sub, array[index] - index)

    return max(max_add - min_add, max_sub - min_sub)
