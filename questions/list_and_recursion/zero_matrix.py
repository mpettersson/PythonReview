"""
    ZERO MATRIX (CCI 1.8: ZERO MATRIX
                 50CIQ 6: ZERO MATRIX)

    Write a function that accepts an MxN matrix of 0's and 1's, and sets all values in a row/column containing 0 to 0.

    Example:
        Input =  [[1, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]]
        Output = [[1, 0, 1],
                  [0, 0, 0],
                  [1, 0, 1]]
"""
import copy


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Modify the given matrix, or return a new matrix?
#   - What dimensions will the matrix be?
#   - Will the matrix consist of ragged or jagged lists?


# NOTE: If you naively try to update values in a single iteration (without tracking changes for a second iteration) then
# the matrix will end up all zeros if a single zero originally existed.


# APPROACH: Naive Two Lists
#
# Use two lists to indicate the rows and columns that will be zeroed, iterate over over each row and column of the
# provided matrix updating the lists, then iterate over the provided matrix zeroing rows and columns according to the
# two lists.
#
# Time Complexity: O(r * c), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(r + c), where r and c are the number of rows and columns in the matrix.
def update_matrix_naive(m):
    if m and isinstance(m, list) and len(m) > 0 and isinstance(m[0], list) and len(m[0]) > 0:
        t = type(m[0][0])
        rows_to_update = []
        cols_to_update = []
        for r in range(len(m)):
            for c in range(len(m[r])):
                if not m[r][c]:
                    rows_to_update.append(r)
                    cols_to_update.append(c)
        for r in rows_to_update:
            for c in range(len(m[r])):
                if m[r][c]:
                    m[r][c] = t(False)
        for r in range(len(m)):
            for c in cols_to_update:
                if m[r][c]:
                    m[r][c] = t(False)
    return m


# APPROACH: Optimal Two Flags
#
# This approach is very similar to that above, however, the first row and column of the matrix will act as the lists,
# and a flag variable for the first row and first column will track if they need to be zeroed:  First create two flags
# and iterate over the first row and column, zeroing their corresponding flag if a zero exists, then use the first row
# and first column (as the lists in the first approach) to track what rows and columns need to be zeroed.  Then, iterate
# over the first row and column zeroing the respective columns and rows.  Finally, zero the first row and column
# according to the flag variables.
#
# Time Complexity: O(r * c), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(1).
def update_matrix(m):
    if m and isinstance(m, list) and len(m) > 0 and isinstance(m[0], list) and len(m[0]) > 0:
        t = type(m[0][0])
        has_false_in_row_0 = not all(m[0])
        has_false_in_col_0 = not all([r[0] for r in m])
        for r in range(1, len(m)):
            for c in range(1, len(m[r])):
                if not m[r][c]:
                    m[0][c] = m[r][0] = t(False)
        for r in range(1, len(m)):
            if not m[r][0]:
                for c in range(1, len(m[r])):
                    m[r][c] = t(False)
        for c in range(1, len(m[0])):
            if not m[0][c]:
                for r in range(1, len(m)):
                    m[r][c] = t(False)
        if has_false_in_row_0:
            for c in range(len(m[0])):
                m[0][c] = t(False)
        if has_false_in_col_0:
            for r in range(len(m)):
                m[r][0] = t(False)
    return m


def format_matrix(m):
    try:
        w = max([len(str(e)) for r in m for e in r]) + 1
    except (ValueError, TypeError):
        return f"\n{None}"
    return m if not m else "\n" + '\n'.join([''.join([f'{e!r:{w}}' for e in r if len(r) > 0]) for r in m if len(m) > 0])


matrices = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[False, False, False], [False, False, False], [False, False, False]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[True, True, True], [True, True, True], [True, True, True]],
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[True, True, True], [True, False, True], [True, True, True]],
            [[0, 1, 1], [1, 1, 1], [1, 1, 0]],
            [[False, True, True], [True, True, True], [True, True, False]],
            [[1, 1, 1], [1, 0, 1], [1, 1, 0]],
            [[True, True, True], [True, False, True], [True, True, False]],
            [[0, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[False, True, True], [True, True, True], [True, True, True]],
            [[0, 1, 1]],
            [[False, True, True]],
            [[0], [1], [1]],
            [[False], [True], [True]],
            [[1]],
            [[0]],
            [[]],
            [],
            None]
fns = [update_matrix_naive,
       update_matrix]

for i, m in enumerate(matrices):
    print(f"matrices[{i}]:{format_matrix(m)}\n")
    for fn in fns:
        print(f"{fn.__name__}(matrices[{i}]):{format_matrix(fn(copy.deepcopy(m)))}")
    print()


