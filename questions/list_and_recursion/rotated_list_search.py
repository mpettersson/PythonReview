"""
    ROTATED LIST SEARCH (CCI 10.3: SEARCH IN ROTATED LIST,
                         leetcode.com/problems/search-in-rotated-sorted-array-ii
                         leetcode.com/problems/search-in-rotated-sorted-array)

    Write a function, which accepts a sorted then rotated list (l) and a target value (t), then returns the index of the
    target value if it is in the list, None otherwise.

    Example:
        Input = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5
        Output = 8
"""
import copy
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What was the sort order?
#   - Are there DUPLICATE values in the list?
#   - What are the size limits of the list?
#   - Are the values negative & positive?
#   - What data type does the list contain?


# OBSERVATIONS:
#   - If NO Duplicate Values:
#       - Then 1 SIDE, at most, will be out of order.
#       - Find the side that is ORDERED, then check if it contains the target value, else, check the other side.
#   - If DUPLICATES Values:
#       - There are three possibilities for the low/mid/high values:
#           - 3 are different (None are the same).
#           - 1 is different (2 are the same).
#           - None are different (3 are the same).
#       - If low/mid/high values are all the same, CAN'T eliminate a side (just increment by one, or O(n) time...).
#       - If low/high values are the same, still CAN'T eliminate a side (just increment by one, or O(n) time...).
#       - In some circumstances, can eliminate a side (i.e., if low < mid values and the target isn't in that range).
#
# NOTE: It really helps to draw the list as a graph; where the index is the x coordinate and value is y coordinate.


# APPROACH: List Index Method
#
# This approach seems to be the fastest.  However, this probably isn't what the interviewer wants...
#
# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(1).
def search_rotated_list_via_index(l, t):
    try:
        return l.index(t)
    except (ValueError, AttributeError):
        pass


# APPROACH: Naive Search
#
# This approach simply iterates over the values of the list; if the desired target value is found, then its index is
# returned.  However, this probably isn't what the interviewer wants...
#
# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(1).
def search_rotated_list_naive(l, t):
    if l is not None and t is not None and len(l) > 0:
        for i, v in enumerate(l):
            if v is t:
                return i


# APPROACH: Recursive (Modified Binary Search)
#
# This approach is a modified binary search. After considering the above observations, systematically modify the binary
# search algorithm (after checking if the middle value is what you are looking for) to first check if either the
# low/high value is less than, greater than, or equal to the middle value.  For each of the three cases, modify the
# low and high values.  Note, if the low/high value is equal to the middle value, then only low/high is
# incremented/decremented.
#
# Time Complexity: O(log(n)) if the list only contains DISTINCT values, else O(n), where n is the size of the list.
# Space Complexity: O(log(n)), where n is the number of elements in the list.
def search_rotated_list_rec(l, t):

    def _rec(l, t, lo, hi):
        if lo < hi:
            mid = (hi + lo) // 2
            if l[mid] == t:
                return mid
            if l[mid] < l[hi]:                  # If the RIGHT side IS sorted:
                if l[mid] <= t < l[hi]:             # If the target IS IN the RIGHT side:
                    return _rec(l, t, mid+1, hi)        # Continue ONLY with the RIGHT side.
                return _rec(l, t, lo, mid-1)        # Else, ONLY Continue on the LEFT side
            elif l[mid] > l[hi]:                # Else, if l[mid] > l[hi] IS True then the LEFT side IS SORTED:
                if l[lo] <= t < l[mid]:             # If the target value IS IN the (Sorted) LEFT side:
                    return _rec(l, t, lo, mid-1)        # ONLY continue with the LEFT side.
                return _rec(l, t, mid+1, hi)        # Else, ONLY continue on the RIGHT side.
            else:                               # Else, (l[mid] == l[hi]), just continue with high decremented...
                return lo if l[lo] == t else _rec(l, t, lo, hi-1)

    if l is not None and t is not None and len(l) > 0:
        return _rec(l, t, 0, len(l)-1)


# APPROACH: Iterative (Modified Binary Search)
#
# NOTE: This is probably the approach you will want to use in a programming interview situation.
#
# This approach is a modified binary search. After considering the above observations, systematically modify the binary
# search algorithm (after checking if the middle value is what you are looking for) to first check if either the
# low/high value is less than, greater than, or equal to the middle value.  For each of the three cases, modify the
# low and high values.  Note, if the low/high value is equal to the middle value, then only low/high is
# incremented/decremented.
#
# Time Complexity: O(log(n)) if the list only contains DISTINCT values, else O(n), where n is the size of the list.
# Space Complexity: O(1).
def search_rotated_list(l, t):
    if l is not None and t is not None and len(l) > 0:
        lo = 0
        hi = len(l) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if l[mid] == t:
                return mid
            if l[mid] < l[hi]:                  # If the RIGHT side IS sorted:
                if l[mid] < t <= l[hi]:             # If the target IS IN the RIGHT side:
                    lo = mid + 1                        # Update low, to ONLY continue with the RIGHT side.
                else:                               # Else, if the target IS NOT in the RIGHT side:
                    hi = mid - 1                        # Update high, to ONLY continue with the LEFT side.
            elif l[mid] > l[hi]:                # Else, if l[mid] > l[hi] IS True then the LEFT side IS SORTED:
                if l[lo] <= t < l[mid]:             # If the target value IS IN the (Sorted) LEFT side:
                    hi = mid - 1                        # Update high, to ONLY continue with the LEFT side.
                else:                               # Else (since the target IS NOT in the LEFT SORTED side):
                    lo = mid + 1                        # Update low, to ONLY continue with the RIGHT side.
            else:                               # Else, (if we are here l[mid] == l[hi]):
                hi -= 1                             # decrement high.
                # NOTE: At this point, we could add checks for the left side (see the next approach), however, it will
                #       not change the fact that the best we can do (for the right side) is to decrement high by one.
                #       The following approach
                #       explores additional checks for the left side, however,
        return lo if l[lo] == t else None       # This moves multiple checks from inside the loop to one check outside..


# APPROACH: Iterative (Modified Binary Search) With Extra Checks
#
# This is the above iterative approach with additional checks when the middle list value is the same as the high list
# value (See the note in the above approach.)
#
# NOTE: This isn't too much faster (than the two previous attempts) for lists with up to 1 million elements; therefore,
#       it may be easier to stick with the shorter/first iterative approach).
#
# Time Complexity: O(log(n)) if the list only contains DISTINCT values, else O(n), where n is the size of the list.
# Space Complexity: O(1).
def search_rotated_list_extra(l, t):
    if l is not None and t is not None and len(l) > 0:
        lo = 0
        hi = len(l) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if l[mid] == t:
                return mid
            if l[mid] < l[hi]:
                if l[mid] < t <= l[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif l[mid] > l[hi]:
                if l[lo] <= t < l[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                hi -= 1
                if l[lo] < l[mid]:
                    if l[lo] < t <= l[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                elif l[lo] == l[mid]:
                    lo += 1

        return lo if l[lo] == t else None


# APPROACH: Iterative With Binary Search
#
# This is just an interesting variation; whenever possible use binary search (in it's original form), else, increment
# low, or decrement high (if there are duplicates preventing binary search).
#
# NOTE: This isn't too much faster (than the two previous attempts) for lists with up to 1 million elements; therefore,
#       it may be easier to stick with the shorter/first iterative approach).
#
# Time Complexity: O(log(n)) if the list only contains DISTINCT values, else O(n), where n is the size of the list.
# Space Complexity: O(1).
def search_rotated_list_bin_search(l, t):

    def _binary_search(l, x, lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2
            if l[mid] < x:
                lo = mid + 1
            elif l[mid] > x:
                hi = mid - 1
            else:
                return mid

    if l is not None and t is not None and len(l) > 0:
        lo = 0
        hi = len(l) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if l[mid] == t:
                return mid
            if l[lo] == t:
                return lo
            if l[hi] == t:
                return hi
            if l[lo] < l[mid]:
                if l[lo] < t < l[mid]:
                    return _binary_search(l, t, lo+1, mid-1)
                else:
                    lo = mid + 1
            else:
                lo += 1
            if l[mid] < l[hi]:
                if l[mid] < t < l[hi]:
                    return _binary_search(l, t, mid+1, hi-1)
                else:
                    hi = mid - 1
            else:
                hi -= 1


# NOTE: If the list values are unique (no duplicates), then the following will work:
def search_rotated_list_unique_values(l, t):
    lo = 0
    hi = len(l) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if l[mid] == t:
            return mid
        elif l[mid] > l[lo]:
            if l[lo] <= t < l[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if l[hi] >= t > l[mid]:
                lo = mid + 1
            else:
                hi = mid - 1


# NOTE: To find the MINIMUM VALUE in a rotated list (with duplicates):
def min_value_in_rotated_list(l):
    lo = 0
    hi = len(l)-1
    if l[0] < l[-1]:                    # If it's in sorted order:
        return l[0]                         # Just return the first element.
    while lo < hi:
        mid = (lo + hi) // 2
        if l[mid] < l[hi]:              # Case 1:   The right side is sorted.
            hi = mid                                # Then the min value MUST be in the left side (or middle value).
        elif l[mid] > l[hi]:            # Case 2:   The right side is NOT sorted:
            lo = mid + 1                            # Then the min value MUST be in the right side.
        else:                           # Case 3:   Can't rule out either side (l[mid] == l[hi]):
            hi -= 1                                 # Just decrement high (but we keep l[mid], which has the same value)
    return l[hi]        # Return hi for how many 'times' the list was rotated right.


# NOTE: To find the MAXIMUM VALUE in a rotated list (with duplicates):
def max_value_in_rotated_list(l):
    if l is not None and len(l) > 0:
        lo = 0
        hi = len(l)-1
        if l[0] < l[-1]:                # If it's in sorted order:
            return l[-1]                     # Just return the last element.
        while lo <= hi:
            if hi - lo < 2:             # If just one or two elements left, just return the max...
                return max(l[hi], l[lo])
            mid = (lo + hi) // 2
            if l[lo] < l[mid]:          # Case 1: The max value MUST be in either the middle/pivot list value OR in the
                lo = mid                        # RIGHT side.
            elif l[lo] > l[mid]:        # Case 2: The max value MUST be LEFT of the middle/pivot list value.
                hi = mid-1
            else:                       # Case 3: Don't know for sure; but since the low list value is equal to the
                lo += 1                         # middle/pivot value, we can rule out the low list value.


args = [([52, 75, 80, 92, 99, -95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49], 10),
        ([52, 75, 80, 92, 99, -95, -79, -75, -62, -59, -29, -28, -28, -28, 10, 21, 27, 41, 45, 49], -1),
        ([3, 4, 1, 3, 3, 3, 3], 4),
        ([3, 1], 1),
        ([3, 1], 3),
        ([3, 1], 0),
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
        ([2, 5, 6, 0, 0, 1, 2], 0),
        ([5], 5),
        ([], 5),
        ([5], -1),
        ([], None),
        (None, None)]
fns = [search_rotated_list_via_index,
       search_rotated_list_naive,
       search_rotated_list_rec,
       search_rotated_list,
       search_rotated_list_extra,
       search_rotated_list_bin_search]

for l, t in args:
    print(f"l: {l!r}\nt: {t!r}")
    for fn in fns:
        print(f"{fn.__name__}(l, t):", fn(copy.copy(l), t))
    print()

args = [([2]*10000, 1),
        ([2]*10000, 2),
        ([2]*10000000, 1),
        ([2]*10000000, 2),
        (list(range(7500, 10000)) + list(range(7500)), 10000),
        (list(range(7500, 10000)) + list(range(7500)), 7501),
        (list(range(7500000, 10000000)) + list(range(7500000)), 10000000),
        (list(range(7500000, 10000000)) + list(range(7500000)), 7500001)]
for l, t in args:
    print(f"len(l): {len(l)}\nt: {t!r}")
    for fn in fns:
        t = time.time()
        try:
            fn(copy.copy(l), t)
            print(f"{fn.__name__}(l, t) took {time.time() - t} seconds.")
        except RecursionError as e:
            class bcolors:
                FAIL = '\033[91m'
                ENDC = '\033[0m'
            print(f"{bcolors.FAIL}{fn.__name__}(l, t): {e!r}{bcolors.ENDC}")
    print()


