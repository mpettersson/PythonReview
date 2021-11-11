"""
    NUM NEG VALUES IN SORTED MATRIX

    Given a non-raged matrix (list of lists) in ascending order, write a function that returns the number of negative
    integers in the matrix.

    Example:
        Input = [[-3, -2, -1, 1],
                 [-2,  2,  3, 4],
                 [ 4,  5,  7, 8]]
        Output = 4
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Sublist/Substring or Subsequence? (Don't get them confused!)
#   - What are the size limits of the list?
#   - Are the values negative & positive?
#   - Are there duplicate values in the list?
#   - The whole list can be a sublist?


# APPROACH: Naive/Brute Force
#
# This approach simply iterates over all of the values in the matrix, counting the number of times a negative value is
# encountered.  Once done, the count is returned as the result.
#
# Time Complexity: O(r * c), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(1).
def num_neg_values_in_sorted_matrix_bf(m):
    if isinstance(m, list) and isinstance(m[0], list):
        count = 0
        for r in range(len(m)):
            for c in range(len(m[r])):
                if m[r][c] < 0:
                    count += 1
        return count


# APPROACH: Naive/Brute Force
#
# This approach starts at the top right cell of the matrix and continues to move down or left by one for each iteration
# until the matrix has been covered.  Each cell (along the way) is checked for a negative value; if a negative value is
# found then the column count (plus one) is added to the result.  The result is returned at the end of the traversal.
#
# Time Complexity: O(r + c), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(1).
def num_neg_values_in_sorted_matrix(m):
    count = 0
    row = 0
    col = len(m[0]) - 1
    while col >= 0 and row < len(m):
        if m[row][col] < 0:
            count += (col + 1)
            row += 1
        else:
            col -= 1
    return count


def format_matrix(m):
    try:
        w = max([len(str(e)) for r in m for e in r]) + 1
    except (ValueError, TypeError):
        return f"\n{None}"
    return m if not m else '\t' + '\n\t'.join(
        [''.join([f'{e!r:{w}}' for e in r if len(r) > 0]) for r in m if len(m) > 0])


matrices = [[[-3, -2, -1, 1],
             [-2,  2,  3, 4],
             [ 4,  5,  7, 8]],
            [[-1, 0, 3]],
            [[-1, 0],
             [ 0, 1]],
            [[-5, -4, -3, -2],
             [-4, -3, -2, -1],
             [-3, -2, -1, 0]]]
fns = [num_neg_values_in_sorted_matrix_bf,
       num_neg_values_in_sorted_matrix]

for m in matrices:
    print("m:\n", format_matrix(m))
    for fn in fns:
        print(f"{fn.__name__}(m):", fn(m))
    print()


