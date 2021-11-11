"""
    HAS TWO SUM SORTED

    Write a function that accepts a SORTED list l and an integer total t, then returns True if there exists two elements
    in the list with the sum t, False otherwise.

    Example:
        Input = [-2, 1, 2, 4, 7, 11], 6
        Output = True
"""


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
def has_two_sum_bf(l, t):
    if l is not None and t is not None:
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[i] + l[j] == t and i != j:
                    return True
    return False


# APPROACH: Two Pointer/Invariant (Invariant: A Condition That Remains True During Execution)
#
# In this case the invariant is the sublist (l[lo:hi+1]) that holds the solution, if it exits.  Two pointers are used,
# one pointing at the lowest and one pointing at the highest value.  The pointers are incremented/decremented until
# either the desired total value is found or the lower index is no longer less than the higher index.
#
# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(1).
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


args = [([-4, -1, 0, 1, 2], 0),
        ([-2, 1, 2, 4, 7, 11], 6),
        ([-2, 1, 2, 4, 7, 11], 10),
        ([2, 4], 6),
        ([0, 0], 0),
        ([3], 6),
        ([6], 6),
        ([-2, -1, 0, 3, 5, 6, 7, 9, 13, 14], 6),
        ([], 6),
        ([-2, 1, 2, 4, 7, 11], None),
        (None, 6),
        (None, None)]
fns = [has_two_sum_bf,
       has_two_sum]

for l, n in args:
    for fn in fns:
        print(f"{fn.__name__}({l}, {n}): {fn(l, n)}")
    print()


