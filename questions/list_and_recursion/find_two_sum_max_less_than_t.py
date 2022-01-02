"""
    FIND TWO SUM MAX LESS THAN T (leetcode.com/problems/two-sum-less-than-k)

    Write a function, which accepts an integer list l and an integer target t, then returns the maximum sum of two
    unique elements from the list that is less than t.

    Example:
        Input = [34, 23, 1, 24, 75, 33, 54, 8], 60
        Output = 58
"""
import copy
from bisect import bisect_left


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Are the numbers in the list unique?
#   - Can there be duplicates numbers in a result set?
#   - Can there be duplicate pairs/sets in the result list?
#   - Can the list be modified?


# APPROACH: Naive/Brute Force
#
# Loop over every pair and add any that sum to t and are not the same value to the results.
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space complexity: O(1).
def find_two_sum_max_less_than_t_via_bf(l, t):
    if l is not None and t is not None:
        result = -1
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] < t:
                    result = max(result, l[i] + l[j])
        return result


# APPROACH: Via Binary Search
#
# Sort the list, then use binary search to find a complement (t - current) value, each time a result is found that is
# greater than the current result, and less than the target value, the result is updated.
#
# Time Complexity: O(n * log(n)), where n is the number of elements in the list.
# Space complexity: O(n) for the result list, where n is the number of elements in the list.
#
# NOTE: Although this approach has the same time complexity as the final approach, this solution is much slower.
def find_two_sum_max_less_than_t_via_bin_search(l, t):
    if l is not None and t is not None:
        result = -1
        l.sort()
        for i in range(len(l)):
            j = bisect_left(l, t-l[i], i+1) - 1
            if j > i:
                result = max(result, l[i] + l[j])
        return result


# APPROACH: (Optimal) Via Two Pointer
#
# Sort the list, then use a low and high pointer to unilaterally search for the maximum sum less than the target value.
#
# Time Complexity: O(n * log(n)), where n is the number of elements in the list.
# Space complexity: O(n) for the result list, where n is the number of elements in the list.
def find_two_sum_max_less_than_t_via_pointer(l, t):
    if l is not None and t is not None:
        result = -1
        l.sort()                                    # O(n * log(n)) to sort.
        lo = 0
        hi = len(l) - 1
        while lo < hi:
            temp = l[lo] + l[hi]
            if temp < t:
                result = max(result, temp)
                lo += 1
            else:
                hi -= 1
        return result


args = [([34, 23, 1, 24, 75, 33, 54, 8], 60),
        ([13, 0, 14, -2, -1, 7, 9, 5, 3, 6], 6),
        ([2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2], 2),
        ([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8], 0),
        ([-2, 1, 2, 4, 8, 11], 6),
        ([3], 6),
        ([2, 4], 6),
        ([2, 2], 4),
        ([2], 4),
        ([6], 6),
        ([-2, -1, 0, 3, 5, 6, 7, 9, 13, 14], 6),
        ([], 6),
        ([-2, 1, 2, 4, 7, 11], None),
        (None, 6),
        (None, None)]
fns = [find_two_sum_max_less_than_t_via_bf,
       find_two_sum_max_less_than_t_via_bin_search,
       find_two_sum_max_less_than_t_via_pointer]

for l, n in args:
    for fn in fns:
        print(f"{fn.__name__}({l}, {n}): {fn(copy.copy(l), n)}")
    print()


