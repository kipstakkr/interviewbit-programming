"""
Contains the solution to problem 3 of the array section.

Problem
-------
Find the contiguous subarray within an array `a` of length `n` which has the largest sum. Also find
the start and end indices of the subarray which has the maximum sum.

Write a function to return a tuple containing the maximum possible sum with the start and end
indices of the contiguous subarray.

Constraints
-----------
1 <= n <= 10 ** 5
-1000 <= a[i] <= 1000
0 <= i < n

"""


def is_non_negative(array):
    """Return a boolean which denotes whether all the elements in given array are non-negative."""
    return all(element >= 0 for element in array)


def is_non_positive(array):
    """Return a boolean which denotes whether all the elements in given array are non-positive."""
    return all(element <= 0 for element in array)


def max_subarray(array):
    """Return the maximum possible sum with start and end indices of contiguous subarray."""
    # if all the elements in the array are non-positive
    if is_non_positive(array):
        max_sum = max(array)
        start_index = array.index(max_sum)
        end_index = start_index + 1

    # if all the elements in the array are non-negative
    elif is_non_negative(array):
        max_sum = sum(array)
        start_index, end_index = 0, len(array)

    # if the elements are a combination of positive, negative and/or zero.
    else:
        max_sum, current_sum = 0, 0
        start_index, end_index = 0, 1
        for current_index, current_element in enumerate(array):

            # if the current sum is less than or equal to zero,
            # reset the current sum to start from the current element
            if current_sum <= 0:
                current_sum = current_element
                current_start = current_index

            # if the current sum is greater than zero
            else:
                current_sum += current_element

            # if the current sum is greater than max sum
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = current_start
                end_index = current_index + 1

    return max_sum, start_index, end_index
