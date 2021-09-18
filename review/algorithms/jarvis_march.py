"""
    JARVIS MARCH AKA 2D Gift Wrapping (Convex Hull Via BRUTE FORCE)

    Average Runtime:    O(n*h), where n is the number of points and h is the number of points on the convex hull.
    Worst Runtime:      O(n**2), where n is the number of points and h is the number of points on the convex hull.

    The Jarvis march/gift wrapping algorithm computes the Convex Hull of a set of N points; where the convex hull may be
    visualized as the shape enclosed by a rubber band stretched around the set of points.

    NOTE: This is the BRUTE FORCE (NON-SORTING) Convex Hull approach.

    In the two-dimensional case the algorithm is also known as Jarvis march, after R. A. Jarvis, who published it in
    1973; it has O(nh) time complexity, where n is the number of points & h is the number of points on the convex hull.

    Algorithm:
        1. Select the point with the lowest y-coordinate (if two or more points share the smallest y-coordinate, then
           choose the one with the lowest x-coordinate) as the first (initial) vertex, and add it to the hull (result).
        2. Select the point (from ALL points) with the smallest counter clockwise angle in reference to the previous
           point (last point on the hull, or result list), and:
              a.  If the point is NOT the first/start point, add it to the hull (result list) and repeat step 2.
              b.  If the point IS the first/start point, return the hull (result list).  The algorithm is done.

    Applications:
        - Image recognition.
        - Animal's range in ethology.

    References:
        - wikipedia.org/wiki/Gift_wrapping_algorithm
        - wikipedia.org/wiki/Convex_hull
        - youtu.be/B2AJoQSZf4M
        - bitbucket.org/StableSort/play/src/master/src/com/stablesort/convexhull/
"""
import math
import random


def get_2d_convex_hull_via_jarvis_march_by_angle(points):

    def get_angle(a, b):
        angle = math.degrees(math.atan2(b.y - a.y, b.x - a.x))
        if angle < 0:
            angle += 360
        return angle

    def get_distance(a, b):
        return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)

    result = []                                             # Convex Hull
    if isinstance(points, list) and len(points) > 0:
        points = list(set(points))
        start_point = min(points, key=lambda p: (p.y,p.x))  # Find the lowest, or minimum, point on the y-axis.
        result.append(start_point)
        prev_point = start_point
        prev_angle = -1
        while True:
            min_angle = float('inf')
            max_dist = 0
            curr_point = None
            for p in points:                                # Iterate over all points p to find p with largest angle.
                if p != prev_point:
                    angle = get_angle(prev_point, p)
                    dist = get_distance(prev_point, p)
                    if min_angle >= angle > prev_angle:
                        if angle < min_angle or dist > max_dist:
                            min_angle = angle
                            max_dist = dist
                            curr_point = p
            if curr_point is None or curr_point == start_point:
                break                               # Alg is done!
            result.append(curr_point)               # Add point w/ smallest counterclockwise angle w.r.t. prev_point.
            prev_angle = get_angle(prev_point, curr_point)
            prev_point = curr_point
    return result


def get_2d_convex_hull_via_jarvis_march(points):

    def get_distance(a, b):
        return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)

    def get_cross_product_sign(a, b, c):  # a is origin
        area = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
        if area < 0: return -1  # Clockwise
        if area > 0: return 1  # Counter Clockwise
        return 0  # Collinear

    result = []                                             # Convex Hull
    if isinstance(points, list) and len(points) > 0:
        points = list(set(points))
        start_point = min(points, key=lambda p: (p.y,p.x))  # Find the lowest, or minimum, point on the y-axis.
        result.append(start_point)
        prev_point = start_point
        while True:
            candidate = None
            for p in points:                                # Iterate over all points p to find p with largest angle.
                if p != prev_point:
                    if candidate is None:
                        candidate = p
                        continue
                    cps = get_cross_product_sign(prev_point, candidate, p)
                    if cps == 0 and get_distance(prev_point, candidate) < get_distance(prev_point, p):
                        candidate = p       # collinear tie is decided by distance (don't need angle)
                    elif cps < 0:
                        candidate = p
            if candidate is None or candidate == start_point:
                break
            result.append(candidate)        # Add point w/ smallest counterclockwise angle w.r.t. prev_point.
            prev_point = candidate
    return result


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
fns = [get_2d_convex_hull_via_jarvis_march_by_angle,
       get_2d_convex_hull_via_jarvis_march]

for points in points_list:
    print(f"points: {points}")
    for fn in fns:
        print(f"{fn.__name__}(points): {fn(points)}")
    print()


