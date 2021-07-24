"""
    FIND MISSING ELEMENTS (CCI 17.19: MISSING TWO)

    Given a list with all the numbers from 1 to N appearing exactly once, except for two numbers, write a function to
    find the missing numbers in O(N) time and O(1) space?

        Input = [5, 1, 2]
        Output = 3, 4

    Variations:
        SEE: find_missing_element.py, find_duplicate_element.py, find_duplicate_and_missing_elements.py.
"""
import math
import random


# APPROACH: Summed Squares & Quadratic Formula:
#
# Find two values via applying the sum of the list and the sum of the squared list equations to the quadratic formula.
# Equations:
#   x + y = sum_diff
#   x**2 + y**2 = sum_sqr_diff
#   ax**2 + bx + x    ->    x = (-b +- math.sqrt(b**2 - 4ac)) / 2a
#
# Time Complexity: O(n), where n is the length of the list.
# Space complexity: O(1).
def find_missing_elements(l):
    n = len(l) + 2
    sum_diff = (n * (n + 1) // 2) - sum(l)
    sum_sqr_diff = sum(list(map((lambda x: x**2), [x for x in range(1, n + 1)]))) - sum(list(map((lambda x: x**2), l)))
    a = 2
    b = -2 * sum_diff
    c = sum_diff * sum_diff - sum_sqr_diff
    missing_x = int(((-1 * b) + math.sqrt(b * b - 4 * a * c)) // (2 * a))
    missing_y = sum_diff - missing_x
    return missing_x, missing_y


nums = [10, 20, 50, 100]
fns = [find_missing_elements]

for n in nums:
    l = [i for i in range(1, n + 1)]
    random.shuffle(l)
    missing = (l.pop(), l.pop())
    print(f"List l (n is {n}): {l}\nMissing Elements: {missing}",)
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l)}\n")
    print()


