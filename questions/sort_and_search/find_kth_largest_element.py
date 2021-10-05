"""
    FIND KTH LARGEST ELEMENT (EPI 12.8: FIND THE KTH LARGEST ELEMENT)

    Design an algorithm for computing the kth largest element in a list.

    Example:
        Input = [3, 2, 1, 5, 4], 2
        Output = 4

    Variations:
        - Design an algorithm to find the median of a list.
        - Find the best place to put a single mailbox on a new street to minimize the distance residents walk.  Assume
          that the input is a list of building objects with the number of residents, and the distance from the beginning
          of the street.
        SEE: find_k_largest_elements.py, find_kth_smallest_element.py, and find_k_smallest_elements.py
"""
import heapq


# APPROACH: Naive/Brute Force Via Sorting
#
# This basic approach simply sorts the list then returns the kth element (from the end of the sorted list).
#
# Time Complexity: O(n log(n)), where n is the length of the list.
# Space Complexity: O(n), where n is the length of the list.
#
# NOTE: If you're doing MORE than what the interviewer wants (especially if it's in a worse time), then, there is
#       probably a better way to solve the problem (i.e., this can be solved in better than O(n log(n)) time...).
def find_kth_largest_element_via_sorted(l, k):
    if l is not None and k is not None and 0 < k <= len(l):
        return sorted(l)[-k]


# APPROACH: Via Min Heap
#
# This approach creates a min heap of size k from the first k items in the list, then pushes and pops (one at a time)
# each of the remaining list items.  Once this is done, pop and return the kth largest element.
#
# Time Complexity: O(n log(k)), where n is the length of the list.
# Space Complexity: O(k).
def find_kth_largest_element_via_min_heap(l, k):
    if l is not None and k is not None and 0 < k <= len(l):
        heap = l[:k]
        heapq.heapify(heap)
        for i in l[k:]:
            heapq.heappushpop(heap, i)
        return heapq.heappop(heap)


# APPROACH: Quick Select
#
# Using a pivot value (convention is last value), swap the elements such that all of the elements smaller than the pivot
# value comes before, and everything larger comes after. Recursively repeat this on the the partition that holds k,
# until k is reached.
#
# Average Time Complexity: O(n), where n is the number of elements in the list.
# Worst Time Complexity: O(n**2), where n is the number of elements in the list.
# Space Complexity: O(log(n)), where n is the number of elements in the list (because of the recursion stack).
#
# NOTE: Quick select (and this solution) is (usually) an in-place algorithm.
def find_kth_largest_element_via_quick_select(l, k):

    def _find_kth_largest_element_via_quick_select(l, k, lo, hi):
        pivot_idx = _partition(l, lo, hi)
        if pivot_idx - lo is k - 1:
            return l[pivot_idx]
        if pivot_idx - lo > k - 1:
            return _find_kth_largest_element_via_quick_select(l, k, lo, pivot_idx - 1)
        return _find_kth_largest_element_via_quick_select(l, k - pivot_idx + lo - 1, pivot_idx + 1, hi)

    def _partition(l, lo, hi):
        pivot_val = l[hi]
        i = lo
        for j in range(lo, hi):
            if l[j] > pivot_val:            # DIFFERENT THAN QUICK SELECT
                l[i], l[j] = l[j], l[i]
                i += 1
        l[i], l[hi] = l[hi], l[i]
        return i

    if l is not None and k is not None and 0 < k <= len(l):
        return _find_kth_largest_element_via_quick_select(l, k, 0, len(l)-1)


# NOTE: Alternatively, k could be modified to reflect the largest, then use the 'normal' select search/partition algs.
def find_kth_largest_element_via_quick_select_alt(l, k):

    def _find_kth_largest_element_via_quick_select_alt(l, k, lo, hi):
        pivot_idx = _partition(l, lo, hi)
        if pivot_idx - lo is k - 1:
            return l[pivot_idx]
        if pivot_idx - lo > k - 1:
            return _find_kth_largest_element_via_quick_select_alt(l, k, lo, pivot_idx - 1)
        return _find_kth_largest_element_via_quick_select_alt(l, k - pivot_idx + lo - 1, pivot_idx + 1, hi)

    def _partition(l, lo, hi):
        pivot_val = l[hi]
        i = lo
        for j in range(lo, hi):
            if l[j] <= pivot_val:
                l[i], l[j] = l[j], l[i]
                i += 1
        l[i], l[hi] = l[hi], l[i]
        return i

    if l is not None and k is not None and 0 < k <= len(l):
        k = len(l) - (k - 1)                                                # DIFFERENT THAN QUICK SELECT
        _find_kth_largest_element_via_quick_select_alt(l, k, 0, len(l)-1)   # DIFFERENT THAN QUICK SELECT
        return l[k-1]                                                       # DIFFERENT THAN QUICK SELECT


lists = [[3, 6, 0, 1, 5, 9, 2, 8, 7, 4],
         [420, 857, 223, 744, 637, 14, 128, 882, 28, 431, 32, 894, 332, 780, 394, 789, 830, 564, 592, 252, 485, 363,
          385, 69, 903, 26, 666, 99, 806, 986, 126, 596, 56, 992, 102, 193, 466, 923, 173, 127, 719, 640, 543, 853, 487,
          408, 210, 629, 709, 4, 395, 296, 756, 343, 652, 367, 187, 982, 175, 409, 182, 17, 710, 440, 940, 0, 785, 779,
          428, 5, 702, 677, 571, 858, 54, 76, 693, 346, 558, 668, 22, 590, 522, 470, 48, 598, 130, 999, 639, 71, 31,
          444, 206, 840, 294, 927, 234, 19, 311, 609],
         [468, 54, 689, 342, 992, 540, 534, 49, 389, 624, 794, 941, 805, 83, 935, 714, 738, 36, 130, 34, 10, 953, 374,
          445, 226, 675, 489, 854, 579, 938, 677, 740, 958, 92, 105, 69, 982, 375, 827, 466, 438, 318, 181, 767, 129,
          782, 645, 409, 556, 714, 553, 197, 697, 974, 763, 247, 736, 159, 858, 391, 223, 883, 527, 612, 501, 702, 849,
          837, 679, 395, 807, 982, 195, 69, 548, 746, 767, 158, 874, 620, 605, 551, 133, 73, 672, 405, 466, 90, 874,
          971, 214, 960, 12, 465, 183, 680, 174, 375, 393, 647]]
k_vals = [-10, 0, 1, 2, 3, 98, 99, 100, None]
fns = [find_kth_largest_element_via_sorted,
       find_kth_largest_element_via_min_heap,
       find_kth_largest_element_via_quick_select,
       find_kth_largest_element_via_quick_select_alt]

for l in lists:
    for k in k_vals:
        print(f"l: {l}")
        for fn in fns:
            print(f"{fn.__name__}(l, {k}):", fn(l[:], k))
        print()


