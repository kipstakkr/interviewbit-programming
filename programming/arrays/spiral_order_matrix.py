"""
Contains the solution to problem 8 of the array section.

Problem
-------
Given an integer `n`, generate a square matrix filled with elements from `1` to `n ** 2` in
spiral order.

For example,
    if the given integer is `3`, then the square matrix to generate which satisfied the
    spiral order is:
        [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]

Return a 2-d matrix of size `n x n` satisfying the spiral order.

Constraints
-----------
*   1 <= A <= 1000

"""


class Direction:
    """Contains the constants for the directions based on the scenario of spiral order."""

    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


def generate_spiral_matrix(size):  # T(n ** 2), S(1)
    """Return a 2-d square matrix of size `size x size`, which satisfies the spiral order."""
    spiral_matrix = [[0 for _ in range(size)] for _ in range(size)]

    left = top = 0
    right = bottom = size - 1

    # this is the start direction for the spiral order matrix
    direction = Direction.EAST

    number = 1
    while left <= right and top <= bottom:  # T(n ** 2)

        if direction == Direction.EAST:
            for index in range(left, right + 1):
                spiral_matrix[top][index] = number
                number += 1
            top += 1

        elif direction == Direction.SOUTH:
            for index in range(top, bottom + 1):
                spiral_matrix[index][right] = number
                number += 1
            right -= 1

        elif direction == Direction.WEST:
            for index in reversed(range(left, right + 1)):
                spiral_matrix[bottom][index] = number
                number += 1
            bottom -= 1

        elif direction == Direction.NORTH:
            for index in reversed(range(top, bottom + 1)):
                spiral_matrix[index][left] = number
                number += 1
            left += 1

        direction = (direction + 1) % 4

    return spiral_matrix
