"""
    HAS THREE SUM (EPI 18.4: THE 3-SUM PROBLEM)

    Write a function, that accepts a list and a number, then returns True if a combination of three elements, which may
    or may not be duplicate values, sum to the specified number.

    Example:
        Input = [11, 2, 5, 7, 3], 21
        Output = True   # Either [2, 7, 11] OR [5, 5, 11], Notice that 5 was used twice...

    Variations:
        - Solve the same problem when the three elements must be distinct.
        - Write a program that takes as input a list of integers l and an integer t, and returns a 3-tuple
          (l[x], l[y], l[z]) where z, y, z are all distinct, minimizing abs(t - (l[x] + l[y] + l[z])), and
          l[x] <= l[y] <=l[z].
        - Write a program that takes as input a list of integers l and an integer t, and returns the number of 3-tuples
          (z, y, z) such that l[x] + l[y] + l[z] <= t and l[x] <= l[y] <=l[z].
"""
import itertools


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Are the numbers in the list unique?
#   - Can there be duplicates numbers in a result set?
#   - Can there be duplicate sets in the result list?


# Brute Force Approach:  Use three loops to find three values that sum to the provided total.
# Time Complexity: O(n**3), where n is the number of elements in the list.
# Space Complexity: O(1).
def has_three_sum_bf(l, t):
    if l is not None and t is not None:
        for i in range(len(l)):
            for j in range(len(l)):             # BC duplicates CAN be used, start at 0, not i + 1
                for k in range(len(l)):         # BC duplicates CAN be used, start at 0, not j + 1
                    if l[i] + l[j] + l[k] == t:
                        return True
    return False


# Naive/Combinations Approach:  REMEMBER, the formula (and time complexity), for the number of combinations (of r items)
# from a set (of size n) is (n+r-1)!/(r!*(n-1)!), so tread lightly...
# Time Complexity:  O((n+r-1)!/(r!*(n-1)!)), which reduces to O(n**3), where n is the number of elements in the list.
# Space Complexity: O(1) (assuming itertools generators are O(1)).
def has_three_sum_naive(l, t):
    if l is not None and t is not None:
        for combination in itertools.combinations_with_replacement(l, 3):  # Use itertools.combinations if no dups.
            if sum(combination) is t:
                return True
    return False


# Set Approach:  Iterating over the list values, using a set to quickly check if there exists three distinct values in
# the set, x, y, and z, where t = x + y + z, if so return True, False otherwise.
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space complexity: O(n) for the set, O(n) for the result list, where n is the number of elements in the list.
def has_three_sum_set(l, t):
    if l and t is not None:
        elements = set(l)
        for x in elements:
            for y in elements:
                z = t - x - y
                if z in elements:
                    return True
    return False


# Invariant Approach:  Find a l[x] + l[y] = t - l[z] if such entries exists.  The invariant, or a condition that remains
# true during execution, is that if two elements which sum to the desired value t exists, then they must lie within the
# sublist currently under construction.
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


# Distinct Brute Force Approach:  Use three loops to find three values that sum to the provided total.
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


# Distinct Naive/Combinations Approach:  REMEMBER, the formula (and time complexity), for the number of combinations
# (of r items) from a set (of size n) is (n+r-1)!/(r!*(n-1)!), so tread lightly...
# Time Complexity:  O((n+r-1)!/(r!*(n-1)!)), which reduces to O(n**3), where n is the number of elements in the list.
# Space Complexity: O(1) (assuming itertools generators are O(1)).
def has_distinct_three_sum_naive(l, t):
    if l is not None and t is not None:
        for combination in itertools.combinations(l, 3):
            if sum(combination) is t:
                return True
    return False


# Distinct Set Approach:  Iterating over the list values, using a set to quickly check if there exists three distinct
# values in the set, x, y, and z, where t = x + y + z, if so return True, False otherwise.
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space complexity: O(n) for the set, O(n) for the result list, where n is the number of elements in the list.
def has_distinct_three_sum_set(l, t):
    if l is not None and t is not None:
        elements = set(l)
        if len(elements) > 2:
            for x in elements:
                for y in elements:
                    z = t - x - y
                    if x != y != z != x and z in elements:
                        return True
    return False


# Distinct Invariant Approach:  Find a l[x] + l[y] = t - l[z] if such entries exists.  The invariant is that if two
# elements which sum to the desired value t exists, they must lie within the sublist currently under construction.
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


args = [([11, 2, 5, 7, 3], 21),
        ([11, 7, -2, 2, 1, 4], 6),
        ([11, 7, -2, 2, 1, 4], 10),
        ([2, 4], 6),
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
       has_distinct_three_sum_bf,       # Variation: Distinct three elements.
       has_distinct_three_sum_naive,    # Variation: Distinct three elements.
       has_distinct_three_sum_set,      # Variation: Distinct three elements.
       has_distinct_three_sum]          # Variation: Distinct three elements.

for fn in fns:
    for l, t in args:
        print(f"{fn.__name__}({l}, {t}): {fn(l, t)}")
    print()


