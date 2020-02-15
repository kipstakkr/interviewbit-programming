"""
Contains the solution to problem 1 of the array section.

Problem
-------
In an infinite 2D grid, you can move in any of the given 8 directions from a point (x, y):
    (x, y) to   (x, y + 1)
                (x + 1, y + 1)
                (x + 1, y)
                (x + 1, y - 1)
                (x, y - 1)
                (x - 1, y - 1)
                (x - 1, y)
                (x - 1, y + 1)
A single move in a given direction is represented as a `step`.

Given an array `a` of tuples containing `n` sequence of points, which denotes the order in which
you need to cover the points, find the minimum number of steps to reach the end point (last element
of the sequence) from the start point (first element of the sequence).

Write a function to return the minimum number of steps for a given sequence of points.

Constraints
-----------
*   2 <= n <= 10 ** 9
*   -10 ** 5 <= a[i] <= 10 ** 5
*   0 <= i < n

"""


def get_min_steps(array):  # T(n), S(1)
    """Return the minimum number of steps to reach the end from the start point of the array."""
    steps = 0
    for index in range(len(array) - 1):  # T(n)
        start_x, start_y = array[index][0], array[index][1]
        end_x, end_y = array[index + 1][0], array[index + 1][1]

        # using the formula for calculation chebyshev distance
        steps += max(abs(start_x - end_x), abs(start_y - end_y))

    return steps
