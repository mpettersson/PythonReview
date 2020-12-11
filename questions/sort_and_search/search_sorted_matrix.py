"""
    SEARCH SORTED MATRIX (CCI 10.9: SORTED MATRIX SEARCH)

    Given an MxN matrix in which each row and each column is sorted in ascending order, write a function to find an
    element.

    Example:
        Input = 105, [[15, 20,  40,  85],
                      [20, 35,  80,  95],
                      [30, 50,  95, 105],
                      [40, 55, 100, 120]]
        Output = 2, 3

    Variations:
        - Same question, however, the first value of each row is greater than the last value on the previous row.
"""


# Brute Force Approach:  Iterate over all elements, looking for the provided value.
# Time Complexity: O(rc), where r and c are the number of rows and columns in m.
# Space Complexity: O(1).
def search_sorted_matrix_bf(mat, val):
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == val:
                return r, c


# Naive/Binary Search Each Row Approach:  Iteratively execute binary search on each row in the matrix.
# Time Complexity: O(r * log(c)), where r and c are the number of rows and columns in m.
# Space Complexity: O(log(c)), where c is the number of columns in m.
def search_sorted_matrix_naive(mat, val):

    def _binary_search(l, val):
        if l is not None and val is not None and len(l) > 0:
            lo = 0
            hi = len(l) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if l[mid] is val:
                    return mid
                if val < l[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

    if val is not None:
        for r in range(len(mat)):
            c = _binary_search(mat[r], val)
            if c is not None:
                return r, c


# Observations:
#   1) If the start of a col is greater than x; x is to the left.
#   2) If the end of a col is less than x; then x is to the right.
#   3) If the start of a row is greater than x; x is above.
#   4) If the end of a row is less than x; x is below.

# Saddleback Algorithm Solution:  Using observations 1 and 4 above, and starting at the top right of the matrix, iterate
# across the matrix looking for the element.
# Time Complexity: O(r + c), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(1).
def sorted_matrix_search_saddleback(mat, val):
    if mat is not None and val is not None and len(mat) > 0:
        row = 0
        col = len(mat[row]) - 1
        while row < len(mat) and col >= 0:
            if mat[row][col] is val:
                return row, col
            if mat[row][col] > val:
                col -= 1
            else:
                row += 1


# Binary Search Observations:
#
# NOTE: The performance for binary matrix search is NOT O(log(n*m)), it is O(s * log(l/s)) where s and l are the smaller
# and the larger of the two sides (m and n).
#
# SEE: https://stackoverflow.com/questions/2457792/how-do-i-search-for-a-number-in-a-2d-array-sorted-left-to-right-and-top-to-botto/2458113#answer-2458113
#
# Similar to binary search on a list, we can perform a binary search on a sorted matrix.  However, be VERY careful,
# and it is suggested to break the code into smaller functions and even classes (see last solution).
# Like binary search, you will need to partition the matrix, HOWEVER, while the matrix has two dimensions, you will need
# to divide it into 4 quadrants.  Consider the following matrix:
#           15  20  40  85
#           20  35  80  95
#           30  50  95  105
#           40  55  100 120
#
# Partitioning the matrix with middle row and column values, and applying the observations above, we can quickly narrow
# down our search for a given element.  For example, using a middle row and column value of 2, we could view the matrix
# above as the following matrices:
#       15  20          40  85
#       20  35          80  95
#
#       30  50          95  105
#       40  55          100 120
#
# Now we simply compare the top left and bottom right matrix to the element we are searching for; if the element is less
# than the largest value (35) of the top left matrix, then the element can ONLY be in the top left matrix.  If the
# element is less than the smallest value of the bottom right submatrix then BOTH the top right and bottom left
# sub-matrices need to be searched. If the element is larger than the smallest element of the bottom right submatrix,
# then ALL sub-matrices, except the top left, need to be searched.
#
# TLDR: Get a high ((2,2) or 95) and a low ((1,1) or 35) middle value then compare the search element to them.  If the
# search element is greater than the middle high value, it's in the high matrix, if it's lower than the middle low, it's
# in the low matrix.  Else, recurse on BOTH the other two matrices.


# Recursive Binary Matrix Search With Coordinate Class Approach:
# Time Complexity: O(s * log(l/s)) where s and l are the smaller and the larger of the two sides (m and n).
# Space Complexity: O(s * log(l/s)) where s and l are the smaller and the larger of the two sides (m and n).
def sorted_matrix_search_w_coordinates(m, e):

    def _partition_and_search(m, origin, dest, pivot, e):
        lower_left_origin = Coordinate(pivot.r, origin.c)
        lower_left_dest = Coordinate(dest.r, pivot.c - 1)
        upper_right_origin = Coordinate(origin.r, pivot.c)
        upper_right_dest = Coordinate(pivot.r - 1, dest.c)
        res = _sorted_matrix_search_w_coordinates(m, lower_left_origin, lower_left_dest, e)
        if res is None:
            return _sorted_matrix_search_w_coordinates(m, upper_right_origin, upper_right_dest, e)
        return res

    def _sorted_matrix_search_w_coordinates(m, origin, dest, e):
        if origin.is_in_matrix(m) and dest.is_in_matrix(m):
            if m[origin.r][origin.c] == e:
                return origin.r, origin.c
            if origin.is_before(dest):
                start = origin.clone()
                diag_dist = min(dest.r - origin.r, dest.c - origin.c)
                end = Coordinate(start.r + diag_dist, start.c + diag_dist)
                p = Coordinate(0, 0)
                while start.is_before(end):
                    p.set_to_avg(start, end)
                    if e > m[p.r][p.c]:
                        start.r = p.r + 1
                        start.c = p.c + 1
                    else:
                        end.r = p.r - 1
                        end.c = p.c - 1
                return _partition_and_search(m, origin, dest, start, e)

    if m is not None and e is not None and len(m) > 0:
        orig = Coordinate(0, 0)
        dest = Coordinate(len(m)-1, len(m[0])-1)
        return _sorted_matrix_search_w_coordinates(m, orig, dest, e)


class Coordinate:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def is_in_matrix(self, m):
        return 0 <= self.r <= len(m)-1 and 0 <= self.c <= len(m[0])-1

    def is_before(self, coordinate):
        return self.r <= coordinate.r and self.c <= coordinate.c

    def clone(self):
        return Coordinate(self.r, self.c)

    def set_to_avg(self, coordinate_a, coordinate_b):
        self.r = (coordinate_a.r + coordinate_b.r) // 2
        self.c = (coordinate_a.c + coordinate_b.c) // 2


# VARIATION:  Same question, however, the first value of each row is greater than the last value on the previous row.


# Variation Observations:
# This variation has an additional property (the first value of each row is greater than the last value of the previous
# row), thus allowing for a simple two way mapping of matrix <=> list.
#
# NxM Matrix to a List Mapping:
#       mat[r][c] => l[(r * m) + c], where m is the number of columns.
#
# List to NxM Matrix Mapping:
#       l[x] => mat[x / m][x % m], where m is the number of columns in the matrix.


# Iterative Binary Matrix Search Approach:  Using the mappings from Matrix <==> List from above, execute a binary search
# returning the row and column indices or None.
# Time Complexity: O(log(r * c)), where r and c are the number of rows and columns in the matrix.
# Space Complexity: O(log(r * c)), where r and c are the number of rows and columns in the matrix.
def bin_search_sorted_matrix_alt(mat, val):
    if mat is not None and val is not None and len(mat) > 0:
        num_cols = len(mat[0])
        lo = 0
        hi = num_cols * len(mat) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mat[mid // num_cols][mid % num_cols] < val:
                lo = mid + 1
            elif mat[mid // num_cols][mid % num_cols] > val:
                hi = mid - 1
            else:
                return mid // num_cols, mid % num_cols


def format_matrix(m):
    return "\n" + '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m])


matrices = [[[15, 20,  40,  85],
             [20, 35,  80,  95],
             [30, 50,  95, 105],
             [40, 55, 100, 120]],
            [[ 1,  4,  7, 11, 15],
             [ 2,  5,  8, 12, 19],
             [ 3,  6,  9, 16, 22],
             [10, 13, 14, 17, 24],
             [18, 20, 23, 26, 30]]]
alt_matrices = [[[10, 20, 40]],
                [[10],
                [20],
                [40]],
               [[ 1,  3,  5,  7],
                [10, 11, 16, 20],
                [23, 30, 34, 60]]]
vals = [-10, 10, 20, 40, 94, 95, None]
fns = [search_sorted_matrix_bf,
       search_sorted_matrix_naive,
       sorted_matrix_search_saddleback,
       sorted_matrix_search_w_coordinates]
alt_fns = [bin_search_sorted_matrix_alt]

for i, m in enumerate(matrices + alt_matrices):
    print(f"m{i}:", format_matrix(m))
    print()
    for fn in fns:
        for v in vals:
            print(f"{fn.__name__}(m{i}, {v}): {fn(m, v)}")
        print()

for i, m in enumerate(alt_matrices):
    print(f"m{i}:", format_matrix(m))
    print()
    for fn in alt_fns:
        for v in vals:
            print(f"{fn.__name__}(m{i}, {v}): {fn(m, v)}")
        print()


