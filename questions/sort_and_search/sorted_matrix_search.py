"""
    SORTED MATRIX SEARCH (CCI 10.9)

    Given an MxN matrix in which each row and each column is sorted in ascending order, write a function to find an
    element.

    Example:
        Input = 105, [[15, 20,  40,  85],
                      [20, 35,  80,  95],
                      [30, 50,  95, 105],
                      [40, 55, 100, 120]]
        Output = 2, 3
"""


# Brute Force Approach:  Time complexity is O(rc), where r and c are the number of rows and columns in m.  Space
# complexity is O(1).
def sorted_matrix_search_bf(m, n):
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == n:
                return r, c


# Binary Search On Each List (Naive) Approach:  Time complexity is O(r * log(c)), where r and c are the number of rows
# and columns in m.  Space complexity is O(log(c)), where c is the number of columns in m.
def sorted_matrix_search_naive(m, n):

    def _binary_search(l, n):
        if l is not None and n is not None and len(l) > 0:
            lo = 0
            hi = len(l) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if l[mid] is n:
                    return mid
                if n < l[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

    if n is not None:
        for r in range(len(m)):
            c = _binary_search(m[r], n)
            if c is not None:
                return r, c


# Observations:
#   1) If the start of a col is greater than x; x is to the left.
#   2) If the end of a col is less than x; then x is to the right.
#   3) If the start of a row is greater than x; x is above.
#   4) If the end of a row is less than x; x is below.

# Iterative Solution:  Using observations 1 and 4 above, and starting at the top right of the matrix, iterate across the
# matrix looking for the element e.  Time complexity is O(r + c), where r and c are the number of rows and columns in
# the matrix.  Space complexity is O(1).
def sorted_matrix_search(m, e):
    if m is not None and e is not None and len(m) > 0:
        row = 0
        col = len(m[row]) - 1
        while row < len(m) and col >= 0:
            if m[row][col] is e:
                return row, col
            if m[row][col] > e:
                col -= 1
            else:
                row += 1


# Binary Search Observations:
# Similar to binary search on a list, we can perform a binary search on a sorted matrix.  However, be VERY careful,
# and it is suggested to break the code into smaller functions and even classes (see last solution).
# Like binary search, you will need to partition the matrix, HOWEVER, while the matrix has two dimensions, you will need
# to divide it into 4 quadrants. Consider the following matrix:
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
# than the largest value (35) of the top left matrix, then the element can ONLY be in the top left matrix.  Likewise,
# if the element is greater than the smallest element of the bottom right matrix, then the element can ONLY be in the
# bottom right matrix.  HOWEVER, if it isn't in either the top left OR the bottom right, (and it is in the range of our
# matrix) then we must search BOTH the bottom left AND the top right matrix.
#
# TLDR: Get a high ((2,2) or 95) and a low ((1,1) or 35) middle value then compare the search element to them.  If the
# search element is greater than the middle high value, it's in the high matrix, if it's lower than the middle low, it's
# in the low matrix.  Else, recurse on BOTH the other two matrices.


# Recursive Binary Matrix Search Approach:  Time and space complexity is O(log(r + c)), where r and c are the number of
# rows and columns in the matrix.
def sorted_matrix_search_rec(m, e):

    def _valid(m, r, c):
        return 0 <= r <= len(m)-1 and 0 <= c <= len(m[r])-1

    def _sorted_matrix_search_rec(m, e, lo_r, lo_c, hi_r, hi_c):
        if _valid(m, lo_r, lo_c) and _valid(m, hi_r, hi_c) and lo_r <= hi_r and lo_c <= hi_c:
            if m[lo_r][lo_c] == e:                              # Must check lo.
                return lo_r, lo_c
            if m[hi_r][hi_c] == e:                              # Must check high.
                return hi_r, hi_c
            if m[lo_r][lo_c] < e < m[hi_r][hi_c]:               # Only continue if e is in the range of the matrix.
                if (hi_r - lo_r + 1) * (hi_c - lo_c + 1) > 2:   # Only continue if lo to hi matrix has 2 or more values.
                    mi_hi_r = (lo_r + hi_r + 1) // 2            # Get the high mid indexes.
                    mi_hi_c = (lo_c + hi_c + 1) // 2
                    if m[mi_hi_r][mi_hi_c] == e:                # Check if e is in the range of the high matrix.
                        return mi_hi_r, mi_hi_c
                    elif m[mi_hi_r][mi_hi_c] < e:
                        return _sorted_matrix_search_rec(m, e, mi_hi_r, mi_hi_c, hi_r, hi_c)
                    mi_lo_r = mi_hi_r - 1 if lo_r != hi_r else mi_hi_r      # Get the next lower mid indexes.
                    mi_lo_c = mi_hi_c - 1 if lo_c != hi_c else mi_hi_c
                    if m[mi_lo_r][mi_lo_c] == e:                # Check if e is in the range of the low matrix.
                        return mi_lo_r, mi_lo_c
                    elif e < m[mi_lo_r][mi_lo_c]:
                        return _sorted_matrix_search_rec(m, e, lo_r, lo_c, mi_lo_r, mi_lo_c)
                    res = _sorted_matrix_search_rec(m, e, mi_hi_r, lo_c, hi_r, mi_lo_c)         # Try bottom left matrix
                    if res is None:
                        res = _sorted_matrix_search_rec(m, e, lo_r, mi_hi_c, mi_lo_r, hi_c)     # Try top right matrix.
                    return res

    if m is not None and e is not None and len(m) > 0:
        return _sorted_matrix_search_rec(m, e, 0, 0, len(m) - 1, len(m[0]) - 1)


# Recursive Binary Matrix Search With Coordinate Class Approach:  Time and space complexity is O(log(r + c)), where r
# and c are the number of  rows and columns in the matrix.
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


# Helper Function:
def format_matrix(m):
    return "\n" + '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m])


matrices = [[[10, 20, 40]],
            [[10],
             [20],
             [40]],
            [[15, 20,  40,  85],
             [20, 35,  80,  95],
             [30, 50,  95, 105],
             [40, 55, 100, 120]]]
vals = [-10, 10, 20, 40, 94, 95, None]
fns = [sorted_matrix_search_bf, sorted_matrix_search_naive, sorted_matrix_search_rec, sorted_matrix_search_w_coordinates]

for i, m in enumerate(matrices):
    print(f"m{i}:", format_matrix(m))
    print()
    for fn in fns:
        for v in vals:
            print(f"{fn.__name__}(m{i}, {v}): {fn(m, v)}")
        print()


