"""
    NUMBER OF MATRIX TRAVERSALS (EPI 17.3: COUNT THE NUMBER OF WAYS TO TRAVERSE A 2D ARRAY)

    Write a function which accepts the number of rows and columns of a matrix, then returns the number of traversal
    paths from the top left to the bottom right of the matrix, where moves can either be down or right.

    Example:
        Input = 5, 5
        Output = 70

    Variations:
        - Solve the same problem using O(min(n, m)) space.
        - Solve the same problem in the presence of obstacles, specified by a Boolean 2D list, where the presence of a
          True value represents an obstacle.
        - A fisherman is in a rectangular sea.  The value of the fish at point (i, j), in the sea is specified by an
          n x m 2D list a.  Write a program that computes the maximum value of fish a fisherman can catch on a path from
          the upper leftmost point to the lower rightmost point.  The fisherman can only move down or right.
        - Solve the same problem when the fisherman can begin and end at any point.  He must still move down or right.
          Note that the value at (i, j) may be negative.
        - A decimal number is a sequence of digits, i.e., a sequence over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].  The sequence
          has to be of length 1 or more, and the first element in the sequence cannot be 0.  Call a decimal number d
          monotone if d[i] <= d[i+1], 0 <=i < abs(d).  Write a program which takes as in put a positive integer k and
          computes the number of decimal numbers of length k that are monotone.
        - Call a decimal number d, as defined above, strictly monotone if d[i] < d[i+1], 0 <= i < abs(d).  Write a
          program which takes as input a positive integer k and computes the number of decimal numbers of length k that
          are strictly monotone.
"""
import math


# Recursion/Brute Force Approach:  Using recursion, traverse all possible paths, return the sum of all paths.
# Time Complexity: O((n + m)!/(n! * m!)).
# Space Complexity: O(m + n).
def num_matrix_traversals_rec(n, m):

    def _num_matrix_traversals_rec(n, m, r, c):
        if r is n - 1 and c is m - 1:
            return 1
        goin_down = goin_right = 0
        if r + 1 < n:
            goin_down = _num_matrix_traversals_rec(n, m, r+1, c)
        if c + 1 < m:
            goin_right = _num_matrix_traversals_rec(n, m, r, c+1)
        return goin_down + goin_right

    if n is not None and m is not None and n > 0 and m > 0:
        return _num_matrix_traversals_rec(n, m, 0, 0)


# Memoization/Dynamic Programming Approach:  Use a cache to record the number of number of possible paths from each
# position in the matrix.   Consider the cache, memo, after computation for a 5x5 matrix:
#       [[1, 1,  1,  1,  1],
#        [1, 2,  3,  4,  5],
#        [1, 3,  6, 10, 15],
#        [1, 4, 10, 20, 35],
#        [1, 5, 15, 35, 70]]
# Time Complexity: O(n * m).
# Space Complexity: O(n * m).
def num_matrix_traversals_memo(n, m):
    if n is not None and m is not None and n > 0 and m > 0:
        memo = [[1 if c is 0 or r is 0 else 0 for c in range(m)] for r in range(n)]
        for r in range(1, n):
            for c in range(1, m):
                memo[r][c] = memo[r-1][c] + memo[r][c-1]
        return memo[-1][-1]


# Optimal Analytic Approach:  Fact (Bears, Beets, Battlestar Galactica); each path from (0, 0) to (n-1, m-1) is a
# sequence of m-1 horizontal steps and n-1 vertical steps.  There are (n+m-2 choose n-1) OR (n+m-2 choose m-1) OR
# (n+m-2)!/(n-1)!(m-1)! such paths.
# Time Complexity: O(1).
# Space Complexity: O(1).
def num_matrix_traversals(n, m):
    if n is not None and m is not None and n > 0 and m > 0:
        return math.factorial(n + m - 2) // (math.factorial(n - 1) * math.factorial(m - 1))


args = [(10, 10),
        (5, 5),
        (5, 4),
        (4, 5),
        (5, 1),
        (1, 4),
        (5, 0),
        (5, None)]
fns = [num_matrix_traversals_rec,
       num_matrix_traversals_memo,
       num_matrix_traversals]

for fn in fns:
    for r, c in args:
        print(f"{fn.__name__}({r}, {c}): {fn(r, c)}")
    print()


