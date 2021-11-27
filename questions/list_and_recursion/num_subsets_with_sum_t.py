"""
    NUMBER OF SUBSETS (OR COMBINATIONS) WITH SUM T

    Given a list of integers and a target sum t, write a function that returns the number of subsets with a sum of t.

    Example:
        Input = [2, 4, 6, 10], 16
        Output = 2 (or the subsets {2, 4, 10} and {6, 10})
"""
import copy
import itertools
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Input Validation?
#   - Can there be repeating values?
#   - Can there be negative values?
#   - What if k is zero?


# APPROACH: Naive Via Power Set & Sum.
#
# TODO: DESCRIPTION
#
# Time Complexity: TODO
# Space Complexity: TODO
def num_subsets_with_sum_t_powerset(l, t):

    def _power_set(l):
        if l is not None:
            if len(l) == 0:
                return [set()]
            h = l.pop(0)
            t = _power_set(l)
            ht = copy.deepcopy(t)
            for s in ht:
                s.add(h)
            return t + ht

    if l is not None and t is not None:
        count = 0
        ps = _power_set(l)
        for s in ps:
            if sum(s) is t:
                count += 1
        return count


# APPROACH: Itertools Combinations
#
# This approach uses exactly the same logic as the power set approach above.  Despite the similar time complexities (as
# above), this approaches use of optimizations (including cpython) result in a much faster execution time (when compared
# to the function above).
#
# Time Complexity: TODO
# Space Complexity: TODO
def num_subsets_with_sum_t_itertools(l, t):
    if l is not None and t is not None:
        count = 0
        for r in range(len(l) + 1):
            for s in itertools.combinations(l, r):
                if sum(s) is t:
                    count += 1
        return count


# APPROACH: Via Recursion
#
# NOTE: This assumes that the list CONTAINS POSITIVE INTEGERS ONLY.
#
# TODO: DESCRIPTION
#
# Time Complexity: TODO
# Space Complexity: TODO
def num_subsets_with_sum_t_rec(l, t):

    def _rec(l, t, i):
        if t == 0:
            return 1
        if t < 0 or i < 0:
            return 0
        if t < l[i]:
            return _rec(l, t, i - 1)
        return _rec(l, t - l[i], i - 1) + _rec(l, t, i - 1)

    if l is not None and t is not None:
        return _rec(l, t, len(l) - 1)


# APPROACH: Top Down Dynamic Programming
#
# NOTE: For memoization use a dictionary (as opposed to the traditional list/table)!
#
# TODO: DESCRIPTION
#
# Time Complexity: O(n * t), where n is the number of items in the list.
# Space Complexity: TODO
def num_subsets_with_sum_t_top_down(l, t):

    def _rec(l, t, i, dp):
        key = str(t) + ":" + str(i)
        if t == 0:
            return 1
        if t < 0 or i < 0:
            return 0
        if key in dp:
            return dp[key]
        if t < l[i]:
            dp[key] = _rec(l, t, i - 1, dp)
            return dp[key]
        dp[key] = _rec(l, t - l[i], i-1, dp) + _rec(l, t, i-1, dp)
        return dp[key]

    if l is not None and t is not None:
        dp = {}
        return _rec(l, t, len(l) - 1, dp)


args = [([2, 4, 6, 10], 16),
        ([10, 6, 4, 2], 16),
        ([2, 4, 6, 10], 0),
        ([1, 2, 4, 6, 8, 10, 12, 16, 22, 25, 99], 30)]
fns = [num_subsets_with_sum_t_itertools,
       num_subsets_with_sum_t_powerset,
       num_subsets_with_sum_t_rec,
       num_subsets_with_sum_t_top_down]

for (l, t) in args:
    print(f"l: {l}\nt: {t}")
    for fn in fns:
        print(f"{fn.__name__}(l, t):", fn(l[:], t))
    print()


l = list(range(1, 18))
t = 42
print(f"l: {l}\nt: {t}")
for fn in fns:
    start = time.time()
    print(f"{fn.__name__}(s,t)", end="")
    fn(l[:], t)
    print(f" took {time.time() - start} seconds")


