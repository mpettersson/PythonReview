r"""
    GRAHAM SCAN (Convex Hull Via Sorting)

    Average Runtime:    O(n * log(n)), where n is the number of points.
    Space Complexity:   O(n), where n is the number of points.

    NOTE: If the points are already sorted, then this could be done in O(n) time.

    NOTE: This approach uses SORTING to find the Convex Hull; the sorting function, however, is TRICKY.  In an interview
          situation, be very careful, or use an algorithm with a simpler sort (i.e., Monotone Chain).

    The Graham scan algorithm computes the Convex Hull of a set of N points; may be visualized as the shape enclosed by
    a rubber band stretched around the subset.

    Graham's scan is a method of finding the convex hull/envelope/closure of a finite set of points in the plane with
    time complexity O(n log n). It is named after Ronald Graham, who published the original algorithm in 1972. The
    algorithm finds all vertices of the convex hull ordered along its boundary. It uses a stack to detect and remove
    concavities in the boundary efficiently.

    Algorithm:
        1. Select the point with the lowest y-coordinate (if two or more points share the smallest y-coordinate, then
           choose the one with the lowest x-coordinate) as the first (initial) vertex, and add it to the hull (result).
        2. Sort the points by (1) ANGLE, and possibly (2) DISTANCE (if collinear), relative to the bottom most point:
            (1) The angle is defined as the angle from the origin (point in step 1) to (each) point.
            (2) If two or more points have the same angle, THEN the DISTANCE is considered, this has two cases:
                a. The angle formed by the origin and point is positive (relative to the horizontal value of the origin
                   point), in which case the CLOSEST point comes first.
                b. The angle formed by the origin and point is between 90 (inclusive) and 180 (exclusive) degrees
                   (again, relative to the horizontal value of the origin point), then the FARTHEST point comes first.
                Example:

                    Negative Slope          Vertical Slope          Positive Slope
                          ⬤ (-6, 6)             ⬤ (0, 6)               ⬤ (6, 6)
                            ⟍                    ｜                    ⟋
                               ⟍                 ｜                 ⟋
                                 ⬤ (-4, 4)      ⬤ (0, 4)       ⬤ (4, 4)
                                    ⟍            ｜            ⟋
                                       ⟍  (-2, 2)｜(0, 2)   ⟋
                                         ⬤      ⬤      ⬤ (2, 2)
                                            ⟍    ｜    ⟋
                                               ⟍ ｜ ⟋
                                                 ⬤ (0, 0)

                    ORDER AFTER SORTED:

                          ⬤ (7)                 ⬤ (4)                  ⬤ (3)
                            ⟍                    ｜                    ⟋
                               ⟍                 ｜                 ⟋
                                 ⬤ (8)          ⬤ (5)          ⬤ (2)
                                    ⟍            ｜            ⟋
                                       ⟍         ｜         ⟋
                                         ⬤ (9)  ⬤ (6)  ⬤ (1)
                                            ⟍    ｜    ⟋
                                               ⟍ ｜ ⟋
                                                 ⬤ (Reference Point)

        3. For each of the sorted points, do the following:
           a. If the stack has more than two points, do the following:
              i.  If the last two points (on the stack) form a counter clockwise angle with point p, then do step 3.b.
              ii. If the last two points (on the stack) form a clockwise (or are collinear) with point p, then pop the
                  last item on the stack and repeat this step (if more than two points on stack, else, do 3.b).
           b. Push the point on the stack.
        4. Once done with all of the sorted points, if there are more than two items on the stack, make sure that the
           last two points (on the stack) form a counter clockwise angle with the first point on the stack (and are not
           collinear), else pop off the last item from the stack.
        5. The stack now contains the convex hull.

    References:
        - algorithmtutor.com/Computational-Geometry/Convex-Hull-Algorithms-Graham-Scan/
        - wikipedia.org/wiki/Graham_scan
        - wikipedia.org/wiki/Convex_hull
        - youtu.be/B2AJoQSZf4M

"""
import random
import math
import copy


# Computes the convex hull (without collinear duplicates) of a set of 2D points.
def get_2d_convex_hull_via_graham_scan(points):
    if isinstance(points, list) and all([isinstance(p, Point) for p in points]):
        result = []                                                             # Convex Hull
        if len(points) > 0:
            points = list(set(points))                                          # Remove duplicates.
            start = min(points, key=lambda p: (p.y, p.x))                       # Reference (origin) point.
            points.sort(key=lambda p: sort_fn(p, start))
            for p in points:
                while len(result) >= 2:
                    if get_angle_sign(result[-1], result[-2], p) < 0:
                        break
                    else:
                        result.pop()
                result.append(p)
            if len(result) >= 3:
                if not get_angle_sign(result[-1], result[-2], result[0]) < 0:   # Check last two points against first.
                    result.pop()
        return result


# Computes the convex hull (including collinear hull vertices) of a set of 2D points.
def get_2d_convex_hull_via_graham_scan_w_collinear_vertices(points):
    if isinstance(points, list) and all([isinstance(p, Point) for p in points]):
        result = []                                                             # Convex Hull
        if len(points) > 0:
            points = list(set(points))                                          # Remove duplicates.
            start = min(points, key=lambda p: (p.y, p.x))                       # Reference (origin) point.
            points.sort(key=lambda p: sort_fn(p, start))
            for p in points:
                while len(result) >= 2:
                    if get_angle_sign(result[-1], result[-2], p) <= 0:
                        break
                    else:
                        result.pop()
                result.append(p)
            if len(result) >= 3:
                if not get_angle_sign(result[-1], result[-2], result[0]) <= 0:   # Check last two points against first.
                    result.pop()
        return result


def sort_fn(p, start):
    angle = math.degrees(math.atan2(p.y - start.y, p.x - start.x))
    if angle < 0:
        angle += 360
    dist = (start.x - p.x) * (start.x - p.x) + (start.y - p.y) * (start.y - p.y)
    if angle >= 90:
        return angle, -dist
    return angle, dist


def get_cross_product(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)


# This function finds the SIGN of the ANGLE between the vectors ab and ac.  This is done by first computing the cross
# product of the two vectors (ab and ac), then by simply comparing if the areas are positive, negative, or zero.
#   Consider the following examples:
#
#                           c
#      Positive Angle:     /
#                         /
#                        a -------- b
#
#                           b
#      Negative Angle:     /     (Notice that b and c switched places.)
#                         /
#                        a -------- c
#
#                             c
#                            /
#      Collinear Angle      b
#                          /
#                         /
#                        a
#
def get_angle_sign(a, b, c):
    cross_prod = get_cross_product(a, b, c)
    if cross_prod < 0:
        return -1       # CW/Clockwise/Negative Angle.
    if cross_prod > 0:
        return 1        # CCW/Counter-clockwise/Positive Angle.
    return 0            # Collinear/Same Angle.


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
               [Point(-1, 6), Point(1, 5), Point(-2, 4), Point(-2.5, 2), Point(-3, 4), Point(0, 0), Point(3, 3), Point(2, 2), Point(4, 2.25)],
               [Point(3, 3), Point(4, 1), Point(4, 2), Point(5, 1)],
               [Point(2, 2), Point(1, 3), Point(1, 1), Point(0, 2), Point(3, 1)],
               [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4), Point(5, 5)],
               [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3), Point(1, 2)],
               [Point(random.randint(0, 100), random.randint(0, 100)) for i in range(50)],
               [Point(i // 10, i % 10) for i in range(100)],
               [],
               None]
fns = [get_2d_convex_hull_via_graham_scan,
       get_2d_convex_hull_via_graham_scan_w_collinear_vertices]

for points in points_list:
    print(f"points: {points}")
    for fn in fns:
        print(f"{fn.__name__}(points): {fn(copy.deepcopy(points))}")
    print()


