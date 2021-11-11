"""
    LEN LONGEST SUBLIST WITH SUM

    Write a function, which takes a list and a target value t, and returns the length of the longest sublist with sum t.

    Example:
        Input = [1, 2, 1, 3], 3
        Output = 2

    Variations:
        - SEE: find_sublists_with_sum.py and num_sublists_with_sum.py
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
# the length of the longest matching sublist.
#
# Time Complexity: O(n**3), where n is the length of the list.
# Space Complexity: O(1).
def len_longest_sublist_with_sum_via_naive_bf(l, t=0):
    if l is not None:
        result = 0
        for i in range(len(l)):
            for j in range(i, len(l)):
                curr_sum = 0
                for k in range(i, j+1):
                    curr_sum += l[k]
                if curr_sum == t and (j - i + 1 > result):
                    result = j - i + 1
        return result


# APPROACH: Improved Brute Force
#
# For each possible starting index, iteratively add each of the values.  If the running sum is ever equal to the target
# sum, then compare the found sublist length to the result.  If the new sublist length is greater than the (previous)
# result update the result.  After all iterations, return the length of the longest matching sublist result.
#
# Time Complexity: O(n**2), where n is the length of the list.
# Space Complexity: O(1).
def len_longest_sublist_with_sum_via_bf(l, t=0):
    if l is not None:
        result = 0
        for i in range(len(l)):
            curr_sum = 0
            for j in range(i, len(l)):
                curr_sum += l[j]
                if curr_sum == t and (j - i + 1 > result):
                    result = j - i + 1
        return result


# APPROACH: Via Dictionary
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
# associated index (of the complement) would make for a longer sublist and update max_len accordingly.
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(n), where n is the length of the list.
def len_longest_sublist_with_sum_via_dict(l, t=0):
    d = {}
    total = 0
    max_len = 0
    counter = 0
    for i in range(len(l)):
        counter += 1
        total += l[i]
        if total == t:                                      # If sum from beginning to curr pointer is equal to t
            max_len = i + 1                                     # Then update max_len (a longer sublist doesn't exists).
        if total - t in d and i - d[total - t] > max_len:   # If the difference has been seen before and is > max_len:
            max_len = i - d[total - t]                          # Update max_len to be the larger of the two.
        if total not in d:
            d[total] = i
    return max_len


lists = [[1, 2, 1, 3],
         [0, 0, 0, 0, 0, 0, 0],
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
t_vals = [0, 3, -3]
fns = [len_longest_sublist_with_sum_via_naive_bf,
       len_longest_sublist_with_sum_via_bf,
       len_longest_sublist_with_sum_via_dict]

for l in lists:
    for t in t_vals:
        print(f"l: {l}")
        for fn in fns:
            print(f"{fn.__name__}(l, {t}): {fn(l[:], t)}")
        print()


