"""
    FIND NON-ADJACENT MAX SUM (leetcode.com/problems/house-robber/)

    Given a list of integers, find and return the maximum sum of values from the list, where the summed values may not
    be adjacent to each other in the list.

    Example:
        Input = [2, 7, 9, 3, 1]
        Output = 12

    Variations:
        - Same question, however, consider the first and last item in the list as being adjacent.
"""


# Recursive Approach:  Recursively compare the values when the current item is, and is not, used.
# Time Complexity: O(2**n), where n is the number of elements in the list.
# Space Complexity: O(log(n)), where n is the number of elements in the list.
def find_non_adjacent_max_sum_rec(l):

    def _find_non_adjacent_max_sum_rec(l, i):
        if i >= len(l):
            return 0
        if i is len(l) - 1:
            return max(l[i], 0)
        with_curr = l[i] + _find_non_adjacent_max_sum_rec(l, i + 2)
        without_curr = _find_non_adjacent_max_sum_rec(l, i + 1)
        return max(with_curr, without_curr, 0)

    if l:
        return _find_non_adjacent_max_sum_rec(l, 0)
    return 0


# Memoization/Dynamic Programming Approach:  Similar to the recursive approach above, however, with a cache.
# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(n), where n is the number of elements in the list.
def find_non_adjacent_max_sum_memo(l):
    def _find_non_adjacent_max_sum_memo(l, i, cache):
        if i is len(l):
            return 0
        if i is len(l) - 1:
            return max(l[i], 0)
        if cache[i] is None:
            with_curr = l[i] + _find_non_adjacent_max_sum_memo(l, i + 2, cache)
            without_curr = _find_non_adjacent_max_sum_memo(l, i + 1, cache)
            cache[i] = max(with_curr, without_curr, 0)
        return cache[i]

    if l:
        cache = [None] * len(l)
        return _find_non_adjacent_max_sum_memo(l, 0, cache)
    return 0


# Optimal/Tabulation/Dynamic Programming Approach:  Maintain two sums, one with and one without the previous value, then
# for each value in the list, use a third variable to track the current max, and update the two sums (which will switch
# places with each other).  After a single iteration of the list, return the greater of the two sums.
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(1).
def find_non_adjacent_max_sum(l):
    if l:
        sum_with_prev = 0
        sum_without_prev = 0
        for curr_val in l:
            curr_max_sum = sum_without_prev if sum_without_prev > sum_with_prev else sum_with_prev
            sum_with_prev = sum_without_prev + curr_val
            sum_without_prev = curr_max_sum
        return sum_without_prev if sum_without_prev > sum_with_prev else sum_with_prev
    return 0


args = [[1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [955, 912, 660, 753, 924, 754, 748, 40, 445, 714],
        [29, 10, 65, 5, 60, 51, 58, 25, 6, 24, 54, 73, 63, 70, 38, 99, 7, 22, 27, 6],
        [904, 40, 523, 12, -335, -385, -124, 481, -31],
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [-1, 1, -1, 1, -1, 1, -1, 1, -1],
        [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6],
        [1],
        [0],
        [-1],
        [-2, -1],
        [1, 2],
        []]
fns = [find_non_adjacent_max_sum_rec,
       find_non_adjacent_max_sum_memo,
       find_non_adjacent_max_sum]

for fn in fns:
    for l in args:
        print(f"{fn.__name__}({l}): {fn(l)}")
    print()


