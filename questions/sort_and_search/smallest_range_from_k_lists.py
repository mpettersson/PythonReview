"""
    SMALLEST RANGE FROM K LISTS

    Given k sorted (ascending) lists of integers (may contain duplicates), find the smallest range that includes an
    element from each of the k lists.

    The range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

    Example:
        Input = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
        Output = [20, 24]
"""
import sys
import heapq


# This approach uses a pointer for each array (each starting at index zero), then increments the pointer pointing at the
# lowest value, each time comparing the ranges (stored as a lowest range result set of max/min and the iterations set of
# max/min values) until the pointer with the lowest value can no longer be incremented (it's at the end of the array).
# The runtime is O(k * n^2), where k is the number of lists and n is the number of items in each list, the space
# complexity is O(k).
# NOTE: This algorithm is often INCORRECTLY claimed to have a O(k * n) runtime.
def smallest_range(l):
    result_min_val = 0
    result_max_val = sys.maxsize + 1
    p = [0] * len(l)
    min_val = min_idx = max_val = 0

    while True:
        min_val = sys.maxsize
        min_idx = -1
        max_val = -sys.maxsize

        for i in range(len(l)):
            if l[i][p[i]] < min_val:
                min_val = l[i][p[i]]
                min_idx = i
            if l[i][p[i]] > max_val:
                max_val = l[i][p[i]]

        if max_val - min_val < result_max_val - result_min_val:
            result_min_val = min_val
            result_max_val = max_val

        p[min_idx] += 1

        if p[min_idx] == len(l[min_idx]):
            return [result_min_val, result_max_val]


# This approach, although quicker, is slightly more complicated and uses more advanced language features; it is similar
# to the pointer approach above, however, it uses a min heap with three tuples (of value-pointed-at and which-list) that
# are popped off (then the value is updated and pushed back) thus preventing iterative comparisons of the values.
# The runtime is O(kn log k), where k is the number of lists and n is the number of items in each list, the space
# complexity is O(k).
def smallest_range_min_heap(l):
    min_heap = []
    result_min_val = float("inf")
    result_max_val = -float("inf")

    for i, sl in enumerate(l):
        heapq.heappush(min_heap, (sl[0], i, 0))
        result_min_val = sl[0] if sl[0] < result_min_val else result_min_val
        result_max_val = sl[0] if sl[0] > result_max_val else result_max_val
    min_range = result_max_val - result_min_val
    res = [result_min_val, result_max_val]

    while min_heap:
        v, i, ai = heapq.heappop(min_heap)
        result_min_val = v if v > result_min_val else result_min_val
        if result_max_val - result_min_val < min_range:
            res = [result_min_val, result_max_val]
            min_range = result_max_val - result_min_val
        if ai + 1 < len(l[i]):
            post = l[i][ai + 1]
            heapq.heappush(min_heap, (post, i, ai + 1))
            result_max_val = post if post > result_max_val else result_max_val
        else:
            return res


args = [[[0], [0]],
        [[1], [0], [99]],
        [[0, 9], [8, 9]],
        [[0, 10, 15, 24, 26], [0, 9, 12, 20], [0, 18, 22, 30]],
        [[4, 10, 15, 21, 26], [0, 9, 12, 22], [5, 18, 22, 30]],
        [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],
        [[-200], [-199, -56, -45, -34, 20], [-198, -55, -44, -33, 20], [-200, -54, -43, -32, 20], [-199, -42, -31, 19]],
        [[21], [-199, -56, -45, -34, 20], [-198, -55, -44, -33, 20], [-200, -54, -43, -32, 20], [-199, -42, -31, 19]],
        # The following two lines are the worst case for 5 lists, each with 5 elements:
        [[-600, -500, -450, 0, 20], [-580, -490, -445, 2, 19], [-560, -480, -440, 4, 18], [-540, -470, -435, 6, 17],
         [-520, -460, -430, 8, 16]],
        # The following line is the worst case for 5 lists, each with 4 elements:
        [[-600, -450, 0, 20], [-580, -445, 2, 19], [-560, -440, 4, 18], [-540, -435, 6, 17], [-520, -430, 8, 16]],
        [[-99, -56, -45, -34, 20], [-95, -55, -44, -33, 20], [-85, -54, -43, -32, 20], [-53, -42, -31, 19]]]

for l in args:
    print(f"smallest_range({l}):", smallest_range(l))
print()

for l in args:
    print(f"smallest_range_min_heap({l}):", smallest_range_min_heap(l))

