"""
    NUM SUBSETS WITH SUM K

    Given a list of integers and a value (k) write a function that returns the number of subsets with sum equal to k.

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
def num_subsets_with_sum_k_powerset(l, k):

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

    if l is not None and k is not None:
        count = 0
        ps = _power_set(l)
        for s in ps:
            if sum(s) is k:
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
def num_subsets_with_sum_k_itertools(l, k):
    if l is not None and k is not None:
        count = 0
        for r in range(len(l) + 1):
            for s in itertools.combinations(l, r):
                if sum(s) is k:
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
def num_subsets_with_sum_k_rec(l, k):

    def _num_subsets_with_sum_k_rec(l, k, i):
        if k == 0:
            return 1
        if k < 0 or i < 0:
            return 0
        if k < l[i]:
            return _num_subsets_with_sum_k_rec(l, k, i - 1)
        return _num_subsets_with_sum_k_rec(l, k - l[i], i - 1) + _num_subsets_with_sum_k_rec(l, k, i - 1)

    if l is not None and k is not None:
        return _num_subsets_with_sum_k_rec(l, k, len(l) - 1)


# APPROACH: Top Down Dynamic Programming
#
# NOTE: For memoization use a dictionary (as opposed to the traditional list/table)!
#
# TODO: DESCRIPTION
#
# Time Complexity: O(n * k), where n is the number of items in the list.
# Space Complexity: TODO
def num_subsets_with_sum_k_memo(l, k):

    def _num_subsets_with_sum_k_memo(l, k, i, memo):
        key = str(k) + ":" + str(i)
        if k == 0:
            return 1
        if k < 0 or i < 0:
            return 0
        if key in memo:
            return memo[key]
        if k < l[i]:
            memo[key] = _num_subsets_with_sum_k_memo(l, k, i - 1, memo)
            return memo[key]
        memo[key] = _num_subsets_with_sum_k_memo(l, k - l[i], i-1, memo) + _num_subsets_with_sum_k_memo(l, k, i-1, memo)
        return memo[key]

    if l is not None and k is not None:
        memo = {}
        return _num_subsets_with_sum_k_memo(l, k, len(l) - 1, memo)


args = [([2, 4, 6, 10], 16),
        ([10, 6, 4, 2], 16),
        ([2, 4, 6, 10], 0),
        ([1, 2, 4, 6, 8, 10, 12, 16, 22, 25, 99], 30)]
fns = [num_subsets_with_sum_k_itertools,
       num_subsets_with_sum_k_powerset,
       num_subsets_with_sum_k_rec,
       num_subsets_with_sum_k_memo]

for (l, k) in args:
    for fn in fns:
        print(f"{fn.__name__}({l}, {k}):", fn(l[:], k))
    print()


l = list(range(1, 18))
k = 42

print(f"l: {l}\nk: {k}")
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(s,k)", end="")
    fn(l[:], k)
    print(f" took {time.time() - t} seconds")


