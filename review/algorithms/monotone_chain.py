"""
    MONOTONE CHAIN (AKA Andrew's Algorithm, Convex Hull Via Sorting)

    Average Runtime:    O(n * log(n)), where n is the number of points.
    Space Complexity:   O(n), where n is the number of points.

    NOTE: If the points are already sorted (lexicographically), then this can be done in O(n) time.

    The Monotone Chain, or Andrew's, algorithm computes the Convex Hull of a set of N points.  The Convex Hull may be
    visualized as the shape enclosed by a rubber band stretched around the subset.

    This algorithm was published in 1979 by A. M. Andrew, and can be seen as a variant of Graham scan which sorts the
    points lexicographically by their coordinates. When the input is already sorted, the algorithm takes O(n) time.

    Algorithm:
        1.  Sort the points by x-coordinate (in case of a tie, sort by y-coordinate).
        2.  Use two lists to hold the upper and lower hulls vertices.
        3.  For each point in the sorted list, do the following:
           a. While the lower list contains at least two points, and the sequence of last two points and the current
              point does not make a counter-clockwise turn, remove the last point from the lower list.
           b. Append the current point to the lower list.
        4.  For each point in the REVERSED sorted list, do the following:
           a. While the upper list contains at least two points, and the sequence of last two points and the current
              point does not make a counter-clockwise turn, remove the last point from the upper list.
           b. Append the current point to the upper list.
        5. Remove the last point of the upper and lower list (it's the same as the first point of the other list).
        6. Concatenate the lower and upper lists to obtain the Convex Hull.
           Points in the result will be listed in counter-clockwise order.

    References:
        - en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain
        - algorithmist.com/wiki/Monotone_chain_convex_hull.py
"""
import random


# Computes the convex hull (without collinear duplicates) of a set of 2D points.
def get_2d_convex_hull_via_monotone_chain(points):

    def cross(o, a, b):  # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
        return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)    # If val >0: ccw turn, <0: cw turn, 0: collinear

    if isinstance(points, list):
        points.sort()                       # Sort points lexicographically (First by X, Then by Y).
        i = 1                               # Remove duplicate points.
        while i < len(points):
            if points[i] == points[i-1]:
                points.pop(i)
            else:
                i += 1
        if len(points) <= 1:                # If no points or a single (possibly repeated) point:
            return points                       # Then return an empty list, or a list with a single unique point.
        lower = []
        for p in points:                    # Build lower hull
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:  # USE < 0 to include collinear points.
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(points):          # Notice that the points are REVERSED.
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:  # USE < 0 to include collinear points.
                upper.pop()
            upper.append(p)
        return lower[:-1] + upper[:-1]      # lower + upper == convex hull. FIRST point in each list is others LAST.


# Computes the convex hull (including collinear hull vertices) of a set of 2D points.
def get_2d_convex_hull_via_monotone_chain_w_collinear_vertices(points):

    def cross(o, a, b):  # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
        return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)    # If val >0: ccw turn, <0: cw turn, 0: collinear

    if isinstance(points, list):
        points.sort()                       # Sort points lexicographically.
        i = 1                               # Remove duplicate points.
        while i < len(points):
            if points[i] == points[i-1]:
                points.pop(i)
            else:
                i += 1
        if len(points) <= 1:                # If no points or a single (possibly repeated) point:
            return points                       # Then return an empty list, or a list with a single unique point.
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:   # USE <= 0 to exclude collinear points.
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(points):          # Notice that the points are REVERSED.
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:   # USE <= 0 to exclude collinear points.
                upper.pop()
            upper.append(p)
        result = lower + upper              # lower + upper == convex hull.
        return list(set(result))            # Because ALL collinear points are added there will be duplicates.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return self.y < other.y or (self.y == other.y and self.x < other.x)
        return False


points_list = [[Point(0, 0), Point(0, 0), Point(0, 3), Point(0, 5), Point(3, 0), Point(3, 3), Point(3, 5), Point(5, 0), Point(5, 3), Point(5, 5)],
               [Point(0, 0), Point(0, 0), Point(0, 0)],
               [Point(-1, 6), Point(1, 5), Point(-2, 4), Point(-2.5, 2), Point(-3, 4), Point(0, 0), Point(3, 3), Point(2, 2), Point(4, 2)],
               [Point(3, 3), Point(4, 1), Point(4, 2), Point(5, 1)],
               [Point(2, 2), Point(1, 3), Point(1, 1), Point(0, 2), Point(3, 1)],
               [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4), Point(5, 5)],
               [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3), Point(1, 2)],
               [Point(random.randint(0, 100), random.randint(0, 100)) for i in range(50)],
               [Point(i // 10, i % 10) for i in range(100)],
               [],
               None]
fns = [get_2d_convex_hull_via_monotone_chain,
       get_2d_convex_hull_via_monotone_chain_w_collinear_vertices]

for points in points_list:
    print(f"points: {points}")
    for fn in fns:
        print(f"{fn.__name__}(points): {fn(points)}")
    print()


