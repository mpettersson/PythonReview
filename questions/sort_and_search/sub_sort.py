"""
    SUB SORT

    Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n,
    the entire array would be sorted.  Minimize n - m (that is, find the smallest such sequence).

    Example:
        Input = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        Output = (3, 9)
"""


def sub_sort(l):
    garbled_min = None
    garbled_max = None
    curr_max = None
    for i in l:
        if curr_max is None or curr_max < i:
            curr_max = i
        if i < curr_max and garbled_min is None or i < curr_max and i < garbled_min:
            garbled_min = i
            garbled_max = curr_max
    m = 0
    n = 0
    for i in l:
        if garbled_min > i:
            m += 1
        if i < garbled_max:
            n += 1

    return (m, n)


input = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(sub_sort(input))