"""
    NUM SUBLISTS WITH K SUM (50CIQ 11: ZERO SUM SUBARRAY,
                              leetcode.com/problems/subarray-sum-equals-k)

    Write a function, which takes a list and a value k, and returns the number of all sublists that sum to k.

    Example:
        Input = [1, 2, 1, 3], 3
        Output = 3  # That is; [[1, 2], [2, 1], [3]]

    Variations:
        - SEE: find_sublists_with_k_sum.py, find_longest_sublist_with_k_sum.py, len_longest_sublist_with_k_sum.py
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
# Space Complexity: O(n), where n is the length of the list.
def num_sublists_with_k_sum_naive_bf(l, k=0):
    if l is not None:
        result = 0
        for i in range(len(l)):         # O(n)
            for j in range(i, len(l)):      # O(n)
                temp = l[i:j+1]                 # O(n)
                if sum(temp) == k:              # O(n)
                    result += 1
        return result


# APPROACH: Brute Force
#
# This approach is basically the same as the approach above, however, a few optimizations have been included.
#
# Time Complexity: O(n**2), where n is the length of the list.
# Space Complexity: O(1).
def num_sublists_with_k_sum_bf(l, k=0):
    if l is not None:
        result = 0
        for i in range(len(l)):         # O(n)
            curr_sum = 0
            for j in range(i, len(l)):      # O(n)
                curr_sum += l[j]
                if curr_sum == k:
                    result += 1
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
# Iterate over the values of the list, maintaining a dictionary with the sublists totals.  If the difference between the
# current total and k is zero, or is in the dictionary, then add one to the result.
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(n), where n is the length of the list.
def num_sublists_with_k_sum(l, k=0):
    if l is not None:
        result = total = 0
        d = {0: 1}                          # If the total is ever equal to k.
        for i in range(len(l)):
            total += l[i]                   # Update total first.
            result += d.get(total - k, 0)   # Add the count associated with the difference to result (0 is not in d).
            d[total] = d.get(total, 0) + 1  # Update or add a value for the current total to d.
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
fns = [num_sublists_with_k_sum_naive_bf,
       num_sublists_with_k_sum_bf,
       num_sublists_with_k_sum]

for l in lists:
    for k in k_vals:
        for fn in fns:
            print(f"{fn.__name__}({l}, {k}): {fn(l, k)}")
        print()


