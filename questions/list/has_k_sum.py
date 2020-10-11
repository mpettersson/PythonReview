"""
    HAS K SUM

    Design an algorithm that takes as input a list l, and two numbers; k and n.  The function determines if there are k
    NOT NECESSARILY DISTINCT elements in the list that sum to the integer n.

    Example:
        Input = [11, 2, 5, 7, 3], 3, 21
        Output = True   # either [2, 7, 11], [5, 5, 11], or [7, 7, 7]

    Variations:
        - SEE: pairs_with_sum.py
        - SEE: has_two_sum.py
        - SEE: has_three_sum.py
"""
import itertools


# Naive/Brute Force Approach:  REMEMBER, the formula (and time complexity), for the number of combinations (of k items)
# from a set (of size n) is (n+k-1)!/(k!*(n-1)!), so tread lightly...
# Time complexity (reduced from above) is O(n**k), where n is the number of elements in the list.  Space complexity is
# O(1) (because of itertools use of generators).
# NOTE: You could use recursion to achieve k nested loops, which would be able to sum k items; this would have the same
# time complexity (with added stack space complexity).
def has_k_sum_naive(l, k, t):
    if l is not None and t is not None:
        for combination in itertools.combinations_with_replacement(l, k):
            if sum(combination) is t:
                return True
        return False


# REMEMBER: An invariant is a condition that remains true during execution.

# Invariant Approach:  The invariant, which is kinda obvious, is that if some sum of k (not necessarily distinct)
# elements exists, they must lie within the remaining subarray. Time complexity is O(n ** (k-1)) where n is the number
# of elements in the list.  Space complexity is O(1).
def has_k_sum(l, k, t):

    def has_two_sum(l, t):
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

    def _has_k_sum(l, k, t):
        if k > 0:
            if k is 1:
                left = 0
                right = len(l) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if l[mid] is t:
                        return True
                    elif l[mid] > t:
                        right = mid - 1
                    else:
                        left = mid + 1
            if k is 2:
                return has_two_sum(l, t)
            for i in l:
                if _has_k_sum(l, k - 1, t - i):
                    return True
        return False

    if l is not None and t is not None and k is not None and 0 < k <= len(l):
        l.sort()
        return _has_k_sum(l, k, t)


# VARIATION:
#   Doesn't allow duplicates.
#   Returns a list of lists that sum to k.
def find_k_sum(l, k, t):

    def _has_k_sum(k, left, right, t):
        if k is 1:
            while left <= right:
                mid = (left + right) // 2
                if l[mid] is t:
                    results.append([l[mid]])
                    return
                elif l[mid] > t:
                    right = mid - 1
                else:
                    left = mid + 1
        elif (k > right + 1 - left
                or t < k * l[left]
                or t > k * l[right]):
            return                                  # There are no solutions in these cases
        elif k is 2:                                # If k is 2, solve using the two pointers algorithm
            lo, hi = left, right
            while lo < hi:
                if l[lo] + l[hi] == t:
                    results.append(current_candidates + [l[lo], l[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and l[lo] == l[lo - 1]:
                        lo += 1
                    while lo < hi and l[hi] == l[hi + 1]:
                        hi -= 1
                elif l[lo] + l[hi] < t:
                    lo += 1
                else:
                    hi -= 1
        else:                                        # If not, recurse to k - 1
            for i in range(left, right + 1):
                if i == left or l[i] != l[i - 1]:
                    current_candidates.append(l[i])
                    _has_k_sum(k - 1, i + 1, right, t - l[i])
                    current_candidates.pop()

    if k is not None and l is not None and t is not None and k > 0:
        results = []
        current_candidates = []
        l.sort()
        _has_k_sum(k, 0, len(l) - 1, t)
        return results


args = [([11, 2, 5, 7, 3], 4, 21),
        ([11, 7, 8, -2, 2, 1, 4], 2, 6),
        ([11, 7, -2, 2, 1, 4], 4, 10),
        ([2, 4], 2, 6),
        ([6], 1, 6),
        ([13, 0, 14, -2, -1, 7, 9, 5, 3, 6], 8, 6),
        ([], 2, 6),
        ([11, 7, -2, 2, 1, 4], 4, None),
        (None, 3, 6),
        (None, None, None)]

for l, k, t in args:
    print(f"has_k_sum_naive({l}, {k}, {t}): {has_k_sum_naive(l, k, t)}")
print()

for l, k, t in args:
    print(f"has_k_sum({l}, {k}, {t}): {has_k_sum(l, k, t)}")
print()

for l, k, t in args:
    print(f"find_k_sum({l}, {k}, {t}): {find_k_sum(l, k, t)}")
print()


