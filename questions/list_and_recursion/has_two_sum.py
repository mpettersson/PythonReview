"""
    HAS TWO SUM

    Write a function that accepts a (unsorted) list l and an integer total t, then returns True if there exists two
    elements in the list with the sum t, False otherwise.

    Example:
        Input = [11, 2, -2, 7, 4, 1], 6
        Output = True
"""
import copy

# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Can the list be modified?
#   - Are the numbers in the list unique?
#   - Can there be duplicates in the k elements?


# APPROACH: Naive/Brute Force
#
# Loop over every pair, if a pair sum to t and are not the same value, return True, False otherwise.
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space Complexity: O(1).
def has_two_sum_via_bf(l, t):
    if l is not None and t is not None:
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[i] + l[j] == t and i != j:
                    return True
#                   return i, j             # Alternatively, the indices of the first found set could be returned.
    return False


# APPROACH: (Time Optimized) Via Dict
#
# This approach uses a dictionary for O(1) lookup times.
#
# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(n), where n is the number of elements in the list.
def has_two_sum_via_dict(l, t):
    if l is not None and isinstance(t, int):
        d = {}                              # Value: Index
        for i, n in enumerate(l):
            diff = t - n
            if diff in d:
                return True
#               return i, d[diff]           # Alternatively, the indices of the first found set could be returned.
            d[n] = i
    return False


# APPROACH: (Space Optimized) Two Pointer/Invariant (Invariant: A Condition That Remains True During Execution)
#
# In this case the invariant is: "the sublist (l[lo:hi+1]), holds the solution, if it exits".  This approach uses two
# pointers pointing at the lowest and highest values in a sorted list.  The two pointers incrementally converge until
# either two values with the desired sum are found (True is returned) or the lower pointers index is no longer less than
# the higher pointers index (False is returned).
#
# Time Complexity: O(n * log(n)), where n is the number of elements in the list.
# Space Complexity: O(1) (if allowed to modify the list, O(n) otherwise).
def has_two_sum_via_pointer(l, t):
    if l is not None and t is not None:
        l.sort()                            # O(n * log(n))
        if len(l) > 1:
            lo = 0
            hi = len(l)-1
            while lo < hi:
                if l[lo] + l[hi] == t:
                    return True
                elif l[lo] + l[hi] < t:
                    lo += 1
                else:
                    hi -= 1
    return False


args = [([13, 0, 14, -2, -1, 7, 9, 5, 3, 6], 6),
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
fns = [has_two_sum_via_bf,
       has_two_sum_via_dict,
       has_two_sum_via_pointer]

for l, n in args:
    for fn in fns:
        print(f"{fn.__name__}({l}, {n}): {fn(copy.copy(l), n)}")
    print()


