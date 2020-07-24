"""
    CLOSEST K POINTS TO ORIGIN

    Given a list of points in the form [(X1, Y1), X2, Y2), ... , (XN-1, YN-1), (XN, YN)], and an integer k, write a
    function that returns the k nearest points to the origin (0, 0).

    Example:
        Input = [(-2, 4), (0, -2), (-1, 0), (3, 5), (-2, -3), (3, 2)], 3
        Output = [(-2, 4), (0, -2), (-1, 0)]

    NOTE: Variations on this program could include:
            - K nearest points to a specified (non-origin) point.
"""
import heapq
import math


# Iterative Approach using a Max Heap (of size k): The runtime is O(n + (n - k)log(k)), and space is O(k).
def closest_k_points_to_origin(l, k):
    if k == len(l):
        return l
    elif k < len(l):
        max_heap = []
        for (x, y) in l[0:k]:
            max_heap.append((-dist_between_two_points(x, y, 0, 0), (x, y)))
        heapq.heapify(max_heap)
        for (x, y) in l[k:]:
            dist = -dist_between_two_points(x, y, 0, 0)
            if dist < max_heap[0][0]:
                heapq.heappushpop(max_heap, (dist, (x, y)))
        return [p for _, p in heapq.nsmallest(k, max_heap)]


def dist_between_two_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print(closest_k_points_to_origin([(-2, 4), (0, -2), (-1, 0), (3, 5), (-2, -3), (3, 2)], 3))


