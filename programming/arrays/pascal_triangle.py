"""
Contains the solution to problem 9 of the array section.

Problem
-------
Given an integer `n`, generate the first `n` rows of Pascal's triangle.

For example,
    Pascal's triangle for n = 5 will be of the given form:
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1

Write a function to return a list of list of integers which represents the first `n` rows of the
Pascal's triangle.

For example,
    for n = 5, the output will be of the form:
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]

Constraints
-----------
*   0 <= n <= 10 ** 4

"""


def generate_pascal_triangle(size):  # T(n ** 2), S(n)
    """Return the generated Pascal's triangle of the first `size` rows."""
    if not size:
        return []

    triangle = [[1]]
    for row_index in range(size - 1):  # T(n)
        row_elements = [1]  # S(n)
        for index in range(1, len(triangle[row_index])):  # T(n)
            current_element = triangle[row_index][index - 1] + triangle[row_index][index]
            row_elements.append(current_element)
        row_elements.append(1)

        triangle.append(row_elements)

    return triangle
