"""
Contains the solution to problem 12 of the array section.

Problem
-------
Given an integer array `A`, find if an integer `p` exists in the array such that the number of
integers greater than `p` in the array equals to `p`. If such an integer is found, return `1`
else return `-1`.

Write a function to return an integer (either `1` or `-1`) based on the above condition.

Constraints
-----------
*   1 <= len(A) <= 10 ** 5

"""


def check_noble_integer_exists(array):  # T(n * log(n)), S(1)
    """
    Return a integer by checking whether a noble integer is present in the given array or not.

    Noble integer `p` in an array is (as defined for the problem) an integer, such that the
    integers greater than `p` in the array equals to `p`.
    """
    array.sort(reverse=True)  # T(n * log(n))

    # case when the first element in the reverse sorted array is zero
    if not array[0]:
        return 1

    for index in range(1, len(array)):  # T(n)

        # handling the duplicate values
        if array[index] == array[index - 1]:
            continue

        if array[index] == index:
            return 1

    return -1
