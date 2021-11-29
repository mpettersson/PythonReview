"""
    FIND SUBLIST WITH MAX SUM

    Given a list of integers, find and return the sublist with the maximum sum.

    Example:
        Input = [904, 40, 523, 12, -335, -385, -124, 481, -31]
        Output = 1479
"""
import copy
from numbers import Number


# APPROACH: Naive Brute Force
#
# For any possible start and end point (where start point is less than or equal to the end point) calculate the sum,
# returning the largest sublist.
#
# Time Complexity: O(n**3), where n is the length of the list.
# Space Complexity: O(1).
def find_sublist_with_max_sum_naive(l):
    if isinstance(l, list) and len(l) > 0 and all(isinstance(n, Number) for n in l):
        max_sum = l[0]
        res_start = res_end = 0
        for i in range(len(l)):             # O(n)
            for j in range(i, len(l)):      # O(n)
                curr_sum = sum(l[i:j+1])    # O(n)
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    res_start = i
                    res_end = j
        return l[res_start:res_end+1], max_sum


# APPROACH: Divide & Conquer/Binary Search
#
# Recursively find, then return, the starting index, ending index, and max sum of the left half, right half, and middle
# of the list.
#
# Time Complexity: O(n log(n)), where n is the length of the list.
# Space Complexity: O(log(n)), where n is the length of the list.
#
# NOTE: The major difference to binary search is that the max sum might CROSS the middle; that case must be checked.
def find_sublist_with_max_sum_dc(l):

    def _find_middle_sublist_with_max_sum(l, lo, mid, hi):
        curr_left_sum = 0
        max_left_sum = l[mid]
        max_left_start = max_left_end = mid
        for i in range(mid, lo-1, -1):                      # START at middle, work towards low!
            curr_left_sum = curr_left_sum + l[i]
            if curr_left_sum > max_left_sum:
                max_left_sum = curr_left_sum
                max_left_start = i
        curr_right_sum = 0
        max_right_sum = l[mid+1]
        max_right_start = max_right_end = mid+1
        for i in range(mid+1, hi+1):
            curr_right_sum = curr_right_sum + l[i]
            if curr_right_sum > max_right_sum:
                max_right_sum = curr_right_sum
                max_right_end = i
        return max((max_left_start, max_right_end, max_left_sum + max_right_sum),
                   (max_left_start, max_left_end, max_left_sum),
                   (max_right_start, max_right_end, max_right_sum),
                   key=lambda x: x[2])

    def _find_sublist_with_max_sum(l, lo, hi):
        if lo == hi:
            return lo, hi, l[lo]
        mid = (lo + hi) // 2                                        # Return maximum of following three possible cases:
        return max(_find_sublist_with_max_sum(l, lo, mid),              # a) Maximum sublist sum in left half
                   _find_sublist_with_max_sum(l, mid+1, hi),            # b) Maximum sublist sum in right half
                   _find_middle_sublist_with_max_sum(l, lo, mid, hi),   # c) Maximum sublist crossing middle
                   key=lambda x: x[2])

    if isinstance(l, list) and len(l) > 0 and all(isinstance(n, Number) for n in l):
        result = _find_sublist_with_max_sum(l, 0, len(l)-1)
        return l[result[0]:result[1]+1], result[2]


# APPROACH: (Optimal) Dynamic Programming/Kadane's Algorithm
#
# Iterate over the list only once, maintaining the max sum at the current index and the overall max sum (result).
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(1).
def find_sublist_with_max_sum_dp(l):
    if isinstance(l, list) and len(l) > 0 and all(isinstance(n, Number) for n in l):
        res_sum = l[0]                      # res_sum = max sublist sum. (Don't forget to init with l[0]!)
        res_start = res_end = 0
        curr_sum = l[0]                     # curr_sum = max sublist sum ENDING at curr pos. (Also init with l[0]!)
        curr_start = 0
        for i in range(1, len(l)):
            if l[i] < (curr_sum + l[i]):    # NOTE:
                curr_sum = curr_sum + l[i]
            else:
                curr_sum = l[i]
                curr_start = i
            if res_sum < curr_sum:
                res_sum = curr_sum
                res_start = curr_start
                res_end = i
        return l[res_start:res_end+1], res_sum


args = [[904, 40, 523, 12, -335, -385, -124, 481, -31],
        [-2, -3, 4, -1, -2, 1, 5, -3],
        [-3, -3, -2, -2, -1, 1, 4, 5],
        [5, 4, 1, -1, -2, -2, -3, -3],
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [-1, 1, -1, 1, -1, 1, -1, 1, -1],
        [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6],
        [-2, -3, -4, -1, -2, -1, -5, -3],
        [-5, -4, -3, -3, -2, -2, -1, -1],
        [-1, -1, -2, -2, -3, -3, -4, -5],
        [22, 12, -4, -77, 75, -71, 4, -42, 42, -12, -61, -30, -92, -52, -35],
        [1],
        [0],
        [-1],
        [-2, -1],
        [1, 2],
        [7, 1, 5, 3, 6, 4],
        [1, 7, 4, 11],
        [0, 6, -3, 7],
        [0, 3],
        [3, 0],
        [3],
        [],
        None]
fns = [find_sublist_with_max_sum_naive,
       find_sublist_with_max_sum_dc,
       find_sublist_with_max_sum_dp]

for l in args:
    print(f"\nl: {l!r}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(copy.copy(l))}")
    print()


