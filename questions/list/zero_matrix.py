"""
    ZERO MATRIX (CCI 1.8)

    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.

    Example:
        Input =  [[1, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]]
        Output = [[1, 0, 1],
                  [0, 0, 0],
                  [1, 0, 1]]

    NOTE: If you naively try to do this in one iteration it'll all end up zeros, so you have to go over it twice.
          You can create a duplicate matrix, but that's not the most efficient way. You can make two new list (X, Y) but
          that's still not the most efficient way; create two flags (row_has_zero and column_has_zero) then store if
          each row/column needs to be zeroed out in the first row and first column.
"""


def zero_matrix(m):
    if not m or len(m) is 0 or not m[0] or len(m[0]) is 0:
        return None
    num_row = len(m)
    num_col = len(m[0])
    top_has_zero = False
    left_has_zero = False
    for c in range(num_col):
        if m[0][c] == 0:
            top_has_zero = True
            break
    for r in range(num_row):
        if m[r][0] == 0:
            left_has_zero = True
            break
    for r in range(1, num_row):
        for c in range(1, num_col):
            if m[r][c] == 0:
                m[r][0] = 0
                m[0][c] = 0
    for r in range(1, num_row):
        if m[r][0] == 0:
            nullify_row(m, r)
    for c in range(1, num_col):
        if m[0][c] == 0:
            nullify_col(m, c)
    if top_has_zero:
        nullify_row(m, 0)
    if left_has_zero:
        nullify_col(m, 0)
    return m


def nullify_row(m, row):
    for c in range(len(m[row])):
        m[row][c] = 0


def nullify_col(m, col):
    for r in range(len(m)):
        m[r][col] = 0


def format_matrix(m):
    return m if not m else "\n" + '\n'.join([''.join(['{:4}'.format(item) for item in row if len(row) > 0]) for row in m if len(m) > 0])


m0 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
print("m0:", format_matrix(m0))
print("zero_matrix(m0):", format_matrix(zero_matrix(m0)), "\n")

m1 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]
print("m1:", format_matrix(m1))
print("zero_matrix(m1):", format_matrix(zero_matrix(m1)), "\n")

m2 = [[1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]]
print("m2:", format_matrix(m2))
print("zero_matrix(m2):", format_matrix(zero_matrix(m2)), "\n")

m3 = [[0, 1, 1],
      [1, 1, 1],
      [1, 1, 0]]
print("m3:", format_matrix(m3))
print("zero_matrix(m3):", format_matrix(zero_matrix(m3)), "\n")

m4 = [[1, 1, 1],
      [1, 0, 1],
      [1, 1, 0]]
print("m4:", format_matrix(m4))
print("zero_matrix(m4):", format_matrix(zero_matrix(m4)), "\n")

m5 = [[0, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]
print("m5:", format_matrix(m5))
print("zero_matrix(m5):", format_matrix(zero_matrix(m5)), "\n")

m6 = [[0, 1, 1]]
print("m6:", format_matrix(m6))
print("zero_matrix(m6):", format_matrix(zero_matrix(m6)), "\n")

m7 = [[0],
      [1],
      [1]]
print("m7:", format_matrix(m7))
print("zero_matrix(m7):", format_matrix(zero_matrix(m7)), "\n")

m8 = [[1]]
print("m8:", format_matrix(m8))
print("zero_matrix(m8):", format_matrix(zero_matrix(m8)), "\n")

m9 = [[0]]
print("m9:", format_matrix(m9))
print("zero_matrix(m9):", format_matrix(zero_matrix(m9)), "\n")

m10 = [[]]
print("m10:", format_matrix(m10))
print("zero_matrix(m10):", format_matrix(zero_matrix(m10)), "\n")

m11 = []
print("m11:", format_matrix(m11))
print("zero_matrix(m11):", format_matrix(zero_matrix(m11)), "\n")

m12 = None
print("m12:", format_matrix(m12))
print("zero_matrix(m12):", format_matrix(zero_matrix(m12)), "\n")

