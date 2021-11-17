"""
     INTERVAL: MERGE INTERVALS LIST WITH OPEN AND CLOSED ENDPOINTS (EPI 14.6: COMPUTE THE UNION OF INTERVALS)

    Consider a set of intervals with integer endpoints, where the endpoints may be open or closed (and are provided in a
    four element tuple (start, is_start_open, end, is_end_open)).  We want to compute the union of the intervals in such
    sets.

    Write a function, which accepts a list of intervals, then computes and returns their union expressed as a list of
    disjoint intervals.

    Example:
        Input = [(0, True, 3, True), (1, False, 1, False), (2, False, 4, False), (3, False, 4, True),
                 (5, False, 7, True), (7, False, 8, True), (8, False, 11, True), (9, True, 11, False),
                 (12, False, 14, False), (12, True, 16, False), (13, True, 15, True), (16, True, 17, True)]
        Output = [(0, True, 4, False), (5, False, 11, False), (12, False, 17, True)]

    REMEMBER: '(', ')' is open (up to, not including), '[', ']' is closed (up to, including).
"""
import copy
import operator


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible list lengths (empty)?
#   - How are the intervals (in the list) represented (are they objects, tuples, lists, etc.)?
#   - Will each interval be correctly formatted (have a start and and end, start < end)?
#   - Are the interval endpoints open or closed?


# APPROACH: Brute Force (NOT IMPLEMENTED)
#
# Form a set with all the list intervals and the new interval.  Find the smallest start and the largest end point from
# the set, then create the result list from testing each integer in the range from the smallest to the largest for
# membership in the set.
#
# Time Complexity: O(d * n), where d is the difference between the two extreme values, and n is the (new) set size.
# Space Complexity: O(r), where r is the length of the result list.


# APPROACH: Via Sort/Greedy
#
# Observations:
#   - Sorting the intervals on their left value (first) and if their left value is open (second), will allow for
#     incrementally processing a subset of the intervals (and give a clear starting point).
#   - Iterating through the intervals there are three cases:
#       (1) The most recently added result doesn't intersect the current interval (nor does it's right endpoint equal
#           the current intervals left endpoint); append the current interval to results.
#       (2) The most recently added result intersects the current interval; update the recently added interval to the
#           union of it with the current interval.
#       (3) The most recently added result's right endpoint is equal to the current interval's left endpoint (and one
#           or both are closed); update the most recently added interval to the union of it with the current interval.
#
# Time Complexity: O(n log(n)), where n is the number of intervals.
# Space Complexity: O(n), where n is the number of intervals.
def find_union_of_interval_tuples(l):
    if l is not None:
        results = []
        if len(l):
            l.sort(key=operator.itemgetter(0, 1))
            curr = list(l[0])
            for i in range(1, len(l)):
                if l[i][0] < curr[2] or (l[i][0] is curr[2] and (l[i][1] or curr[3])):
                    if l[i][2] > curr[2] or (l[i][2] is curr[2] and not l[i][3]):
                        curr[2], curr[3] = l[i][2], l[i][3]
                else:
                    results.append(curr)
                    curr = list(l[i])
            results.append(curr)
        return results


# APPROACH: Via Sort/Greedy (With Interval Object)
#
# NOTE: Sometimes it is better/easier to use a class to make things clearer!
#
# This approach uses the same logic as the approach above, however, a list of interval objects is first created to allow
# for more descriptive code.
#
# Time Complexity: O(n log(n)), where n is the number of intervals.
# Space Complexity: O(n), where n is the number of intervals.
def find_union_of_interval_tuples_with_interval_object(l):
    if l is not None:
        results = []
        l = [Interval(i[0], i[1], i[2], i[3]) for i in l]
        if len(l):
            l.sort(key=lambda x: (x.left_val, x.is_left_open))
            curr = l[0].copy()
            for i in range(1, len(l)):
                if l[i].left_val < curr.right_val or \
                        (l[i].left_val is curr.right_val and (l[i].is_right_open or curr.is_right_open)):
                    if l[i].right_val > curr.right_val or \
                            (l[i].right_val is curr.right_val and not l[i].is_right_open):
                        curr.right_val, curr.is_right_open = l[i].right_val, l[i].is_right_open
                else:
                    results.append(curr)
                    curr = l[i].copy()
            results.append(curr)
        return results


class Interval:
    def __init__(self, left_val, is_left_open, right_val, is_right_open):
        self.left_val = left_val
        self.is_left_open = is_left_open
        self.right_val = right_val
        self.is_right_open = is_right_open

    def __repr__(self):
        return ('(' if self.is_left_open else '[') + str(self.left_val) + ', ' + str(self.right_val) + (')' if self.is_right_open else ']')

    def copy(self):
        return Interval(self.left_val, self.is_left_open, self.right_val, self.is_right_open)


args = [[(0, True, 3, True), (1, False, 1, False), (2, False, 4, False), (3, False, 4, True), (5, False, 7, True),
         (7, False, 8, True), (8, False, 11, True), (9, True, 11, False), (12, False, 14, False), (12, True, 16, False),
         (13, True, 15, True), (16, True, 17, True)]]
fns = [find_union_of_interval_tuples,
       find_union_of_interval_tuples_with_interval_object]

for l in args:
    print(f"\nl: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(copy.deepcopy(l))}")
    print()


