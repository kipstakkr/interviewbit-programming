"""
Contains the solution to problem 6 of the array section.

Problem
-------
You are given a binary string `S` (i.e. with characters `0` and `1`) consisting of characters
S1, S2, …, SN. In a single "OPERATION", you can choose two indices `L` and `R`
such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, we mean change
character `0` to `1` and vice-versa.

Your aim is to perform "ATMOST ONE OPERATION" such that in final string number of `1`s is
maximised.

Write a function to return an array consisting of two elements denoting `L` and `R`, in which the
number of `1`s in the given string in the range `L` and `R` is maximized.

Note
----
1.  If you don’t want to perform the operation, return an empty array/tuple.
2.  If there are multiple solutions, return the lexicographically smallest pair of `L` and `R`.
3.  Pair (a, b) is lexicographically smaller than pair (c, d) if a < c (or) if a == c and b < d.

Constraints
-----------
*   1 <= N <= 10 ** 5
*   S[i] = 0, 1
*   0 <= i < N

"""


def max_flip_bits(string):  # T(n), S(1)
    """Return the index pair (range) in the given string which has the maximum number of `1`s."""
    # if `0` is not present
    if '0' not in string:  # T(n)
        return ()

    max_sum, current_sum = 0, 0
    start_index, end_index = 0, 0
    current_start = 0
    for index in range(len(string)):  # T(n)

        if string[index] == '1':
            current_sum -= 1
            if current_sum < 0:
                current_sum = 0
                current_start = index + 1

        elif string[index] == '0':
            current_sum += 1
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = current_start + 1
                end_index = index + 1

    return start_index, end_index
