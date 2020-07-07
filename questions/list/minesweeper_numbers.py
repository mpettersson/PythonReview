"""
    MINESWEEPER NUMBERS

    Given an array of two digit lists, which represent the row and column where mines are located, the total number of
    rows, and the total number of columns, write a method that will produce a list of list with the number of mines next
    to each index (mines will be represented as -1).

    Example:
        Input = [[0, 0], [0, 1]], 3, 4)
        Output = [[-1, -1, 1, 0],
                  [ 2,  2, 1, 0],
                  [ 0,  0, 0, 0]]
"""


def minesweeper_numbers(bombs, num_rows, num_cols):
    matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    for [r, c] in bombs:
        matrix[r][c] = -1
        for ri in range(r - 1, r + 2):
            if 0 <= ri < num_rows:
                for ci in range(c - 1, c + 2):
                    if 0 <= ci < num_cols:
                        if matrix[ri][ci] >= 0:
                            matrix[ri][ci] += 1
    return matrix


print("minesweeper_numbers([[0, 0], [0, 1]], 3, 4):", minesweeper_numbers([[0, 0], [0, 1]], 3, 4))
print("minesweeper_numbers([[0, 2], [2, 0]], 3, 3):", minesweeper_numbers([[0, 2], [2, 0]], 3, 3))
print("minesweeper_numbers([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5):", minesweeper_numbers([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5))



