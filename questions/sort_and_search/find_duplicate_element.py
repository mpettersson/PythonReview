"""
    FIND DUPLICATE ELEMENT (leetcode.com/problems/find-the-duplicate-number)

    You are given a list of n+1 integers, each between 0 and n-1, inclusive, with exactly one element appearing twice,
    write a function to return the duplicate number in O(n) time and O(1) space?

    Example:
        Input = [5, 3, 0, 1, 2, 4, 3]
        Output = 3

    Variations:
        SEE: find_missing_element.py, find_duplicate_and_missing_elements.py, and missing_two.py.

    TODO:
        - SEE LEETCODE SOLUTIONS.
"""
import functools
import random


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Can the list be modified?


# WRONG APPROACHES:
#   Sorting: O(n log(n)) time, O(1) space.
#   Dictionary/Bytearray: O(n) time, O(n) space.


# APPROACH: Summation/Formula
#
# Using the equation ((n-1)n)/(2), we can determine what the sum from 0 to n ought to be.  Using the given list we know
# what n should be (via len), so we can simply compare the total sum to the sum of the list.
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(1).
#
# NOTE: This only works if you start at 0; if starting at 1, change the equation to ((n+1)n)/(2).
def find_duplicate_element_via_sum(l):
    if l is not None:
        n = len(l) - 1
        return sum(l) - (((n - 1) * n) // 2)


# APPROACH: XOR
#
# Return the XOR of all the numbers from 0 to n and the XOR of all of the numbers in the provided list.
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(1).
def find_duplicate_element_via_xor(l):
    if l is not None:
        n = len(l) - 1
        xor_all = functools.reduce(lambda a, x: a ^ x, [i for i in range(n)], 0)
        xor_l = functools.reduce(lambda a, x: a ^ x, l, 0)
        return xor_all ^ xor_l


nums = [10, 20, 50, 100]
fns = [find_duplicate_element_via_sum,
       find_duplicate_element_via_xor]

for n in nums:
    l = [i for i in range(n)]
    duplicate = random.choice(l)
    l.append(duplicate)
    random.shuffle(l)
    print(f"List l (n is {n}):", l, f"\nDuplicate element: {duplicate}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l)}")
    print()


