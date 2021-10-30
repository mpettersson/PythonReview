"""
    NUM GEOMETRIC PROGRESSION K TUPLES

    Write a function, which accepts a list l, a (common) ratio r, and a number of indices k, then find and return a
    count of the number of k-tuple elements (from the list) in a geometric progression for the provided common ratio.

    Wikipedia's definition of a geometric progression (SEE: wikipedia.org/wiki/Geometric_progression):

        "In mathematics, a geometric progression, also known as a geometric sequence, is a sequence of non-zero numbers
         where each term after the first is found by multiplying the previous one by a fixed, non-zero number called the
         common ratio. For example, the sequence 2, 6, 18, 54, ... is a geometric progression with common ratio 3.
         Similarly 10, 5, 2.5, 1.25, ... is a geometric sequence with common ratio 1/2."

    Example:
        Input = [1, 4, 16, 64], 4, 3
        Output = 2 # [1,4,16] at indices 0, 1, 2 and [4, 16, 64] at indices 1, 2, 3.
"""
from collections import defaultdict


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Return value (number of sets, list of indices, list of values)?
#   - What are the size limits of the list?
#   - Are the values negative & positive?
#   - Are there duplicate values in the list?
#   - Is the list sorted?


# APPROACH: Via a Dictionary With Recursion
#
# This approach first constructs a dictionary of values to their indices (this is used to prevent unnecessary
# combinations).  Then each index is recursively called and is added to an accumulation list as the first of the k
# elements.  The recursion continues until either the list has reached a size of k or there is no longer a value in the
# geometric sequence.  Whenever a value is added to the list, it is temporarily removed from the dictionary so that
# duplicate combinations are not created.  Once all valid k-tuples have been created, the length of the list of tuples
# is then returned.
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
        return len(result)


# APPROACH: Via k-1 Dictionaries (2nd Term to kth Term)
#
# This approach uses k-1 dictionaries (of a values to counts) to sum the number of geometric sequences seen.  For each
# value in the list, if the value is the kth terms dictionary, its count is added to the result count.  Then, working
# (backwards) from the kth term's dictionary to the second term's dictionary, the values are updated from the previous
# (smaller) terms (to the current terms) dictionaries.  The last step (of the iteration over all values) is to update
# the second terms dictionary.  Once all values have been iterated over, the resulting count is returned.
#
# NOTE: For this approach, the first term's counts are not tracked/used in a dictionary-this is because only k-1
#       dictionaries are required and we are using dictionaries for the 2nd term to the kth term.  (The next approach
#       uses the first term to the k-1th term dictionaries, and the math/order is a bit different.)
#
# NOTE: It is much easier to first solve this for 3 (or maybe 2) element tuples then convert it to k element tuples,
#       the math can be a bit confusing to conceptualize.
#
# Time Complexity:  O(n*k), where n is the size of the list.
# Space Complexity: O(n*k), where n is the size of the list.
def num_geometric_progression_k_tuples(l, r, k=3):
    if isinstance(l, list) and isinstance(r, int) and isinstance(k, int) and 0 <= k:
        if k == 0:
            return 0
        if k == 1:
            return len(l)
        ratio_dicts = [defaultdict(int) for _ in range(k-1)]    # NOT REVERSED: idx 0 is 2nd term count, ids 1 is 3rd
        result = 0                                              # term count, ... idx k-2 is kth term count.
        for v in l:                                             # NOTE: Forward iteration through list when the ratio.
            result += ratio_dicts[-1][v]                              # term dicts skips first term & includes kth term.
            for i in range(k-2, 0, -1):                         # NOTE: Reverse Iteration, LATER terms first.
                ratio_dicts[i][v*r] += ratio_dicts[i-1][v]
            ratio_dicts[0][v*r] += 1
        return result


# APPROACH: Via k-1 Dictionaries (1st Term to k-1th Term)
#
# This approach uses k-1 dictionaries (of a values to counts) to sum the number of geometric sequence seen.  For each
# value in the list, if the value * ratio is the k-1th terms dictionary, its count is added to the result count.
# Then, working (backwards) from the k-1th term's dictionary to the first term's dictionary (of counts), the values are
# updated each of the previous (smaller) terms (to the current terms) dictionaries.  The last step (of the iteration
# over all values) is to update the first terms dictionary.  Once all values have been iterated over, the resulting
# count is returned.
#
# NOTE: For this approach, the last term's counts are not tracked/used in a dictionary--this is because only k-1
#       dictionaries are required and we are using dictionaries for the 1st term to the k-1th term.  (The previous
#       approach uses the second term to the kth term dictionaries, and the math/order is a bit different.)
#
# NOTE: It is much easier to first solve this for 3 (or maybe 2) element tuples then convert it to k element tuples,
#       the math can be a bit confusing to conceptualize.
#
# Time Complexity:  O(n*k), where n is the size of the list.
# Space Complexity: O(n*k), where n is the size of the list.
def num_geometric_progression_k_tuples_alt(l, r, k=3):
    if isinstance(l, list) and isinstance(r, int) and isinstance(k, int) and 0 <= k:
        if k == 0:
            return 0
        if k == 1:
            return len(l)
        ratio_dicts = [defaultdict(int) for _ in range(k-1)]    # NOTE: THIS IS REVERSED: idx 0 is k-1th term count, idx
        result = 0                                              # 1 is k-2th term count, ... last idx is 1st term count.
        for v in reversed(l):                                   # NOTE: This is also reversed because we DON'T store the
            result += ratio_dicts[0][v*r]                       # Add the last terms count to the results.
            for i in range(k-2):                                # NOTE: ratio_dicts IS reversed, so this ISN't REVERSED.
                ratio_dicts[i][v] += ratio_dicts[i+1][v*r]
            ratio_dicts[-1][v] += 1                             # Update the first term count.
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
fns = [find_geometric_progression_k_tuples,
       num_geometric_progression_k_tuples,
       num_geometric_progression_k_tuples_alt]

for l, r in args:
    for k in k_vals:
        print(f"l: {l!r}")
        for fn in fns:
            print(f"{fn.__name__}(l, {r}, {k}): {fn(l, r, k)!r}")
        print()


