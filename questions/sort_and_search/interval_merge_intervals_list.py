"""
    INTERVAL: MERGE INTERVALS LIST (leetcode.com/problems/merge-intervals)

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
#   - Will each interval be correctly formatted (have a start and and end, start < end)?
#   - Are the interval endpoints open or closed?


# APPROACH: Brute Force (NOT IMPLEMENTED)
#
# Find the smallest start and the largest end point from the list, then create the result list from testing each integer
# in the range from the smallest to the largest for membership in the set.
#
# Time Complexity: O(d * n), where d is the difference of the two extreme values, and n is the (new) set (list) size.
# Space Complexity: O(r), where r is the length of the result list.


# Approach: Via Sort
#
# This approach improves on the brute force approach (above) and does not check ALL integers in the range of lowest to
# highest interval, only the integers in the combined set of intervals endpoints.
#
# This approach is:
#   (1) Sort intervals by start then end times.
#   (2) Add the first interval to the result list, set 'current' to the next interval then:
#   (3) Loop until 'current' reaches the end of the list; where each 'current' is compared to the last interval in the
#       result list.  If 'current' would extend the last results interval, update the last interval, else, append the
#       'current' interval to the result list.  Update 'current' to point to the next interval.
#   (4) Return the result list.
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(r), where r is the length of the result list.
def merge_intervals_list(l):
    if isinstance(l, list):
        if len(l) == 0:
            return l
        l.sort(key=lambda x: (x[0], x[1]))
        results = [l[0][:]]
        curr = 1
        while curr < len(l):
            if l[curr][0] <= results[-1][1]:
                if l[curr][1] > results[-1][1]:
                    results[-1][1] = l[curr][1]
            else:
                results.append(l[curr][:])
            curr += 1
        return results


args = [[[1, 8], [-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]],
        [[1, 8], [-4, -1], [11, 12], [0, 2], [3, 6], [7, 9], [14, 17]],
        [[15, 18], [2, 6], [1, 3], [8, 10]],
        [[1, 4], [4, 5]],
        []]
fns = [merge_intervals_list]

for interval_list in args:
    print(f"\ninterval_list: {interval_list}")
    for fn in fns:
        print(f"{fn.__name__}(intervals_list): {fn(interval_list)}")
    print()


