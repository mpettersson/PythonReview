"""
    MERGE K SORTED LISTS (50CIQ 8: MERGE K ARRAYS)

    Write a function that accepts k sorted (ascending) lists and returns a merged list (in ascending order).

    Example:
        Input = [1, 4, 7], [2, 5, 8], [3, 6, 9]
        Output = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    Variations:
        - SEE: merge_k_sorted_linked_lists.py
"""
import copy
import heapq
from queue import PriorityQueue


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Should I modify the given lists?
#   - What are the possible number of lists?


# APPROACH: Naive Sort
#
# This probably isn't what the interviewer wants, however, you could always combine the lists, then sort them.
#
# Time Complexity: O(n * log(n)), where n is the combined size of the lists.
# Space Complexity: O(n), where n is the combined size of the lists.
def merge_k_sorted_lists_naive(*args):
    if len(args) > 0 and all(map(lambda x: isinstance(x, list), args)):
        return sorted([e for l in args for e in l])


# APPROACH: Priority Queue
#
# Use a min heap of size k, where k is the number of lists, to track the value of each of the first values in the lists.
# While there are values in the heap, continually pop the lowest value, replacing it with the next value, if one exists
# in its list, until a resulting merged list is created.
#
# Time Complexity: O(n * log(k)), where n is the total number of elements, and k is the number of lists.
# Space Complexity: O(k), where k is the number of lists
#
# NOTE: PriorityQueue is implemented for synchronized tasks, may be be heavier/slower than the heapq approach below.
def merge_k_sorted_lists_via_priority_queue(*args):
    k = len(args)
    if k > 0:
        q = PriorityQueue(maxsize=k)
        result = []
        for i in range(k):
            if len(args[i]) > 0:
                q.put((args[i][0], i))
        while q.qsize() > 0:
            _, i = q.get()
            result.append(args[i].pop(0))
            if len(args[i]) > 0:
                q.put((args[i][0], i))
        return result


# APPROACH: Min Heap/Heapq
#
# Use a min heap of size k, where k is the number of lists, to track the value of each of the first values in the lists.
# While there are values in the heap, continually pop the lowest value, replacing it with the next value, if one exists
# in its list, until a resulting merged list is created.
#
# Time Complexity: O(n * log(k)), where n is the total number of elements, and k is the number of lists.
# Space Complexity: O(k), where k is the number of lists
def merge_k_sorted_lists_via_heapq(*args):
    if len(args) > 0:
        result = []
        min_heap = []
        for i in range(len(args)):
            if len(args[i]) > 0:
                heapq.heappush(min_heap, (args[i][0], i, 0))
        while min_heap:
            val, arg_idx, list_idx = heapq.heappop(min_heap)
            result.append(val)
            list_idx += 1
            if list_idx < len(args[arg_idx]):
                heapq.heappush(min_heap, (args[arg_idx][list_idx], arg_idx, list_idx))
        return result


# APPROACH: Dynamic Programming/Merge Sort
#
# While there are more than two lists, merge two lists at a time; when only one list remains, return it.  That is;
# Pair up the k lists and merge each pair, (after the first pairing, k lists are merged into k/2 lists with average of
# 2N/k length, then k/4, k/8, etc.), repeat this procedure until the final sorted list is formed, and return it.
#
# Time Complexity: O(n * log(k)), where n is the total number of elements, and k is the number of lists.
# Space Complexity: O(1).
#
# NOTE: IF the k lists were merged one at a time (for example; via merging 2 lists k-1 times, or fold(merge, args, [])),
# then the time complexity would be O(k * n) NOT O(n * log(k)).  This is because the summation of the series would be;
# the sum from 1 to k-1, of ((i * (n/k)) + (n/k)), which equals O(k * n).
def merge_k_sorted_lists_dp(*args):

    def merge_two_sorted_lists(l1, l2):
        result = []
        p1 = p2 = 0
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] < l2[p2]:
                result.append(l1[p1])
                p1 += 1
            else:
                result.append(l2[p2])
                p2 += 1
        while p1 < len(l1):
            result.append(l1[p1])
            p1 += 1
        while p2 < len(l2):
            result.append(l2[p2])
            p2 += 1
        return result

    if len(args) > 0:
        curr_lists = list(args)
        temp_lists = []
        while True:
            if len(curr_lists) == 1:
                return curr_lists.pop()
            while len(curr_lists) >= 2:
                temp_lists.append(merge_two_sorted_lists(curr_lists.pop(), curr_lists.pop()))
            if len(curr_lists):
                temp_lists.append(curr_lists.pop())
            curr_lists, temp_lists = temp_lists, curr_lists


args_list = [([1, 4, 7], [2, 5, 8], [3, 6, 9]),
             ([1, 4, 6], [4, 5, 6], [5, 6, 9]),
             ([0, 5, 10], [1, 2, 3, 4, 6, 7, 8, 9]),
             ([0, 1, 2, 3, 4, 5], []),
             ([], [1, 4, 7], [-2, 69], [2, 5, 8, 68, 69, 70, 72], [3, 6, 9], [0], [100], [], [2, 3]),
             ([],),
             ()]
fns = [merge_k_sorted_lists_naive,
       merge_k_sorted_lists_via_priority_queue,
       merge_k_sorted_lists_via_heapq,
       merge_k_sorted_lists_dp]

for args in args_list:
    print(f"args: {args}")
    for fn in fns:
        print(f"{fn.__name__}(*args):", fn(*copy.deepcopy(args)))
    print()


