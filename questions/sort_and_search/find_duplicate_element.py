"""
    FIND (THE) DUPLICATE ELEMENT

    You are given a list of n+1 integers, each between 0 and n-1, inclusive, with exactly one element appearing twice,
    how would you compute the duplicate number in O(n) time and O(1) space?

    Example:
        Input = [5, 3, 0, 1, 2, 4, 3]
        Output = 3

    Variations:
        SEE: find_missing_element.py, find_duplicate_and_missing_elements.py, and missing_two.py.
"""
import functools
import random

# Wrong Approaches:
#   Sorting: O(n log(n)) time, O(1) space.
#   Dictionary/Bytearray: O(n) time, O(n) space.


# Sum Approach: Using the equation ((n-1)n)/(2), we can determine what the sum from 0 to n ought to be.  Using the given
# list we know what n should be (via len), so we can simply compare the total sum to the sum of the list.
# O(n) time complexity, where n is the length of the list, and O(1) space.
# NOTE: This only works if you start at 0; if starting at 1, change the equation to ((n+1)n)/(2).
def find_duplicate_element_via_sum(l):
    if l is not None:
        n = len(l) - 1
        return sum(l) - (((n - 1) * n) // 2)


# XOR Approach:  Return the XOR of all the numbers from 0 to n and the XOR of all of the numbers in the provided list.
# O(n) time complexity, where n is the length of the list, and O(1) space.
def find_duplicate_element_via_xor(l):
    if l is not None:
        n = len(l) - 1
        xor_all = functools.reduce(lambda a, x: a ^ x, [i for i in range(n)], 0)
        xor_l = functools.reduce(lambda a, x: a ^ x, l, 0)
        return xor_all ^ xor_l


nums = [1, 10, 100]

for n in nums:
    l = [i for i in range(n)]
    duplicate = random.choice(l)
    l.append(duplicate)
    random.shuffle(l)
    print(f"List l (n is {n}):", l)
    print(f"Duplicate element: {duplicate}")
    print(f"find_duplicate_element_via_sum(l): {find_duplicate_element_via_sum(l)}")
    print(f"find_duplicate_element_via_xor(l): {find_duplicate_element_via_xor(l)}\n")


