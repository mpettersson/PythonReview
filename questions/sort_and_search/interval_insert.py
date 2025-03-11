"""
    INTERVAL INSERT (EPI 14.5: MERGING INTERVALS,
                     leetcode.com/problems/insert-interval)

    Write a function which takes an interval to be added and a list of disjoint closed intervals with integer endpoints
    (sorted by left endpoint), then computes and returns the union of the intervals in the list and the added interval
    (sorted by left endpoint).

    Example:
        Input = ([1,8], [[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]])
        Output = [[-4, -1], [0, 9], [11, 12], [14, 17]]

    REMEMBER: '(', ')' is open (up to, not including), '[', ']' is closed (up to, including).
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible list lengths (empty)?
#   - Will each interval be correctly formatted (have a start and end, start < end)?
#   - Are the interval endpoints open or closed?


# APPROACH: Brute Force (NOT IMPLEMENTED)
#
# Form a set with all the list intervals and the new interval.  Find the smallest start and the largest end point from
# the set, then create the result list from testing each integer in the range from the smallest to the largest for
# membership in the set.
#
# Time Complexity: O(d * n), where d is the difference between the two extreme values, and n is the (new) set size.
# Space Complexity: O(r), where r is the length of the result list.


# Approach: Improved
#
# This approach improves on the brute force approach (above) and does not check ALL integers in the range of lowest to
# highest interval, only the integers in the combined set of intervals endpoints.
#
# The process is:
#   (1) Add each interval that (starts and) ends BEFORE the added (new) interval to the result.
#   (2) Once at the interval that intersects with the added (new) interval, compute the union, iterating through
#       subsequent intervals (if they intersect with the added interval), and add (the union interval) to result.
#   (3) Iterate through remaining intervals, adding them to result.
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(r), where r is the length of the result list.
def insert_interval(new_interval, intervals):
    if intervals is not None and new_interval is not None:
        result = []
        i = 0
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= new_interval[1]:
            new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
            i += 1
        result.append(new_interval)
        result += intervals[i:]
        return result


args = [([1, 8], [[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]]),
        ([2, 6], [[1, 3], [8, 10], [15, 18]]),
        ([1, 4], [[4, 5]])]
fns = [insert_interval]

for new_interval, intervals in args:
    print(f"new_interval: {new_interval}\nintervals: {intervals}")
    for fn in fns:
        print(f"{fn.__name__}(new_interval, intervals): {fn(new_interval, intervals)}")
    print()


