"""
    QUICK SELECT

    Average Runtime:    O(n)
    Worst Runtime:      O(n**2)
    Best Runtime:       O(n)
    Space Complexity:   O(log(n))
    Alg Paradigm:       Divide and Conquer
    Sorting In Place:   Yes
    Stable:             No      (the default alg changes the relative order of elements with equal keys)
    Online:             No      (can search a list as it receives it)

    Select the kth smallest element in an unordered list; pick a random element (convention uses last), then swap the
    elements such that all of the elements smaller than it comes before, and everything larger comes after.
    Recursively do this on the part with k (different than Quick Sort).
"""


def quick_select(arr, k):
    return quick_select_rec(arr, 0, len(arr) - 1, k)


def quick_select_rec(arr, l, r, k):
    # if k is smaller than number of  elements in array
    if 0 < k <= r - l + 1:

        # Partition the array around last element and get position of pivot element in sorted array
        index = partition(arr, l, r)

        # if position is same as k
        if index - l == k - 1:
            return arr[index]

        # If position is more, recur for left subarray
        if index - l > k - 1:
            return quick_select_rec(arr, l, index - 1, k)
        return quick_select_rec(arr, index + 1, r, k - index + l - 1)
    return None


# Partition is the same as Quick Sorts partition.
def partition(arr, l, r):
    pivot = arr[r]
    i = l

    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


k_list = [-1, 0, 6, 9, 20, 22]
orig_list = [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 33]
print("orig_list:", orig_list)
print("sorted(orig_list):", sorted(orig_list))
print()

for k in k_list:
    print("quick_select(orig_list,", k, "):", quick_select(orig_list, k))






