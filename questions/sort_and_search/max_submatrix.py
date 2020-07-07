"""
    MAX SUBMATRIX

    Given an NxN matrix of positive and negative integers, write code to find the submatrix with the largest possible
    sum.
"""


# Approach 1: Brute Force, O(N**6) runtime (O(N**4) to iterate through all possible submatrix, then O(N**2) to compute
# the sum of that submatrix.
# NOTE: The runtime could be lowered to O(N**4) if the sum of each row/col was precomputed and stored (in val[][]). It
# could then be accessed via: val(x, y) = val(x-1, y) + val(y-1, x) - val(x-1, y-1) + matrix[x][y]
def max_submatrix_brute_force(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    best = None

    for row_one in range(0, row_count):
        for row_two in range(row_one, row_count):
            for col_one in range(0, col_count):
                for col_two in range(col_one, col_count):
                    m_sum = compute_sum(matrix, row_one, col_one, row_two, col_two)
                    if best is None or best.total < m_sum:
                        best = SubMatrix(row_one, col_one, row_two, col_two, m_sum)
    return best.total, best.row_one, best.col_one, best.row_two, best.col_two


def compute_sum(matrix, row_one, col_one, row_two, col_two):
    total = 0
    for r in range(row_one, row_two + 1):
        for c in range(col_one, col_two + 1):
            total += matrix[r][c]
    return total


class SubMatrix:
    def __init__(self, row_one, col_one, row_two, col_two, total):
        self.row_one = row_one
        self.col_one = col_one
        self.row_two = row_two
        self.col_two = col_two
        self.total = total


# Approach 2:  Optimized--This runtime is O(N**3) (or O(R**2C) where R is num of rows and C is num of columns).
# NOTE: This uses the same approach as in ContiguousSequences.py
def max_submatrix(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    best = None

    for row_start in range(row_count):
        partial_sum = [0] * col_count

        for row_end in range(row_start, row_count):
            for i in range(col_count):
                partial_sum[i] += matrix[row_end][i]
            best_range = max_subarray_range(partial_sum, col_count)
            if best is None or best.total < best_range.total:
                best = SubMatrix(row_start, best_range.start, row_end, best_range.end, best_range.total)
    return best.total, best.row_one, best.col_one, best.row_two, best.col_two


def max_subarray_range(array, n):
    best = None
    start = 0
    total = 0

    for i in range(n):
        total += array[i]
        if best is None or total > best.total:
            best = Range(start, i , total)

        if total < 0:
            start = i + 1
            total = 0
    return best


class Range:
    def __init__(self, start, end, total):
        self.start = start
        self.end = end
        self.total = total


matrix = [[-353, 463, 123, -222, 270, -172, 460, -244, 36, 112],
          [456, -148, 171, 369, -450, 192, 279, 58, -358, 279],
          [90, -288, -96, -244, -3, -67, 84, -97, 191, -50],
          [-134, -76, -169, 368, 74, 353, -268, -176, 50, -98],
          [-458, -477, 273, 211, 478, -4, -25, -327, 421, 424],
          [-462, -41, 272, -253, -466, -13, 106, -326, -422, -254],
          [218, 161, 225, 171, 471, -393, 55, 253, 162, 290],
          [-338, 50, -282, 123, -120, 125, 341, 294, -336, 229],
          [494, 304, -451, 28, -21, -253, -356, 224, 187, -24],
          [157, -427, 289, 299, 162, -251, 7, -398, -441, -323]]
print("matrix:", matrix)
print()

print("max_submatrix_brute_force(matrix):", max_submatrix_brute_force(matrix))
print("max_submatrix(matrix):", max_submatrix(matrix))

