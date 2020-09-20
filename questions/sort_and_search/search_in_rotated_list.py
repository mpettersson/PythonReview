"""
    SEARCH IN ROTATED LIST (CCI 10.3)

    Given a sorted list of n integers that has been rotated an unknown number of times, write code to find an element
    in the list.  You may assume that the array was originally sorted in increasing order.

    Example:
        Input = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5
        Output = 8
"""


# Naive Approach:  This isn't what the interviewer wants...  Time complexity is O(s), where s is the number of elements
# in l.  Space complexity is O(1).
def search_rotated_list_naive(l, n):
    if l is not None and n is not None and len(l) > 0:
        for i, v in enumerate(l):
            if v is n:
                return i


# Recursive Approach: Time complexity without duplicates (the best case) is O(log s), where s is the number of elements
# in l. With duplicates (worst case) time complexity is O(s), where s is the number of elements in l. Space complexity
# is O(log s), where s is the number of elements in l.
def search_rotated_list_rec(l, n):

    def _search_rotated_list_rec(l, n, lo, hi):
        if lo <= hi:
            mid = (hi + lo) // 2
            if l[mid] is n:
                return mid
            if l[lo] is l[hi]:                                          # If l[lo] == l[hi], then search both.
                res = _search_rotated_list_rec(l, n, lo, mid-1)
                return res if res is not None else _search_rotated_list_rec(l, n, mid+1, hi)
            if l[lo] < l[mid]:                                          # Sorted left.
                if l[lo] <= n < l[mid]:                                 # n is in left.
                    return _search_rotated_list_rec(l, n, lo, mid-1)
                else:                                                   # n isn't in left.
                    return _search_rotated_list_rec(l, n, mid+1, hi)
            elif l[mid] < n <= l[hi]:                                   # Sorted right.
                return _search_rotated_list_rec(l, n, mid+1, hi)        # n is in right.
            else:
                return _search_rotated_list_rec(l, n, lo, mid-1)        # n isn't in right.

    if l is not None and n is not None and len(l) > 0:
        return _search_rotated_list_rec(l, n, 0, len(l) - 1)


# Iterative Approach: Time complexity without duplicates (the best case) is O(log s), where s is the number of elements
# in l. With duplicates (worst case) time complexity is O(s), where s is the number of elements in l. Space complexity
# is O(1).
def search_rotated_list(l, n):
    if l is not None and n is not None and len(l) > 0:
        lo = 0
        hi = len(l) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if l[mid] is n:
                return mid
            if l[lo] is l[hi]:              # If l[lo] == l[hi], then search both.
                lo += 1
            elif l[lo] < l[mid]:            # Sorted left.
                if l[lo] <= n < l[mid]:     # n is in left.
                    hi = mid - 1
                else:                       # n isn't in left.
                    lo = mid + 1
            elif l[mid] < n <= l[hi]:       # Sorted right.
                lo = mid + 1                # n is in right.
            else:
                hi = mid - 1                # n isn't in right.


args = [([52, 75, 80, 92, 99, -95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49], 10),
        ([52, 75, 80, 92, 99, -95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49], -1),
        ([4, 5, 5, 2, 2, 2, 2, 2, 3], 4),
        ([3, 4, 5, 5, 2, 2, 2, 2, 2], 4),
        ([2, 3, 4, 5, 5, 2, 2, 2, 2], 4),
        ([2, 2, 3, 4, 5, 5, 2, 2, 2], 4),
        ([2, 2, 2, 3, 4, 5, 5, 2, 2], 4),
        ([2, 2, 2, 2, 3, 4, 5, 5, 2], 4),
        ([2, 2, 2, 2, 2, 3, 4, 5, 5], 4),
        ([5, 2, 2, 2, 2, 2, 3, 4, 5], 4),
        ([5, 5, 2, 2, 2, 2, 2, 3, 4], 4),
        ([5, 5, 2, 2, 2, 2, 2, 3, 4], 1),
        ([5], 5),
        ([], 5),
        ([5], -1),
        ([], None),
        (None, None)]

for l, n in args:
    print(f"rotated_list_search_naive({l}, {n}):", search_rotated_list_naive(l, n))
print()

for l, n in args:
    print(f"search_rotated_list_rec({l}, {n}):", search_rotated_list_rec(l, n))
print()

for l, n in args:
    print(f"search_rotated_list({l}, {n}):", search_rotated_list(l, n))


