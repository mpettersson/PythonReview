"""
    FIND LONGEST SUBLIST WITH SUM T

    Write a function, which takes a list and a target value t, and returns the start and end indices of the longest
    sublist with sum t (None otherwise).

    Example:
        Input = [1, 2, 1, 3], 3
        Output = (0, 1)  # or the list [1, 2], or indices/list (1, 2)/[2, 1]]
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Sublist/Substring or Subsequence? (Don't get them confused!)
#   - What are the size limits of the list?
#   - Are the values negative & positive?
#   - Are there duplicate values in the list?
#   - The whole list can be a sublist?


# APPROACH: Naive/Brute Force
#
# For each possible starting indices in the list, iterate over the values to find the sum.  If the sum is equal to the
# target sum and greater (in length) than the result, update the result.  After all iterations have completed, return
# the longest matching sublist.
#
# Time Complexity: O(n**3), where n is the length of the list.
# Space Complexity: O(1).
def find_longest_sublist_with_sum_via_naive_bf(l, t=0):
    if l is not None:
        result = None
        for i in range(len(l)):
            for j in range(i, len(l)):
                curr_sum = 0
                for k in range(i, j+1):
                    curr_sum += l[k]
                if curr_sum == t and (result is None or j - i > result[1] - result[0]):
                    result = (i, j)
        return result   # NOTE: Could return max_len here too, or result, longest_len.


# APPROACH: (Space Optimized) Improved Brute Force
#
# For each possible starting index, iteratively add each of the values.  If the running sum is ever equal to the target
# sum, then compare the found sublist length to the result.  If the new sublist length is greater than the (previous)
# result update the result.  After all iterations, return the result.
#
# Time Complexity: O(n**2), where n is the length of the list.
# Space Complexity: O(1).
def find_longest_sublist_with_sum_via_bf(l, t=0):
    if l is not None:
        result = None
        for i in range(len(l)):
            curr_sum = 0
            for j in range(i, len(l)):
                curr_sum += l[j]
                if curr_sum == t and (result is None or j - i > result[1] - result[0]):
                    result = i, j
        return result   # NOTE: Could return max_len here too, or result, longest_len.


# APPROACH: (Time Optimized) Via Dictionary
#
# If the cumulative total (or sum), is maintained/cached, we don't need re-iterate or recalculate sums. If a dictionary
# is used to cache the cumulative sums (to their indices), then fast (O(1)) lookups will allow for both checking IF the
# complement (t - current sum) value has been seen, and (if so) the index it was last seen.
#
# For example:
#   Consider the list [1, 2, 1, 3] and t value of 3.
#   Cumulative sums:  [1, 3, 4, 7]
#
# Therefore, iterate over the values in the list ONCE.  During the iteration; maintain a cumulative sum (total), current
# max sublist length (max_len) and the indices of the longest sublist (result).  IF the cumulative sum (total) is EVER
# equal to the target value it automatically becomes the longest sublist (because 0 is the smallest index), else
# calculate the complement (target sum - cumulative sum) and check if it is in the dictionary.  If so, then check if the
# associated index (of the complement) would make for a longer sublist and update max_len/result accordingly.
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(n), where n is the length of the list.
def find_longest_sublist_with_sum_via_dict(l, t=0):
    d = {}                                                  # Dictionary of Total :-> Index
    total = 0                                               # Cumulative total (i.e., sum(l[:i+1] for i in loop).
    max_len = 0                                             # Length of longest seen sublist.
    result = None                                           # Indices of longest seen sublist.
    for i in range(len(l)):                                 # O(n), just one loop...
        total += l[i]                                       # Need to keep a running total.
        if total == t:                                      # If total is ever equal to target value:
            max_len = i + 1                                     # Update max_len (a longer sublist DNE).
            result = 0, i                                       # Update Result.
        else:                                               # Else:
            c = total - t                                       # Compute the COMPLEMENT/DIFF.
            if c in d and i - d[c] > max_len:                   # If the DIFF in dict, curr idx - diff idx > max_len:
                max_len = i - d[total - t]                          # Update max_len.
                result = d[total - t] + 1, i                        # Update result.
        if total not in d:
            d[total] = i
    return result


lists = [[1, 2, 1, 3],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 1, 2, 1, 3],
         [2, -2, 2, -2, 2, -2],
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
t_vals = [0, 3, -3]
fns = [find_longest_sublist_with_sum_via_naive_bf,
       find_longest_sublist_with_sum_via_bf,
       find_longest_sublist_with_sum_via_dict]

for l in lists:
    for t in t_vals:
        print(f"l: {l}")
        for fn in fns:
            print(f"{fn.__name__}(l, {t}): {fn(l[:], t)}")
        print()


