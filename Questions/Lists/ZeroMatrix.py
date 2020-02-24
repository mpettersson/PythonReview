"""
    ZERO MATRIX (CCI 1.8)

    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.

    NOTE: If you naively try to do this in one iteration it'll all end up zeros, so you have to go over it twice.
          You can create a duplicate matrix, but that's not the most efficient way. You can make two new list (X, Y) but
          that's still not the most efficient way; create two flags (row_has_zero and column_has_zero) then store if
          each row/column needs to be zeroed out in the first row and first column.
"""


def zero_matrix(mat):
    row_has_zero = False
    column_has_zero = False

    for x in range(len(mat[0])):
        if mat[0][x] == 0:
            row_has_zero = True
            break

    for x in range(len(mat)):
        if mat[x][0] == 0:
            column_has_zero = True
            break

    for x in range(1, len(mat[0])):
        for y in range(1, len(mat)):
            if mat[x][y] == 0:
                mat[x][0] = 0
                mat[0][y] = 0

    for x in range(1, len(mat[0])):
        if mat[x][0] == 0:
            nullify_row(mat, x)

    for x in range(1, len(mat)):
        if mat[0][x] == 0:
            nullify_column(mat, x)

    if row_has_zero:
        nullify_row(mat, 0)

    if column_has_zero:
        nullify_column(mat, 0)

    return mat


def nullify_row(mat, row):
    for x in range(len(mat[row])):
        mat[row][x] = 0


def nullify_column(mat, column):
    for x in range(len(mat)):
        mat[x][column] = 0


m0 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
print("m0:", m0)
print("zero_matrix(m0):", zero_matrix(m0))
print()

m1 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]
print("m1:", m1)
print("zero_matrix(m1):", zero_matrix(m1))
print()

m2 = [[1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]]
print("m2:", m2)
print("zero_matrix(m2):", zero_matrix(m2))
print()

m3 = [[0, 1, 1],
      [1, 1, 1],
      [1, 1, 0]]
print("m3:", m3)
print("zero_matrix(m3):", zero_matrix(m3))
print()

m4 = [[1, 1, 1],
      [1, 0, 1],
      [1, 1, 0]]
print("m4:", m4)
print("zero_matrix(m4):", zero_matrix(m4))
print()
