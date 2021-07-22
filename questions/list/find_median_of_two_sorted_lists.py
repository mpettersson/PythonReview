"""
    FIND MEDIAN OF TWO SORTED LISTS (50CIQ 1: MEDIAN OF ARRAYS
                                     leetcode.com/problems/median-of-two-sorted-arrays)

    Write a function which accepts two sorted lists and returns the median.

    Example:
        Input = [1, 3, 5], [2, 4, 6]
        Output = 3.5
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Are the lists the same length?
#   - If the total number of elements is even, should the two median elements be returned or the average of the two?


# APPROACH: Naive/Combine Then Sort
#
# Simply create a new list consisting of the two provided lists, sort the new list, then return the median of the new
# list.
#
# Time Complexity: O((m + n) * log(m + n)), where m and n are the number of elements in a and b.
# Space Complexity: O(m + n), where m and n are the number of elements in a and b.
def find_median_of_two_sorted_lists_naive(a, b):
    l = None
    if a is None or b is None:
        l = a if a else b
    else:
        l = a + b
        l.sort()
    if l:
        mid = len(l) // 2
        return l[mid] if len(l) % 2 == 1 else (l[mid - 1] + l[mid]) / 2


# APPROACH: Merge/Build Sorted List
#
# Construct a new sorted list via two pointers, one pointing to the current element to be considered from each list,
# then copy the lower of the two elements to the new list and increment the associated pointer.  Once a new sorted list
# is produced, return the median.
#
# Time Complexity: O(m + n), where m and n are the number of elements in a and b.
# Space Complexity: O(m + n), where m and n are the number of elements in a and b.
def find_median_of_two_sorted_lists_via_merge(a, b):
    if a or b:
        l = []
        if a and b:
            p = q = 0
            while p < len(a) and q < len(b):
                if a[p] < b[q]:
                    l.append(a[p])
                    p += 1
                else:
                    l.append(b[q])
                    q += 1
            while p < len(a):
                l.append(a[p])
                p += 1
            while q < len(b):
                l.append(b[q])
                q += 1
        else:
            l = a if a else b
        s = len(l)
        if s % 2 == 1:
            return l[s//2]
        return (l[s//2] + l[s//2 - 1]) / 2


# APPROACH: Recursive
#
# If the total number of elements is odd then simply find the median, or the kth smallest element where
# k = (len(a) + len(b)) // 2, or if even find the kth AND k-1th smallest elements recursively via the get_kth function.
# The get_kth function is similar to binary search, HOWEVER, for each call only ONE of the two lists search
# areas is reduced by half (the other is unaffected).  Once a list is eliminated, then simply return the kth offset
# into the remaining list as the median value.
#
# Time Complexity: O(log(m + n)), where m and n are the number of elements in a and b.
# Space Complexity: O(log(m + n)), where m and n are the number of elements in a and b.
def find_median_of_two_sorted_lists_rec(a, b):

    def get_kth(a, b, a_lo, a_hi, b_lo, b_hi, k):
        if a_lo > a_hi:                 # if done searching a:
            return b[k - a_lo]              # just return the kth value (minding the lo offset) of b.
        if b_lo > b_hi:                 # if done searching b:
            return a[k - b_lo]              # just return the kth value (minding the lo offset) of a.
        a_mid = (a_lo + a_hi) // 2      # else update mid indices and:
        b_mid = (b_lo + b_hi) // 2
        if a_mid + b_mid < k:               # if k is lo/left:
            if a[a_mid] > b[b_mid]:
                return get_kth(a, b, a_lo, a_hi, b_mid + 1, b_hi, k)
            return get_kth(a, b, a_mid + 1, a_hi, b_lo, b_hi, k)
        else:                               # if k is mid or hi/right:
            if a[a_mid] > b[b_mid]:
                return get_kth(a, b, a_lo, a_mid - 1, b_lo, b_hi, k)
            return get_kth(a, b, a_lo, a_hi, b_lo, b_mid - 1, k)

    a_len = len(a) if a else 0
    b_len = len(b) if b else 0
    if a_len + b_len > 0:
        if (a_len + b_len) % 2 == 1:
            return get_kth(a, b, 0, a_len - 1, 0, b_len - 1, (a_len + b_len) // 2)
        mid_sum = get_kth(a, b, 0, a_len - 1, 0, b_len - 1, (a_len + b_len) // 2)
        mid_sum += get_kth(a, b, 0, a_len - 1, 0, b_len - 1, ((a_len + b_len) // 2) - 1)
        return mid_sum / 2


# APPROACH: Optimal
#
# Time Complexity: O(log(min(m, n))), where m and n are the number of elements in a and b.
# Space Complexity: O(1).
def find_median_of_two_sorted_lists(a, b):
    if a or b:
        a_len = len(a) if a else 0
        b_len = len(b) if b else 0
        if a_len < b_len:
            a_len, b_len = b_len, a_len
            a, b = b, a
        lo = 0
        hi = 2 * b_len
        while lo <= hi:
            mid2 = (lo + hi) // 2
            mid1 = a_len + b_len - mid2
            lo_val_1 = -float('inf') if mid1 == 0 else a[(mid1 - 1) // 2]
            lo_val_2 = -float('inf') if mid2 == 0 else b[(mid2 - 1) // 2]
            hi_val_1 = float('inf') if mid1 == a_len * 2 else a[mid1 // 2]
            hi_val_2 = float('inf') if mid2 == b_len * 2 else b[mid2 // 2]
            if lo_val_1 > hi_val_2:
                lo = mid2 + 1
            elif lo_val_2 > hi_val_1:
                hi = mid2 - 1
            else:
                return (max(lo_val_1, lo_val_2) + min(hi_val_1, hi_val_2)) / 2


# APPROACH: Optimal (Verbose)
#
# SEE: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
#
# Time Complexity: O(log(min(m, n))), where m and n are the number of elements in a and b.
# Space Complexity: O(1).
def find_median_of_two_sorted_lists_alt(a, b):
    if a or b:
        a_len = len(a) if a else 0
        b_len = len(b) if b else 0
        if a_len > b_len:
            a, b, a_len, b_len = b, a, b_len, a_len
        lo, hi, half_len = 0, a_len, (a_len + b_len + 1) // 2
        while lo <= hi:
            i = (lo + hi) // 2
            j = half_len - i
            if i < a_len and b[j - 1] > a[i]:               # i is too small, must increase it
                lo = i + 1
            elif i > 0 and a[i - 1] > b[j]:                 # i is too big, must decrease it
                hi = i - 1
            else:                                           # i is perfect
                if i == 0:
                    max_of_left = b[j - 1]
                elif j == 0:
                    max_of_left = a[i - 1]
                else:
                    max_of_left = max(a[i - 1], b[j - 1])
                if (a_len + b_len) % 2 == 1:
                    return max_of_left
                if i == a_len:
                    min_of_right = b[j]
                elif j == b_len:
                    min_of_right = a[i]
                else:
                    min_of_right = min(a[i], b[j])
                return (max_of_left + min_of_right) / 2.0


lists = [([1, 3, 5], [2, 4, 6]),
         ([1, 3, 5], [2, 4]),
         ([1, 2, 3], [4, 5, 6]),
         ([3, 7, 9, 15, 18, 21, 25], [4, 6, 8, 10, 11, 18]),
         ([4, 6, 8, 10, 11, 18], [3, 7, 9, 15, 18, 21, 25]),
         ([-5, -3, 13, 13, 20, 27, 35, 38, 39, 46], [-5, 0, 4, 13, 15, 25, 29, 30, 33, 36, 39, 40, 41, 45]),
         ([-5, -5, -3, 0, 4, 13, 13, 13, 15, 20, 25, 27, 29, 30, 33, 35, 36, 38, 39, 39, 40, 41, 45], [46]),
         ([46], [-5, -5, -3, 0, 4, 13, 13, 13, 15, 20, 25, 27, 29, 30, 33, 35, 36, 38, 39, 39, 40, 41, 45]),
         ([-3, 13, 13, 20, 27, 35, 38, 39, 46], [-5, 0, 4, 13, 15, 25, 29, 30, 33, 36, 39, 40, 41, 45]),
         ([-5, -3, 0, 4, 13, 13, 13, 15, 20, 25, 27, 29, 30, 33, 35, 36, 38, 39, 39, 40, 41, 45], [46]),
         ([46], [-5, -3, 0, 4, 13, 13, 13, 15, 20, 25, 27, 29, 30, 33, 35, 36, 38, 39, 39, 40, 41, 45]),
         ([1, 2, 3, 4, 5, 6], [0]),
         ([0, 1, 2, 3, 4, 5], [6]),
         ([1, 2, 3, 4, 5, 6], []),
         ([1, 2, 3, 4, 5, 6], None),
         ([0], [1, 2, 3, 4, 5, 6]),
         ([6], [0, 1, 2, 3, 4, 5]),
         ([], [1, 2, 3, 4, 5, 6]),
         ([1, 2, 3, 4, 5, 6], []),
         ([], [1, 2, 3, 4, 5]),
         ([1, 2, 3, 4, 5], []),
         (None, [1, 2, 3, 4, 5, 6]),
         ([1, 2, 3, 4, 5, 6], None),
         (None, [1, 2, 4, 5, 6]),
         ([1, 2, 4, 5, 6], None),
         ([], []),
         (None, []),
         (None, None)]
fns = [find_median_of_two_sorted_lists_naive,
       find_median_of_two_sorted_lists_via_merge,
       find_median_of_two_sorted_lists_rec,
       find_median_of_two_sorted_lists,
       find_median_of_two_sorted_lists_alt]

for l1, l2 in lists:
    for fn in fns:
        print(f"{fn.__name__}({l1}, {l2}): {fn(l1, l2)}")
    print()


