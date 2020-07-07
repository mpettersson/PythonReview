"""
    SMALLEST K

    Design an algorithm to find the smallest K numbers in a list.
"""
import heapq
import random
import sys


# Approach 1:  Sort and return the k smallest elements, the time complexity is O(N log(N)).
def smallest_k_via_sorting(l, k):
    if k <= 0 or k > len(l):
        raise ValueError
    l.sort()
    return l[:k]


# Approach 2:  Max Heap; runtime is O(N log(K)), where K is the number of values we're looking for.
def smallest_k_via_max_heap(l, k):
    if k <= 0 or k > len(l):
        raise ValueError
    if k == len(l):
        return l

    # NOTE: We're using k + 1 because _heapreplace_max pops then pushes (so it doesn't guarantee pushed item is smaller
    # that the popped item, therefore, if we increase the size to k + 1, we'll always have the k smallest items.
    heap = l[0:k + 1]
    heapq._heapify_max(heap)
    for i in l[k + 1:]:
        heapq._heapreplace_max(heap, i)
    # Drop it back down to size k.
    heapq._heappop_max(heap)

    return heap


# Approach 3:  Selection Rank Algorithm
def smallest_k_via_selection_rank(array, k):
    if k <= 0 or k > len(array):
        raise ValueError
    if k == len(array):
        return array
    threshold = rank(array, k - 1, 0, len(array) - 1)
    smallest = [0] * k
    count = 0
    for i in array:
        if i < threshold:
            smallest[count] = i
            count += 1
    while count < k:
        smallest[count] = threshold
        count += 1
    return smallest


def rank(array, k, start, end):
    pivot = array[random.randint(start, end)]
    part = partition(array, start, end, pivot)
    left_size = part.left_size
    middle_size = part.middle_size
    if k < left_size:
        return rank(array, k, start, start + left_size -1)
    elif k < left_size + middle_size:
        return pivot
    else:
        return rank(array, k - left_size - middle_size, start + left_size + middle_size, end)


def partition(array, start, end, pivot):
    left = start
    right = end
    middle = start
    while middle <= right:
        if array[middle] < pivot:
            array[left], array[middle] = array[middle], array[left]
            middle += 1
            left += 1
        elif array[middle] > pivot:
            array[middle], array[right] = array[right], array[middle]
            right -= 1
        elif array[middle] == pivot:
            middle += 1
    return PartitionResult(left - start, right - left + 1)


class PartitionResult:
    def __init__(self, left_size, middle_size):
        self.left_size = left_size
        self.middle_size = middle_size


unique_list = [420, 857, 223, 744, 637, 14, 128, 882, 28, 431, 32, 894, 332, 780, 394, 789, 830, 564, 592, 252, 485,
               363, 385, 69, 903, 26, 666, 99, 806, 986, 126, 596, 56, 992, 102, 193, 466, 923, 173, 127, 719, 640, 543,
               853, 487, 408, 210, 629, 709, 4, 395, 296, 756, 343, 652, 367, 187, 982, 175, 409, 182, 17, 710, 440,
               940, 0, 785, 779, 428, 5, 702, 677, 571, 858, 54, 76, 693, 346, 558, 668, 22, 590, 522, 470, 48, 598,
               130, 999, 639, 71, 31, 444, 206, 840, 294, 927, 234, 19, 311, 609]

non_unique_list = [468, 54, 689, 342, 992, 540, 534, 49, 389, 624, 794, 941, 805, 83, 935, 714, 738, 36, 130, 34, 10,
                   953, 374, 445, 226, 675, 489, 854, 579, 938, 677, 740, 958, 92, 105, 69, 982, 375, 827, 466, 438,
                   318, 181, 767, 129, 782, 645, 409, 556, 714, 553, 197, 697, 974, 763, 247, 736, 159, 858, 391, 223,
                   883, 527, 612, 501, 702, 849, 837, 679, 395, 807, 982, 195, 69, 548, 746, 767, 158, 874, 620, 605,
                   551, 133, 73, 672, 405, 466, 90, 874, 971, 214, 960, 12, 465, 183, 680, 174, 375, 393, 647]
print("unique_list:", unique_list)
print("non_unique_list:", non_unique_list)
print()

print("smallest_k_via_sorting(unique_list, 10):", smallest_k_via_sorting(unique_list, 10))
print("smallest_k_via_sorting(non_unique_list, 10):", smallest_k_via_sorting(non_unique_list, 10))
print()

print("sorted(smallest_k_via_max_heap(unique_list, 10)):", sorted(smallest_k_via_max_heap(unique_list, 10)))
print("sorted(smallest_k_via_max_heap(non_unique_list, 10)):", sorted(smallest_k_via_max_heap(non_unique_list, 10)))
print()

print("sorted(smallest_k_via_selection_rank(unique_list, 10)):", sorted(smallest_k_via_selection_rank(unique_list, 10)))
print("sorted(smallest_k_via_selection_rank(non_unique_list, 10)):", sorted(smallest_k_via_selection_rank(non_unique_list, 10)))




