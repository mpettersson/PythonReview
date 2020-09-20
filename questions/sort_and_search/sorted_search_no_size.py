"""
    SORTED SEARCH, NO SIZE (CCI 10.4)

    You are given a list/array-like data structure, Listy, which lacks a size method.  It does, however, have an
    element_at(i) method that returns the element at index i in O(1) time.  If i is beyond the bounds of the data
    structure, it returns -1.  (For this reason, the data structure only supports positive integers.) Given a Listy,
    which contains sorted, positive integers, find the index at which an element x occurs.  If x occurs multiple times,
    you may return any index.
"""
import random


# Naive Approach:  Time complexity is O(n), where n is the length of l (listy), space complexity is O(1).
def sorted_search_no_size_naive(l, x):
    if l is not None and x is not None:
        i = 0
        v = l.element_at(i)
        while v > 0:
            if v is x:
                return i
            i += 1
            v = l.element_at(i)


# Find Length (_get_high_first:) & Binary Search Approach:  Time complexity is O(log(n)), where n is the length of
# l (listy), and space complexity is O(1).
def sorted_search_no_size_get_high_first(l, x):

    def _get_high_first(l):
        i = 0
        while 0 <= l.element_at(i) and l.element_at(i + 1) != -1:
            p = 0
            while 0 <= l.element_at(2 ** p + i):
                p += 1
            i += 2 ** (p - 1)
        return i

    if l is not None and x is not None:
        lo = 0
        hi = _get_high_first(l)
        if hi is not None:
            while lo <= hi:
                mid = (lo + hi) // 2
                if l.element_at(mid) is x:
                    return mid
                if x < l.element_at(mid):
                    hi = mid - 1
                else:
                    lo = mid + 1


# Optimal Approach:  REMEMBER; You DON'T need to know the last index for binary search to work!  Time complexity is
# O(log(n)), where n is the size of l (listy), and space complexity is O(1).
def sorted_search_no_size(l, x):
    if l is not None and x is not None:
        hi = 1
        while l.element_at(hi) != -1 and l.element_at(hi) < x:
            hi *= 2
        lo = hi // 2
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_val = l.element_at(mid)
            if x < mid_val or mid_val == -1:
                hi = mid - 1
            elif mid_val < x:
                lo = mid + 1
            else:
                return mid


class Listy:
    def __init__(self, val_range=(0, 1000), len_range=(500, 1000)):
        self.l = None
        if 0 <= len_range[0] <= len_range[1] and 0 <= val_range[0] <= val_range[1]:
            rand_range = random.randint(len_range[0], len_range[1])
            self.l = [random.randint(val_range[0], val_range[1]) for _ in range(rand_range)]
            self.l.sort()
        else:
            raise ValueError("Invalid Range")

    def element_at(self, i):
        try:
            return self.l[i]
        except:
            return -1

    def get_test_nums(self, k):
        try:
            return random.choices(self.l, k=k)
        except:
            return []


listy = Listy()
nums = listy.get_test_nums(5) + [0, 100, 1000, 1500, -10, None]

print("Listy's Secret Length:", len(listy.l))
print("Listy's Secret Elements:", listy.l)
print()

for x in nums:
    print(f"sorted_search_no_size_naive(listy, {x})", sorted_search_no_size_naive(listy, x))
print()

for x in nums:
    print(f"sorted_search_no_size_get_high_first(listy, {x})", sorted_search_no_size_get_high_first(listy, x))
print()

for x in nums:
    print(f"sorted_search_no_size(listy, {x})", sorted_search_no_size(listy, x))


