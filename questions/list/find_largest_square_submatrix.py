"""
    FIND LARGEST SQUARE SUBMATRIX (50CIQ 7: SQUARE SUBMATRIX,
                                   leetcode.com/problems/maximal-square)

    Given an MxN matrix of values and a value k, write a function to find and return the size of the largest square
    submatrix of all ks.

    Example:
        Input =  [[1, 1, 1, 0],[1, 1, 1, 1],[1, 1, 0, 0]], 1
        Output = 2

    Variations:
        - Find largest non-ragged (rectangular) submatrix.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Can I modify the given matrix?
#   - What are the possible matrix dimensions?
#   - Will the matrix consist of ragged or jagged lists?


# APPROACH: Naive Brute Force
#
# Iterate over all of the values in the matrix, when a value is found that matches k.  Once a match is found, starting
# at one, check for sum-matrices consisting of k values, terminating immediately if a non-k value is found.  Return the
# maximum size sub-matrix found.
#
# Time Complexity: O((r * c)**2), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(1)
def find_largest_square_submatrix_naive(m, k):

    def is_submatrix_homogeneous(m, row, col, size, k):
        if 0 <= row <= (row + size - 1) < len(m) and 0 <= col <= (col + size - 1) < len(m[row]):
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if m[r][c] != k:
                        return False
            return True
        return False

    if m is not None and k is not None:
        max_size = 0
        start_r = start_c = None
        for r in range(len(m)):
            for c in range(len(m[r])):
                if m[r][c] == k:
                    size = 1
                    while is_submatrix_homogeneous(m, r, c, size, k):
                        if size > max_size:
                            max_size = size
                            start_r, start_c = r, c
                        size += 1
        return max_size  # Could also return start row and column: return max_size, start_r, start_c


# APPROACH: Dynamic Programming
#
# This approach uses an additional matrix to track the size where the count is zero if the corresponding cell in the
# provided matrix doesn't equal the value, or the running (current) size submatrix to which it belongs. This is
# accomplished a single iteration (from matrix[0][0] to matrix[-1][-1]) over all of the values in the provided matrix,
# and checking a maximum of four cells (three from the new matrix) to identify the maximum size. Then, return the
# highest value from the tabulation matrix as the largest square submatrix.
#
# Essentially, each cell in the tabulation matrix:
#   tab[r][c] = min(tab[r-1][c-1], tab[r][c-1], tab[r-1][c]) + 1 if matrix[r][c] == k else 0
#
# Using the example matrix:
#   [[1, 1, 1, 0],
#    [1, 1, 1, 1],
#    [1, 1, 0, 0]]
#
# With a k value of 1, then the tabulation matrix would be:
#   [[1, 1, 1, 0],
#    [1, 2, 2, 1],
#    [1, 2, 0, 0]]
#
# Time Complexity: O(rc), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(rc), where r and c are the number of rows and columns in the matrix.
def find_largest_square_submatrix_dp(m, k):
    if m is not None and k is not None:
        tab = [[0 for _ in r] for r in m]
        max_size = 0
        start_r = start_c = None
        for r in range(len(m)):
            for c in range(len(m[r])):
                if m[r][c] == k:
                    tab[r][c] = 1 if r == 0 or c == 0 else min(tab[r-1][c-1], tab[r][c-1], tab[r-1][c]) + 1
                    if tab[r][c] > max_size:
                        max_size = tab[r][c]
                        start_r, start_c = r - max_size, c - max_size
        return max_size  # Could also return start row and column: return max_size, start_r, start_c


def format_matrix(m):
    try:
        w = max([len(str(e)) for r in m for e in r]) + 1
    except (ValueError, TypeError):
        return f"\n{None}"
    return m if not m else "\n" + '\n'.join([''.join([f'{e!r:{w}}' for e in r if len(r) > 0]) for r in m if len(m) > 0])


matrices = [[[-2, -2, -2, -2],
             [-2,  2,  2, -2],
             [-2,  2,  2,  1]],
            [[ 2, -2, -2, -2],
             [-2,  2,  2, -2],
             [-2,  2,  2,  1]],
            [[True, True, True],
             [True, True, True],
             [True, True, False]],
            [[1, 1, 1]],
            [[1, 1],
             [1, 1]],
            [[0, 0, 0, 0],
             [1, 0, 0, 0],
             [1, 0, 0, 0]],
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],
            [["b", "a", "a", "b"],
             ["a", "a", "a", "b"],
             ["c", "a", "a", "b"],
             ["a", "a", "a", "b"],
             ["c", "b", "b", "a"]]]
fns = [find_largest_square_submatrix_naive,
       find_largest_square_submatrix_dp]

for i, m in enumerate(matrices):
    print(f"matrices[{i}]:{format_matrix(m)}\n")
    for fn in fns:
        print(f"{fn.__name__}(matrices[{i}], {m[0][0]}):{fn(m, m[0][0])}")
    print()


