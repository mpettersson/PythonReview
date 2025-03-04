"""
    FIND K SMALLEST ELEMENTS

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
import time


# APPROACH: Naive/Brute Force Via Sorting
#
# This basic approach simply sorts the list then returns the k smallest elements from the (sorted) lists head.
#
# Time Complexity: O(n log(n)), where n is the length of the list.
# Space Complexity: O(n), where n is the length of the list.
#
# NOTE: If you're doing MORE than what the interviewer wants (especially if it's in a worse time), then, there is
#       probably a better way to solve the problem (i.e., this can be solved in better than O(n log(n)) time...).
def find_k_smallest_elements_via_sorted(l, k):
    if l is not None and k is not None and 0 < k <= len(l):
        return sorted(l)[:k]


# APPROACH: Via Max Heap
#
# NOTE: Python's heapq uses a single leading underscore on the max heap functions (to indicate the functions are for
#       internal use); if you do not want to use them, an additional example using a min heap is next.
#
# NOTE: In order to save a bit of time, the heap is returned (not popped off and returned), so the order of the k
#       smallest elements is not guaranteed.
#
# This approach creates a max heap of size k+1 from the first k+1 items in the list (the extra one is because of the
# _heapreplace_max function, see below), then pushes and pops (one at a time) each of the remaining list items.  Once
# this is done one element is popped (to reduce the heap to size k), then the heap, or the k smallest elements, are
# returned.
#
# Time Complexity: O(n log(k)), where n is the length of the list.
# Space Complexity: O(k).
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


# APPROACH: Via Min Heap
#
# NOTE: In order to save a bit of time, the heap is returned (not popped off and returned), so the order of the k
#       smallest elements is not guaranteed.
#
# This approach creates a min heap of size k from the negated values of the first k items in the list, then negates,
# pushes and pops (one at a time) each of the remaining list items.  Once this is done the remaining k values are
# negated and returned.
#
# Time Complexity: O(n log(k)), where n is the length of the list.
# Space Complexity: O(k).
def find_k_smallest_elements_via_min_heap(l, k):
    if l is not None and k is not None and 0 < k <= len(l):
        heap = [-v for v in l[:k]]
        heapq.heapify(heap)
        for i in l[k:]:
            heapq.heappushpop(heap, -i)
        return [-i for i in heap]


# APPROACH: Via Quick Select
#
#
# This approach is simply a modified version of quick select, with Lomuto partition, algorithm.
#
# Average Time Complexity: O(n), where n is the number of elements in the list.
# Worst Time Complexity: O(n**2), where n is the number of elements in the list.
# Space complexity is O(log(n)), where n is the number of elements in the list (because of the recursion stack).
#
# NOTE: Quick select, and this solution, are in-place algorithms (but, could be easily changed to out-of-place).
# NOTE: The return list is not truly sorted (this is quick select, not quick sort).
def find_k_smallest_elements_via_quick_select(l, k):

    def _rec(l, k, left, right):
        p = _partition(l, left, right)          # Pivot Index
        if k == p:
            return p
        if k < p:
            return _rec(l, k, left, p-1)
        return _rec(l, k, p+1, right)

    def _partition(l, left, right):
        pivot_val = l[right]
        p = left
        for i in range(left, right):
            if l[i] <= pivot_val:
                l[p], l[i] = l[i], l[p]
                p += 1
        l[p], l[right] = l[right], l[p]
        return p

    if l is not None and k is not None and 0 < k <= len(l):
        p = _rec(l, k-1, 0, len(l)-1)       # Don't forget to -1 for the index.
        return l[:p+1]                            # Return the values.


fns = [find_k_smallest_elements_via_sorted,
       find_k_smallest_elements_via_max_heap,
       find_k_smallest_elements_via_min_heap,
       find_k_smallest_elements_via_quick_select]
l = [8, -19, 2, 1, -4, 8, -5, 9, 666, 99, 806, 986, 126, 596, 5, 7, 4, 6, -7, 6, 6, -22, 15, 0, 0, 1, 88, -82, 3, -5, 4]
l_sorted = sorted(l)
for k in range(len(l) + 2):
    print(f"l:         {l}")
    print(f"sorted(l): {l_sorted}")
    for fn in fns:
        print(f"{fn.__name__}(l, {k}):", fn(l[:], k))
    print()

l = [-19, 54, 805, 0, 181, 126, 982, 69, 938, 551, 438, 88, 0, -647, 195, 645, -982, 666, 223, -405, -341, 740, -548,
     36, 391, 806, 746, 534, 15, 466, 6, 605, 677, 736, 689, 226, 938, 794, 738, 8, -620, 596, 874, 174, 874, 680, 854,
     393, 83, 767, 4, 527, 6, 858, 1, -466, -2, -938, 501, 49, 579, 953, 214, 73, 489, 12, -767, 5, 105, 992, 679, 395,
     -714, 10, 389, 612, 697, 675, -5, 960, 130, 2, -4, -333, 782, 468, -7, 8, 92, -714, -837, 374, 807, 4, -82, -22,
     197, 986, 465, 958, 69, 9, -5, 941, 974, 540, -215, 556, 7, 99, 405, 1, 129, 827, 158, 672, 445, 702, -849, 3, 375,
     624, -971, 90, 6, 133, 183, -763, 159, 375, 553, 34]
l_sorted = sorted(l)
k = 42
print(f"l:         {l}")
print(f"sorted(l): {l_sorted}")
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(l) took ", end='')
    fn(l[:], k)
    print(f"{time.time() - t} seconds.")



