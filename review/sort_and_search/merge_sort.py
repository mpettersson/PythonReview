"""
    MERGE SORT

    Average Runtime:    O(n log(n))
    Worst Runtime:      O(n log(n))
    Best Runtime:       O(n log(n))
    Space Complexity:   O(n)
    Alg Paradigm:       Divide and Conquer
    Sorting In Place:   No      (in a typical implementation)
    Stable:             Yes     (does not change the relative order of elements with equal keys)
    Online:             NO      (can sort a list as it receives it)

    Find the middle index.
    Call Merge Sort on everything up to (and including) the middle.
    Call Merge Sort on everything after the middle.
    Merge the sorted halves.
"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left; only one will ever be True.
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


import copy
orig_list = [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 100]
l = copy.deepcopy(orig_list)
l.sort()
print(l)

sorted_list = copy.deepcopy(orig_list)
merge_sort(sorted_list)

print(sorted_list)

