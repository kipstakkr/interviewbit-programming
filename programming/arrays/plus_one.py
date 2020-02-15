"""
Contains the solution to problem 2 of the array section.

Problem
-------
Given a non negative number represented as an array `a` of `n` digits (0 - 9), increment the number
(which is represented by array of digits) by 1 .
The digits are stored such that the most significant digit is at the head of the list.

Write a function to return the array of digits after incrementing the number by 1.

Constraints
-----------
*   1 <= n <= 10 ** 7
*   0 <= a[i] <= 9
*   0 <= i < n

"""


def reverse(array):
    """Return the reverse of the array as a list."""
    return list(reversed(array))


def add_one_to_number(digits):
    """Return the array of digits after incrementing the number by 1."""
    # reverse the given digits list
    rev_digits = reverse(digits)

    # trim the zeros from the end of the reversed digits
    for i in reversed(range(len(rev_digits))):
        if rev_digits[i]:
            break
        del rev_digits[i]

    # after removing the trailing zeros from the reversed digits, if the list is empty
    if not rev_digits:
        return [1]

    # if the first digit in the reversed digits is not 9
    if rev_digits[0] != 9:
        rev_digits[0] += 1
        return reverse(rev_digits)

    # if the first digit in the reversed digits is 9
    for i in range(len(rev_digits)):

        # if one of the subsequent digits is not 9
        if rev_digits[i] != 9:
            rev_digits[i] += 1
            return reverse(rev_digits)

        # if it is 9
        rev_digits[i] = 0

        # if it reaches the end of the reversed digits and the digit is 9
        if i == len(rev_digits) - 1:
            rev_digits.append(1)
            return reverse(rev_digits)
