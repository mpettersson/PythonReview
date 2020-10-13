"""
    COMPUTE THE MAXIMUM WATER TRAPPED BY A PAIR OF VERTICAL LINES (EPI 18.7)

    A list of integers naturally defines a set of lines parallel to the Y-axis, starting from x=0.  The goal of this
    program is to find the pair of lines that together with the X-axis "trap" the most water.

    Write a program which takes as input an integer list and returns the pair of entries that trap the maximum amount of
    water.

    Consider the following:
                                            |
                                        |   |
        Max Water Line:         |---|---|---|-----------------------------------|
                            |   |   |   |   |           |       |               |
                    |       |   |   |   |   |   |       |       |   |       |   |
                 |  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
        List l: [1, 2,  1,  3,  4,  4,  5,  6,  2,  1,  3,  1,  3,  2,  1,  2,  4,  1]

    Example:
        Input = [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
        Output = (6, 4)

    Variations:
        - SEE: volume_of_histogram.py
        - SEE: largest_rectangle.py
"""


# Naive/Brute Force Approach: Time complexity is O(n**2), where n is the number of elements in the list.  Space
# complexity is O(1).
def get_max_trapped_water_naive(l):
    if l is not None and len(l) > 1:
        max_water = 0
        for i in range(1, len(l)):
            for j in range(i):
                curr_area = (i - j) * min(l[j], l[i])
                if curr_area > max_water:
                    max_water = curr_area
        return max_water


# NOTE: A divide and conquer approach would have the same time complexity of the naive/brute force approach because it
# would have to find the max on the left, right, and across the center (mid) of the list, that is:
#   T(left) = T(n/2)
#   T(right) = T(n/2)
#   T(mid) = O((n**2)/4)
# Therefore:
#   T(n) = 2T(n/2) + O((n**2)/4)
# Or:
#   T(n) = O(n**2)


# Optimal Approach:  Using two pointers (lo, hi) compare pairs, starting on the outside working in, maintaining the max
# area of the water.  Each iteration will advance one or both pointers towards the middle.  Time complexity is O(n),
# where n is the number of elements in the list.  Space complexity is O(1).
def get_max_trapped_water(l):
    if l is not None and len(l) > 1:
        lo = 0
        hi = len(l) - 1
        max_water = 0
        while lo < hi:
            max_water = max(max_water, (hi - lo) * min(l[lo], l[hi]))
            if l[lo] > l[hi]:
                hi -= 1
            elif l[lo] < l[hi]:
                lo += 1
            else:
                lo += 1
                hi -= 1
        return max_water


args = [[1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1],
        [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0],
        [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 8, 0, 2, 0, 5, 2, 0, 3, 0, 0],
        [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]]

for l in args:
    print(f"l: {l}")
    print(f"get_max_trapped_water_naive(l): {get_max_trapped_water_naive(l)}")
    print(f"get_max_trapped_water(l): {get_max_trapped_water(l)}")
    print()

