"""
    INTERVAL: FIND MINIMUM SET COVERING INTERVALS (EPI 18.3 THE INTERVAL COVERING PROBLEM)

    Write a function, which accepts a set/list of closed intervals (discrete start/end times), then compute a minimum
    sized set/list of numbers hat covers all the provided intervals.

    Example:
        Input = [Interval(0, 3), Interval(2, 6), Interval(3, 4), Interval(6, 9)]
        Output = [3, 6]

    REMEMBER: '(', ')' is open (up to, not including), '[', ']' is closed (up to, including).
"""
import copy


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible set/list sizes/lengths (can it be empty)?
#   - What are the interval data types?
#   - Will each interval be correctly formatted (have a start and and end, start < end)?
#   - Are the interval endpoints open or closed?


# APPROACH: Brute Force (NOT IMPLEMENTED)
#
# Find the smallest start and the largest end point from the list, then create the result list from testing each integer
# in the range from the smallest to the largest for membership in the set.
#
# Time Complexity: O(d * n), where d is the difference of the two extreme values, and n is the (new) set (list) size.
# Space Complexity: O(r), where r is the length of the result list.


# APPROACH: Via Sort/Greedy
#
# This approach improves on the brute force approach (above); it does not check ALL integers in the range of lowest to
# highest interval, only the integers in the combined set of intervals endpoints.
#
# First sort the intervals by END point times. Add the first intervals end to the results list.  Then, for the remaining
# intervals, if their starting time is greater that the last time added to the results list, add that intervals end time
# to the results list.  Once done return the result list.
#
# Time Complexity: O(n * log(n)), where n is the number of intervals.
# Space Complexity: O(n), where n is the number of intervals.
def find_min_set_covering_intervals(intervals):
    if intervals is not None:
        results = []
        if len(intervals) > 0:
            l = sorted(intervals, key=lambda x: x.end)
            results.append(l[0].end)
            for e in l:
                if e.start > results[-1]:
                    results.append(e.end)
        return results


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start},{self.end}]"


args = [[Interval(0, 3), Interval(2, 6), Interval(3, 4), Interval(6, 9)],
        [Interval(6, 9)],
        [Interval(1, 8), Interval(-4, -1), Interval(0, 2), Interval(3, 6), Interval(7, 9), Interval(11, 12),
         Interval(14, 17)],
        [Interval(1, 8), Interval(-4, -1), Interval(11, 12), Interval(0, 2), Interval(3, 6), Interval(7, 9),
         Interval(14, 17)],
        [Interval(15, 18), Interval(2, 6), Interval(1, 3), Interval(8, 10)],
        [Interval(1, 4), Interval(4, 5)],
        []]
fns = [find_min_set_covering_intervals]

for interval_list in args:
    print(f"interval_list: {interval_list}")
    for fn in fns:
        print(f"{fn.__name__}(intervals_list): {fn(copy.deepcopy(interval_list))}")
    print()


