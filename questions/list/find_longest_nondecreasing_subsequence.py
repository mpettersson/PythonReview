"""
    LEN LONGEST NONDECREASING SUBSEQUENCE

    Write a function that takes an integer list l, then computes and returns the length of the longest nondecreasing
    subsequence in the list.  Remember, elements of a non-decreasing subsequence are NOT required to immediately follow
    each other in the given list.

    Example:
        Input = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
        Output = [0, 4, 10, 14]  # or [0, 2, 6, 9], or [0, 8, 10, 14]

    Variations:
        - Define a sequence of points in the plane to be ascending if each point is above and to the right of the
          previous point.  How would you find a maximum ascending subset of a set of points in the plane?

    Applications:
        - String matching.
        - Analyzing card games.
"""
from bisect import bisect_right


# APPROACH: Memoization/Dynamic Programming Approach
#
# This approach uses a memoization cache (which is initialized to all 1s) to record the length of the longest
# nondecreasing subsequence ending at the respective index.  Previous pointers (prev), which point to the previous
# element in the longest nondecreasing subsequence (that the element is a part of), are also maintained so that the
# subsequence can be built and returned.
#
# Starting from index 1, each previous value is compared to the current value; if the previous value is less or equal
# than the current value, and the previous value has a longer subsequence length (memo[current]), then the cache,
# previous pointer is updated.  Furthermore, if the element is the last of the longest seen subsequence, the last
# pointer is also updated.  Once all of the values have been compared, the longest nondecreasing subsequence
# is built from the previous pointers list, and returned.
#
# The following shows the memo (lengths) and prev (pointer to previous index) lists, as well as the (index of the) last
# element in the longest nondecreasing subsequence, for the example above:
#
#     list: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
#     memo: [1, 1, 1,  1, 1,  1, 1,  1, 1, 1]  last: 0  prev: [None,None,None,None,None,None,None,None,None,None]
#           [1, 2, 1,  1, 1,  1, 1,  1, 1, 1]        1        [None, 0, None,None,None,None,None,None,None,None]
#           [1, 2, 2,  1, 1,  1, 1,  1, 1, 1]        1        [None, 0, 0, None,None,None,None,None,None,None]
#           [1, 2, 2,  3, 1,  1, 1,  1, 1, 1]        3        [None, 0, 0, 1, None,None,None,None,None,None]
#           [1, 2, 2,  3, 2,  1, 1,  1, 1, 1]        3        [None, 0, 0, 1, 0, None,None,None,None,None]
#           [1, 2, 2,  3, 2,  3, 1,  1, 1, 1]        3        [None, 0, 0, 1, 0, 1, None,None,None,None]
#           [1, 2, 2,  3, 2,  3, 3,  1, 1, 1]        3        [None, 0, 0, 1, 0, 1, 2, None,None,None]
#           [1, 2, 2,  3, 2,  3, 3,  4, 1, 1]        7        [None, 0, 0, 1, 0, 1, 2, 3, None,None]
#           [1, 2, 2,  3, 2,  3, 3,  4, 2, 1]        7        [None, 0, 0, 1, 0, 1, 2, 3, 0, None]
#           [1, 2, 2,  3, 2,  3, 3,  4, 2, 4]        7        [None, 0, 0, 1, 0, 1, 2, 3, 0, 6]
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space Complexity: O(n), where n is the number of elements in the list.
def find_longest_nondecreasing_subsequence_memo(l):
    if isinstance(l, list):
        result = []
        if len(l) > 0:
            memo = [1] * len(l)                         # Each element of l has a length of one to start with.
            prev = [None] * len(l)
            last = 0
            for i in range(1, len(l)):                  # Start at the second element (the first won't change):
                for j in range(0, i):                       # And for each of the previous elements (starting at idx 0):
                    if l[i] >= l[j] and memo[i] < memo[j] + 1:  # If they are smaller than the current element AND their
                        memo[i] = memo[j] + 1                       # length (memo) is larger, use their length (memo)+1
                        prev[i] = j                                 # Update the elements previous pointer.
                        last = i if memo[last] < memo[i] else last  # Update the last element in longest subsequence.
            while last is not None:                     # Build the longest nondecreasing subsequence.
                result.insert(0, l[last])
                last = prev[last]
        return result


# APPROACH: Greedy With Binary Search (Or Modified Patience Sort)
#
# The following is a Greedy approach that uses Binary Search (essentially a modified version of Patience Sort).
#
# Patience Sort uses 'piles' (or lists) of 'cards' (numbers), where each 'new card' (or a current value) is placed on
# the furthest left 'pile' (list) with a value greater than the current value.  If there is no 'pile' with a top 'card'
# less than the current 'card' a new 'pile' (list) is created (on the right).  The number of 'piles' at the end of the
# sort is the length of the longest nondecreasing subsequence.  Consider the following example:
#
#   cards: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
#   piles:  0   8  12  14
#               4  10   9
#               2   6
#               1
#
# This approach DOES NOT use 2D 'piles' due to the high overhead to sort/search 2D lists. However, two lists, a values
# and an index list, is used to emulate the tops of the 'piles'.  With this implementation, the list of 'top cards' can
# be quickly searched via binary search (bisect_left). An additional list (prev, which is initialized to all None
# values) is used to map a 'card' with the previous 'card' in a nondecreasing subsequence.  If a new pile is needed, the
# (values/indices) lists append the corresponding value/index, else the value/index of the 'top card' on the 'pile' is
# replaced.  When a 'card' is placed on any non-initial 'pile', it's pointer is updated to point to the top 'card' in
# the immediately preceding 'pile'. Once complete, the longest nondecreasing subsequence is then built, and returned,
# using the previous pointers list.
#
# The following shows the top_val, top_idx, and prev lists values for the example above:
#
#         l: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
#   top_val: []                top_idx: []                    prev: []
#            [0]                        [0]                         [None,None,None,None,None,None,None,None,None,None]
#            [0, 8]                     [0, 1]                      [None, 0, None,None,None,None,None,None,None,None]
#            [0, 4]                     [0, 2]                      [None, 0, 0, None,None,None,None,None,None,None]
#            [0, 4, 12]                 [0, 2, 3]                   [None, 0, 0, 2, None, None ,None, None, None, None]
#            [0, 2, 12]                 [0, 4, 3]                   [None, 0, 0, 2, 0, None, None, None, None, None]
#            [0, 2, 10]                 [0, 4, 5]                   [None, 0, 0, 2, 0, 4, None, None, None, None]
#            [0, 2, 6]                  [0, 4, 6]                   [None, 0, 0, 2, 0, 4, 4, None, None, None]
#            [0, 2, 6, 14]              [0, 4, 6, 7]                [None, 0, 0, 2, 0, 4, 4, 6, None, None]
#            [0, 1, 6, 14]              [0, 8, 6, 7]                [None, 0, 0, 2, 0, 4, 4, 6, 0, None]
#            [0, 1, 6, 9]               [0, 8, 6, 9]                [None, 0, 0, 2, 0, 4, 4, 6, 0, 6]
#
# Time Complexity: O(n * log(n)), where n is the number of elements in the list.
# Space Complexity: O(n), where n is the number of elements in the list.
def find_longest_nondecreasing_subsequence(l):
    if isinstance(l, list):
        result = []
        if len(l) > 0:
            top_val = []            # NOTE: We use two lists (as opposed to a (val, idx) tuple) so bisect can be used
            top_idx = []            # w/o being modified (if (val,idx) it'd compare idx too, which isn't what we want).
            prev = [None] * len(l)
            for i, x in enumerate(l):
                pile = bisect_right(top_val, x)     # Binary search to find the 'pile' that the 'card' goes on.
                if pile == len(top_val):
                    top_val.append(x)
                    top_idx.append(i)
                else:
                    top_val[pile] = x
                    top_idx[pile] = i
                if pile > 0:
                    prev[i] = top_idx[pile - 1]     # 'cards' in first pile won't have a prev pointer, all others do.
            curr = top_idx[-1]
            while curr is not None:
                result.insert(0, l[curr])
                curr = prev[curr]
        return result


lists = [[0, 8, 4, 12, 2, 10, 6, 14, 1, 9],
         [0, 8, 0, 0, 2, 8, 2, 8, 0, 8],
         [10, 5, 8, 3, 9, 4, 12, 11],
         [9, 11, 7, 16, 7, 15, 10, 14, 19, 2],
         [7, 3, 7, 6, 5, 3, 4, 2, 4, 10],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
         []]
fns = [find_longest_nondecreasing_subsequence_memo,
       find_longest_nondecreasing_subsequence]

for l in lists:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l[:])}")
    print()


