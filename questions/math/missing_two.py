"""
    MISSING TWO

    You are given an array with all the numbers from 1 to N appearing exactly once, except for one number that is
    missing.  How can you find the missing number in O(N) time and O(1) space?

    What if there were two numbers missing?
"""
import functools
import math


# Find one missing value by dividing the product of 1 to N by the product of the given list.
# NOTE: The numbers get very large, very fast...
def find_missing_one_via_product(l):
    n = len(l) + 1
    list_product = functools.reduce((lambda x, y: x * y), l)
    actual_product = functools.reduce((lambda x, y: x * y), [x for x in range(1, n + 1)])
    return actual_product // list_product


# Find one missing value by the square root of the difference of the calculated sum of 1**2 to N**2 from the sum of
# squared values in the list.
# NOTE: These values don't get as big as the products above!
def find_missing_one_via_summed_squares(l):
    n = len(l) + 1
    sqr_sum_to_n = sum(list(map((lambda x: x**2), [x for x in range(1, n + 1)])))
    list_sqr_sum = sum(list(map((lambda x: x**2), l)))
    return int(math.sqrt(sqr_sum_to_n - list_sqr_sum))


# Find one missing value by subtracting the calculated sum from 1 to N from the sum of the given list.
def find_missing_one_via_sum(l):
    n = len(l) + 1
    return (n * (n + 1) // 2) - sum(l)  # Sum via closed form expression.


# Find two values via applying the sum of the list and the sum of the squared list equations to the quadratic formula.
# Equations:
#   x + y = sum_diff
#   x**2 + y**2 = sum_sqr_diff
#   ax**2 + bx + x    ->    x = (-b +- math.sqrt(b**2 - 4ac)) / 2a
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


num_list = [3, 34, 67, 18, 19, 28, 45, 4, 15, 63, 74, 29, 76, 17, 7, 14, 48, 24, 85, 57, 52, 22, 31, 30, 70, 83, 84, 62,
            47, 93, 90, 37, 38, 66, 73, 55, 87, 46, 20, 72, 86, 54, 96, 5, 6, 89, 68, 40, 43, 1, 71, 61, 10, 12, 64, 32,
            80, 50, 82, 59, 13, 8, 53, 58, 81, 42, 98, 60, 2, 39, 11, 21, 35, 77, 9, 51, 79, 56, 92, 94, 97, 16, 95, 26,
            78, 49, 65, 33, 88, 75, 100, 36, 25, 27, 44, 91, 99, 41, 23]
print("num_list:", num_list)
print()

print("find_missing_one_via_product(num_list):", find_missing_one_via_product(num_list))
print("find_missing_one_via_summed_squares(num_list):", find_missing_one_via_summed_squares(num_list))
print("find_missing_one_via_sum(num_list):", find_missing_one_via_sum(num_list))
print("find_missing_two(num_list):", find_missing_two(num_list))






