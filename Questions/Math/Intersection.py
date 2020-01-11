"""
    INTERSECTION

    Given two straight line segments (represented as a start point and an end point), compute the point of intersection
    if any.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start_point, end_point):
        delta_y = end_point.y - start_point.y
        delta_x = end_point.x - start_point.x
        self.slope = delta_y / delta_x
        self.y_intercept = end_point.y - self.slope * end_point.x


def is_between(start, middle, end):
    if start > end:
        return end <= middle <= start
    else:
        return start <= middle <= end


def is_between_points(start, middle, end):
    return is_between(start.x, middle.x, end.x) and is_between(start.y, middle.y, end.y)


def intersection(line_one_start, line_one_end, line_two_start, line_two_end):

    # Rearranging these such that x values start is before end and point one is before point two.
    # This will make future calculations easier.
    if line_one_start.x > line_one_end.x:
        line_one_start.x, line_one_end.x = line_one_end.x, line_one_start.x
    if line_two_start.x > line_two_end.x:
        line_two_start.x, line_two_end.x = line_two_end.x, line_two_start.x
    if line_one_start.x > line_two_start.x:
        line_one_start, line_two_start = line_two_start, line_one_start
        line_one_end, line_two_end = line_two_end, line_one_end

    # Compute lines (including slope and y-intercept)
    line_one = Line(line_one_start, line_one_end)
    line_two = Line(line_two_start, line_two_end)

    # If the lines are parallel, they intercept IFF they have the same y-intercept and start two is on line one.
    if line_one.slope == line_two.slope:
        if line_one.y_intercept == line_two.y_intercept and is_between_points(line_one_start, line_two_start, line_two_end):
            return line_two_start
        else:
            return None

    # Get intersection coordinate
    x = (line_two.y_intercept - line_one.y_intercept) / (line_one.slope - line_two.slope)
    y = x * line_one.slope + line_one.y_intercept
    line_intersection = Point(x, y)

    # Check if within line segment range
    if is_between_points(line_one_start, line_intersection, line_one_end) and is_between_points(line_two_start, line_intersection, line_two_end):
        return line_intersection
    else:
        return None


first_intersection = intersection(Point(0,0), Point(2,2), Point(0,3), Point(1,0))
print(first_intersection.x, "", first_intersection.y)