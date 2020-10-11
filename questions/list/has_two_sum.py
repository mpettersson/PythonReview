"""
    HAS TWO SUM

    Write a function that accepts a SORTED list l and a number t, then returns True if there exists two elements in the
    list that sum to the number t, False otherwise.

    Example:
        Input = [-2, 1, 2, 4, 7, 11], 6
        Output = True

    Variations:
        - SEE: pairs_with_sum.py
        - SEE: has_three_sum.py
        - SEE: has_k_sum.py
"""


# Naive/Brute Force Approach:  Time complexity is O(n**2), where n is the number of elements in the list.  Space
# complexity is O(1).
def has_two_sum_naive(l, t):
    if l is not None and t is not None:
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[i] + l[j] == t and i != j:
                    return True
        return False


# Invariant Approach:  Remember, an invariant is a condition that remains true during execution.  In this case the
# invariant is the subarray (l[lo:hi+1]), that holds the solution, if it exits.  Time complexity is O(n), where n is the
# number of elements in the list.
def has_two_sum(l, t):
    if l is not None and t is not None:
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


args = [([-2, 1, 2, 4, 7, 11], 6),
        ([-2, 1, 2, 4, 7, 11], 10),
        ([2, 4], 6),
        ([6], 6),
        ([-2, -1, 0, 3, 5, 6, 7, 9, 13, 14], 6),
        ([], 6),
        ([-2, 1, 2, 4, 7, 11], None),
        (None, 6),
        (None, None)]

for l, n in args:
    print(f"has_two_sum_naive({l}, {n}): {has_two_sum_naive(l, n)}")
print()

for l, n in args:
    print(f"has_two_sum({l}, {n}): {has_two_sum(l, n)}")


