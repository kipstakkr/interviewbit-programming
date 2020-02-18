"""
Contains the solution to problem 5 of the array section.

Problem
-------
You are given a read only array of `n` integers, in which the elements ranges from 1 to n.
Each integer in the array (within the range) appears exactly once except `A` which appears twice
and `B` which is missing.

Write a function to return the repeated `A` and missing `B` numbers as a tuple.

"""


def repeat_and_missing_number_using_linear_space(array):  # T(n), S(n)
    """Return the repeated and missing number using sets."""
    num_elements = len(array)

    sum_actual = (num_elements * (num_elements + 1)) // 2
    sum_given = sum(array)  # T(n)
    sum_given_unique = sum(set(array))  # T(n), S(n)

    repeated_number = sum_given - sum_given_unique
    missing_number = sum_actual - sum_given_unique

    return repeated_number, missing_number


def repeat_and_missing_number_using_constant_space(array):  # T(n), S(1)
    """Return the repeated and missing number without using any extra space."""
    num_elements = len(array)

    diff, diff_square = 0, 0
    for index in range(num_elements):  # T(n)
        # calculate A - B
        diff += array[index]
        diff -= (index + 1)

        # Calculate A ** 2 - B ** 2
        diff_square += array[index] ** 2
        diff_square -= (index + 1) ** 2

    # Calculate A + B by expanding A ** 2 - B ** 2 and substituting A - B
    summation = diff_square // diff

    # using the formula created for A and B
    repeated_number = (summation + diff) // 2
    missing_number = summation - repeated_number

    return repeated_number, missing_number
