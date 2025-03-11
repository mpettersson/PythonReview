"""
    INTERVAL NON-OVERLAPPING (leetcode.com/problems/non-overlapping-intervals)

    Write a function which takes a list of intervals, then computes and returns the minimum number of interval deletions
    to ensure the remaining intervals disjoint (non-overlapping). Note that the two intervals a and b are not considered
    overlapping if a.end is the same as b.start.

    Example:
        Input = [[1,2], [2,3], [3,4], [1,3]]
        Output = 1  # for the interval [1,3]

    Variations:
        - Find Maximum Number of Non-Overlapping Intervals
        - Maximum Overlapping Intervals
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible list lengths (empty)?
#   - Will each interval be correctly formatted (have a start and end, start < end, etc.)?
#   - Are the interval endpoints open or closed?


# APPROACH: Via Sort
#
# TODO: FINISH THE DESCRIPTION...
#
# This approach first sorts the intervals by their start values.  This ensures that any overlapping intervals will be
# next to each other...
#
# This approach:
#   (1) Sorts the intervals by start then end times.
#   (2)
#   (3) Iterates over the remaining intervals; either...
#   (4) Returns the result count.
#
# Time Complexity: O(n log(n)), where n is the length of the list.
# Space Complexity: O(1).
def merge_intervals(l):
    if isinstance(l, list):
        l.sort(key=lambda x: (x[0], x[1]))
        result = 0
        prev_end = None
        for interval in l:
            if prev_end is None or prev_end <= interval[0]:
                prev_end = interval[1]
            else:
                result += 1
                prev_end = min(prev_end, interval[1])
        return result


fns = [merge_intervals]
args = [[[1, 8], [-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]],
        [[1, 8], [-4, -1], [11, 12], [0, 2], [3, 6], [7, 9], [14, 17]],
        [[15, 18], [2, 6], [1, 3], [8, 10]],
        [[1, 4], [4, 5]],
        [[1, 1]],
        [[5, 6], [6, 7], [2, 3], [0, 1], [9, 10], [1, 2], [3, 4], [7, 8], [4, 5], [8, 9]],
        []]

for intervals in args:
    print(f"\nintervals: {intervals}")
    for fn in fns:
        print(f"{fn.__name__}(intervals): {fn(intervals)}")
    print()


