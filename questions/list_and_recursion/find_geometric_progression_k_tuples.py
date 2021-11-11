"""
    NUM GEOMETRIC PROGRESSION K TUPLES

    Write a function, which accepts a list l, a (common) ratio r, and a number of indices k, then find and return all
    sets indices, of size k, such that the elements at those indices are in geometric progression for the provided
    common ratio.

    Wikipedia's definition of a geometric progression (SEE: wikipedia.org/wiki/Geometric_progression):

        "In mathematics, a geometric progression, also known as a geometric sequence, is a sequence of non-zero numbers
         where each term after the first is found by multiplying the previous one by a fixed, non-zero number called the
         common ratio. For example, the sequence 2, 6, 18, 54, ... is a geometric progression with common ratio 3.
         Similarly 10, 5, 2.5, 1.25, ... is a geometric sequence with common ratio 1/2."

    Example:
        Input = [1, 4, 16, 64], 4, 3
        Output = [[0, 1, 2], [1, 2, 3]] # Or, the values [1,4,16] and [4, 16, 64].
"""
from collections import defaultdict
from itertools import combinations


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Return value (number of sets, list of indices, list of values)?
#   - What are the size limits of the list?
#   - Are the values negative & positive?
#   - Are there duplicate values in the list?
#   - Is the list sorted?


# APPROACH: Naive/Brute Force
#
# This approach uses itertools' combinations to produce all k sized combinations of indices, then checks if the values
# at the the indices are a geometric progression.  Thus, there is no optimization, and many unnecessary comparisons.
#
# Time Complexity:  O(k*(n!/(n-k)!)), where n is the size of the list.
# Space Complexity: O(k*(n!/(n-k)!)), where n is the size of the list.
#
# NOTE: The time for this approach is for all cases, not just worst case...
def find_geometric_progression_k_tuples_bf(l, r, k=3):
    if isinstance(l, list) and isinstance(r, int) and isinstance(k, int) and 0 <= k:
        n = len(l)
        result = []
        for comb in combinations(range(n), k):
            if k == 1 or all([l[comb[i-1]] * r == l[comb[i]] for i in range(1, k)]):
                result.append(list(comb))

        return result


# APPROACH: Via a Dictionary With Recursion
#
# This approach first constructs a dictionary of values to their indices (this is used to prevent unnecessary
# combinations).  Then each index is recursively called and is added to an accumulation list as the first of the k
# elements.  The recursion continues until either the list has reached a size of k or there is no longer a value in the
# geometric sequence.  Whenever a value is added to the list, it is temporarily removed from the dictionary so that
# duplicate combinations are not created.  Once all valid k-tuples have been created, the results are returned.
#
# Best Case Time Complexity:  O(n), where n is the size of the list.
# Worst Case Time Complexity:  O(n!/(n-k)!), where n is the size of the list.
# Space Complexity: O(n!/(n-k)!), where n is the size of the list.
def find_geometric_progression_k_tuples(l, r, k=3):

    def _rec(d, k, i, a, result):
        if len(a) == k:
            result.append(a[:])
        else:
            if l[i] * r in d:
                for idx in d[l[i] * r]:
                    if idx > i:
                        a.append(idx)
                        _rec(d, k, idx, a, result)
                        a.pop()

    if isinstance(l, list) and isinstance(r, int) and isinstance(k, int) and 0 <= k:
        n = len(l)
        d = defaultdict(list)
        result = []
        for i, num in enumerate(l):
            d[num].append(i)
        for i in range(n):
            _rec(d, k, i, [i], result)
        return result


args = [([1, 4, 16, 64], 4),                    # 2
        ([1, 3, 9, 9, 27, 81], 3),              # 6
        ([1, 5, 5, 25, 125], 5),                # 4
        ([2, 0, 4], 2),                         # 0
        ([1, 2, 1, 2, 4], 2),                   # 3
        ([1, 1, 1, 1], 1),                      # 4
        ([1, 2, 2, 4], 2),                      # 2
        ([4, 2, 1, 2, 1], 2),                   # 0
        ([1, 3, 9, 9, 27, 81], 3),              # 6
        ([9, 9, 9, 9, 9], 1),                   # 10
        ([5, 5, 5, 7, 7, 5, 5, 7, 7, 7], 1),    # 20
        ([4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 1),    # 120
        ([1, 5, 26], 5)]                        # 0
k_vals = [-2, 0, 1, 2, 3, 4]
fns = [find_geometric_progression_k_tuples_bf,
       find_geometric_progression_k_tuples]

for l, r in args:
    for k in k_vals:
        print(f"l: {l!r}")
        for fn in fns:
            print(f"{fn.__name__}(l, {r}, {k}): {fn(l, r, k)!r}")
        print()


