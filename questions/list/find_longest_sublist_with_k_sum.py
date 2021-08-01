"""
    FIND LONGEST SUBLIST WITH K SUM (geeksforgeeks.org/find-the-largest-subarray-with-0-sum)

    Write a function, which takes a list and a value k, and returns the start and end indices of the longest sublists
    that sum to k (None otherwise).

    Example:
        Input = [1, 2, 1, 3], 3
        Output = [[1, 2], [2, 1], [3]]

    Variations:
        - SEE: find_sublists_with_k_sum.py, num_sublists_with_k_sum.py, len_longest_sublist_with_k_sum.py
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Sublist/Substring or Subsequence? (Don't get them confused!)
#   - What are the size limits of the list?
#   - Are the values negative & positive?
#   - Are there duplicate values in the list?


# APPROACH: Brute Force
#
# This approach is basically the same as the approach above, however, a few optimizations have been included.
#
# Time Complexity: O(n**2), where n is the length of the list.
# Space Complexity: O(1).
def find_longest_sublist_with_k_sum_bf(l, k=0):
    if l is not None:
        result = None
        for i in range(len(l)):         # O(n)
            curr_sum = 0
            for j in range(i, len(l)):      # O(n)
                curr_sum += l[j]
                if curr_sum == k and (result is None or j - i > result[1] - result[0]):
                    result = i, j
        return result   # NOTE: Could return max_len here too, or result, longest_len.


# APPROACH: Via Dictionary
#
# Observation:
# If the cumulative total (or sum), is maintained/cached, we don't need re-iterate or recalculate sums. If a dictionary
# is used to cache the total sums, then O(1) lookups will further reduce the search time.
# For example:
#   Consider the list [1, 2, 1, 3] and k value of 3.
#   Cumulative sums:  [1, 3, 4, 7]
#
# Iterate over the values adding them up.  If a sum is equal to k, then a list (starting at 0) is added to the results.
# Also maintain a dictionary of (total: indices) to be able to search (in O(1) time) if sublists have the sum of k.
#
# Time Complexity: O(n**2), where n is the length of the list.
# Space Complexity: O(n), where n is the length of the list.
def find_longest_sublist_with_k_sum(l, k=0):
    d = {}
    total = max_len = 0
    result = None
    for i in range(len(l)):
        total += l[i]
        if total == k:                                      # If sum from beginning to curr pointer is equal to k
            max_len = i + 1                                     # Then update max_len (a longer sublist doesn't exists).
            result = 0, i                                       # Update Result.
        if total - k in d and i - d[total - k] > max_len:   # If the difference has been seen before and is > max_len:
            max_len = i - d[total - k]                          # Update max_len to be the larger of the two.
            result = d[total - k] + 1, i                        # Update result.
        if total not in d:
            d[total] = i
    return result


lists = [[1, 2, 1, 3],
         [0, 1, 2, 1, 3],
         [3, -1, 1],
         [0, 3, -1, 1, 0],
         [1, 2, 1, 0, 3],
         [1, 1, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 1, 1, 1, 0, 0, 1, -1, 0],
         [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [1, 2, -5, 1, 2, -1],
         [1, 2, -5, 1, 2, 0, 0, -1]]
k_vals = [0, 3]
fns = [find_longest_sublist_with_k_sum_bf,
       find_longest_sublist_with_k_sum]

for l in lists:
    for k in k_vals:
        for fn in fns:
            print(f"{fn.__name__}({l}, {k}): {fn(l, k)}")
        print()


