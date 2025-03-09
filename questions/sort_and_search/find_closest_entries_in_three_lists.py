"""
    FIND (THE) CLOSEST ENTRIES IN THREE (SORTED) LISTS (EPI 15.6)

    Design an algorithm that takes three sorted arrays and returns one entry from each such that the minimum interval
    containing these three entries is as small as possible.

    Example:
        Input = [5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]
        Output = [15, 15, 16]
"""
import heapq


# Questions you should ask the interviewer (if not explicitly stated):
# TODO - Go over this.
#   - What time/space complexity are you looking for?
#   - What about similar items (upper/lower cased strings, etc.)?
#   - What if there are multiple elements, all with the same (minimum) distance (what should be returned)?
#   - What is the behavior for invalid arguments?


# APPROACH: Naive/Brute Force
#
# TODO: Add Description.
#
# Time Complexity: O(nmo) where n, m, and o are the lengths of the lists l1, l2, and l3.
# Space Complexity: O(1).
def closest_entries_in_three_lists_naive(l0, l1, l2):
    if l0 and l1 and l2:
        entries = ()
        for i0 in l0:
            for i1 in l1:
                for i2 in l2:
                    if len(entries) == 0 or max(i0, i1, i2) - min(i0, i1, i2) < max(entries) - min(entries):
                        entries = (i0, i1, i2)
        return entries


# APPROACH: Min Heap
#
# TODO: Add Description.
#
# Time Complexity: O(n + m + o) where n, m, and o are the lengths of the lists.
# Space Complexity: O(1).
def closest_entries_in_three_lists_min_heap(l0, l1, l2):
    if l0 and l1 and l2:
        l = [l0, l1, l2]
        num = len(l)
        p = [0 for _ in range(num)]
        closest_entries = (l[0][0], l[1][0], l[2][0])
        min_heap = [(li[0], i) for i, li in enumerate(l) if len(li) > 1]
        heapq.heapify(min_heap)
        while True:
            _, i = heapq.heappop(min_heap)
            if p[i] + 1 < len(l[i]):
                p[i] += 1
                heapq.heappush(min_heap, (l[i][p[i]], i))
            if max(l[0][p[0]], l[1][p[1]], l[2][p[2]]) - min(l[0][p[0]], l[1][p[1]], l[2][p[2]]) \
                    < max(closest_entries) - min(closest_entries):
                closest_entries = (l[0][p[0]], l[1][p[1]], l[2][p[2]])
            if len(min_heap) == 0:
                return closest_entries


# APPROACH: List Approach
#
# TODO: Add Description.
#
# Time Complexity: O(n + m + o) where n, m, and o are the lengths of the lists.
# Space Complexity: O(1).
def closest_entries_in_three_lists(l0, l1, l2):
    if l0 and l1 and l2:
        l = [l0, l1, l2]
        num = len(l)
        p = [0 for _ in range(num)]
        closest_entries = (l[0][0], l[1][0], l[2][0])
        while True:
            i, _ = min([(i, l[i][p[i]]) for i in range(num) if p[i] < len(l[i]) - 1], key=lambda x: x[1])
            p[i] += 1
            if max(l[0][p[0]], l[1][p[1]], l[2][p[2]]) - min(l[0][p[0]], l[1][p[1]], l[2][p[2]]) \
                    < max(closest_entries) - min(closest_entries):
                closest_entries = (l[0][p[0]], l[1][p[1]], l[2][p[2]])
            if p[0] is len(l[0]) - 1 and p[1] is len(l[1]) - 1 and p[2] is len(l[2]) - 1:
                return closest_entries


args_list = [([5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]),
             ([5, 10, 15], [3, 6, 9, 12, 15], []),
             ([5, 10, 15], [3, 6, 9, 12, 15], None)]
fns = [closest_entries_in_three_lists_naive,
       closest_entries_in_three_lists_min_heap,
       closest_entries_in_three_lists]

for args in args_list:
    print(f"l: {args}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(*args)}")
    print()


