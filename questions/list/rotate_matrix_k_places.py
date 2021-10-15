"""
    ROTATE MATRIX K PLACES (hackerrank.com/challenges/matrix-rotation-algo)

    Write a function, which when given a matrix m, an integer k, and a boolean ccw, then returns a the matrix with the
    elements rotated k positions in the counter-clockwise direction if ccw was True, or the clockwise direction if ccw
    was False.

    For example, one counter-clockwise rotation of a 4x5 matrix is:

        [['00', '01', '02', '03', '04'],           [['01', '02', '03', '04', '14'],
         ['10', '11', '12', '13', '14'],    -->     ['00', '12', '13', '23', '24'],
         ['20', '21', '22', '23', '24'],            ['10', '11', '21', '22', '34'],
         ['30', '31', '32', '33', '34']]            ['20', '30', '31', '32', '33']]

    And the clockwise rotation is:

        [['00', '01', '02', '03', '04'],           [['10', '00', '01', '02', '03'],
         ['10', '11', '12', '13', '14'],    -->     ['20', '21', '11', '12', '04'],
         ['20', '21', '22', '23', '24'],            ['30', '22', '23', '13', '14'],
         ['30', '31', '32', '33', '34']]            ['31', '32', '33', '34', '24']]

    In general, the counter-clockwise movement (for one rotation) is:

        m00  ←  m01  ←  m02  ←  m03  ←  m04
         ↓                               ↑
        m10     m11  ←  m12  ←  m13     m14
         ↓       ↓               ↑       ↑
        m20     m21  →  m22  →  m23     m24
         ↓                               ↑
        m30  →  m31  →  m32  →  m33  →  m34

    And the clockwise movement (for one rotation) is:

        m00  →  m01  →  m02  →  m03  →  m04
         ↑                               ↓
        m10     m11  →  m12  →  m13     m14
         ↑       ↑               ↓       ↓
        m20     m21  ←  m22  ←  m23     m24
         ↑                               ↓
        m30  ←  m31  ←  m32  ←  m33  ←  m34

    Example:
        input =  [['00', '01', '02', '03', '04'],
                  ['10', '11', '12', '13', '14'],
                  ['20', '21', '22', '23', '24'],
                  ['30', '31', '32', '33', '34']]
        output = [['01', '02', '03', '04', '14'],
                  ['00', '12', '13', '23', '24'],
                  ['10', '11', '21', '22', '34'],
                  ['20', '30', '31', '32', '33']]

    Variations:
        - Rotate the matrix 90 degrees (rotate_matrix_ninety_degrees.py).
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Can I modify the given matrix?
#   - What direction should it rotate?
#   - What are the possible matrix dimensions?
#   - Can the shorter side be odd/even?
#   - If the shorter side IS ODD, how should the middle row/col of the shorter side be handled?
#   - Will the matrix consist of ragged or jagged lists?


# APPROACH: Via Rotating 'Layers' Verbose
#
# This approach works on matrix 'layers', that is, all elements with a row or column value of zero are in 'layer 0', all
# elements that have a row, or column, value of 1 are in 'layer 1', etc...
# Iterative over each layer, this approach finds all of the elements the 'layer', starting at the top left point, then
# traversing the circumference of the 'layer', adding each of the elements to a temporary list.  Once the list of
# 'layer' elements has been created, it is shifted, or rotated, via a slice operation.  Finally, the shifted/rotated
# elements are inserted into the matrix, using the same traversal (that  first populated the list).  After all layers
# have been processed, the matrix is returned.
#
# NOTE: If the minimum of row length and column length is odd, then this question becomes very ambiguous (such as should
# the odd col/row cycle up/down/left/right, or not at all); to this end sometimes the question comes with the condition,
# or guarantee, that the minimum of the two sides will be even.
#
# This approach implemented a solution that treats the odd/single row/column as if it is the first of two rows/cols in
# an even/matched case.  That is, it rotates down (col), or it rotates left (row).
#
# Time Complexity: O(m * n), where m and n are the number of rows and columns in the matrix.
# Space Complexity: O(m + n), where m and n are the number of rows and columns in the matrix.
def rotate_matrix_k_places_verbose(matrix, k, ccw=False):
    if not(isinstance(matrix, list) and all([isinstance(e, list) for e in matrix]) and isinstance(k, int) and
           isinstance(ccw, bool)):
        raise ValueError("Invalid arguments...")
    if k == 0:
        return matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    num_layers = min(num_rows, num_cols) // 2
    for layer in range(num_layers):                 # CIRCULARLY Traverse ALL values in each circular 'layer'.
        temp = []                                   # This contains ALL the values of this layer (all 4 sides), read
        row = col = layer                           # in circularly, so they can easily be shifted.
        num_layer_rows = num_rows - layer
        num_layer_cols = num_cols - layer
        while row < num_layer_rows - 1:             # Add layer's LEFT COL, from TOP to BOTTOM (except the last
            temp.append(matrix[row][col])           # element, which will be included with the bottom row) to temp.
            row += 1
        while col < num_layer_cols - 1:             # Add layer's BOTTOM ROW, from LEFT to RIGHT (except the last
            temp.append(matrix[row][col])           # element, which will be included with the right row) to temp.
            col += 1
        while row > layer:                          # Add layer's RIGHT COL, from BOTTOM to TOP (except the last
            temp.append(matrix[row][col])           # element, which will be included with the top row) to temp.
            row -= 1
        while col > layer:                          # Add layer's TOP ROW, from RIGHT to LEFT (except the last
            temp.append(matrix[row][col])           # element, which was already added first) to temp.
            col -= 1
        if ccw:                                     # Shift the layer in a Counter-ClockWise (CCW) direction.
            temp = (temp[-(k % len(temp)):] +
                   temp[:-(k % len(temp))])
        else:                                       # Shift the layer in a ClockWise (CCW) direction.
            temp = (temp[k % len(temp):] +
                   temp[:k % len(temp)])
        i = 0
        row = col = layer                           # Reset row and col to the layer, so values can be replaced.
        while row < num_layer_rows - 1:
            matrix[row][col] = temp[i]              # Update LEFT COL of matrix (Top Down) from rotated/shifted list.
            row += 1
            i += 1
        while col < num_layer_cols - 1:
            matrix[row][col] = temp[i]              # Update BOTTOM ROW of matrix (L → R) from rotated/shifted list.
            col += 1
            i += 1
        while row > layer:
            matrix[row][col] = temp[i]              # Update RIGHT COL of matrix (Bottom Up) from rotated/shifted list.
            row -= 1
            i += 1
        while col > layer:
            matrix[row][col] = temp[i]              # Update TOP ROW of matrix (L ← R) from rotated/shifted list.
            col -= 1
            i += 1

    # OPTIONAL: This last if block is often not needed (if the min length side is even) for this question.
    if min(num_rows, num_cols) % 2 == 1:            # If the number of layers is ODD, update the odd/middle layer.
        start_row = start_col = num_layers
        if num_rows < num_cols:                     # Number of rows is ODD:
            end_col = num_cols - num_layers - 1
            h = matrix[start_row][:start_col]
            temp = matrix[start_row][start_col:end_col+1]
            t = matrix[start_row][end_col+1:]
            if ccw:                                 # If CCW rotate middle ROW DOWN (from TOP to BOTTOM).
                temp = (temp[k % len(temp):] +
                        temp[:k % len(temp)])
            else:                                   # If CW rotate middle ROW UP (from BOTTOM to TOP).
                temp = (temp[-(k % len(temp)):] +
                        temp[:-(k % len(temp))])
            matrix[start_row] = h + temp + t
        else:                                       # Number of cols is ODD:
            end_row = num_rows - num_layers - 1
            temp = [matrix[i][start_col] for i in range(start_row, end_row+1)]
            if ccw:                                 # If CCW rotate middle COL from LEFT to RIGHT.
                temp = (temp[k % len(temp):] +
                        temp[:k % len(temp)])
            else:                                   # If CW rotate middle COL from RIGHT to LEFT.
                temp = (temp[-(k % len(temp)):] +
                        temp[:-(k % len(temp))])
            for i in range(start_row, end_row+1):
                matrix[i][start_col] = temp.pop(0)
    return matrix


# APPROACH: Via Rotating 'Layers'
#
# This is the same approach as above, construct a list representing the traversal of a 'layer', then rotate the list,
# and update the matrix.  This approach, however, is much more succinct via a liberal use of list slices and list
# comprehensions.
#
# NOTE: If the minimum of row length and column length is odd, then this question becomes very ambiguous (such as should
# the odd col/row cycle up/down/left/right, or not at all); to this end sometimes the question comes with the condition,
# or guarantee, that the minimum of the two sides will be even.
#
# Time Complexity: O(m * n), where m and n are the number of rows and columns in the matrix.
# Space Complexity: O(m + n), where m and n are the number of rows and columns in the matrix.
def rotate_matrix_k_places(m, k, ccw=True):
    if not(isinstance(m, list) and all([isinstance(e, list) for e in m]) and isinstance(k, int) and isinstance(ccw, bool)):
        raise ValueError("Invalid arguments...")
    if k == 0:
        return m
    if not ccw:
        k *= -1
    num_rows = len(m)
    num_cols = len(m[0])
    num_layers = min(num_rows, num_cols) // 2

    for layer in range(num_layers):
        temp = []                                                           # temp = temp list for 'layer' elements.
        temp += m[layer][layer:num_cols-layer]                              # TOP:    LEFT → RIGHT
        temp += [m[r][-1-layer] for r in range(layer+1, num_rows-1-layer)]  # RIGHT:  TOP → BOTTOM
        temp += m[-1-layer][layer:num_cols-layer][::-1]                     # BOTTOM: RIGHT → LEFT
        temp += [m[r][layer] for r in range(num_rows-2-layer, layer, -1)]   # LEFT:   BOTTOM → TOP
        offset = k % len(temp)
        temp = temp[offset:] + temp[:offset]                                # Rotate this layer (temp list).
        i = 0
        for col in range(layer, num_cols-layer):                            # Update Matrix TOP:    LEFT → RIGHT
            m[layer][col] = temp[i]
            i += 1
        for row in range(layer+1, num_rows-1-layer):                        # Update Matrix RIGHT:  TOP → BOTTOM
            m[row][-1-layer] = temp[i]
            i += 1
        for col in range(num_cols-layer-1, layer-1, -1):                    # Update Matrix BOTTOM: RIGHT → LEFT
            m[-1-layer][col] = temp[i]
            i += 1
        for row in range(num_rows-2-layer, layer, -1):                      # Update Matrix LEFT:   BOTTOM → TOP
            m[row][layer] = temp[i]
            i += 1

    # OPTIONAL: This last if block is often not needed (if the min length side is even) for this question.
    if min(num_rows, num_cols) % 2 == 1:                                    # Check if there is an ODD ROW/COL.
        layer = min(num_rows, num_cols) // 2                                # ODD layer index (this was skipped above).
        temp = (m[layer][layer:num_cols-layer] if num_rows < num_cols else  # temp = the middle ROW or,
                [m[r][layer] for r in range(num_rows-1-layer, layer-1, -1)])    # the middle COL.
        offset = k % len(temp)
        temp = temp[offset:] + temp[:offset]                                # Rotate the temp list.
        i = 0
        if num_rows < num_cols:
            for col in range(layer, num_cols-layer):                        # Update middle ROW of ODD layer.
                m[layer][col] = temp[i]
                i += 1
        else:
            for row in range(num_rows-1-layer, layer-1, -1):                # Update middle COL of ODD layer.
                m[row][layer] = temp[i]
                i += 1
    return m


def format_matrix(m):
    w = max([len(str(e)) for r in m for e in r]) + 1
    return m if not m else '\t' + '\n\t'.join([''.join([f'{e:{w}}' for e in r if len(r) > 0]) for r in m if len(m) > 0])


matrices = [[['00', '01'],
             ['10', '11']],
            [['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'],
             ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19'],
             ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29'],
             ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39'],
             ['40', '41', '42', '43', '44', '45', '46', '47', '48', '49']],
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
k_vals = [-1, 1, 3, -3, 5, -5, 8]
fns = [rotate_matrix_k_places_verbose,
       rotate_matrix_k_places]

for matrix in matrices:
    for ccw in [True, False]:
        for fn in fns:
            print(f"\nmatrix:\n{format_matrix(matrix)}")
            for k in k_vals:
                print(f"{fn.__name__}(matrix, {k}, ccw={ccw}):")
                try:
                    print(f"{format_matrix(fn([r[:] for r in matrix], k, ccw))}")
                except (IndexError, ValueError) as e:
                    print(f"\t{e!r}")
        print()


