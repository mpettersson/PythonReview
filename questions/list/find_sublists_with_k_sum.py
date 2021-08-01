"""
    FIND SUBLISTS WITH K SUM

    Write a function, which takes a list and a value k, and returns a list of all sublists that sum to k.

    Example:
        Input = [1, 2, 1, 3], 3
        Output = [[1, 2], [2, 1], [3]]

    Variations:
        - SEE: num_sublists_with_k_sum.py, find_longest_sublist_with_k_sum.py, len_longest_sublist_with_k_sum.py
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Sublist/Substring or Subsequence? (Don't get them confused!)
#   - What are the size limits of the list?
#   - Are the values negative & positive?
#   - Are there duplicate values in the list?


# APPROACH: Naive Brute Force
#
# Starting at each index, iterating and summing all possible sublists, without any attempt to optimize.
#
# Time Complexity: O(n**3), where n is the length of the list.
# Space Complexity: O(n**2), where n is the length of the list.
def find_sublists_with_k_sum_naive_bf(l, k=0):
    if l is not None:
        result = []
        for i in range(len(l)):         # O(n)
            for j in range(i, len(l)):      # O(n)
                temp = l[i:j+1]                 # O(n)
                if sum(temp) == k:              # O(n)
                    result.append(temp)
        return result


# APPROACH: Brute Force
#
# This approach is basically the same as the approach above, however, a few optimizations have been included.
#
# Time Complexity: O(n**3), where n is the length of the list.
# Space Complexity: O(n**2), where n is the length of the list.
def find_sublists_with_k_sum_bf(l, k=0):
    if l is not None:
        result = []
        for i in range(len(l)):         # O(n)
            curr_sum = 0
            sublist = []
            for j in range(i, len(l)):      # O(n)
                curr_sum += l[j]
                sublist.append(l[j])
                if curr_sum == k:
                    result.append(sublist[:])   # O(n)
        return result


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
# Space Complexity: O(n**2), where n is the length of the list.
#
# NOTE: If only a count was needed (i.e., the variations listed above), then O(n) time and space could be achieved.
def find_sublists_with_k_sum(l, k=0):
    if l is not None:
        result = []
        total = 0
        d = dict()                                      # Keys: Totals, Values: Indices (of list) with totals.
        for i in range(len(l)):
            total += l[i]                                   # Update total first.
            if total == k:                                  # If total from index 0/start to i is equal to k.
                result.append(l[0:i+1])                         # Add the sublist to the results list.
            difference = total - k
            if difference in d:                             # Check if a sublist (NOT starting at 0), that sums to k has
                for start_index in d[difference]:           # been seen (or, is in d).
                    result.append(l[start_index+1:i+1])         # If so, then that sublist, is a solution.
            d[total] = d.setdefault(total, []) + [i]        # Add current total: current index to dict.
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
fns = [find_sublists_with_k_sum_bf,
       find_sublists_with_k_sum_naive_bf,
       find_sublists_with_k_sum]

for l in lists:
    for k in k_vals:
        for fn in fns:
            print(f"{fn.__name__}({l}, {k}): {fn(l, k)}")
        print()


