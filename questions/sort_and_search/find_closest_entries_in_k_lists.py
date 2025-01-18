"""
    FIND (THE) CLOSEST ENTRIES IN K (SORTED) LISTS

    Write a function that takes k sorted lists and returns one entry from each list such that the minimum interval
    containing the entries is as small as possible.

    Example:
        Input = [1, 2, 3], [5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]
        Output = [3, 5, 3, 8]
"""
import heapq


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What about similar items (upper/lower cased strings, etc.)?
#   - What if there are multiple elements, all with the same (minimum) distance (what should be returned)?
#   - What is the behavior for invalid arguments?


# APPROACH: Naive/Brute Force:
#
# TODO
#
# Time Complexity: O(kn) where k is the number of lists and n is the length of the longest list.
# Space Complexity: O(1).
def closest_entries_in_k_lists_naive(*args):

    def _rec(i, items):
        nonlocal result
        if i == 0:
            if len(result) == 0 or max(items) - min(items) < max(result) - min(result):
                result = tuple(items)
        else:
            for x in args[i - 1]:
                items.insert(0, x)
                _rec(i - 1, items)
                items.pop(0)

    if len(args) >= 2 and all([l is not None and len(l) > 0 for l in args]):
        result = ()
        _rec(len(args), [])
        return list(result)


# APPROACH: Min Heap Approach
#
# Due to the fact that the lists are sorted and using a pointer for each list, increment the pointer
# pointing to the lowest value and compare the values to current 'closest entries' set.  If the current set is lower,
# then update the 'lowest entries' set. This approach uses a min heap to maintain the lowest value/list tuple.
#
# Time Complexity: O(n1 + n2 + ... + nk-1 + nk) or, the sum of the lengths of the k lists.
# Space Complexity: O(k).
def closest_entries_in_k_lists_min_heap(*args):
    if len(args) >= 2 and all([l is not None and len(l) > 0 for l in args]):
        l = list(args)
        size = len(l)
        p = [0 for _ in range(size)]            # TODO: Add comments...
        result = [l[0] for l in args]
        min_heap = [(li[0], i) for i, li in enumerate(l) if len(li) > 1]
        heapq.heapify(min_heap)
        while True:
            _, i = heapq.heappop(min_heap)
            if p[i] + 1 < len(l[i]):
                p[i] += 1
                heapq.heappush(min_heap, (l[i][p[i]], i))
            curr_set = [l[i][p[i]] for i in range(size)]
            if max(curr_set) - min(curr_set) < max(result) - min(result):
                result = curr_set
            if len(min_heap) == 0:
                return result


# APPROACH: List Approach
#
# Due to the fact that the lists are sorted and using a pointer for each list, increment the pointer
# pointing to the lowest value and compare the values to current 'closest entries' set.  If the current set is lower,
# then update the 'lowest entries' set. This approach uses a list to maintain the lowest list index/value tuple.
#
# Time Complexity: O(n1 + n2 + ... + nk-1 + nk) or, the sum of the lengths of the k lists.
# Space Complexity: O(k).
def closest_entries_in_k_lists(*args):
    if len(args) >= 2 and all([l is not None and len(l) > 0 for l in args]):
        l = list(args)
        size = len(l)
        p = [0 for _ in range(size)]
        result = [l[0] for l in args]
        while True:
            i, _ = min([(i, l[i][p[i]]) for i in range(size) if p[i] < len(l[i]) - 1], key=lambda x: x[1])
            p[i] += 1
            curr_set = [l[i][p[i]] for i in range(size)]
            if max(curr_set) - min(curr_set) < max(result) - min(result):
                result = curr_set
            if all([p[i] is len(l[i]) - 1 for i in range(size)]):
                return result


args_list = [([5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]),
             ([1, 2, 3], [5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]),
             ([5, 10, 15], [3, 6, 9, 12, 15]),
             ([5, 10, 15], [3, 6, 9, 12, 15], None),
             ([5, 10, 15],)]
fns = [closest_entries_in_k_lists_naive,
       closest_entries_in_k_lists_min_heap,
       closest_entries_in_k_lists]

for args in args_list:
    print(f"l: {args}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(*args)}")
    print()


