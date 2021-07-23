"""
    FIND MATRIX PATH MAX PRODUCT (50CIQ 3: MATRIX PRODUCT)

    Write a function which accepts a matrix, then returns the maximum product of the path values, when starting at the
    top left and ending at the bottom right of the matrix.

    Consider the following 2d lists:
        [[1, 2, 3],     [[-1, 2, 3],
         [4, 5, 6],      [4, 5, -6],
         [7, 8, 9]]      [7, 8, 9]]

    Example:
        Input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Output = 2016  # or, 1 * 4 * 7 * 8 * 9

        Input = [[-1, 2, 3], [4, 5, -6], [7, 8, 9]]
        Output = 1080  # or, -1 * 4 * 5 * -6 * 9

    Variations:
        - Use subtraction as the operator (not multiplication).
"""
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - CAN THE VALUES BE NEGATIVE?
#   - What time/space complexity are you looking for?
#   - Does the matrix consist of ragged or jagged lists?


# (POSITIVE VALUES ONLY/WRONG IF NEG VALUES) APPROACH: Recursive
#
# This approach ONLY works if all values are POSITIVE; if there are some NEGATIVE values such as the second example
# above, then the result will be wrong. This is due to the order being reversed because of the recursion.
#
# Time Complexity: O((r + c)!/(r! * c!)), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(r + c), where r and c are the number of rows and columns in the matrix.
def find_matrix_product_for_positive_values_only_rec(m):

    def _rec(m, r, c):
        if r is len(m) - 1 and c is len(m[-1]) - 1:
            return m[r][c]
        if r + 1 is len(m):
            return m[r][c] * _rec(m, r, c+1)
        if c + 1 is len(m[r]):
            return m[r][c] * _rec(m, r+1, c)
        res_r = m[r][c] * _rec(m, r, c + 1)
        res_d = m[r][c] * _rec(m, r + 1, c)
        return max(res_r, res_d)

    if m and len(m) > 0 and len(m[0]) > 0:
        return _rec(m, 0, 0)


# APPROACH: Recursive
#
# This is essentially the same as the wrong solution above, however, this solution handles the possibility of NEGATIVE
# value.  This is accomplished by returning BOTH the minimum AND the maximum possible value for (or, if starting at)
# EACH cell.
#
# NOTE: Either direction (starting at the end and working towards beginning or starting at the beginning and working to
# the end) will work because we are using multiplication; we start at the end and work to the beginning to just check
# for index 0 (not len(m)-1).
#
# Time Complexity: O((r + c)!/(r! * c!)), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(r + c), where r and c are the number of rows and columns in the matrix.
def find_matrix_product_rec(m):

    def _rec(m, r, c):
        if r == 0 and c == 0:                                   # Last position.
            return m[r][c], m[r][c]
        if r == 0:                                              # Can only recurse left.
            res = _rec(m, r, c-1)
            return m[r][c] * res[0], m[r][c] * res[1]
        if c == 0:                                              # Can only recurse up.
            res = _rec(m, r-1, c)
            return m[r][c] * res[0], m[r][c] * res[1]
        res_l = _rec(m, r, c - 1)                               # Recurse up and recurse left.
        res_u = _rec(m, r - 1, c)
        res = [m[r][c] * res_l[0], m[r][c] * res_l[1], m[r][c] * res_u[0], m[r][c] * res_u[1]]  # LMin, LMax, RMin, RMax
        return min(res), max(res)

    if m and len(m) > 0 and len(m[0]) > 0:
        res_min, res_max = _rec(m, len(m)-1, len(m[-1])-1)
        return res_max


# APPROACH: Top Down Dynamic Programming With Memoization
#
# This approach is similar to the plain recursive approach above, however, a cache (that maintains the max and min
# values for each cell) has been added to reduce duplicate recursive calls.
#
# Time Complexity: O(r * c), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(r * c), where r and c are the number of rows and columns in the matrix.
def find_matrix_product_top_down_memo(m):

    def _rec(m, r, c):
        if r == 0 and c == 0:
            return m[r][c], m[r][c]
        if cache[r][c] is None:
            if r == 0:
                res = _rec(m, r, c-1)
                cache[r][c] = m[r][c] * res[0], m[r][c] * res[1]
            elif c == 0:
                res = _rec(m, r-1, c)
                cache[r][c] = m[r][c] * res[0], m[r][c] * res[1]
            else:
                res_l = _rec(m, r, c-1)
                res_u = _rec(m, r-1, c)
                res = [m[r][c] * res_l[0], m[r][c] * res_l[1], m[r][c] * res_u[0], m[r][c] * res_u[1]]
                cache[r][c] = min(res), max(res)
        return cache[r][c]

    if m and len(m) > 0 and len(m[0]) > 0:
        cache = [[None] * len(m[0]) for _ in range(len(m))]
        res_min, res_max = _rec(m, len(m)-1, len(m[-1])-1)
        return res_max


# APPROACH: Top Down Dynamic Programming With Memoization
#
# Fill a max and min cache starting at the top left and ending at the bottom right, then return the max cache's bottom
# right value.
#
# Time Complexity: O(r * c), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(r * c), where r and c are the number of rows and columns in the matrix.
def find_matrix_product_bottom_up_memo(m):
    min_cache = [[float('inf')] * len(m[0]) for _ in range(len(m))]
    max_cache = [[-float('inf')] * len(m[0]) for _ in range(len(m))]
    for r in range(len(m)):                                 # Iterate over Rows (No Recursion)
        for c in range(len(m[0])):                              # Iterate over Columns (No Recursion)
            if r == 0 and c == 0:                                   # Top Left
                max_cache[r][c] = min_cache[r][c] = m[r][c]
            if r > 0:                                               # All Non-First Rows
                max_cache[r][c] = max(m[r][c] * max_cache[r-1][c], m[r][c] * min_cache[r-1][c], max_cache[r][c])
                min_cache[r][c] = min(m[r][c] * max_cache[r-1][c], m[r][c] * min_cache[r-1][c], min_cache[r][c])
            if c > 0:                                               # All Non-First Cols
                max_cache[r][c] = max(m[r][c] * max_cache[r][c-1], m[r][c] * min_cache[r][c-1], max_cache[r][c])
                min_cache[r][c] = min(m[r][c] * max_cache[r][c-1], m[r][c] * min_cache[r][c-1], min_cache[r][c])
    return max_cache[-1][-1]


def format_matrix(m):
    return "\n" + '\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in m])


matrices = [[[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [[-1, 2, 3],
             [4, 5, -6],
             [7, 8, 9]],
            [[9, -6, 3],
             [8, 5, 2],
             [7, 4, -1]],
            [[-1, -2, -3],
             [-2, -3, -3],
             [-3, -3, -2]],
            [[-3, 3, 3, 3, 3, 3, 3, 1, 1, -3],
             [3, 3, 3, 3, 3, 3, 3, 1, 1, 1],
             [3, 3, 3, 3, 3, 3, 3, 1, 1, 1],
             [3, 3, 3, 3, 3, 3, 3, 1, 1, 1],
             [3, 3, 3, 3, 3, 3, 3, 1, 1, 33333],
             [3, 3, 3, 3, 3, 3, 3, 1, 1, 1],
             [3, 3, 3, 3, 3, 3, 3, 1, 1, 1],
             [3, 3, 3, 3, 3, 3, 3, 1, 1, 1],
             [3, 3, 3, 3, 3, 3, 3, 1, 1, 1],
             [3, 3, 3, 3, 3, 3, 3, 3, 3, -3]],
            [[1, -2, 1],
             [1, -2, 1],
             [3, -4, 1]],
            [[1, 2, 3, -4, 5]],
            [[1, 2, 3, 0, 5]],
            [[1],
             [2],
             [3]],
            [[1],
             [0],
             [3]],
            [[1, 1],
             [0, 1]]]
fns = [find_matrix_product_rec,
       find_matrix_product_top_down_memo,
       find_matrix_product_bottom_up_memo]

for matrix in matrices:
    print("matrix:", format_matrix(matrix))
    for fn in fns:
        print(f"{fn.__name__}(matrix): {fn(matrix)}")
    print()


print("matrix:", format_matrix(matrices[4]))
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(matrices[4]),", end="")
    result = fn(matrices[4])
    print(f" took {time.time() - t} seconds: {result}")


