"""
    ROTATE MATRIX NINETY DEGREES (CCI 1.7: ROTATE MATRIX)

    Write a function, which when given a matrix m, and a boolean ccw, rotates the matrix by 90 degrees in the
    counter-clockwise direction if ccw is True, or 90 degrees in the clockwise direction if ccw is False.

    For example, given the following 4x4, the following is a counter-clockwise rotation:

        [['00', '01', '02', '03'],           [['03', '13', '23', '33'],
         ['10', '11', '12', '13'],    -->     ['02', '12', '22', '32'],
         ['20', '21', '22', '23'],            ['01', '11', '21', '31'],
         ['30', '31', '32', '33']]            ['00', '10', '20', '33']]

    Alternatively, this is a clockwise rotation:

        [['00', '01', '02', '03'],           [['30', '20', '10', '00'],
         ['10', '11', '12', '13'],    -->     ['31', '21', '11', '01'],
         ['20', '21', '22', '23'],            ['32', '22', '12', '02'],
         ['30', '31', '32', '33']]            ['33', '23', '13', '03']]


    Example:
        Input =  [['00', '01'], ['10', '11']], False
        Output = [['10', '00'], ['11', '01']]

        Input =  [['00', '01'], ['10', '11']], True
        Output = [['01', '11'], ['00', '10']]

    NOTE: If the given matrix is square (NxN), and you are permitted to modify the matrix, it is unnecessary to use
          additional space.

    Variations of this question can include:
        - Rotate the elements by k places (rotate_matrix_k_places.py).
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Can I modify the given matrix?
#   - What direction should it rotate?
#   - What are the possible matrix dimensions?
#   - Will the matrix consist of ragged or jagged lists?


# APPROACH: Out-Of-Place
#
# NOTE: Since this approach does NOT modify the provided matrix, this approach can rotate non-square matrices.
#
# This approach first creates a list with an empty list for each of the columns, then simply iterates over the rows and
# columns of the provided matrix and appends, or inserts the values into their new positions.  Once done the new matrix
# is returned.
#
# Time Complexity: O(n ** 2), where n is the number of rows and columns in the matrix.
# Space Complexity: O(n ** 2) , where n is the number of rows and columns in the matrix.
def rotate_matrix_out_of_place(m, ccw=False):
    num_rows = len(m)
    num_cols = len(m[0])
    result = [[] for _ in range(num_cols)]
    if ccw:
        for row in range(num_rows):
            for col in range(num_cols):
                result[num_cols - 1 - col].append(m[row][col])
    else:
        for row in range(num_rows-1, -1, -1):
            for col in range(num_cols):
                result[col].append(m[row][col])
    return result


# APPROACH: Out-Of-Place
#
# NOTE: Since this approach does NOT modify the provided matrix, this approach can rotate non-square matrices.
#
# This approach is very similar to the first, however, this creates a full matrix with zero values, then iterates over
# the rows and columns, copying values to their new positions.  Once done the new matrix is returned.
#
# Time Complexity: O(n ** 2), where n is the number of rows and columns in the matrix.
# Space Complexity: O(n ** 2) , where n is the number of rows and columns in the matrix.
def rotate_matrix_out_of_place_alt(m, ccw=False):
    num_rows = len(m)
    num_cols = len(m[0])
    result = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
    if ccw:
        for row in range(num_rows):
            for col in range(num_cols):
                new_row, new_col = num_cols - 1 - col, row
                result[new_row][new_col] = m[row][col]
    else:
        for row in range(num_rows):
            for col in range(num_cols):
                new_row, new_col = col, num_rows - 1 - row
                result[new_row][new_col] = m[row][col]
    return result


# APPROACH: In-Place
#
# NOTE: Evidently, this approach does NOT work on non-square matrices.
#
# This approach iterates over the matrix 'layers', where a 'layer' is the set of elements at a uniform distance from the
# outside set (or all elements that do not have an element on their top/bottom/left/right).  For example, given the
# example above, there are two layers:
#
#         [['00', '01', '02', '03'],          [[1, 1, 1, 1],
#          ['10', '11', '12', '13'],           [1, 2, 2, 1],
#          ['20', '21', '22', '23'],           [1, 2, 2, 1],
#          ['30', '31', '32', '33']]           [1, 1, 1, 1],
#
# Since the matrix is square, iterating x times, where x is equal to the length of a side, and performing 4 swaps
# (during each iteratino) can update the full layer.  Initially, save the first element, then update the first element
# with the second, update the second with the third, etc, until the last (of the four) is assigned the temp value. After
# all of the 'layers' have been iterated over, the rotation is done (and the reference to the matrix is returned).
#
# Time Complexity: O(n ** 2), where n is the number of rows and columns in the matrix.
# Space Complexity: O(1).
def rotate_matrix_in_place(m, ccw=False):
    n = len(m)
    if n != len(m[0]):
        raise IndexError("Matrix is not square.")
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = m[first][i]                                       # TEMP =  TOP
            if ccw:
                m[first][i] = m[i][last]                            # TOP = RIGHT
                m[i][last] = m[last][last - offset]                 # RIGHT = BOTTOM
                m[last][last - offset] = m[last - offset][first]    # BOTTOM = LEFT
                m[last - offset][first] = top                       # LEFT = TEMP
            else:
                m[first][i] = m[last - offset][first]               # TOP = LEFT
                m[last - offset][first] = m[last][last - offset]    # LEFT = BOTTOM
                m[last][last - offset] = m[i][last]                 # BOTTOM = RIGHT
                m[i][last] = top                                    # RIGHT = TEMP
    return m


def format_matrix(m):
    w = max([len(str(e)) for r in m for e in r]) + 1
    return m if not m else '\t' + '\n\t'.join([''.join([f'{e:{w}}' for e in r if len(r) > 0]) for r in m if len(m) > 0])


matrices = [[['00', '01'],
             ['10', '11']],
            [['04', '14', '24', '34', '44', '54', '64', '74', '84', '94'],
             ['03', '13', '23', '33', '43', '53', '63', '73', '83', '93'],
             ['02', '12', '22', '32', '42', '52', '62', '72', '82', '92'],
             ['01', '11', '21', '31', '41', '51', '61', '71', '81', '91'],
             ['00', '10', '20', '30', '40', '50', '60', '70', '80', '90']],
            [['00', '01', '02', '03', '04'],
             ['10', '11', '12', '13', '14'],
             ['20', '21', '22', '23', '24'],
             ['30', '31', '32', '33', '34'],
             ['40', '41', '42', '43', '44'],
             ['50', '51', '52', '53', '54'],
             ['60', '61', '62', '63', '64'],
             ['70', '71', '72', '73', '74'],
             ['80', '81', '82', '83', '84'],
             ['90', '91', '92', '93', '94']],
            [['00', '01'],
             ['10', '11']],
            [['00', '01', '02'],
             ['10', '11', '12'],
             ['20', '21', '22']],
            [['00', '01', '02', '03'],
             ['10', '11', '12', '13'],
             ['20', '21', '22', '23'],
             ['30', '31', '32', '33']],
            [['00', '01', '02', '03', '04'],
             ['10', '11', '12', '13', '14'],
             ['20', '21', '22', '23', '24'],
             ['30', '31', '32', '33', '34'],
             ['40', '41', '42', '43', '44']]]
fns = [rotate_matrix_out_of_place,
       rotate_matrix_out_of_place_alt,
       rotate_matrix_in_place]

for matrix in matrices:
    for ccw in [False, True]:
        print(f"matrix:\n{format_matrix(matrix)}")
        for fn in fns:
            print(f"{fn.__name__}(matrix, ccw={ccw}):")
            try:
                print(f"{format_matrix(fn([r[:] for r in matrix], ccw))}")
            except IndexError as e:
                print(f"\t{e!r}")
        print()


