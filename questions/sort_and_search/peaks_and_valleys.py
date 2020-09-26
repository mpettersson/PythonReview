"""
    PEAKS AND VALLEYS (CCI 10.11)

    In a list of integers, a "peak" is an element which is greater than or equal to the adjacent integers and a
    "valley" is an element which is less than or equal to the adjacent integers.  For example, in the list
    [5, 8, 6, 2, 3, 4, 6], [8,6] are peaks and [5,2] are valleys.  Given a list of integers, sort the list into an
    alternating sequence of peaks and valleys.

    Example:
        Input = [5, 3, 1, 2, 3]
        Output = [5, 1, 3, 2, 3]
"""
import sys


# Naive Approach:  This probably isn't what the interviewer wants (but it'll handle more cases than the optimal approach
# below).  Time complexity is O(n log(n)), where n is the number of element in the lst.
def peaks_and_valleys_naive(lst):
    if lst is not None:
        l = sorted(lst)
        temp = [l.pop()] if len(l) % 2 is 1 else []
        return temp + [y for x in zip(l[:len(l) // 2], l[len(l) // 2:]) for y in x]


# Sub-Optimal Approach:  Start at index 1, swap the value with the previous value, increasing the index by 2, until the
# end.  This will move small <= medium <= large to medium >= small <= large.  Time complexity is O(n log(n)), where n
# is the number of elements in lst.
# NOTE: This still doesn't fix/address the issue when there are many duplicates.
def peaks_and_valleys_suboptimal(lst):
    if lst is not None:
        l = lst[:]
        if len(l) > 2:
            l.sort()
            for i in range(1, len(l), 2):
                l[i], l[i - 1] = l[i - 1], l[i]
        return l


# Optimal (IFF MINIMAL DUPLICATES) Approach:  Starting at index 0, compare the value at index to index - 1, and
# index + 1, moving the largest value to index, then increment by 2.  Time complexity (IFF minimal duplicates) is O(n)
# where n is the number of items in the lst.
def peaks_and_valleys(lst):

    def max_index(l, a, b, c):
        a_val = l[a] if 0 <= a < len(l) else -sys.maxsize - 1
        b_val = l[b] if 0 <= b < len(l) else -sys.maxsize - 1
        c_val = l[c] if 0 <= c < len(l) else -sys.maxsize - 1
        max_val = max(a_val, b_val, c_val)
        if a_val is max_val:
            return a
        elif b_val is max_val:
            return b
        else:
            return c

    if lst is not None:
        l = lst[:]
        for i in range(1, len(l), 2):
            biggest_index = max_index(l, i - 1, i, i + 1)
            if i != biggest_index:
                l[i], l[biggest_index] = l[biggest_index], l[i]
        return l


lists = [[75, 45, -29, 41, -28, 10, 27, 49, -75, -28, 80, -28, -59, -79, -62, 92, 52, 21],
         [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],
         [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [0, 0, 1],
         [0, 1, 1],
         [0,1],
         [42],
         None]
fns = [peaks_and_valleys_naive, peaks_and_valleys_suboptimal, peaks_and_valleys]

for fn in fns:
    for l in lists:
        print(f"{fn.__name__}({l}): {fn(l)}")
    print()


