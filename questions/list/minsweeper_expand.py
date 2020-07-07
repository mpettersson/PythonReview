"""
    MINESWEEPER EXPAND



"""


def click(field, r, c):

    if field[r][c] != 0:
        return field
    num_rows = len(field)
    num_cols = len(field[0])
    queue = [[r, c]]
    while len(queue) > 0:
        curr_row, curr_col = queue.pop(0)
        for ri in range(curr_row - 1, curr_row + 2):
            for ci in range(curr_col - 1, curr_col + 2):
                if 0 <= ri < num_rows and 0 <= ci < num_cols and field[ri][ci] == 0:
                    queue.append([ri, ci])
                    field[ri][ci] = -2
    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

print(to_string(click(field1, 2, 2)))
# click(field1, 2, 2) should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

print(to_string(click(field1, 1, 4)))

# click(field1, 3, 5, 1, 4) should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

print(to_string(click(field2, 0, 1)))
# click(field2, 0, 1) should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

print(to_string(click(field2, 1, 3)))
# click(field2, 4, 4, 1, 3) should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]
