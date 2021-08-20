"""
    FIND MISSING ELEMENT

    Given a list of n distinct integers, each between 0 and n-1 (inclusive), implying that exactly one number between
    0 and n-1 is missing, write a function to find the missing elements in O(n) time and O(1) space.

    Example:
        Input = [5, 3, 0, 1, 2]
        Output = 4

    Variations:
        SEE: find_duplicate_element.py, find_duplicate_and_missing_elements.py, and missing_two.py.
"""
import functools
import math
import random


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify the question (is zero included, is n included, etc...)?
#   - What will the data type be (floats, ints)?
#   - Can the list be modified?


# Wrong Approaches:
#   Sorting:  O(n log(n)) time, O(1) space.
#   Dictionary/Bytearray: O(n) time, O(n) space.


# APPROACH: Calculate Product (*)
#
# Using the properties of multiplication, calculate the product of all of the values in the list (not including zero),
# then divide by the expected product to find the missing value, or element.
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(1).
#
# NOTE: The numbers get very large, very fast..
def find_missing_element_via_product(l):        # For the range 0 to n-1.
    if l:
        n = len(l)
        list_product = actual_product = 1
        if 0 in l:
            for e in l:
                if e > 0:
                    list_product *= e
            for v in range(1, n + 1):
                actual_product *= v
            return actual_product // list_product
        else:
            return 0

# NOTE: The following could be used for the range 1 to N (not the specified 0 to N-1):
# def find_missing_element_via_product_1_to_n(l):
#     n = len(l) + 1
#     list_product = functools.reduce((lambda x, y: x * y), l)
#     actual_product = functools.reduce((lambda x, y: x * y), [x for x in range(1, n + 1)])
#     return actual_product // list_product


# APPROACH: Calculate Summed Squares
#
# This approach also leverages the properties of multiplication by adding the squares values, finding the difference
# (compared to the expected value), then returning the square root of the found value.
#
# Time complexity: O(n), where n is the length of the list.
# Space complexity: O(1).
#
# NOTE: These values don't get as big as the products above!
def find_missing_element_via_summed_squares(l):             # for 0 to N-1
    if l:
        n = len(l)
        list_sqr_sum = sqr_sum_to_n = 0
        if 0 in l:
            for e in l:
                if e > 0:
                    list_sqr_sum += e * e
            for v in range(1, n + 1):
                sqr_sum_to_n += v ** 2
            return int(math.sqrt(sqr_sum_to_n - list_sqr_sum))
        else:
            return 0

# NOTE: The following could be used for the range 1 to N (not the specified 0 to N-1):
# def find_missing_element_via_summed_squares_1_to_n(l):
#     n = len(l) + 1
#     sqr_sum_to_n = sum(list(map((lambda x: x**2), [x for x in range(1, n + 1)])))
#     list_sqr_sum = sum(list(map((lambda x: x**2), l)))
#     return int(math.sqrt(sqr_sum_to_n - list_sqr_sum))


# APPROACH: Summation Formula
#
# Using the closed form equation ((n - 1) * n) / (2), we can determine what the sum from 0 to n ought to be.
# Using the given list we know what n should be (via len), so we can compare the total sum to the sum of the list.
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(1).
#
# NOTE: This only works if you start at 0; if starting at 1, change the equation to: ((n + 1) * n) / (2).
def find_missing_element_via_sum(l):
    if l is not None:
        n = len(l) + 1
        return (n * (n - 1) // 2) - sum(l)      # Closed form expression sum 0 to n-1,
        # return (n * (n + 1) // 2) - sum(l)    # Closed form expression for Sum 1 to n.


# APPROACH: XOR
#
# Return the XOR of all the numbers from 0 to n and the XOR of all of the numbers in the provided list.
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(1).
def find_missing_element_via_xor(l):
    if l is not None:
        n = len(l) + 1
        xor_all = functools.reduce(lambda a, x: a ^ x, [i for i in range(n)], 0)
        xor_l = functools.reduce(lambda a, x: a ^ x, l, 0)
        return xor_all ^ xor_l


nums = [10, 20, 50, 100]
fns = [find_missing_element_via_product,
       find_missing_element_via_summed_squares,
       find_missing_element_via_sum,
       find_missing_element_via_xor]

for n in nums:
    l = [i for i in range(n)]
    random.shuffle(l)
    missing = l.pop()
    print(f"\nList l (n:{n}, missing element:{missing}): {l}\n")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l[:])}")
    print()


