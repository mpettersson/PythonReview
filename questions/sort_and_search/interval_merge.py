"""
    INTERVAL MERGE (leetcode.com/problems/merge-intervals)

    Write a function which takes a list of intervals with integer endpoints, then computes and returns the union, or
    merge, of the intervals in the list.

    Example:
        Input = [[1,8], [-4, -1], [11, 12], [0, 2], [3, 6], [7, 9], [14, 17]]
        Output = [[-4, -1], [0, 9], [11, 12], [14, 17]]

    REMEMBER: '(', ')' is open (up to, not including), '[', ']' is closed (up to, including).
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible list lengths (empty)?
#   - Will each interval be correctly formatted (have a start and end, start < end, etc.)?
#   - Are the interval endpoints open or closed?


# APPROACH: Brute Force (NOT IMPLEMENTED)
#
# Find the smallest start and the largest end point from the list, then create the result list from testing each integer
# in the range from the smallest to the largest for membership in the set.
#
# Time Complexity: O(d * n), where d is the difference of the two extreme values, and n is the (new) set (list) size.
# Space Complexity: O(r), where r is the length of the result list.


# APPROACH: Via Sort
#
# This approach improves on the brute force approach (above) by first sorting the intervals by their start values.  This
# ensures that any overlapping intervals will be next to each other, thus simplifying the number of comparisons.
#
# This approach:
#   (1) Sorts the intervals by start then end times.
#   (2) Adds the first interval to the result list.
#   (3) Iterates over the remaining intervals; either merging the current interval with the last interval of the result
#       list, OR appended it to the result list.
#   (4) Returns the result list of merged intervals.
#
# Time Complexity: O(n log(n)), where n is the length of the list.
# Space Complexity: O(n), where n is the length of the list.
def merge_intervals(l):
    if isinstance(l, list):
        l.sort(key=lambda x: (x[0], x[1]))
        result = []
        for interval in l:
            if len(result) == 0 or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
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


