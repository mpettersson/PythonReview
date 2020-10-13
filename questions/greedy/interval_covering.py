"""
    THE INTERVAL COVERING PROBLEM (EPI 18.3)

    Consider a foreman responsible for a number of tasks on the factory floor.  Each task starts at a fixed time and
    ends at a fixed time.  The foreman wants to visit the floor to check on the tasks.  Your job is to help him minimize
    the number of visits he makes.  In each visit, he can check on all the tasks taking place at the time of the visit.
    A visit takes place at a fixed time, and he can only check on tasks taking place at exactly that time.

    You are given a set of closed intervals.  Design an efficient algorithm for finding a minimum sized set of numbers
    that covers all the intervals.

    Example:
        Input = [Interval(0, 3), Interval(2, 6), Interval(3, 4), Interval(6, 9)]
        Output = [3, 6]
"""


# Greedy Approach:  Time complexity is O(n * log(n)), where n is the number of intervals.  Space complexity is O(n),
# where n is the number of intervals.
def min_interval_cover(intervals):
    if intervals is not None:
        results = []
        if len(intervals) > 0:
            if len(intervals) > 1:
                intervals.sort(key=lambda x: x.end)
            results.append(intervals[0].end)
            for interval in intervals:
                if interval.start > results[-1]:
                    results.append(interval.end)
        return results


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start},{self.end}]"


args = [[Interval(0, 3), Interval(2, 6), Interval(3, 4), Interval(6, 9)],
        [Interval(6, 9)],
        []]

for intervals in args:
    print(f"min_interval_cover({intervals}): {min_interval_cover(intervals[:])}")


