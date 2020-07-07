"""
    PEAKS AND VALLEYS

    In an array of integers, a "peak" is an element which is greater than or equL to the adjacent integers and a
    "valley" is an element which is less than or equal to the adjacent integers.  For example, in the array
    [5,8,6,2,3,4,6], [8,6] are peaks and [5,2] are valleys.
    Given an array of integers, sort the array into an alternating sequence of peaks and valleys.
"""
import sys


# OPTIMAL O(n) APPROACH IFF MINIMAL DOUBLES:
# Starting at index = 0,
# compare index to index - 1, and index + 1, moving the largest value to index, then increment by 2
def peaks_and_valleys(arr):
    i = 0
    while i < len(arr):
        biggest_index = max_index(arr, i, i - 1, i + 1)
        if i != biggest_index:
            arr[i], arr[biggest_index] = arr[biggest_index], arr[i]
        i += 2


def max_index(arr, a, b, c):
    arr_len = len(arr)
    a_val = arr[a] if a >= 0 and a < arr_len else -sys.maxsize - 1
    b_val = arr[b] if b >= 0 and b < arr_len else -sys.maxsize - 1
    c_val = arr[c] if c >= 0 and c < arr_len else -sys.maxsize - 1
    max_val = max(a_val, max(b_val, c_val))
    if a_val == max_val:
        return a
    elif b_val == max_val:
        return b
    else:
        return c


def peaks_and_valleys_suboptimal(arr):
    if len(arr) < 3:
        return arr

    # Mergesort
    merge_sort(arr)

    # Rearrange
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]

    i = j = k = 0
    while i < len(left) and j < len(right):
        arr[k] = right[j]
        arr[k + 1] = left[i]
        k += 2
        i += 1
        j += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[0:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [75, 45, -29, 41, -28, 10, 27, 99, 49, -75, -28, 80, -28, -59, -95, -79, -62, 92, 52, 21]
print(arr)
peaks_and_valleys(arr)
print(arr)

arr_w_doubs = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print(arr_w_doubs)
peaks_and_valleys(arr_w_doubs)
print(arr_w_doubs)

print(arr_w_doubs)
peaks_and_valleys_suboptimal(arr_w_doubs)
print(arr_w_doubs)