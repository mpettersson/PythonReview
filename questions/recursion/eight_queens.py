"""
    EIGHT QUEENS (CCI 8.12)

    Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them share the
    same row, column, or diagonal. In this case, "diagonal" means all diagonals, not just the two that bisect the board.
"""
import copy
grid_size = 8


def eight_queens_rec():
    results = []
    columns = [0] * 8
    _eight_queens_rec(0, columns, results)
    return results


def _eight_queens_rec(row, columns, results):
    global grid_size
    if row == grid_size:
        # Found valid placement
        results.append(copy.deepcopy(columns))
    else:
        col = 0
        while col < grid_size:
            if check_valid(columns, row, col):
                # Place Queen
                columns[row] = col
                _eight_queens_rec(row + 1, columns, results)
            col += 1


def check_valid(columns, row1, column1):
    row2 = 0
    while row2 < row1:
        column2 = columns[row2]

        # Check if (row2, column2) invalidates (row1, column1) as a queen spot

        # Check if rows have a queen in the same column
        if column1 == column2:
            return False

        # Check Diagonals:  If the distance between the columns equals the distance between the rows, then they're the
        # same diagonal.
        column_distance = abs(column2 - column1)
        # row1 > row2 so no need for abs
        row_distance = row1 - row2
        if column_distance == row_distance:
            return False
        row2 += 1
    return True


eight_queens = eight_queens_rec()
print(len(eight_queens))
print(eight_queens)

