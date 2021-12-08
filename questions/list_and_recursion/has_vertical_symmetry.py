"""
    HAS VERTICAL SYMMETRY (leetcode.com/problems/line-reflection)

    Write a function, which accepts a list of n points (on a 2D plane), and returns True if there is a line parallel to
    the y-axis that after reflecting all points over the given line, the original points' set is the same as the
    reflected ones.

    Example:
        Input = [[1, 1], [-1, 1]]
        Output = True

"""
import copy
import time
from collections import defaultdict


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - How are the points stored (object, list, etc.)?
#   - Can the list be modified (should alg. be in-place)?
#   - What are the possible lengths of the list?
#   - Is the list of points unique (or does it have duplicates)?
#   - What about points on the line (parallel to the y-axis)?


# APPROACH: (Slower) Linear
#
# Convert the list to a set (to remove duplicates).  Then find the middle x (or reflective axis) value, and for each
# point, check if the reflected point is also in the set.  If at any point it is not, return False.  Otherwise, return
# True (when done).
#
# Time Complexity: O(n), where n is the number of points.
# Space Complexity: O(n), where n is the number of points.
def has_vertical_symmetry(points):
    if not points:
        return True
    points = set([tuple(p) for p in points])
    mid = (min(x for x, _ in points) + max(x for x, _ in points)) / 2
    for x, y in points:
        if (mid + (mid - x), y) not in points:
            return False
    return True


# APPROACH: (Slower) Linear, Minimized
#
# This is simply a minified version of the approach above.
#
# Time Complexity: O(n), where n is the number of points.
# Space Complexity: O(n), where n is the number of points.
def has_vertical_symmetry_min(points):
    if not points:
        return True
    mid = min(points)[0] + max(points)[0]
    return {(x, y) for x, y in points} == {(mid - x, y) for x, y in points}


# APPROACH: (Faster) Non-Linear Via Sort
#
# This approach first groups the x values by their y coordinates (as a set to remove duplicates), then sorts the values.
# It then uses two pointers to ensure that all of the (unique) points with the same value are symmetric.  For each
# comparison, if the reflective axis is not the same (as the established axis), False is returned.  Otherwise, at the
# completion, True is returned.
#
# Time Complexity: O(n * log(n)), where n is the number of points.
# Space Complexity: O(n * log(n)), where n is the number of points.
def has_vertical_symmetry_via_sort(points):
    if 1 < len(points):
        d = defaultdict(set)
        prev_axis = None
        for x, y in points:
            d[y].add(x)
        for k in d:
            d[k] = sorted(d[k])
            lo, hi = 0, len(d[k]) - 1
            axis = (d[k][lo] + d[k][hi]) / 2
            if prev_axis is not None and prev_axis != axis:
                return False
            lo += 1
            hi -= 1
            while lo <= hi:
                if (d[k][lo] + d[k][hi]) / 2 != axis:
                    return False
                lo += 1
                hi -= 1
            prev_axis = axis
    return True


args = [[[1, 1], [-1, 1]],                                      # True
        [[1, 1], [-1, -1]],                                     # False
        [[-16, 1], [16, 1], [16, 1]],                           # True
        [[1, 1], [2, 2], [3, 3]],                               # False
        [[0, 0], [1, 0], [2, 0]],                               # True
        [],                                                     # True
        [[1, 1]],                                               # True
        [[0, 0], [1, 0], [2, 0], [1, 1], [2, 2], [3, 3]]]       # False
fns = [has_vertical_symmetry,
       has_vertical_symmetry_min,
       has_vertical_symmetry_via_sort]

for points in args:
    print(f"points: {points!r}")
    for fn in fns:
        print(f"{fn.__name__}(points): {fn(copy.deepcopy(points))}")
    print()


points = [[0, 3], [1, 3], [2, 3], [3, 3], [0, 2], [1, 2], [2, 2], [3, 2], [0, 1], [1, 1], [2, 1], [3, 1], [0, 0],
          [1, 0], [2, 0], [3, 0], [1, 1], [0, 1], [1, 1], [2, 1], [3, 1], [0, 4], [1, 4], [2, 4], [3, 4], [0, 0]]
print(f"points: {points!r}")
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(points) took ", end='')
    fn(copy.deepcopy(points))
    print(f"{time.time() - t} seonds.")
print()


