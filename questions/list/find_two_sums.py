"""
    FIND TWO SUMS

    Write a function, which accepts a list and a number, then returns a list of all non-duplicate pairs which sum to the
    specified number.

    Example:
        Input = [-2, 1, 2, 4, 7, 11], 6
        Output = [(2, 4)]

    Variations:
        - Same question, however, duplicate list values are acceptable.
"""
import copy
import itertools


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Are the numbers in the list unique?
#   - Can there be duplicates numbers in a result set?
#   - Can there be duplicate sets in the result list?


# APPROACH: Naive/Brute Force
#
# Loop over every pair and add any that sum to t and are not the same value to the results.
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space complexity: O(n) for the result list, where n is the number of elements in the list.
from typing import List


def find_two_sums_naive_bf(l, t):
    if l is not None and t is not None:
        result = []
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[i] != l[j] and l[i] + l[j] is t:
                    result.append((l[i], l[j]))
        return result if result else None


# APPROACH: Naive/Combinations
#
# Use itertools combinations to get all two element combinations of the list, adding any that sum to t and do not
# contain repeat values.  REMEMBER, the formula (and time complexity), for the number of combinations (of r items) from
# a set (of size n) is (n+r-1)!/(r!*(n-1)!), so tread lightly...
#
# Time Complexity:  O((n+r-1)!/(r!*(n-1)!)), which reduces to O(n**2), where n is the number of elements in the list.
# Space complexity: O(n) for the result list, where n is the number of elements in the list.
def find_two_sums_via_combinations(l, t):
    if l is not None and t is not None:
        result = []
        for s in itertools.combinations(l, 2):
            if sum(s) is t and s[0] != s[1]:
                result.append(s)
        return result if result else None


# APPROACH: Sort & Search
#
# Sort the list, then use a low and high pointer to unilaterally search for pairs with the given sum.
#
# Time Complexity: O(n * log(n)), where n is the number of elements in the list.
# Space complexity: O(n) for the result list, where n is the number of elements in the list.
def find_two_sums_via_sort_n_search(l, t):
    if l is not None and t is not None:
        result = []
        l.sort()                                    # O(n * log(n)) to sort.
        lo = 0
        hi = len(l) - 1
        while lo < hi:                              # O(n) to search.
            temp = l[lo] + l[hi]
            if temp == t:
                if l[lo] != l[hi]:
                    result.append((l[lo], l[hi]))
                lo += 1
                hi -= 1
            elif temp < t:
                lo += 1
            else:
                hi -= 1
        return result if result else None


# APPROACH: Via Set
#
# Iterating over the list values v, using a set to quickly check if there exists a non duplicate compliment value c such
# that v + c = t.  If such values exist, add them to the results list.
#
# Time Complexity: O(n), where n is the number of elements in the list.
# Space complexity: O(n) for the set, O(n) for the result list, where n is the number of elements in the list.
def find_two_sums_via_set(l, t):
    if l is not None and t is not None:
        result = []
        elements = set()
        for x in l:
            complement = t - x
            if complement in elements and x not in elements:
                result.append((x, complement))
            elements.add(x)
        return result if result else None


# we want to return the indices of x,y that equal target... Since we have x for each iteration, we know that each y is
# (y = target - x). So, we map each y to the index of the current num x, since we know that it solves the equation.
def twoSum(nums: List[int], target: int) -> List[int]:
    if nums and target is not None:
        x_to_iy = {}
        for i_x, x in enumerate(nums):
            i_y = x_to_iy.get(x)                    # if the y for this number is found
            if i_y is not None:                     # return i_x and i_y
                return [nums[i_x], nums[i_y]]
            else:
                x_to_iy[target - x] = i_x           # if i_y isn't set, set it as cur i_x


args = [([13, 0, 14, -2, -1, 7, 9, 5, 3, 6], 6),
        ([0, 1, 1, 1, 1, 1, 1, 1, 2], 2),
        ([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8], 0),
        ([-2, 1, 2, 4, 7, 11], 6),
        ([-2, 1, 2, 4, 7, 11], 10),
        ([3], 6),
        ([2, 4], 6),
        ([6], 6),
        ([-2, -1, 0, 3, 5, 6, 7, 9, 13, 14], 6),
        ([], 6),
        ([-2, 1, 2, 4, 7, 11], None),
        (None, 6),
        (None, None)]
fns = [find_two_sums_naive_bf,
       find_two_sums_via_combinations,
       find_two_sums_via_sort_n_search,
       find_two_sums_via_set,
       twoSum]

for l, n in args:
    for fn in fns:
        print(f"{fn.__name__}({l}, {n}): {fn(copy.copy(l), n)}")
    print()


