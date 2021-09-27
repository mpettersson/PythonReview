"""
    TWO DIMENSIONAL (2D) UTILS

    This contains helper functions and classes for elements of geometric two dimensional (2D) space.
"""
import math
import random


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
               [Point(i // 10, i % 10) for i in range(100)]]


# Compute the angle made by two points (w.r.t. the x-axis) using trigonometry.
def get_angle(a, b):
    if hasattr(a, 'x') and hasattr(a, 'y') and hasattr(b, 'x') and hasattr(b, 'y'):
        angle = math.degrees(math.atan2(b.y - a.y, b.x - a.x))
    else:
        angle = math.degrees(math.atan2(b[1]-a[1], b[0]-a[0]))
    if angle < 0:
        angle += 360
    return angle


def get_distance(a, b):
    if hasattr(a, 'x') and hasattr(a, 'y') and hasattr(b, 'x') and hasattr(b, 'y'):
        return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)
    return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])


def get_cross_product(a, b, c):
    if hasattr(a, 'x') and hasattr(a, 'y') and hasattr(b, 'x') and hasattr(b, 'y') and hasattr(c, 'x') and hasattr(c, 'y'):
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def get_cross_product_sign(a, b, c):
    area = get_cross_product(a, b, c)
    if area < 0:
        return -1   # Clockwise
    if area > 0:
        return 1    # Counter Clockwise
    return 0        # Collinear


# This function returns the index (in a list of points) of the point, with the minimum y-coordinate value.  If there is
# a tie for the minimum y-coordinate value, then the point with the minimum x-coordinate will win.  If the x and y
# coordinate values match, then the first point encountered (with the same minimum x and y coordinate values) index will
# be returned.
def get_index_w_min_y(point_list):
    min_y_val = float('inf')
    min_y_idx = None
    for i, p in enumerate(point_list):
        if p.y < min_y_val:
            min_y_val, min_y_idx = p.y, i
        elif p.y == min_y_val and (p.x <= point_list[min_y_idx]):
            min_y_idx = i
    return min_y_idx


def get_point_w_min_y(point_list):
    result = None
    for p in point_list:
        if result is None or p.y < result.y:
            result = p
        elif p.y == result.y and (p.x <= result.y):
            result = p
    return result


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
    cross_prod = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    if cross_prod < 0:
        return -1       # Clockwise/Negative Angle.
    if cross_prod > 0:
        return 1        # Counter-clockwise/Positive Angle.
    return 0            # Collinear/Same Angle.




