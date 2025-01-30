"""
    BINARY SEARCH 

    Average Runtime:    O(log (n))
    Worst Runtime:      O(log (n))
    Best Runtime:       O(1)
    Auxiliary Space:    O(1) Iterative, O(log(n)) Recursive
    
    Compare x with the middle element.
    If x matches with middle element, we return the middle index.
    If x is greater than the middle, then x can only lie in right half; recurse/iterate on the right half.
    Else (x is smaller) recurse/iterate on the left half.
"""


# APPROACH: Iterative
def binary_search(l, x):
    if l is not None and x is not None and len(l) > 0:
        left = 0
        right = len(l) - 1
        while left <= right:
            mid = (left + right) // 2
            if x < l[mid]:
                right = mid - 1
            elif l[mid] < x:
                left = mid + 1
            else:
                return mid


# APPROACH: Recursive
def binary_search_rec(l, x):

    def _rec(l, x, left, right):
        if left <= right:
            mid = (left + right) // 2
            if l[mid] < x:
                return _rec(l, x, mid + 1, right)
            elif l[mid] > x:
                return _rec(l, x, left, mid - 1)
            else:
                return mid

    if l is not None and x is not None and len(l) > 0:
        return _rec(l, x, 0, len(l) - 1)


args_list = [([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], 10),
             ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], -1),
             ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], -28),
             ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], -100),
             ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], 100),
             ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], -95),
             ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], 99),
             ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], -60),
             ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], 60),
             ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], -75),
             ([-95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49, 52, 75, 80, 92, 99], 75),
             ([], 5),
             ([5], -5),
             ([5], 4),
             ([5], 5),
             ([5], 6),
             ([], None),
             (None, None)]
fns = [binary_search,
       binary_search_rec]

for l, x in args_list:
    for fn in fns:
        print(f"{fn.__name__}({l}, {x}): {fn(l, x)}")
    print()


