"""
    LEN LONGEST NONDECREASING SUBSEQUENCE (EPI 17.12: FIND THE LONGEST NONDECREASING SUBSEQUENCE)

    Write a function that takes an integer list l, then computes and returns the length of the longest nondecreasing
    subsequence in the list.  Remember, elements of a non-decreasing subsequence are NOT required to immediately follow
    each other in the given list.

    Example:
        Input = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
        Output = 4  # either len([0, 4, 10, 14]), len([0, 2, 6, 9]), or len([0, 8, 10, 14])

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
# nondecreasing subsequence ending at the respective index.  Starting from index 1, each previous value is compared to
# the current value; if the previous value is less or equal than the current, memo[current] is equal to the larger of
# the memo[previous]+1 OR memo[current].  Once all of the values have been compared, the maximum memo value is returned
# as the result.  The following is an example of the memo table for the example (above):
#
#                list: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
#      memo (initial): [1, 1, 1,  1, 1,  1, 1,  1, 1, 1]
#                      [1, 2, 1,  1, 1,  1, 1,  1, 1, 1]
#                      [1, 2, 2,  1, 1,  1, 1,  1, 1, 1]
#                      [1, 2, 2,  3, 1,  1, 1,  1, 1, 1]
#                      [1, 2, 2,  3, 2,  1, 1,  1, 1, 1]
#                      [1, 2, 2,  3, 2,  3, 1,  1, 1, 1]
#                      [1, 2, 2,  3, 2,  3, 3,  1, 1, 1]
#                      [1, 2, 2,  3, 2,  3, 3,  4, 1, 1]
#                      [1, 2, 2,  3, 2,  3, 3,  4, 2, 1]
#        memo (final): [1, 2, 2,  3, 2,  3, 3,  4, 2, 4]
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space Complexity: O(n), where n is the number of elements in the list.
def len_longest_nondecreasing_subsequence_memo(l):
    if isinstance(l, list):
        memo = [1] * len(l)                         # Each element of l has a length of one to start with.
        for i in range(1, len(l)):                  # Start at the second element (the first won't change):
            for j in range(0, i):                       # And for each of the previous elements (starting at idx 0):
                if l[i] >= l[j] and memo[i] < memo[j] + 1:  # If they are smaller than the current element AND their
                    memo[i] = memo[j] + 1                       # length (memo) is higher, use their length (memo) + 1
        return max(memo) if len(memo) > 0 else 0


# APPROACH: Greedy With Binary Search (AKA Modified Patience Sort)
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
# This approach DOES NOT use multiple 'piles' due to the high overhead to sort/search multiple lists. However, a single
# list can be used to emulate the tops of the piles; the list of 'top cards' can be quickly searched via binary search.
# Then the value of the 'top car' is replaced (as opposed to being stacked on) thus maintaining the number and top value
# of the piles.  Once complete the length of the list of top values is returned. Consider the example above with this
# new Greedy/Binary Search approach:
#
#         l: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
#     piles: []
#            [0]
#            [0, 8]
#            [0, 4]
#            [0, 4, 12]
#            [0, 2, 12]
#            [0, 2, 10]
#            [0, 2, 6]
#            [0, 2, 6, 14]
#            [0, 1, 6, 14]
#            [0, 1, 6, 9]
#
# Time Complexity: O(n * log(n)), where n is the number of elements in the list.
# Space Complexity: O(n), where n is the number of elements in the list.
def len_longest_nondecreasing_subsequence(l):
    if isinstance(l, list):
        tops = []                               # This emulates the tops of the piles in a Patience Sort.
        for e in l:                             # For each value in the list:
            if len(tops) == 0 or e >= tops[-1]:      # If no 'piles' yet, or current value is greater than top values:
                tops.append(e)                          # Make a new 'pile'.
            else:                                   # Else
                tops[bisect_right(tops, e)] = e         # Binary search for the value to replace with the current value.
        return len(tops)                        # Return the number of 'piles'.


lists = [[0, 8, 4, 12, 2, 10, 6, 14, 1, 9],
         [0, 8, 0, 0, 2, 8, 2, 8, 0, 8],
         [10, 5, 8, 3, 9, 4, 12, 11],
         [9, 11, 7, 16, 7, 15, 10, 14, 19, 2],
         [7, 3, 7, 6, 5, 3, 4, 2, 4, 10],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
         []]
fns = [len_longest_nondecreasing_subsequence_memo,
       len_longest_nondecreasing_subsequence]

for l in lists:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l[:])}")
    print()


