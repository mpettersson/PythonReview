"""
    NUMBER OF NEGATIVE VALUES IN (A SORTED) MATRIX

    Given a non-raged matrix (list of lists) in ascending order, write a function that returns the number of negative
    integers in the matrix.

    Example:
        Input = [[-3, -2, -1, 1],
                 [-2,  2,  3, 4],
                 [ 4,  5,  7, 8]]
        Output = 4
"""


def num_neg_val_in_matrix(m):
    count = 0
    i = 0
    j = len(m[0]) - 1
    while j >= 0 and i < len(m):
        if m[i][j] < 0:
            count += (j + 1)
            i += 1
        else:
            j -= 1
    return count


lists = [[[-3, -2, -1, 1],
          [-2,  2,  3, 4],
          [ 4,  5,  7, 8]],
         [[-1, 0, 3]],
         [[-1, 0],
          [ 0, 1]],
         [[-5, -4, -3, -2],
          [-4, -3, -2, -1],
          [-3, -2, -1, 0]]]

for sl in lists:
    print(f"num_neg_val_in_matrix({sl}):", num_neg_val_in_matrix(sl))
