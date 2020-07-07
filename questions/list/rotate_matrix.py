"""
    ROTATE MATRIX (CCI 1.7)

    Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the
    image by 90 degrees.  Can you do this in place?

    Example:
        Input =  [['00', '01'],
                  ['10', '11']]
        Output = [['10', '00'],
                  ['11', '01']]

    NOTE: Given that the matrix is square (NxN), it is unnecessary to use additional space.

    Variations of this question can include:
        - Rotate a non-square (NxM) matrix.
        - Rotate counter clockwise.
"""


# Out-Of-Place Approach: Runtime and Space is O(NM).
# NOTE: Works on non-square (NxM) lists.
def rotate_matrix_out_of_place(m):
    m_rows = len(m)
    m_cols = len(m[0])
    rotated_m = [[0 for _ in range(m_rows)] for _ in range(m_cols)]
    for row in range(m_rows):
        for col in range(m_cols):
            new_row, new_col = col, m_rows - 1 - row
            rotated_m[new_row][new_col] = m[row][col]
    return rotated_m


# In-Place Approach: The (best possible) runtime is O(n^2).
# NOTE: Does NOT work on non-square (NxM) lists.
def rotate_matrix_in_place(m):
    n = len(m)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = m[first][i]                                   # Save Top
            m[first][i] = m[last - offset][first]               # Left   --> Top
            m[last - offset][first] = m[last][last - offset]    # Bottom --> Left
            m[last][last - offset] = m[i][last]                 # Right  --> Bottom
            m[i][last] = top                                    # Top    --> Right
    return m


def format_matrix(m):
    return "\n" + '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m])


m0 = [['00', '01'],
      ['10', '11']]
print("m0:", format_matrix(m0))
print(f"rotate_matrix_out_of_place(m0):", format_matrix(rotate_matrix_out_of_place(m0)), "\n")

m1 = [['00', '01', '02', '03', '04'],
      ['10', '11', '12', '13', '14'],
      ['20', '21', '22', '23', '24'],
      ['30', '31', '32', '33', '34'],
      ['40', '41', '42', '43', '44'],
      ['50', '51', '52', '53', '54'],
      ['60', '61', '62', '63', '64'],
      ['70', '71', '72', '73', '74'],
      ['80', '81', '82', '83', '84'],
      ['90', '91', '92', '93', '94']]
print("m1:", format_matrix(m1))
print(f"rotate_matrix_out_of_place(m1):", format_matrix(rotate_matrix_out_of_place(m1)), "\n")

m2 = [['00', '01'],
      ['10', '11']]
print("m2:", format_matrix(m2))
print(f"rotate_matrix_in_place(m2):", format_matrix(rotate_matrix_in_place(m2)), "\n")

m3 = [['00', '01', '02'],
      ['10', '11', '12'],
      ['20', '21', '22']]
print("m3:", format_matrix(m3))
print(f"rotate_matrix_in_place(m3):", format_matrix(rotate_matrix_in_place(m3)), "\n")

m4 = [['00', '01', '02', '03'],
      ['10', '11', '12', '13'],
      ['20', '21', '22', '23'],
      ['30', '31', '32', '33']]
print("m4:", format_matrix(m4))
print(f"rotate_matrix_in_place(m4):", format_matrix(rotate_matrix_in_place(m4)), "\n")

m5 = [['00', '01', '02', '03', '04'],
      ['10', '11', '12', '13', '14'],
      ['20', '21', '22', '23', '24'],
      ['30', '31', '32', '33', '34'],
      ['40', '41', '42', '43', '44']]
print("m5:", format_matrix(m5))
print(f"rotate_matrix_in_place(m5):", format_matrix(rotate_matrix_in_place(m5)), "\n")




