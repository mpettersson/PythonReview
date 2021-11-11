"""
    FIND TWO SUMS

    Write a function, which accepts an integer list l and an integer total t, then returns a unique list of two-tuples,
    each consisting of two distinct elements from the list, that sum to t.

    Example:
        Input = [2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2], 2
        Output = [(1, 1), (0, 2)]
"""
import copy
import itertools


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Are the numbers in the list unique?
#   - Can there be duplicates numbers in a result set?
#   - Can there be duplicate pairs/sets in the result list?
#   - Can the list be modified?


# APPROACH: Naive/Brute Force
#
# Loop over every pair and add any that sum to t and are not the same value to the results.
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space complexity: O(n) for the result list, where n is the number of elements in the list.
def find_two_sums_via_bf(l, t):
    if l is not None and t is not None:
        result = set()
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[i] <= l[j] and l[i] + l[j] is t:
                    result.add((l[i], l[j]))
        return list(result) if result else None


# APPROACH: Naive/Combinations
#
# Use itertools combinations to get all two element combinations of the list, adding any that sum to t and do not
# contain repeat values.
#
# Time Complexity:  O(n!/(k!*(n-k)!)), which reduces to O(n**2), where n is the number of elements in the list.
# Space complexity: O(n) for the result list, where n is the number of elements in the list.
#
# REMEMBER: The formula (and time complexity), for the number of combinations (of k items) from a set of size n is:
#               n!/(k!*(n-k)!)
def find_two_sums_via_comb(l, t):
    if l is not None and t is not None:
        result = set()
        for s in itertools.combinations(l, 2):
            if sum(s) is t and s[0] <= s[1]:
                result.add(s)
        return list(result) if result else None


# APPROACH: Via Set
#
# Iterating over the list values v, using a set to quickly check if there exists a non duplicate complement value c such
# that v + c = t.  If such values exist, add them to the results list.
#
# Time Complexity: O(n), where n is the number of elements in the list.
# Space complexity: O(n) for the set, O(n) for the result list, where n is the number of elements in the list.
def find_two_sums_via_set(l, t):
    if l is not None and t is not None:
        result = set()
        s = set()                                   # Seen values set.
        for x in l:
            complement = t - x
            if complement in s:
                result.add((x, complement) if x < complement else (complement, x))
            s.add(x)
        return list(result) if result else None


# APPROACH: Via Dictionary
#
# This approach is essentially the same as the set approach above except that a dictionary, mapping values to indices,
# has been used in place of a set.
#
# Time Complexity: O(n), where n is the number of elements in the list.
# Space complexity: O(n) for the dictionary, O(n) for the result list, where n is the number of elements in the list.
def find_two_sums_via_dict(l, t):
    if l is not None and t is not None:
        result = set()
        d = {}                                      # value: index
        for i, x in enumerate(l):
            complement = t - x
            if complement in d:
                result.add((x, complement) if x < complement else (complement, x))
            else:
                d[x] = i
        return list(result) if result else None


# APPROACH: Via Two Pointer
#
# Sort the list, then use a low and high pointer to unilaterally search for pairs with the given sum.
#
# Time Complexity: O(n * log(n)), where n is the number of elements in the list.
# Space complexity: O(n) for the result list, where n is the number of elements in the list.
def find_two_sums_via_pointer(l, t):
    if l is not None and t is not None:
        result = set()
        l.sort()                                    # O(n * log(n)) to sort.
        lo = 0
        hi = len(l) - 1
        while lo < hi:                              # O(n) to search.
            temp = l[lo] + l[hi]
            if temp == t:
                result.add((l[lo], l[hi]))
                lo += 1
                hi -= 1
            elif temp < t:
                lo += 1
            else:
                hi -= 1
        return list(result) if result else None


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
fns = [find_two_sums_via_bf,
       find_two_sums_via_comb,
       find_two_sums_via_set,
       find_two_sums_via_dict,
       find_two_sums_via_pointer]

for l, n in args:
    for fn in fns:
        print(f"{fn.__name__}({l}, {n}): {fn(copy.copy(l), n)}")
    print()


