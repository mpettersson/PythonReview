"""
    BINARY SEARCH 

    Average Runtime:    O(log (n))
    Worst Runtime:      O(log (n))
    Best Runtime:       O(1)
    Auxiliary Space:    O(1) Iterative, O(log(n)) Recursive
    
    Compare x with the middle element.
    If x matches with middle element, we return the mid index.
    If x is greater than the mid, then x can only lie in right half (after mid). So we recur for right half.
    Else (x is smaller) recur for the left half.

"""


# Iterative Approach
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    
    return None


# Recursive Approach
def binary_search_rec(arr, x):
    return _binary_search_rec(arr, x, 0, len(arr) - 1)


def _binary_search_rec(arr, x, low, high):
    if low > high:
        return

    mid = (low + high) // 2
    if arr[mid] < x:
        return _binary_search_rec(arr, x, mid + 1, high)
    elif arr[mid] > x:
        return _binary_search_rec(arr, x, low, mid - 1)
    else:
        return mid


is_in_list = 10;
not_in_list = -1;
print("is_in_list:", is_in_list)
print("not_in_list:", not_in_list)
l_unsorted = [75, 45, -29, 41, -28, 10, 27, 99, 49, -75, -28, 80, -28, -59, -95, -79, -62, 92, 52, 21]
l_sorted = sorted(l_unsorted)
print("l_unsorted:", l_unsorted)
print("l_sorted:", l_sorted)
print()

print("Test Iterative and Recursive Approaches with value in list:")
print("binary_search(l_sorted, is_in_list):", binary_search(l_sorted, is_in_list))
print("binary_search_rec(l_sorted, is_in_list):", binary_search_rec(l_sorted, is_in_list))
print()

print("Test Iterative and Recursive Approaches with value not in list:")
print("binary_search(l_sorted, not_in_list):", binary_search(l_sorted, not_in_list))
print("binary_search_rec(l_sorted, not_in_list):", binary_search_rec(l_sorted, not_in_list))



