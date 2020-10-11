"""
    HAS THREE SUM (EPI 18.4: THE 3-SUM PROBLEM)

    Design an algorithm that takes as input a list and a number, and determines if there are three entries in the list
    (NOT NECESSARILY DISTINCT) which add up to the specified number.

    Example:
        Input = [11, 2, 5, 7, 3], 21
        Output = True   # either [2, 7, 11] OR [5, 5, 11]

    Variations:
        - SEE: pairs_with_sum.py
        - SEE: has_two_sum.py
        - SEE: has_k_sum.py
        - Solve the same problem when the three elements must be distinct.
        - Solve the same problem when k, the number of elements to sum, is an additional input.
        - Write a program that takes as input a list of integers l and an integer t, and returns a 3-tuple
          (l[x], l[y], l[z]) where z, y, z are all distinct, minimizing abs(t - (l[x] + l[y] + l[z])), and
          l[x] <= l[y] <=l[z].
        - Write a program that takes as input a list of integers l and an integer t, and returns the number of 3-tuples
          (z, y, z) such that l[x] + l[y] + l[z] <= t and l[x] <= l[y] <=l[z].
"""
import itertools


# Naive/Brute Force Approach:  REMEMBER, the formula (and time complexity), for the number of combinations (of r items)
# from a set (of size n) is (n+r-1)!/(r!*(n-1)!), so tread lightly...
# Time complexity (reduced from above) is O(n**3), where n is the number of elements in the list.  Space complexity is
# O(1) (because of itertools use of generators).
def has_three_sum_naive(l, t):
    if l is not None and t is not None:
        for combination in itertools.combinations_with_replacement(l, 3):
            if sum(combination) is t:
                return True
        return False


# NOTE: A different naive approach, with same time/space complexity as above, is to use 3 nested loops:
def has_three_sum_alt_naive(l, t):
    if l is not None and t is not None:
        for i in range(len(l)):
            for j in range(len(l)):             # BC duplicates CAN be used, start at 0, not i + 1
                for k in range(len(l)):         # BC duplicates CAN be used, start at 0, not j + 1
                    if l[i] + l[j] + l[k] == t:
                        return True
        return False


# REMEMBER: An invariant is a condition that remains true during execution.

# Invariant Approach:  Find a l[x] + l[y] = t - l[z] if such entries exists.  The invariant is that if two elements
# which sum to the desired value t exists, they must lie within the subarray currently under construction.
# Time complexity is O(n**2) (or, O(n * log(n)) for the sort and O(n) to find the pair that adds to t), where n is the
# number of elements in the list.  Space complexity is O(1).
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
        l.sort()
        for i in l:
            if has_two_sum(l, t - i):
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

for l, t in args:
    print(f"has_three_sum_naive({l}, {t}): {has_three_sum_naive(l, t)}")
print()

for l, t in args:
    print(f"has_three_sum_alt_naive({l}, {t}): {has_three_sum_alt_naive(l, t)}")
print()

for l, t in args:
    print(f"has_three_sum({l}, {t}): {has_three_sum(l, t)}")


