"""
    HAS THREE SUM (EPI 18.4: THE 3-SUM PROBLEM)

    Write a function, that accepts an integer list l and an integer total t, then returns True if a combination of three
    elements, NOT NECESSARILY DISTINCT values, sum to the specified number, False otherwise.

    Example:
        Input = [11, 2, 5, 7, 3], 21
        Output = True   # Either [2, 7, 11] OR [5, 5, 11], Notice that 5 was used twice...

    Variations:
        - Solve the same problem when the three elements must be distinct (leetcode.com/problems/3sum).
        - Write a program that takes as input a list of integers l and an integer t, and returns a 3-tuple
          (l[x], l[y], l[z]) where z, y, z are all distinct, minimizing abs(t - (l[x] + l[y] + l[z])), and
          l[x] <= l[y] <=l[z].
        - Write a program that takes as input a list of integers l and an integer t, and returns the number of 3-tuples
          (z, y, z) such that l[x] + l[y] + l[z] <= t and l[x] <= l[y] <=l[z].
"""
import copy
import itertools


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Can the list be modified?
#   - Are the numbers in the list unique?
#   - Can there be duplicates in the k elements?


# APPROACH: Brute Force
#
# Use three loops to find three values that sum to the provided total.
#
# Time Complexity: O(n**3), where n is the number of elements in the list.
# Space Complexity: O(1).
def has_three_sum_bf(l, t):
    if l is not None and t is not None:
        for i in range(len(l)):
            for j in range(len(l)):             # BC non-distinct/duplicate CAN be used, start at 0, not i + 1
                for k in range(len(l)):         # BC non-distinct/duplicates CAN be used, start at 0, not j + 1
                    if l[i] + l[j] + l[k] == t:
                        return True
    return False


# APPROACH: Naive/Combinations
#
# This approach checks the sum of each possible three element combination (with duplicates) from the list; if the sum
# is equal to t, then True is returned, False otherwise.
#
# Time Complexity:  O((n+r-1)!/(r!*(n-1)!)), which reduces to O(n**3), where n is the number of elements in the list.
# Space Complexity: O(1) (assuming itertools generators are O(1)).
#
# REMEMBER: The formula (and time complexity), for the number of combinations (of k items) from a set of size n is:
#               (n+k-1)!/(k!*(n-1)!)
def has_three_sum_naive(l, t):
    if l is not None and t is not None:
        for combination in itertools.combinations_with_replacement(l, 3):  # Use itertools.combinations if no dups.
            if sum(combination) is t:
                return True
    return False


# APPROACH: Via Set
#
# Iterating over the list values, using a set to quickly check if there exists three distinct values in the set,
# x, y, and z, where t = x + y + z, if so return True, False otherwise.
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space complexity: O(n) for the set, O(n) for the result list, where n is the number of elements in the list.
def has_three_sum_set(l, t):
    if l and t is not None:
        s = set(l)                  # Seen values set.
        for x in s:
            for y in s:
                z = t - x - y
                if z in s:
                    return True
    return False


# APPROACH: Two Pointers/Invariant (Invariant: A Condition That Remains True During Execution)
#
# The two pointers approach is simply the use of two pointers, (one for the lowest value and one at the highest value,)
# that iteratively search a sorted (sub)list in O(n) time, stopping when the lower pointer is equal to, or higher than,
# the index of the higher pointer. The two pointers (in a sorted list) guarantee the following invariant (where an
# invariant is a condition that remains true during execution): "if two elements which sum to the desired value t
# exists, then  they must lie within the sublist within the two pointers".
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space Complexity: O(1).
def has_three_sum(l, t):

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

    if l is not None and t is not None:
        l.sort()                            # O(n * log(n))
        for i in l:                         # O(n)
            if has_two_sum(l, t - i):           # O(n)
                return True
    return False


# VARIATION:  Solve the same problem when the three elements must be distinct.
# SEE:  leetcode.com/problems/3sum


# VARIATION APPROACH: (Distinct) Brute Force
#
# Use three loops to find three values that sum to the provided total.
#
# Time Complexity: O(n**3), where n is the number of elements in the list.
# Space Complexity: O(1).
def has_distinct_three_sum_bf(l, t):
    if l is not None and t is not None and len(l) >= 3:
        for i in range(len(l)-2):
            for j in range(i+1, len(l)-1):
                for k in range(j+1, len(l)):
                    if l[i] + l[j] + l[k] == t:
                        return True
    return False


# VARIATION APPROACH: (Distinct) Naive/Combinations
#
# This approach checks the sum of each possible three element combination from the list; if the sum is equal to t, then
# True is returned, False otherwise.
#
# Time Complexity:  O(n!/(k!*(n-k)!)), which reduces to O(n**3), where n is the number of elements in the list.
# Space Complexity: O(1) (assuming itertools generators are O(1)).
#
# REMEMBER: The formula (and time complexity), for the number of combinations (of k items) from a set of size n is:
#               n!/(k!*(n-k)!)
def has_distinct_three_sum_naive(l, t):
    if l is not None and t is not None:
        for combination in itertools.combinations(l, 3):
            if sum(combination) is t:
                return True
    return False


# VARIATION APPROACH: (Distinct) Via Hash Set
#
# Iterating over the list values, using a set to quickly check if there exists three distinct values in the set,
# x, y, and z, where t = x + y + z, if so return True, False otherwise.
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space complexity: O(n) for the set, O(n) for the result list, where n is the number of elements in the list.
def has_distinct_three_sum_set(l, t):
    def has_distinct_two_sum_set(l, i, t):
        s = set()
        for i in range(i, len(l)):
            complement = t - l[i]
            if complement in s:
                return True
            s.add(l[i])
        return False

    if l is not None and isinstance(t, int):
        for i in range(len(l)-2):
            if has_distinct_two_sum_set(l, i+1, t - l[i]):
                return True
    return False


# VARIATION APPROACH: (Distinct) Two Pointer/Invariant (Invariant: A Condition That Remains True During Execution)
#
# The two pointers approach is simply the use of two pointers, (one for the lowest value and one at the highest value,)
# that iteratively search a sorted (sub)list in O(n) time, stopping when the lower pointer is equal to, or higher than,
# the index of the higher pointer. The two pointers (in a sorted list) guarantee the following invariant (where an
# invariant is a condition that remains true during execution): "if two elements which sum to the desired value t
# exists, then  they must lie within the sublist within the two pointers".
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space Complexity: O(1).
def has_distinct_three_sum(l, t):

    def has_distinct_two_sum(l, lo, hi, t):
        while lo < hi:
            if l[lo] + l[hi] == t:
                return True
            elif l[lo] + l[hi] < t:
                lo += 1
            else:
                hi -= 1
        return False

    if l is not None and t is not None:
        l.sort()                                                    # O(n * log(n))
        for i in range(len(l)-2):                                   # O(n)
            if has_distinct_two_sum(l, i+1, len(l)-1, t - l[i]):        # O(n)
                return True
    return False


args = [([-1, 0, 1, 2, -1, -4], 0),
        ([13, 0, 14, -2, -1, 7, 9, 5, 3, 6], 6),
        ([-2, 1, 2, 4, 7, 11], 7),
        ([11, 2, 5, 7, 3], 21),
        ([-1, 0, 1, 2, -1, -4], 0),
        ([2, 1, 1, 1, 0, 1, 1, 1, 1], 2),
        ([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9], 0),
        ([-7, -9, 9, -1, -7, -2, -10, 5, 9, 3, 4], 0),
        ([11, 7, -2, 2, 1, 4], 6),
        ([11, 7, -2, 2, 1, 4], 10),
        ([0, 1, 1, 5, 5], 6),
        ([2, 2, 2, 0, 5], 6),
        ([3], 6),
        ([2, 4], 6),
        ([0, 2, 4], 6),
        ([2, 2, 2], 6),
        ([-3, -2, -1, -1, -1, 0, 2, 4], 6),
        ([6], 6),
        ([13, 0, 14, -2, -1, 7, 9, 5, 3, 6], 6),
        ([], 6),
        ([11, 7, -2, 2, 1, 4], None),
        (None, 6),
        (None, None)]
fns = [has_three_sum_naive,
       has_three_sum_bf,
       has_three_sum_set,
       has_three_sum,
       has_distinct_three_sum_bf,       # Variation: Three distinct elements.
       has_distinct_three_sum_naive,    # Variation: Three distinct elements.
       has_distinct_three_sum_set,      # Variation: Three distinct elements.
       has_distinct_three_sum]          # Variation: Three distinct elements.

for l, t in args:
    for fn in fns:
        print(f"{fn.__name__}({l}, {t}): {fn(copy.copy(l), t)}")
    print()


