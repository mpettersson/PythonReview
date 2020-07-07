"""
    SUM SWAP

    Given two arrays of integers, find a pair of values (one value from each array) that you can swap to give the two
    arrays the same sum.

    Example:
        input = [4, 1, 2, 1, 1, 2], [3, 6, 3, 3]
        output = [1, 3]
"""


# Approach 1:  Brute Force; runtime of O(AB)
def sum_swap(l1, l2):
    l1_sum = sum(l1)
    l2_sum = sum(l2)
    if l1_sum > l2_sum:  # To minimize if statement below.
        l1_sum, l2_sum = l2_sum, l1_sum
        l1, l2 = l2, l1
    diff = l2_sum - l1_sum
    for i in l1:
        for j in l2:
            if i < j and i + j == diff:
                return [i, j]


# Approach 2:  Optimized via set; runtime of O(A+B)
def sum_swap_optimized(l1, l2):
    l1_sum = sum(l1)
    l2_sum = 0
    l2_set = set()
    for i in l2:
        l2_sum += i
        l2_set.add(i)
    diff = abs(l1_sum - l2_sum)
    for i in l1:
        if diff - i in l2_set:
            return [i, diff - i]


list_one = [4, 1, 2, 1, 1, 2]
list_two = [3, 6, 3, 3]
print("list_one:", list_one)
print("list_two:", list_two)
print("sum_swap(list_one, list_two):", sum_swap(list_one, list_two))
print("sum_swap_optimized(list_one, list_two):", sum_swap_optimized(list_one, list_two))



