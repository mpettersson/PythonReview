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


# Iterative Approach:
def binary_search(l, x):
    if not x or not l or l is []:
        return
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] < x:
            low = mid + 1
        elif l[mid] > x:
            high = mid - 1
        else:
            return mid
    return


# Recursive Approach:
def binary_search_rec(l, x):
    if not x or not l or l is []:
        return

    def _binary_search_rec(l, x, low, high):
        if low > high:
            return
        mid = (low + high) // 2
        if l[mid] < x:
            return _binary_search_rec(l, x, mid + 1, high)
        elif l[mid] > x:
            return _binary_search_rec(l, x, low, mid - 1)
        else:
            return mid

    return _binary_search_rec(l, x, 0, len(l) - 1)


args = [([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], 10),
        ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], -1),
        ([], 5),
        ([5], 5),
        ([5], -1),
        ([], None),
        (None, None)]

for l, x in args:
    print(f"x: {x}, l: {l}")
    print("binary_search(l, x):", binary_search(l, x))
    print("binary_search_rec(l, x):", binary_search_rec(l, x))
    print()



