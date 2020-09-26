"""
    MISSING TWO (CCI 17.19)

    You are given an array with all the numbers from 1 to N appearing exactly once, except for one number that is
    missing.  How can you find the missing number in O(N) time and O(1) space?

    Example:
        Input = [5, 3, 1, 2]
        Output = 4

    What if there were two numbers missing?

        Input = [5, 1, 2]
        Output = 3, 4

    Variations:
        SEE: find_missing_element.py, find_duplicate_element.py, find_duplicate_and_missing_elements.py.
"""
import functools
import math
import random


# Product (*) Approach: Find the missing value by dividing the product of 1 to n by the product of the given list.
# Time complexity is O(n), where n is the length of the list. Space complexity is O(1).
# NOTE: The numbers get very large, very fast...
def find_missing_one_via_product(l):
    n = len(l) + 1
    list_product = functools.reduce((lambda x, y: x * y), l)
    actual_product = functools.reduce((lambda x, y: x * y), [x for x in range(1, n + 1)])
    return actual_product // list_product


# Sum Squared Approach: Find the missing value by using the square root of the difference of the calculated sum of 1**2
# to N**2 from the sum of squared values in the list.  Time complexity is O(n), where n is the length of the list.
# Space complexity is O(1).
# NOTE: These values don't get as big as the products above!
def find_missing_one_via_summed_squares(l):
    n = len(l) + 1
    sqr_sum_to_n = sum(list(map((lambda x: x**2), [x for x in range(1, n + 1)])))
    list_sqr_sum = sum(list(map((lambda x: x**2), l)))
    return int(math.sqrt(sqr_sum_to_n - list_sqr_sum))


# Sum Approach: Find the missing value by subtracting the calculated sum of 1 to n (using the closed from expression
# ((n + 1) * n)/(2)) from the sum of the given list. Time complexity is O(n), where n is the length of the list.
# Space complexity is O(1).
def find_missing_one_via_sum(l):
    n = len(l) + 1
    return (n * (n + 1) // 2) - sum(l)  # Sum via closed form expression.


# Sum Approach (Missing Two Variation): Find two values via applying the sum of the list and the sum of the squared list
# equations to the quadratic formula.
#
# Equations:
#   x + y = sum_diff
#   x**2 + y**2 = sum_sqr_diff
#   ax**2 + bx + x    ->    x = (-b +- math.sqrt(b**2 - 4ac)) / 2a
#
# Time complexity is O(n), where n is the length of the list. Space complexity is O(1).
def find_missing_two(l):
    n = len(l) + 2
    sum_diff = (n * (n + 1) // 2) - sum(l)
    sum_sqr_diff = sum(list(map((lambda x: x**2), [x for x in range(1, n + 1)]))) - sum(list(map((lambda x: x**2), l)))
    a = 2
    b = -2 * sum_diff
    c = sum_diff * sum_diff - sum_sqr_diff
    missing_x = int(((-1 * b) + math.sqrt(b * b - 4 * a * c)) // (2 * a))
    missing_y = sum_diff - missing_x
    return missing_x, missing_y


nums = [2, 10, 100]

for n in nums:
    l = [i for i in range(1, n + 1)]
    random.shuffle(l)
    print(f"List l (n is {n}):", l[:-1])
    print(f"Missing (first) element: {l.pop()}")
    print(f"find_missing_one_via_product(l): {find_missing_one_via_product(l)}")
    print(f"find_missing_one_via_summed_squares(l): {find_missing_one_via_summed_squares(l)}")
    print(f"find_missing_one_via_sum(l): {find_missing_one_via_sum(l)}")
    print(f"Missing (second) element: {l.pop()}")
    print(f"find_missing_two(l): {find_missing_two(l)}\n")


