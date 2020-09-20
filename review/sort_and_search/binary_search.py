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
    if l is not None and x is not None and len(l) > 0:
        lo = 0
        hi = len(l) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if l[mid] < x:
                lo = mid + 1
            elif l[mid] > x:
                hi = mid - 1
            else:
                return mid


# Recursive Approach:
def binary_search_rec(l, x):

    def _binary_search_rec(l, x, lo, hi):
        if lo <= hi:
            mid = (lo + hi) // 2
            if l[mid] < x:
                return _binary_search_rec(l, x, mid + 1, hi)
            elif l[mid] > x:
                return _binary_search_rec(l, x, lo, mid - 1)
            else:
                return mid

    if l is not None and x is not None and len(l) > 0:
        return _binary_search_rec(l, x, 0, len(l) - 1)


args = [([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], 10),
        ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], -1),
        ([], 5),
        ([5], 5),
        ([5], -1),
        ([], None),
        (None, None)]

for l, x in args:
    print(f"binary_search({l}, {x}):", binary_search(l, x))
print()

for l, x in args:
    print(f"binary_search_rec({l}, {x}):", binary_search_rec(l, x))
print()


