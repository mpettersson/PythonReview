"""
    QUICK SORT

    Average Runtime:    O(n log(n))
    Worst Runtime:      O(n**2)
    Best Runtime:       O(n log(n))
    Space Complexity:   O(log(n))
    Alg Paradigm:       Divide and Conquer
    Sorting In Place:   Yes
    Stable:             No      (the default alg changes the relative order of elements with equal keys)
    Online:             No      (can sort a list as it receives it)

    Pick a random element (convention uses last), then swap the elements such that all of the elements smaller than
    it comes before, and everything larger comes after. Recursively do this on the "smaller" and "larger" elements.
"""


def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, left, right):
    if left < right:
        index = _partition(arr, left, right)
        _quick_sort(arr, left, index - 1)
        _quick_sort(arr, index + 1, right)


def _partition(arr, left, right):
    # i will be the index of the last item smaller than the pivot.
    i = left - 1
    pivot = arr[right]

    for j in range(left, right):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


import copy
orig_list = [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 33]
l = copy.deepcopy(orig_list)

sorted_list = copy.deepcopy(orig_list)
quick_sort(sorted_list)

print(sorted_list)

l.sort()
print(l)
