"""
    FIND SUBLISTS WITH SUM

    Write a function, which takes an integer list l and a target sum t, and returns a list of tuples (start_index,
    end_index) of all sublists in l, with sum t.

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
def find_sublists_with_sum_naive_bf(l, t=0):
    if l is not None:
        result = []
        for i in range(len(l)):         # O(n)
            for j in range(i, len(l)):      # O(n)
                temp = l[i:j+1]                 # O(n)
                if sum(temp) == t:              # O(n)
                    result.append((i, j))
#                   result.append(temp)         # Use this to return an actual list of sublists.
        return result


# APPROACH: Brute Force
#
# This approach is basically the same as the approach above, however, a few optimizations have been included.
#
# Time Complexity: O(n**2), where n is the length of the list.
# Space Complexity: O(n**2), where n is the length of the list.
def find_sublists_with_sum_bf(l, t=0):
    if l is not None:
        result = []
        for i in range(len(l)):         # O(n)
            curr_sum = 0
#           sublist = []                        # Use this to return an actual list of sublists.
            for j in range(i, len(l)):      # O(n)
                curr_sum += l[j]
#               sublist.append(l[j])            # Use this to return an actual list of sublists.
                if curr_sum == t:
                    result.append((i, j))
#                   result.append(sublist[:])   # Use this to return an actual list of sublists.
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
# associated index (of the complement) would make for a longer sublist and update max_len/result accordingly.
#
# Time Complexity: O(n**2), where n is the length of the list.
# Space Complexity: O(n**2), where n is the length of the list.
#
# NOTE: If only a count was needed (SEE Variations), then O(n) time and space could be achieved.
def find_sublists_with_sum_via_dict(l, t=0):
    if l is not None:
        result = []
        total = 0
        d = dict()                                      # Dict of Totals :-> Indices (of list) with totals.
        for i in range(len(l)):                         # O(n)
            total += l[i]                                   # Update total first.
            if total == t:                                  # If total from index 0/start to i is equal to k.
                result.append((0, i))                           # Append the sublist indices to the result.
#               result.append(l[0:i+1])                         # Use this to return an actual list of sublists.
            complement = total - t
            if complement in d:                             # Check if complement sublists exist.
                for start_index in d[complement]:           # O(n)
                    result.append((start_index+1, i))           # If so, then the complement sublist is also a solution.
# NOTE: Since the value at start_index is part of the complement, it is NOT used in the sublist.  Hence, start_index+1.
#                   result.append(l[start_index+1:i+1])         # Use this to return an actual list of sublists.
            d[total] = d.setdefault(total, []) + [i]        # Add cumulative/current total and current index to dict.
        return result


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
fns = [find_sublists_with_sum_bf,
       find_sublists_with_sum_naive_bf,
       find_sublists_with_sum_via_dict]

for l in lists:
    for t in t_vals:
        print(f"l: {l}")
        for fn in fns:
            print(f"{fn.__name__}({l}, {t}): {fn(l, t)}")
        print()


