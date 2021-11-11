"""
    HAS K SUM

    Write a function that takes an integer list l, and two integers k and t.  The function returns True if there are k,
     DISTINCT elements in the list, which sum to t, False otherwise.

    Example:
        Input = [11, 2, 5, 7, 3], 3, 21
        Output = True   # either [2, 7, 11], [5, 5, 11], or [7, 7, 7]

    Variations:
        - Solve the same problem, however, the k elements (which sum to t) MAY NOT NECESSARILY BE DISTINCT.

    TODO:
        - Create a long list scenario that will return false to better test the optimized/unoptimized functions.
"""
import itertools
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Can the list be modified?
#   - Are the numbers in the list unique?
#   - Can there be duplicates in the k elements?


# APPROACH: (DISTINCT k-sum) Via Naive/Brute Force (Itertools Combinations)
#
# This approach checks the sum of each possible k element combinations from the list; if at any point a sum is equal to
# t, then True is returned.  If no combinations sum to t, False is returned.
#
# Time Complexity: O(n**k) (as reduced from the formula below), where n is the number of elements in the list.
# Space Complexity: O(1) (because of itertools use of generators).
#
# REMEMBER: The formula (and time complexity), for the number of combinations (of k items) from a set of size n is:
#               n!/(k!*(n-k)!)
#
# NOTE: You could use recursion to achieve k nested loops, which would be able to sum k items; this would have the same
#       time complexity (with added stack space complexity).
def has_k_sum_via_bf_comb(l, k, t):
    if isinstance(l, list) and isinstance(k, int) and 0 <= k and isinstance(t, int):
        for combination in itertools.combinations(l, k):
            if sum(combination) is t:
                print(combination)
                return True
    return False


# APPROACH: (DISTINCT k-sum) Via Two Pointers Pattern
#
# This approach uses a generalized, find k sum, function where k-2 nested calls are followed by a find two sum call.
# The first step is to sort the list, this required by the two pointers pattern/approach. Then recursively call the
# generalized has k sum function (2 times) until k is two, at which point, the has two sum is called.  The has two sum
# function simply uses a high and low pointer that unilaterally converge until either they pass each other or a pair
# with the desired sum is found.  When k elements are found, with a sum equal to t, True is returned.  If there are not
# k distinct elements with a sum of t, False is returned.
#
# Time Complexity: O(n ** (k-1)), where n is the number of elements in the list.
# Space Complexity: max(O(n), O(k)), where n is the number of elements in the list.
def has_k_sum_via_pointer(l, k, t):

    def _rec(l, idx, k, t):
        n = len(l)
        if idx == n or l[idx] * k > t or t > l[-1] * k:
            return False
        if k == 2:
            return _has_two_sum(l, idx, t)
        for i in range(idx, n):
            if i == idx or l[i - 1] != l[i]:
                if _rec(l, i+1, k-1, t-l[i]):
                    return True
        return False

    def _has_two_sum(l, start, t):
        lo = start
        hi = len(l) - 1
        while lo < hi:
            curr_sum = l[lo] + l[hi]
            if curr_sum < t or (lo > start and l[lo] == l[lo - 1]):         # curr_sum<t or ALREADY processed l[lo] val.
                lo += 1
            elif curr_sum > t or (hi < len(l) - 1 and l[hi] == l[hi + 1]):  # curr_sum>t or ALREADY processed l[hi] val.
                hi -= 1
            else:
                return True
        return False

    if isinstance(l, list) and isinstance(k, int) and 0 <= k and isinstance(t, int):
        if k == t == 0:                             # Edge case.
            return True
        if k == 1:
            return t in l                           # O(n), (but better than sorting and binary search...)
        l.sort()
        return _rec(l, 0, k, t)
    return False


# APPROACH: (DISTINCT k-sum) Via Hash Set
#
# This approach is very similar to the approach above, the only difference is the has two sum approach/implementation.
# The has two sum function in this approach uses a hash set for quick (O(n) time) lookups, storing seen values, and
# checking for the complement (or difference between the desired total and current value) in the set of seen values.
#
# Time Complexity: O(n ** (k-1)), where n is the number of elements in the list.
# Space Complexity: max(O(n), O(k)), where n is the number of elements in the list.
def has_k_sum_via_hash_set(l, k, t):

    def _rec(l, idx, k, t):
        n = len(l)
        if idx == n or l[idx] * k > t or t > l[-1] * k:
            return False
        if k == 2:
            return _has_two_sum(l, idx, t)
        for i in range(idx, n):
            if i == idx or l[i - 1] != l[i]:
                if _rec(l, i+1, k-1, t-l[i]):
                    return True
        return False

    def _has_two_sum(l, start, t):
        s = set()                                               # Set of seen values.
        for i in range(start, len(l)):
            if t - l[i] in s:                               # If the complement is in s:
                return True
            s.add(l[i])                                         # Add current value to seen set.
        return False

    if isinstance(l, list) and isinstance(k, int) and 0 <= k and isinstance(t, int):
        if k == t == 0:                             # Edge case.
            return True
        if k == 1:
            return t in l                           # O(n), (but better than sorting and binary search...)
        l.sort()
        return _rec(l, 0, k, t)
    return False


# APPROACH: (DISTINCT k-sum) Via Two Pointers Pattern WITHOUT Optimizations
#
# This approach is an unoptimized (and refactored) version of the two pointers approach above.
#
# NOTE: This (duplicate) code is included to illustrate the importance of optimizations and early terminations; it is
#       several times slower than the optimized version.  Still, this is not remotely as bad as the naive/combinations
#       approach.
#
# Time Complexity: O(n ** (k-1)), where n is the number of elements in the list.
# Space Complexity: max(O(n), O(k)), where n is the number of elements in the list.
def has_k_sum_unoptimized(l, k, t):

    def _rec(l, low, high, k, t, a):
        if k == 0 and t == 0:                                   # k == 0:  O(1). Don't need to sort.
            return True
        elif k == 1:                                            # k == 1:  O(n). Don't need to sort.
            return True if t in l else False
        elif k == 2:                                            # k == 2: Solve 2-sum via two pointers approach.
            while low < high:
                curr_sum = l[low] + l[high]
                if curr_sum == t:
                    return True
                elif curr_sum < t:
                    low += 1
                else:
                    high -= 1
        else:                                                   # k >= 3:  Recurse down to k == 2.
            for i in range(low, high + 1):
                if _rec(l, i + 1, high, k - 1, t - l[i], a + [l[i]]):
                    return True
        return False

    if isinstance(l, list) and isinstance(k, int) and 0 <= k and isinstance(t, int):
        l.sort()
        return _rec(l, 0, len(l)-1, k, t, [])
    return False


# APPROACH: (DISTINCT k-sum) Via Two Pointers Pattern WITH Optimizations
#
# This approach is just an optimized and refactored version of the (distinct) two pointers approach above.
#
# This (duplicate) code is included to illustrate the importance of optimizations and early terminations!
#
# Time Complexity: O(n ** (k-1)), where n is the number of elements in the list.
# Space Complexity: max(O(n), O(k)), where n is the number of elements in the list.
def has_k_sum_optimized(l, k, t):

    def _rec(l, low, high, k, t, a):                            # Early Termination Conditions:
        if (high-low + 1 < k                                            # Fewer than k elements in (sub)list to search.
                or t < l[low] * k                                       # Target sum is unobtainable (too small).
                or t > l[high] * k):                                    # Target sum is unobtainable (too big).
            return False
        if k == 2:                                              # k == 2: Solve 2-sum via two pointers approach.
            while low < high:
                curr_sum = l[low] + l[high]
                if curr_sum == t:
                    return True
                elif curr_sum < t:
                    low += 1
                else:
                    high -= 1
        else:                                                   # k >= 3:  Recurse down to k == 2.
            for i in range(low, high + 1):
                if i == low or (i > low and l[i - 1] != l[i]):
                    if _rec(l, i + 1, high, k - 1, t - l[i], a + [l[i]]):
                        return True
        return False

    if isinstance(l, list) and isinstance(k, int) and 0 <= k and isinstance(t, int):
        if k == 0:                                              # k == 0:  O(1). Don't need to sort.
            return True if t == 0 else False
        if k == 1:                                              # k == 1:  O(n). Don't need to sort.
            return True if t in l else False
        l.sort()
        return _rec(l, 0, len(l)-1, k, t, [])
    return False


# VARIATION: Solve the same problem, however, the k elements (which sum to t) MAY NOT NECESSARILY BE DISTINCT.


# VARIATION APPROACH: (NOT NECESSARILY DISTINCT k-sum) Naive/Brute Force
#
# This approach checks the sum of each possible k element combinations with duplicates from the list; if at any point a
# sum is equal to t, then True is returned.  If no combinations sum to t, False is returned.
#
# Time Complexity: O(n**k) (as reduced from the formula below), where n is the number of elements in the list.
# Space Complexity: O(1) (because of itertools use of generators).
#
# REMEMBER: The formula (and time complexity), for the number of combinations (of k items) from a set of size n is:
#               (n+k-1)!/(k!*(n-1)!)
#
# NOTE: You could use recursion to achieve k nested loops, which would be able to sum k items; this would have the same
#       time complexity (with added stack space complexity).
def has_k_sum_via_bf_comb_indistinct(l, k, t):
    if isinstance(l, list) and isinstance(k, int) and 0 <= k and isinstance(t, int):
        for combination in itertools.combinations_with_replacement(l, k):
            if sum(combination) is t:
                return True
    return False


# VARIATION APPROACH: (NOT NECESSARILY DISTINCT k-sum) Two Pointer/Invariant
#
# This approach uses the invariant, that if "a sum of k (not necessarily distinct) elements exists, they must lie within
# the remaining sublist".  Therefore, this recursively attempts to find k numbers which maintain the invariant, thus
# summing to the provided total.
#
# Time Complexity: max(O(n * log(n)), O(n ** (k-1))), where n is the number of elements in the list.
# Space Complexity: O(1).
def has_k_sum_via_pointer_indistinct(l, k, t):

    def _has_two_sum(l, t):
        lo = 0
        hi = len(l)-1
        while lo <= hi:
            if l[lo] + l[hi] == t:
                return True
            elif l[lo] + l[hi] < t:
                lo += 1
            else:
                hi -= 1
        return False

    def _rec(l, k, t):
        if k == 2:                                  # k == 2: Return _has_two_sum result.
            return _has_two_sum(l, t)
        for i in l:                                 # k > 2:  Recurse with k-1 and t = t - current value.
            if _rec(l, k - 1, t - i):
                return True
        return False

    if isinstance(l, list) and isinstance(k, int) and 0 <= k and isinstance(t, int):
        if t == 0 and 0 in l:
            return True
        if k == 0:
            return True if t == 0 else False
        if k == 1:
            return t in l                           # O(n), (but better than sorting and binary search...)
        l.sort()
        return _rec(l, k, t)
    return False


args = [([11, 2, 5, 7, 3], 4, 21),
        ([], 0, 0),
        ([11, 7, 8, -2, 2, 1, 4], 2, 6),
        ([1, 0, -1, 0, -2, 2], 4, 0),
        ([2, 2, 2, 2, 2], 4, 8),
        ([0, 0, 0, 0, 0], 5, 0),
        ([0], 5, 0),
        ([11, 7, -2, 2, 1, 4], 4, 10),
        ([0, 1, 1, 5, 5], 3, 6),
        ([2, 2, 2, 0, 5], 3, 6),
        ([11, 7, -2, 2, 1, 4], 4, 0),
        ([2, 4], 2, 6),
        ([1, 1], 3, 3),
        ([1, 0, 1], 3, 3),
        ([13, 0, 14, -2, -1, 7, 9, 5, 3, 6], 2, 6),
        ([2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2], 2, 2),
        ([-1, 0, 1, 2, -1, -4], 3, 0),
        ([13, 0, 14, -2, -1, 7, 9, 5, 3, 6], 3, 6),
        ([-2, 1, 2, 4, 7, 11], 3, 7),
        ([-1, 0, 1, 2, -1, -4], 3, 0),
        ([0, 1, 1, 1, 1, 1, 1, 1, 2], 3, 2),
        ([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8], 2, 0),
        ([-2, 1, 2, 4, 8, 11], 2, 6),
        ([2, 4], 2, 6),
        ([2, 2], 2, 4),
        ([-2, -1, 0, 3, 5, 6, 7, 9, 13, 14], 2, 6),
        ([6], 1, 6),
        ([13, 0, 14, -2, -1, 7, 9, 5, 3, 6], 8, 6),
        ([], 2, 6),
        ([11, 7, -2, 2, 1, 4], 0, 10),
        ([11, 7, -2, 2, 1, 4], None, 10),
        ([11, 7, -2, 2, 1, 4], 4, None)]
fns = [has_k_sum_via_bf_comb,
       has_k_sum_via_pointer,
       has_k_sum_via_hash_set,
       has_k_sum_unoptimized,
       has_k_sum_optimized,
       has_k_sum_via_bf_comb_indistinct,
       has_k_sum_via_pointer_indistinct]

for l, k, t in args:
    for fn in fns:
        print(f"{fn.__name__}({l[:]}, {k}, {t}): {fn(l, k, t)}")
    print()


