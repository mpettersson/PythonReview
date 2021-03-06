"""
    FIND (THE) K SMALLEST ELEMENTS (FROM A LIST)

    Design an algorithm to find the k smallest elements of a list.

    Example:
        Input = [3, 2, 1, 5, 4], 2
        Output = [1, 2]

    Variations:
        - Design an algorithm to find the median of a list.
        - Find the best place to put a single mailbox on a new street to minimize the distance residents walk.  Assume
          that the input is a list of building objects with the number of residents, and the distance from the beginning
          of the street.
        SEE: find_kth_smallest_element.py, find_kth_largest_element.py, and find_k_largest_elements.py
"""
import heapq


# Brute Force/Sorting Approach:  Sort and return the k smallest elements. Time complexity is O(n log(n)), where n is the
# length of the list.  Space complexity is O(n), where n is the length of the list.
def find_k_smallest_elements_via_sorted(l, k):
    if l is not None and k is not None and 0 < k <= len(l):
        return sorted(l)[:k]


# Max Heap Approach:  Time complexity is O(n log(k)), where n is the length of the list.  Space complexity is O(k).
def find_k_smallest_elements_via_max_heap(l, k):
    if l is not None and k is not None and 0 < k <= len(l):
        if k is len(l):
            return l
        heap = l[:k + 1]                        # Use first k+1 items in l for a heap (bc _heapreplace_max pops THEN
        heapq._heapify_max(heap)                # pushes so it doesn't guarantee pushed items are < popped items)
        for i in l[k + 1:]:                     # For rest of the items in l:
            heapq._heapreplace_max(heap, i)     # Keep on replacing the largest item.
        heapq._heappop_max(heap)                # pop to get size k.
        return heap


# Quick Select Approach:  Using a pivot value (convention is last value), swap the elements such that all of the
# elements smaller than the pivot value comes before, and everything larger comes after. Recursively repeat this on the
# the partition that holds k, until k is reached.
# Average time complexity is O(n) where n is the number of elements in the list; HOWEVER, worst case time is O(n**2).
# Space complexity is O(log(n)), where n is the number of elements in the list, because this is a recursive.
#
# NOTE: Quick select, and this solution, are in-place algorithms (but, could be easily changed to out-of-place).
# NOTE: Only TWO lines differ with quick select!
def find_k_smallest_elements_via_quick_select(l, k):

    def _find_k_smallest_elements_via_quick_select(l, k, lo, hi):
        pivot_idx = _partition(l, lo, hi)
        if pivot_idx - lo is k - 1:
            return l[pivot_idx]
        if pivot_idx - lo > k - 1:
            return _find_k_smallest_elements_via_quick_select(l, k, lo, pivot_idx - 1)
        return _find_k_smallest_elements_via_quick_select(l, k - pivot_idx + lo - 1, pivot_idx + 1, hi)  # Update k!

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
        _find_k_smallest_elements_via_quick_select(l, k, 0, len(l) - 1)     # DIFFERENT THAN QUICK SELECT!!!
        return l[:k]                                                        # DIFFERENT THAN QUICK SELECT!!!


list_wo_dups = [420, 857, 223, 744, 637, 14, 128, 882, 28, 431, 32, 894, 332, 780, 394, 789, 830, 564, 592, 252, 485,
                363, 385, 69, 903, 26, 666, 99, 806, 986, 126, 596, 56, 992, 102, 193, 466, 923, 173, 127, 719, 640,
                543, 853, 487, 408, 210, 629, 709, 4, 395, 296, 756, 343, 652, 367, 187, 982, 175, 409, 182, 17, 710,
                440, 940, 0, 785, 779, 428, 5, 702, 677, 571, 858, 54, 76, 693, 346, 558, 668, 22, 590, 522, 470, 48,
                598, 130, 999, 639, 71, 31, 444, 206, 840, 294, 927, 234, 19, 311, 609]
list_with_dups = [468, 54, 689, 342, 992, 540, 534, 49, 389, 624, 794, 941, 805, 83, 935, 714, 738, 36, 130, 34, 10,
                  953, 374, 445, 226, 675, 489, 854, 579, 938, 677, 740, 958, 92, 105, 69, 982, 375, 827, 466, 438,
                  318, 181, 767, 129, 782, 645, 409, 556, 714, 553, 197, 697, 974, 763, 247, 736, 159, 858, 391, 223,
                  883, 527, 612, 501, 702, 849, 837, 679, 395, 807, 982, 195, 69, 548, 746, 767, 158, 874, 620, 605,
                  551, 133, 73, 672, 405, 466, 90, 874, 971, 214, 960, 12, 465, 183, 680, 174, 375, 393, 647]
vals = [None, -10, 0, 1, 2, 3, 10, 98, 99, 100]
fns = [find_k_smallest_elements_via_sorted, find_k_smallest_elements_via_max_heap,
       find_k_smallest_elements_via_quick_select]

print(f"list_wo_dups: {list_wo_dups}\n")
for fn in fns:
    for v in vals:
        print(f"{fn.__name__}(list_wo_dups, {v}):", fn(list_wo_dups[:], v))
    print()

print(f"list_with_dups: {list_with_dups}\n")
for fn in fns:
    for v in vals:
        print(f"{fn.__name__}(list_with_dups, {v}):", fn(list_with_dups[:], v))
    print()


