"""
    FIND MAX AREA VERTICAL LINES (EPI 18.7: COMPUTE THE MAXIMUM WATER TRAPPED BY A PAIR OF VERTICAL LINES,
                                  leetcode.com/problems/container-with-most-water)

    Given a list of integers l, which define a set of lines all of which are perpendicular to the x-axis, each at x = i,
    where i is their index in the list; write a function that finds the the maximum area that can be formed from two
    lines.

    Consider the following:
                                            |
                                        |   |
                                |---|---|---|-----------------------------------|       <-- Max Area, or 'Water', Line
                            |   |   |   |   |           |       |               |
                    |       |   |   |   |   |   |       |       |   |       |   |
                 |  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
        List l: [1, 2,  1,  3,  4,  4,  5,  6,  2,  1,  3,  1,  3,  2,  1,  2,  4,  1]

    Example:
        Input = [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
        Output = 48

    Variations:
        - SEE: find_max_area_histogram.py
        - SEE: find_max_rectangle.py
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What values can the list contain (negative, floats, etc.)?
#   - What are the size limits of the list?
#   - Can you slant the container?
#   - What about the widths of the lines?


# APPROACH: Naive/Brute Force
#
# Compute the area for all possible starting and ending positions.  Return the maximum of all computations.
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space Complexity: O(1).
def find_max_area_vertical_lines_naive(l):
    if l is not None and len(l) > 1:
        result = 0
        for i in range(1, len(l)):
            for j in range(i):
                curr_area = (i - j) * min(l[j], l[i])
                if curr_area > result:
                    result = curr_area
        return result


# APPROACH (NOT IMPLEMENTED): Divide & Conquer
#
# A divide and conquer approach would have the same time complexity of the naive/brute force approach because it would
# have to find the max on the left, right, and across the center (mid) of the list, that is:
#   T(left) = T(n/2)
#   T(right) = T(n/2)
#   T(mid) = O((n**2)/4)
#
# Therefore:
#   T(n) = 2T(n/2) + O((n**2)/4)
#
# Or:
#   T(n) = O(n**2)
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space Complexity: Depends on implementation.


# APPROACH: Optimal Via Two Pointers
#
# Using two pointers (lo, hi) compare pairs, starting on the outside working in, maintaining the max area of the water.
# Each iteration will advance one or both pointers towards the middle.
#
# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(1).
def find_max_area_vertical_lines(l):
    if l is not None and len(l) > 1:
        lo = 0
        hi = len(l) - 1
        result = 0
        while lo < hi:
            result = max(result, (hi - lo) * min(l[lo], l[hi]))
            if l[lo] > l[hi]:
                hi -= 1
            elif l[lo] < l[hi]:
                lo += 1
            else:
                lo += 1
                hi -= 1
        return result


args = [[1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1],
        [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0],
        [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 8, 0, 2, 0, 5, 2, 0, 3, 0, 0],
        [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]]
fns = [find_max_area_vertical_lines_naive,
       find_max_area_vertical_lines]

for l in args:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l[:])}")
    print()


