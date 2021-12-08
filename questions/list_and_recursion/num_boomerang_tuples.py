"""
    NUM BOOMERANG TUPLES (leetcode.com/problems/number-of-boomerangs)

    Write a function, which accepts a list of distinct points (on a 2D plane), and returns the number of 'boomerangs';
    where a 'boomerang' is defined as a 3-tuple of points, (i, j, k), such that the distance between i and j equals the
    distance between i and k.

    Example:
        Input = [[1, 1], [2, 2], [3, 3]]
        Output = 2  # or ([2, 2], [1, 1], [3, 3]) and ([2, 2], [3, 3], [1, 1])

"""
import copy
import time
from collections import defaultdict


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - How are the points stored (object, list, etc.)?
#   - What are the possible lengths of the list?
#   - Is the list of points unique (or does it have duplicates)?


# APPROACH: Via Dictionary
#
# For each point, this approach uses a dictionary to store the total counts for each distance (a point can be) from the
# point.  Then, each 'boomerang' tuple is added to the result.  Finally the result is returned.
#
# The tricky part of this question is figuring out how to count the 'boomerangs'.  Since the ORDER MATTERS, we will be
# using permutations (not combinations), furthermore, since only TWO items will be selected each time, we can use the
# formula to count the number of permutations, for two items (r) being chosen, from the total number of things (n) (or,
# all of the points that are the same distance from the origin point):
#       = n!/(n-r)!
#       = n!/(n-2)!
#       = n*(n-1)
#
# Time Complexity: O(n**2), where n is the number of points in the points list.
# Space Complexity O(n**2), where n is the number of points in the points list.
def num_boomerang_tuples(points):

    def _get_dist(a, b):
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return dx * dx + dy * dy

    result = 0
    for p in points:
        d = defaultdict(int)
        for q in points:                    # Don't need to worry about p==q, bc there is only 1 p...
            d[_get_dist(p, q)] += 1
        for v in d.values():
            result += v * (v - 1)           # REMEMBER: n!/(n-r)! == n!/(n-2)! == n*(n-1)
    return result


# APPROACH: Via Dictionary
#
# This approach also uses a dictionary, however, the distance is computed inline and there is no loop over the
# dictionary values.
#
# Time Complexity: O(n**2), where n is the number of points in the points list.
# Space Complexity O(n**2), where n is the number of points in the points list.
def num_boomerang_tuples_min(points):
    result = 0
    for px, py in points:
        d = {}
        for qx, qy in points:               # Don't need to worry about p==q, bc there is only 1 p...
            dist = (px-qx) * (px-qx) + (py-qy) * (py-qy)    # (This is slightly faster than ((px-qx)**2+(py-qy)**2).)
            if dist in d:                   # The counting below takes a bit of thinking, but it is faster than above...
                result += 2 * d[dist]       # (2* == Since in each 'boomerang', two points can be swapped...)
                d[dist] += 1
            else:
                d[dist] = 1                 # If just one point, then it's not a 'boomerang' yet...
    return result


args = [[[1, 1], [2, 2], [3, 3]],
        [[0, 0], [1, 0], [2, 0]],
        [[1, 1]],
        [[0, 0], [1, 0], [2, 0], [1, 1], [2, 2], [3, 3]]]
fns = [num_boomerang_tuples,
       num_boomerang_tuples_min]

for points in args:
    print(f"points: {points!r}")
    for fn in fns:
        print(f"{fn.__name__}(points): {fn(copy.deepcopy(points))}")
    print()


points = [[0, 3], [1, 3], [2, 3], [3, 3], [0, 2], [1, 2], [2, 2], [3, 2], [0, 1], [1, 1], [2, 1], [3, 1], [0, 0],
          [1, 0], [2, 0], [3, 0], [.5, .5], [1.5, 1.5], [4, 4], [5, 5], [6, 6], [5, 6], [6, 5]]
print(f"points: {points!r}")
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(points) took ", end='')
    fn(copy.deepcopy(points))
    print(f"{time.time() - t} seonds.")
print()


