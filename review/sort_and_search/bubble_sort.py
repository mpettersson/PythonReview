"""
    BUBBLE SORT

    Average Runtime:    O(n**2)
    Worst Runtime:      O(n**2)
    Best Runtime:       O(n)
    Space Complexity:   O(1)
    Alg Paradigm:       Incremental Approach
    Sorting In Place:   Yes
    Stable:             Yes    (does not change the relative order of elements with equal keys)
    Online:             No     (can not sort a list as it receives it)

    Start at the beginning of the array and swap the first two elements if the first is greater than the seconds.
    Then, continue on with the next pair, and next, until it is sorted.
"""


def bubble_sort(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, n):
            if arr[i + 1] < arr[i]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n -= 1


import copy
orig_list = [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 33]
l = copy.deepcopy(orig_list)
l.sort()
print(l)

sorted_list = copy.deepcopy(orig_list)
bubble_sort(sorted_list)

print(sorted_list)
