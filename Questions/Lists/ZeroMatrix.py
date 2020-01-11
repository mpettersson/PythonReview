"""
    ZERO MATRIX

    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
"""


# NOTE: If you naively try to do this in one iteration it'll all end up zeros, so you have to go over it twice.
#       You can create a duplicate matrix, but that's not the most efficient way,
#       You can make two new list (X, Y) but that's still not the most efficient way,
#       Create two flags (row_has_zero and column_has_zero) then store if each row/column needs to be zeroed
#       out in the first row and first column.


def zero_matrix(mat):
    print(mat)
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
            print("x,y:", x, y)
            if mat[x][y] == 0:
                mat[x][0] = 0
                mat[0][y] = 0

    for x in range(1, len(mat[0])):
        if mat[x][0] == 0:
            nullifyRow(mat, x)

    for x in range(1, len(mat)):
        if mat[0][x] == 0:
            nullifyColumn(mat, x)

    if row_has_zero:
        nullifyRow(mat, 0)

    if column_has_zero:
        nullifyColumn(mat, 0)

    return mat


def nullifyRow(mat, row):
    for x in range(len(mat[row])):
        mat[row][x] = 0


def nullifyColumn(mat, column):
    for x in range(len(mat)):
        mat[x][column] = 0


mat = [[1, 0, 1],
       [1, 1, 1],
       [1, 1, 1]]

print(mat)
print(zero_matrix(mat))

