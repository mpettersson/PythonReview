"""
    FIND MAX SUBLIST SUM (leetcode.com/problems/maximum-subarray/)

    Given a list of integers, find and return the maximum sum of all the sub-lists.

    Example:
        Input = [904, 40, 523, 12, -335, -385, -124, 481, -31]
        Output = 1479
"""


# Naive Brute Force Approach:  For any possible start and end point (where start point is less than or equal to the end
# point) calculate the sum, returning the largest sublist sum.
# Time Complexity: O(n**3), where n is the length of the list.
# Space Complexity: O(1).
#
# NOTE: The time complexity could be reduced to O(n**2) if the sum() was only called once in the outer (i) loop.
def find_max_sublist_sum_naive(l):
    if l is not None and len(l) > 0:
        max_sum = l[0]
        for i in range(1, len(l)):          # O(n)
            for j in range(len(l)):         # O(n)
                curr_sum = sum(l[j:j+i+1])  # O(n)
                if curr_sum > max_sum:
                    max_sum = curr_sum
        return max_sum


# Divide & Conquer/Binary Search Approach:  Recursively find, then return, the max sum of the left half, right half, and
# middle half of the list.
# Time Complexity: O(n log(n)), where n is the length of the list.
# Space Complexity: O(log(n)), where n is the length of the list.
#
# NOTE: The major difference to binary search is that the max sum might CROSS the middle; that case must be checked.
def find_max_sublist_sum_dc(l):

    def _find_max_midlist_sum(l, lo, mid, hi):
        curr_left_sum = 0
        max_left_sum = l[mid]
        for i in range(mid, lo-1, -1):                      # START at middle, work towards low!
            curr_left_sum = curr_left_sum + l[i]
            if curr_left_sum > max_left_sum:
                max_left_sum = curr_left_sum
        curr_right_sum = 0
        max_right_sum = l[mid+1]
        for i in range(mid+1, hi+1):
            curr_right_sum = curr_right_sum + l[i]
            if curr_right_sum > max_right_sum:
                max_right_sum = curr_right_sum
        return max(max_left_sum + max_right_sum, max_left_sum, max_right_sum)

    def _find_max_sublist_sum(l, lo, hi):
        if lo == hi:
            return l[lo]
        mid = (lo + hi) // 2                                # Return maximum of following three possible cases
        return max(_find_max_sublist_sum(l, lo, mid),        # a) Maximum sublist sum in left half
                   _find_max_sublist_sum(l, mid + 1, hi),    # b) Maximum sublist sum in right half
                   _find_max_midlist_sum(l, lo, mid, hi))    # c) Maximum sublist crossing middle

    if l is not None and len(l) > 0:
        return _find_max_sublist_sum(l, 0, len(l)-1)


# Optimal/Dynamic Programming Approach:  Iterate over the list only once, maintaining the max sum at the current index
# and the overall max sum (result).
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(1).
def find_max_sublist_sum(l):
    if l is not None and len(l) > 0:
        result = max_ending_here = l[0]
        for i in range(1, len(l)):
            max_ending_here = max(max_ending_here + l[i], l[i])
            result = max(result, max_ending_here)
        return result


args = [[904, 40, 523, 12, -335, -385, -124, 481, -31],
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [-1, 1, -1, 1, -1, 1, -1, 1, -1],
        [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6],
        [1],
        [0],
        [-1],
        [-2, -1],
        [1, 2],
        []]
fns = [find_max_sublist_sum_naive,
       find_max_sublist_sum_dc,
       find_max_sublist_sum]

for fn in fns:
    for l in args:
        print(f"{fn.__name__}({l}): {fn(l)}")
    print()


