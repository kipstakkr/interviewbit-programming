"""
Contains the solution to problem 7 of the array section.

Problem
-------
Given an array of integers `A` of length `N`, find out the maximum sum sub-array of non negative
numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth
element and skipping the third element is invalid. Maximum sub-array is defined as sum of the
elements in a sub-array.

Note:-
1.  If there is a tie, then compare with segment's length and return segment which has maximum
    length.
2.  If there is still a tie, then return the segment with minimum starting index.

Write a function to return the non-negative sub-array which has the maximum sum.

Constraints
-----------
*   1 <= N <= 10 ** 4
*   -10 ** 4 <= A[i] <= 10 ** 4
*   0 <= i < N

"""
from .max_sum_contiguous_subarray import is_non_negative


def is_negative(array):  # T(n), S(1)
    """Check if the given array contains only negative elements."""
    return all(element < 0 for element in array)


def get_max_non_negative_subarray_sum(array):  # T(n), S(1)
    """Return the non-negative sub-array from the given array which has the maximum sum."""
    if is_non_negative(array):  # T(n)
        return array

    elif is_negative(array):  # T(n)
        return []

    else:
        max_subarray_sum, max_subarray_length = 0, 0
        start_index, end_index = 0, 0
        current_start, current_end = 0, 0
        current_sum, current_subarray_length = 0, 0
        for index, element in enumerate(array):  # T(n)
            if element < 0:
                current_sum = 0
                current_start = index + 1
                continue

            current_sum += element
            current_end = index + 1

            # handling tie situation
            if current_sum == max_subarray_sum:
                current_subarray_length = current_end - current_start
                if current_subarray_length > max_subarray_length:
                    max_subarray_sum = current_sum
                    start_index, end_index = current_start, current_end

            elif current_sum > max_subarray_sum:
                max_subarray_sum = current_sum
                max_subarray_length = current_end - current_start
                start_index, end_index = current_start, current_end

        return array[start_index: end_index]
