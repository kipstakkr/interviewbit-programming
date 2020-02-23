"""
Contains the solution to problem 11 of the array section.

Problem
-------
Given a `n x n` square matrix, return an array od its anti-diagonals.

For example,
    if the given square matrix of size 3 x 3 is,
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
    then the anti-diagonals are:
        [
            [1],
            [2, 4],
            [3, 5, 7],
            [6, 8],
            [9]
        ]

Write a function to return a list of list of integers consisting of the anti-diagonal elements of
the given `n x n` square matrix.

Constraints
-----------
*   1 <= n <= 1000

"""


def get_anti_diagonal_matrix(matrix):
    """Return the anti-diagonal matrix formed from the given matrix."""
    matrix_size = len(matrix)

    diagonal_matrix_size = 2 * (matrix_size - 1) + 1
    diagonal_matrix = [[] for _ in range(diagonal_matrix_size)]

    for row_index in range(matrix_size):
        for column_index in range(matrix_size):
            diagonal_row_index = row_index + column_index
            diagonal_matrix[diagonal_row_index].append(matrix[row_index][column_index])

    return diagonal_matrix
