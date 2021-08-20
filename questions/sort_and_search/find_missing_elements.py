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


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify the question (is zero included, is n included, etc...)?
#   - What will the data type be (floats, ints)?
#   - Can the list be modified?


# APPROACH: XOR With Pivot
#
# This approach first sums both the provided list of numbers and the series of natural numbers from 1 to N.  Once these
# pieces of information are found, the sum of the missing numbers and a a pivot value (the sum of the missing numbers
# divided by two--this is due to the fact that the two missing numbers are NOT equal to each other) is computed. Then,
# all natural numbers in the range one to the pivot value are XORed, all natural numbers in the range pivot plus one to
# N are XORed, and the list is iterated over one last time XORing the values less than or equal to the pivot and XORing
# the value greater than the pivot.  Once the four XORed values have been found, the two less than (or equal to) the
# pivot are XORed and returned as one missing value, and the two higher than the pivot are XORed and returned as the
# second missing value.
#
# Time Complexity: O(n), where n is the length of the list.
# Space complexity: O(1).
def find_missing_elements_via_xor(l):
    n = len(l) + 2
    complete_sum = n * (n + 1) // 2             # Sum of natural numbers 1 to N: 1 + 2 + ... + N-1 + N = N(N + 1)/2
    list_sum = sum(l)
    pivot = (complete_sum - list_sum) // 2      # BC missing_num_a != missing_num_b, we can divide the difference of the
    complete_xor_low = 0                        # sums by 2, and obtain a PIVOT (missing_num_a < pivot < missing_num_b).
    complete_xor_high = 0
    for i in range(1, pivot + 1):               # For all natural number, compute the low (or less than or equal to the
        complete_xor_low ^= i                   # pivot) and high (greater than pivot) XOR values.
    for i in range(pivot + 1, n + 1):
        complete_xor_high ^= i
    list_xor_low = 0
    list_xor_high = 0
    for i in l:                                 # For all the numbers in the supplied list, compute the low (or less
        if i <= pivot:                          # than or equal to the pivot) and high (greater than pivot) XOR values.
            list_xor_low ^= i
        else:
            list_xor_high ^= i
    return complete_xor_low ^ list_xor_low, complete_xor_high ^ list_xor_high   # XOR lows and highs for missing nums!


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
fns = [find_missing_elements,
       find_missing_elements_via_xor]

for n in nums:
    l = [i for i in range(1, n + 1)]
    random.shuffle(l)
    missing = (l.pop(), l.pop())
    print(f"List l (n:{n}, missing elements:{missing}): {l}\n")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l)}")
    print()


