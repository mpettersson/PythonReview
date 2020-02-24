"""
    ROTATE MATRIX (CCI 1.7)

    Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the
    image by 90 degrees.

    Example:
        Input =  [['00', '01'],
                  ['10', '11']]
        Output = [['10', '00'],
                  ['11', '01']]

    Can you do this in place?

    NOTE: It is unnecessary to use additional space.
"""
import copy


# The (best possible) runtime is O(n^2).
def rotate_matrix(original_matrix):
    m = copy.deepcopy(original_matrix)
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


m2 = [['00', '01'],
      ['10', '11']]
print(f"rotate_matrix({m2}):", rotate_matrix(m2), "\n")

m3 = [['00', '01', '02'],
      ['10', '11', '12'],
      ['20', '21', '22']]
print(f"rotate_matrix({m3}):", rotate_matrix(m3), "\n")

m4 = [['00', '01', '02', '03'],
      ['10', '11', '12', '13'],
      ['20', '21', '22', '23'],
      ['30', '31', '32', '33']]
print(f"rotate_matrix({m4}):", rotate_matrix(m4), "\n")

m5 = [['00', '01', '02', '03', '04'],
      ['10', '11', '12', '13', '14'],
      ['20', '21', '22', '23', '24'],
      ['30', '31', '32', '33', '34'],
      ['40', '41', '42', '43', '44']]
print(f"rotate_matrix({m5}):", rotate_matrix(m5))

