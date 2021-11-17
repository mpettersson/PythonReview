"""
    INTERVAL: MERGE WITH SORTED INTERVALS (EPI 14.5: MERGING INTERVALS)

    Write a function which takes an interval to be added and a list of disjoint closed intervals with integer endpoints
    (sorted by left endpoint), then computes and returns the union of the intervals in the list and the added interval
    sorted by left endpoint).

    Example:
        Input = ([1,8], [[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]])
        Output = [[-4, -1], [0, 9], [11, 12], [14, 17]]

    REMEMBER: '(', ')' is open (up to, not including), '[', ']' is closed (up to, including).
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible list lengths (empty)?
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
def merge_with_sorted_intervals(new_interval, intervals_list):
    if intervals_list is not None and new_interval is not None:
        result = []
        i = 0
        while i < len(intervals_list) and intervals_list[i][1] < new_interval[0]:
            result.append(intervals_list[i])
            i += 1
        merged_interval = None
        while i < len(intervals_list) and intervals_list[i][0] <= new_interval[1]:
            merged_interval = [min(new_interval[0], intervals_list[i][0]), max(new_interval[1], intervals_list[i][1])]
            i += 1
        result.append(merged_interval)
        result += intervals_list[i:]
        return result


args = [([1, 8], [[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]]),
        ([2, 6], [[1, 3], [8, 10], [15, 18]]),
        ([1, 4], [[4, 5]])]
fns = [merge_with_sorted_intervals]

for new_interval, interval_list in args:
    print(f"new_interval: {new_interval}\ninterval_list: {interval_list}")
    for fn in fns:
        print(f"{fn.__name__}(new_interval, intervals_list): {fn(new_interval, interval_list)}")
    print()


