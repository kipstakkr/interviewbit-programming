"""
Contains the solution to problem 17 of the array section.

Problem
-------
Given an array `A` of `N` integers, find the maximum value of `j - i` subjected to the constraint
`A[i] <= A[j]`.

Note
----
1.  The value of i and j can be equal.
2.  If there is no solution possible, return -1.

Write a function to return the maximum distance between the indices based on the given constraint.

Constraints
-----------
*   1 <= N <= 10 ** 5
*   -10 ** 4 <= A[u] <= 10 ** 4
*   0 <= u < N

"""


def get_max_distance(array):  # T(n * log(n)), S(n)
    """
    Return the maximum distance between the indices which satisfy the constraint.

    The given constraint is: find maximum of j - i for all array[i] <= array[j].
    """
    if not array:
        return -1

    # get the sorted index based on the corresponding value at that index
    index_array = [index  # T(n * log(n)), S(n)
                   for index, _ in sorted(enumerate(array), key=lambda x: x[1])]

    max_distance = 0
    max_index = index_array[-1]
    for index in reversed(index_array[:-1]):  # T(n)
        distance = max_index - index

        max_distance = max(max_distance, distance)
        max_index = max(max_index, index)

    return max_distance
