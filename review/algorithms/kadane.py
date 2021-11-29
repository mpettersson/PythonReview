"""
    KADANE'S ALGORITHM

    Kadane’s algorithm is an iterative dynamic programming algorithm to find the maximum sum contiguous subarray of a
    one-dimensional numeric list.

    Average Runtime:    O(n)
    Worst Runtime:      O(n)
    Best Runtime:       O(n)
    Space Complexity:   O(1)
    Alg Paradigm:       Dynamic Programming/Greedy
    Online:             YES      (can search a list as it receives it)

    References:
        - wikipedia.org/wiki/Maximum_subarray_problem

"""
import copy
from numbers import Number


# Maximum Sublist Sum Via Kadane's Algorithm
#
# NOTE: Initialize with the first list value (l[0]), as opposed to 0.  This is necessary to cover the case where ALL
#       list values are NEGATIVE (if all values were negative and 0 was used, then 0, would be returned, NOT a negative
#       sum).
#
# This approach simply maintains a result sum, and a current sublist sum, which are updated during a single iteration
# over the list values.  The current sublist sum is updated first, and then, if the result needs to be updated, it is
# updated second.
#
# Time Complexity: O(N)
# Space Complexity: O(1)
def max_sublist_sum_via_kadane(l):
    if isinstance(l, list) and len(l) > 0 and all(isinstance(n, Number) for n in l):
        result = l[0]                       # result = max sublist sum. (Don't forget to init with l[0]!)
        curr_sum = l[0]                     # curr_sum = max sublist sum ENDING at curr pos. (Also init with l[0]!)
        for i in range(1, len(l)):
            if l[i] < (curr_sum + l[i]):
                curr_sum = curr_sum + l[i]
            else:
                curr_sum = l[i]
            if result < curr_sum:
                result = curr_sum
        return result


# Find Sublist With Maximum Sum Via Kadane's Algorithm
#
# NOTE: Initialize with the first list value (l[0]), as opposed to 0.  This is necessary to cover the case where ALL
#       list values are NEGATIVE (if all values were negative and 0 was used, then 0, would be returned, NOT a negative
#       sum).
#
# This uses the same logic as above, with additional variables to store the start and ending indices of the sublists.
#
# Time Complexity: O(N)
# Space Complexity: O(1)
def sublist_with_max_sum_via_kadane(l):
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
fns = [max_sublist_sum_via_kadane,
       sublist_with_max_sum_via_kadane]

for l in args:
    print(f"l: {l!r}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(copy.copy(l))}")
    print()


