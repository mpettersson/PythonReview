"""
    FIND MATRIX PATH MAX PRODUCT (50CIQ 3: MATRIX PRODUCT)

    Write a function which accepts a matrix, then returns the maximum path values product, when starting at the top left
    and ending at the bottom right of the matrix (with o

    Consider the following 2d lists:
        [[1, 2, 3],     [[-1, 2, 3],
         [4, 5, 6],      [4, 5, -6],
         [7, 8, 9]]      [7, 8, 9]]

    Example:
        Input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Output = 2016  # or, 1 * 4 * 7 * 8 * 9

        Input = [[-1, 2, 3], [4, 5, -6], [7, 8, 9]]
        Output = 1080  # or, -1 * 4 * 5 * -6 * 9
"""


# Wrong Approach: This approach ONLY works if all values are positive; if there are some negative values such as the
# second example above, then the result will be wrong. This is due to the order being reversed because of the recursion.
# Time Complexity: O((r + c)!/(r! * c!)), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(r + c), where r and c are the number of rows and columns in the matrix.
def matrix_product_rec_wrong(m):

    def _matrix_product_rec_wrong(m, r, c):
        if r is len(m) - 1 and c is len(m[-1]) - 1:
            return m[r][c]
        if r + 1 is len(m):
            return m[r][c] * _matrix_product_rec_wrong(m, r, c+1)
        if c + 1 is len(m[r]):
            return m[r][c] * _matrix_product_rec_wrong(m, r+1, c)
        res_r = m[r][c] * _matrix_product_rec_wrong(m, r, c + 1)
        res_d = m[r][c] * _matrix_product_rec_wrong(m, r + 1, c)
        return max(res_r, res_d)

    if m and len(m) > 0 and len(m[0]) > 0:
        return _matrix_product_rec_wrong(m, 0, 0)


# Recursive Approach:  START at the END and recurse backwards to the starting location, returning either the minimum of
# two negative values OR the maximum of two positive, or one positive and one negative value, along the way.
# Time Complexity: O((r + c)!/(r! * c!)), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(r + c), where r and c are the number of rows and columns in the matrix.
def matrix_product_rec(m):

    def _matrix_product_rec(m, r, c):
        if r is 0 and c is 0:
            return m[r][c]
        if r - 1 < 0:
            return m[r][c] * _matrix_product_rec(m, r, c-1)
        if c - 1 < 0:
            return m[r][c] * _matrix_product_rec(m, r-1, c)
        l_res = _matrix_product_rec(m, r, c-1)
        u_res = _matrix_product_rec(m, r-1, c)
        if l_res < 0 and u_res < 0:
            return m[r][c] * min(l_res, u_res)
        return m[r][c] * max(l_res, u_res)

    if m and len(m) > 0 and len(m[0]) > 0:
        return _matrix_product_rec(m, len(m)-1, len(m[-1])-1)


# Memoization/Dynamic Programming Approach:  This approach is similar to the regular recursive approach above, however,
# a cache has been added to reduce duplicate recursive calls.
# Time Complexity: O(r * c), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(r * c), where r and c are the number of rows and columns in the matrix.
def matrix_product_memo(m):
    if m and len(m) > 0 and len(m[0]) > 0:
        memo = [[1 for _ in c] for c in m]
        for r in range(len(m)):
            for c in range(len(m[r])):
                if r is 0 and c is 0:
                    memo[r][c] = m[r][c]
                elif r - 1 < 0:
                    memo[r][c] = memo[r][c-1] * m[r][c]
                elif c - 1 < 0:
                    memo[r][c] = memo[r-1][c] * m[r][c]
                else:
                    if memo[r-1][c] < 0 and memo[r][c-1] < 0:
                        memo[r][c] = m[r][c] * min(memo[r-1][c], memo[r][c-1])
                    else:
                        memo[r][c] = m[r][c] * max(memo[r-1][c], memo[r][c-1])
        return memo[-1][-1]


def format_matrix(m):
    return "\n" + '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m])


matrices = [[[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [[-1, 2, 3],
             [4, 5, -6],
             [7, 8, 9]],
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
fns = [matrix_product_rec_wrong,
       matrix_product_rec,
       matrix_product_memo]

for matrix in matrices:
    print("matrix:", format_matrix(matrix))
    for fn in fns:
        print(f"{fn.__name__}(matrix): {fn(matrix)}")
    print()


