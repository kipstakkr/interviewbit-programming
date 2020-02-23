"""
Contains the solution to problem 10 of the array section.

Problem
-------
Given an index `k`, return the `k`th row of the Pascal's triangle.

For example,
    Pascal's triangle for n = 5 will be of the given form:
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
    Thus, if k = 4, then the 4th row indexed elements [1, 4, 6, 4, 1] should be returned.

Write a function to return a list of integers denoting the `k`th row elements of Pascal's triangle.

Constraints
-----------
*   0 <= k <= 10 ** 4

"""


def get_row_elements(row_index):
    """
    Return the given `row_index`th row elements of the Pascal's triangle.

    Formula
    -------
    formula for calculating the combinations using the previous one is:
      nC(r+1) = nCr * ((n - r) / (r + 1)),
      where, C = combinations
             n = row index
             r = index in the `n`th row
    """
    row_elements = [1]  # S(n)
    for index in range(row_index):  # T(n)
        element = (row_elements[index] * (row_index - index)) // (index + 1)
        row_elements.append(element)

    return row_elements
