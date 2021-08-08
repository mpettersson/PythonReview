"""
    SELECTION SORT

    Average Runtime:    O(n**2)
    Worst Runtime:      O(n**2)
    Best Runtime:       O(n**2)
    Space Complexity:   O(1)
    Alg Paradigm:       Incremental Approach
    Sorting In Place:   Yes
    Stable:             No      (default does change the relative order of elements with equal keys)
    Online:             No      (can't sort a list as it receives it)

    Think of a child's algorithm...
    Put the smallest in first index...

    Given a list, take the current element (starting at 0) and exchange it with the smallest element on the right hand
    side of the current element. Continue doing this, incrementing the index of current element by 1 until it's sorted.
"""
import copy


def selection_sort(arr):
    if len(arr) > 1:
        for i in range(len(arr)):
            min_i = i
            for j in range(i + 1, len(arr)):
                if arr[min_i] > arr[j]:
                    min_i = j
            arr[i], arr[min_i] = arr[min_i], arr[i]


orig_list = [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 33]
l = copy.deepcopy(orig_list)
l.sort()
print(l)

sorted_list = copy.deepcopy(orig_list)
selection_sort(sorted_list)

print(sorted_list)
