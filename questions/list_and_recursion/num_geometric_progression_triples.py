"""
    NUM GEOMETRIC PROGRESSION TRIPLES (hackerrank.com/challenges/count-triplets-1)

    Write a function, which accepts a list l, a (common) ratio r, and a number of indices k, then find and return a
    count of the number of 3 element sets (from the list) that form a geometric progression (for the provided common
    ratio).

    Wikipedia's definition of a geometric progression (SEE: wikipedia.org/wiki/Geometric_progression):

        "In mathematics, a geometric progression, also known as a geometric sequence, is a sequence of non-zero numbers
         where each term after the first is found by multiplying the previous one by a fixed, non-zero number called the
         common ratio. For example, the sequence 2, 6, 18, 54, ... is a geometric progression with common ratio 3.
         Similarly 10, 5, 2.5, 1.25, ... is a geometric sequence with common ratio 1/2."

    Example:
        Input = [1, 4, 16, 64], 4
        Output = 2 # [1,4,16] at indices 0, 1, 2 and [4, 16, 64] at indices 1, 2, 3.

    Variations:
        - Same question, only k element tuples (not 3-tuples); SEE: num_geometric_progression_k_tuples.py
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
# This approach uses itertools' combinations to produce all 3 element combinations of indices, then checks if the values
# at the the indices are a geometric progression.  Thus, there is no optimization, and many unnecessary comparisons.
#
# Time Complexity:  O((n!/(n-3)!)), where n is the size of the list.
# Space Complexity: O((n!/(n-3)!)), where n is the size of the list.
def num_geometric_progression_triples_via_brute_force(l, r):
    if isinstance(l, list) and isinstance(r, int) and isinstance(k, int) and 0 <= k:
        n = len(l)
        result = 0
        for comb in combinations(range(n), k):
            if k == 1 or all([l[comb[i-1]] * r == l[comb[i]] for i in range(1, 3)]):
                result += 1
        return result


# APPROACH: Via 2 (or k-1) Dictionaries (1st & 2nd Term Dicts)
#
# This approach uses 2 (or k-1) dictionaries (of a values to counts) to sum the number of geometric sequences seen.
# For each value in the list, if the value * ratio is the 2nd terms dictionary, its count is added to the result count.
# Then, working (backwards) the second terms dictionary is updated from the first, and the first terms dictionary is
# updated by the current value.  Once all values have been iterated over, the resulting count is returned.
#
# NOTE: For this approach, the third term's counts are not tracked/used in a dictionary-this is because only 2 (or k-1)
#       dictionaries are required and we are using dictionaries for the first two terms.  (The following approaches use
#       other combinations of dictionaries, and the math/order is a bit different.)
#
# Time Complexity:  O(n), where n is the size of the list.
# Space Complexity: O(n), where n is the size of the list.
def num_geometric_progression_triples_via_1st_and_2nd_term_dicts(l, r):
    result = 0
    d_first = defaultdict(int)
    d_second = defaultdict(int)
    for v in reversed(l):
        result += d_second[v * r]
        d_second[v] += d_first[v * r]
        d_first[v] += 1
    return result


# APPROACH: Via 2 (or k-1) Dictionaries (1st & 2nd Term Dicts)
#
# This approach uses 2 (or k-1) dictionaries (of a values to counts) to sum the number of geometric sequences seen.
# For each value in the list, if the value is the 3rd terms dictionary, its count is added to the result count.
# Then, the third terms dictionary (for the current value * ratio) is updated with the second terms count, and the
# second terms dictionary (for the current value * ratio) is incremented by one.  Once all values have been iterated
# over, the resulting count is returned.
#
# NOTE: For this approach, the first term's counts are not tracked/used in a dictionary-this is because only 2 (or k-1)
#       dictionaries are required and we are using dictionaries for the second two terms.  (The immediately preceeding
#       and proceeding approaches use the other combinations of dictionaries, and the math/order is different.)
#
# Time Complexity:  O(n), where n is the size of the list.
# Space Complexity: O(n), where n is the size of the list.
def num_geometric_progression_triples_via_2nd_and_3rd_term_dicts(l, r):
    result = 0
    d_second = defaultdict(int)
    d_third = defaultdict(int)
    for v in l:
        result += d_third[v]
        d_third[v*r] += d_second[v]
        d_second[v*r] += 1
    return result


# APPROACH: Via 2 (or k-1) Dictionaries (1st & 3rd Term Dicts)
#
# This approach uses 2 (or k-1) dictionaries (of a values to counts) to sum the number of geometric sequences seen.
# One dictionary is for the first term (or the term on the 'left' of the current value), and the other dictionary is for
# the third term (or the term on the 'right' of the current value).
#
# NOTE: For this approach, the second term's counts are not tracked/used in a dictionary-this is because only 2 (or k-1)
#       dictionaries are required and we are using dictionaries for the first and last terms.  (The previous two
#       approaches use other combinations of dictionaries, and the math/order is different/better.)
#
# Time Complexity:  O(n), where n is the size of the list.
# Space Complexity: O(n), where n is the size of the list.
def num_geometric_progression_triples_via_1st_and_3rd_term_dicts(l, r):
    result = 0
    d_first = defaultdict(int)
    d_third = defaultdict(int)
    for v in l:
        d_third[v] += 1
    for v in l:
        d_third[v] -= 1
        result += d_first[v/r] * d_third[v*r]
        d_first[v] += 1
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
fns = [num_geometric_progression_triples_via_brute_force,
       num_geometric_progression_triples_via_1st_and_2nd_term_dicts,
       num_geometric_progression_triples_via_2nd_and_3rd_term_dicts,
       num_geometric_progression_triples_via_1st_and_3rd_term_dicts]
k = 3
for l, r in args:
    print(f"l: {l!r}\nr: {r}")
    for fn in fns:
        print(f"{fn.__name__}(l, r): {fn(l, r)!r}")
    print()


