"""
    INSERTION SORT

    Average Runtime:    O(n**2)
    Worst Runtime:      O(n**2) (elements are sorted in reverse order)
    Best Runtime:       O(n)    (elements are already sorted)
    Space Complexity:   O(1)
    Alg Paradigm:       Incremental Approach
    Sorting In Place:   Yes
    Stable:             Yes     (does not change the relative order of elements with equal keys)
    Online:             Yes     (can sort a list as it receives it)

    Like sorting a deck of cards, you have a sorted side (usually right) and an unsorted side (usually left).
    You compare one card at a time, starting with the second card, moving it to the correct place in the sorted side.
    Increasing the sorted side by one card at a time.
"""


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


import copy
orig_list = [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 33]
l = copy.deepcopy(orig_list)
l.sort()
print(l)

sorted_list = copy.deepcopy(orig_list)
insertion_sort(sorted_list)

print(sorted_list)
