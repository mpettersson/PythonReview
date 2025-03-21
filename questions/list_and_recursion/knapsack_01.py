"""
    THE 01 KNAPSACK PROBLEM

    Given a set of items that each have a value and a weight, determine which of those items to select to as to maximize
    the total value, constrained by the given knapsack's capacity.

    NOTE: This variation of the problem is called the 01 knapsack problem because each item can be 'picked' or not
          'picked', and because fractional items are not allowed.

    Example:
        Input = [(65, 20), (35, 8), (245, 60), (195, 55), (65, 40), (99, 10), (275, 85), (155, 25), (120, 30), (75, 75),
                 (320, 65), (40, 10), (200, 95), (100, 50), (220, 40), (150, 70)], 130  # (price, weight), total_weight
        Output = 695    # Max value set: [(155, 25), (320, 65), (220, 40)]
"""
import copy
import itertools
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible values for capacity (int, None, negative, etc.)?
#   - Does the full capacity need to be used (what should happen if can't use total capacity)?
#   - What should be returned (total, or list of items, what should happen if failure)?
#   - What are the possible sizes of the list (empty, max size)?
#   - What are the possible values in the list (int/float/None/negative)?
#   - Can the list have unique/duplicate values?
#   - Will the list be sorted?
#   - Can the list be modified?


# BRUTE FORCE APPROACH OBSERVATIONS:
#
# Brute force is simply an exhaustive search, it generates all possible ways of solving a problem, then tests them.  To
# see, or enumerate, all possible ways of solving the 01 knapsack problem consider the following scenario with items A,
# B, and C:
#       A   B   C
#       0   0   0   (not picking any)
#       1   0   0   (picking A only)
#       0   1   0   (picking B only)
#          ...
#       1   1   1   (picking all items)
#
# Therefore, for any 01 knapsack problem, there are 2**n possibilities, or ways to solve the problem, where n is the
# number of items.
#
# Brute Force Time Complexity: O(2**n), where n is the number of items.


# APPROACH: Brute Force Via Powerset/Itertools Combinations
#
# This brute force approach uses Itertools' combinations to generate each possible set (or the powerset) of the items.
# The set is then summed, and then the highest total that is less than or equal to the capacity is returned.
#
# Time Complexity: O(2**n), where n is the number of elements in items list.
# Space Complexity: O(n), where n is the number of elements in items list (could be O(1) if result_set not maintained).
def knapsack_01_bf_via_itertools(items, capacity):
    if items is not None and capacity is not None and capacity > 0:
        result_set = None
        result_tot = -float('inf')
        for r in range(len(items)+1):
            for s in itertools.combinations(items, r):
                if sum(x.weight for x in s) <= capacity:
                    price = sum(x.value for x in s)
                    if price > result_tot:
                        result_tot = price
                        result_set = set(s)
        return result_tot, result_set


# APPROACH: Brute Force Via Combinatorics/Iterative
#
# This approach counts from 0 to 2**n, and uses the binary representation of the number to form a set.  The set is then
# summed and the highest sum, less than or equal to the capacity, is returned.
#
# Time Complexity: O(2**n), where n is the number of elements in items list.
# Space Complexity: O(m), where m is the size of the max value set (could be O(1) if max_price_set isn't maintained).
def knapsack_01_bf_via_combinatorics(items, capacity):

    def _gen_reversed_bits(n):
        while True:
            yield n & 1
            n >>= 1

    if items is not None and capacity is not None and capacity > 0:
        result_set = None
        result_tot = -float('inf')
        for i in range(2**len(items)):
            g = _gen_reversed_bits(i)
            s = {e for e, b in zip(items, g) if b}
            if sum(x.weight for x in s) <= capacity:
                price = sum(x.value for x in s)
                if price > result_tot:
                    result_tot = price
                    result_set = s
        return result_tot, result_set


# APPROACH: Naive Via Recursion
#
# Starting at the first item, this approach computes then returns the best option (either taking or not taking the item
# with the recursive result from the next item).
#
# Consider the following four items:
#     Items:     A   B   C   D
#     Values:   10  40  30  60
#     Weights:   5   4   6   3
#
# Then the recursion stack for this approach, given a capacity of 10 would start as:
#
#                                 value:0, capacity:10
#                             /                         \
#               (include A)  /                           \ (exclude A)
#                           /                             \
#               value:10, capacity:5                 value:0, capacity:10
#              /                  \                  /                  \
#  (include B)/         (exclude B)\                / (include B)        \ (exclude B)
#            /                      \              /                      \
#      val:10, cap:5        val:0, cap:10     val:40, cap:6           val:0, cap:10
#          /    \               /   \             /   \                   /    \
#        ...    ...           ...  ...          ...   ...               ...    ...
#
# Time Complexity: O(2**n), where n is the number of elements in items list.
# Space Complexity: O(2**n), where n is the number of elements in items list.
def knapsack_01_naive_via_rec(items, capacity):

    def _rec(items, i, c):
        if i < 0 or c <= 0:
            return 0, []                        # Value, List of included Items.
        excluded = _rec(items, i-1, c)
        if c >= items[i].weight:
            included = _rec(items, i-1, c-items[i].weight)
            included = (included[0] + items[i].value, included[1] + [items[i]])
            return max(excluded, included, key=lambda x: x[0])
        return excluded

    if items and capacity > 0:
        return _rec(items, len(items)-1, capacity)


# APPROACH: Memoization/Top Down Dynamic Programming
#
# This approach optimizes the naive recursive approach above by adding a cache, or memoization table, (called dp below)
# to prevent duplicated computations.
#
# NOTE: The padding row has been added to this solution to maintain continuity with the bottom-up solution below.
#       That is, this solution does not require a padding row, it was added so the examples code/matrices can be
#       compared more easily.
#
# If given the following four items:
#     Items:     A   B   C   D
#     Values:   10  40  30  60
#     Weights:   5   4   6   3
#
# Then the completed top down dynamic programming cache, or memoization, table:
#              0      1      2      3      4     5      6      7      8      9      10    (Capacity)
#        [[ None,  None,  None,  None,  None, None,  None,  None,  None,  None,   None],  PADDING (for simplified code)
#     A   [    0,     0,  None,     0,     0, None,    10,    10,  None,  None,     10],
#     B   [ None,     0,  None,  None,    40, None,  None,    40,  None,  None,     50],
#     C   [ None,  None,  None,  None,  None, None,  None,    40,  None,  None,     70],
#     D   [ None,  None,  None,  None,  None, None,  None,  None,  None,  None,    100]]
#
# The completed top down dynamic programming boolean table (for tacking the included items):
#              0      1      2      3      4     5      6      7      8      9      10    (Capacity)
#        [[False, False, False, False, False, False, False, False, False, False, False],   PADDING (for simplified code)
#     A   [False, False, False, False, False, False,  True,  True, False, False,  True],
#     B   [False, False, False, False,  True, False, False,  True, False, False,  True],
#     C   [False, False, False, False, False, False, False, False, False, False,  True],
#     D   [False, False, False, False, False, False, False, False, False, False,  True]]
#
# NOTE: This approach ASSUMES INTEGER VALUES for prices and weights; modify with math.ceil() if REAL NUMS are wanted!
#
# Time Complexity: O(n * capacity), where n is the number of the items list.
# Time Complexity: O(n * capacity), where n is the number of the items list.
def knapsack_01_dp_via_top_down(items, capacity):

    def _rec(items, i, c, dp, b):
        if i == 0:
            return 0
        if dp[i][c] is None:
            excluded = _rec(items, i-1, c, dp, b)
            included = 0 if c < items[i-1].weight else items[i-1].value + _rec(items, i-1, c-items[i-1].weight, dp, b)
            # NOTE: UNBOUNDED KNAPSACK recurses on i, not i-1 (ie, _rec(items, i, c-items[i-1].weight, dp, b)).
            if excluded < included:
                dp[i][c] = included
                b[i][c] = True
            else:
                dp[i][c] = excluded
        return dp[i][c]

    if items is not None and capacity is not None:
        n = len(items)
        dp = [[None] * (capacity+1) for _ in range(n+1)]      # dp[-1][-1] has max value when done
        b = [[False] * (capacity+1) for _ in range(n+1)]
        result_tot = _rec(items, n, capacity, dp, b)
        result_set = []                                         # The next few lines builds the result set from the
        c = capacity                                            # boolean mat, see the example above for more info.
        for i in range(n, 0, -1):                               # NOTE: The reverse order (to start at b[-1][-1])!!
            if b[i][c]:
                result_set.append(items[i-1])
                c -= items[i-1].weight
        return result_tot, result_set


# APPROACH: Tabulation/Bottom Up Dynamic Programming
#
# This approach is very similar to the top-down dynamic programming (it uses a cache, or memoization table, to reuse
# computations), however, it iteratively works from the smallest/bottom-up filling the whole cache, or memoization,
# table. (Where top-down starts at the largest/top value, and recursively solves only the directly required smaller
# valued cells.)
#
# NOTE: A padding row consisting only of zero values has been added to reduce the logic when computing the first item;
#       with the padding row, the first item (2nd row) can simply reference the previous row (added padding row of
#       zeros). Without the padding row the comparison for inclusion/exclusion would be drastically more complicated.
#
# If given the following four items:
#     Items:     A   B   C   D
#     Values:   10  40  30  60
#     Weights:   5   4   6   3
#
# Then the completed bottom up dynamic programming cache, or memoization, table:
#              0      1      2      3      4     5      6      7      8      9      10    (Capacity)
#        [[    0,     0,     0,     0,     0,    0,     0,     0,     0,     0,      0],  PADDING (for simplified code)
#     A   [    0,     0,     0,     0,     0,   10,    10,    10,    10,    10,     10],
#     B   [    0,     0,     0,     0,    40,   40,    40,    40,    40,    50,     50],
#     C   [    0,     0,     0,     0,    40,   40,    40,    40,    40,    50,     70],
#     D   [    0,     0,     0,    60,    60,   60,    60,   100,   100,   100,    100]]
#
# REMINDER: Start at dp[A][cap=0], working right, where dp[row][col] = max(dp[row-1][col], dp[row-1][col-A.weight].
#
# The completed bottom up dynamic programming boolean table (for tacking the included items):
#              0      1      2      3      4     5      6      7      8      9      10    (Capacity)
#        [[False, False, False, False, False, False, False, False, False, False, False],  PADDING (for simplified code)
#     A   [False, False, False, False, False,  True,  True,  True,  True,  True,  True],
#     B   [False, False, False, False,  True,  True,  True,  True,  True,  True,  True],
#     C   [False, False, False, False, False, False, False, False, False, False,  True],
#     D   [False, False, False,  True,  True,  True,  True,  True,  True,  True,  True]]
#
# To build the list of items, start at the b[-1][-1], then do:
#   - If the current cell is True, add the row's item to the output list, then update the col as col-rows.weight.
#   - If the current cell is False, do nothing.
#   - Decrement the row (move one row up).
#
# Once at row 0, return the values. For the example above, the two cells (that cause the item to be appended) are:
#   b['D'][10] and b['B'][7] (the full path is: b['D'][10]->b['D'][7]-> b['C'][7]->b['B'][7]->b['B'][3]->b['A'][7]).
#
# NOTE: This approach ASSUMES INTEGER VALUES for prices and weights; modify with math.ceil() if REAL NUMS are wanted!
#
# Time Complexity: O(n * capacity), where n is the number of the items list.
# Time Complexity: O(n * capacity), where n is the number of the items list.
#
# NOTE: This may appear to be a POLYNOMIAL time solution for a np-complete (01 knapsack) problem.  HOWEVER, the metrics
#       are different; n is the size of a list and capacity is just a number--they must be 'the same'.  Therefore, the
#       capacity needs to be encoded, by say, the number of bits required to represent the capacity:
#           capacity_size = log(b, capacity) ==>
#           capacity = b**capacity_size
#       So O(n * capacity) is really O(n * b**capacity_size), or PSEUDO-POLYNOMIAL, or WEAKLY-NP-COMPLETE.


def knapsack_01_dp_via_bottom_up(items, capacity):
    if items is not None and capacity is not None:
        n = len(items)
        dp = [[0] * (capacity+1) for _ in range(n+1)]       # dp[-1][-1] has max value when done
        b = [[False] * (capacity+1) for _ in range(n+1)]    # NOTE: Be VERY careful with the counters!
        for i in range(1, n+1):                             # i=0 is a padding row, i=1 to n are the list items.
            for c in range(capacity+1):                     # c = a discrete capacity from 0 to total capacity
                excluded = dp[i-1][c]
                included = 0 if c < items[i-1].weight else items[i-1].value + dp[i-1][c-items[i-1].weight]
                # NOTE: For UNBOUNDED KNAPSACK, dp would reference dp[i], not dp[i-1] (ie, dp[i-1][c-items[i-1].weight]).
                if excluded < included:                     # If INCLUDED
                    dp[i][c] = included
                    b[i][c] = True
                else:                                       # Else EXCLUDED
                    dp[i][c] = excluded
        result_set = []                                     # The next few lines builds the result set from the
        c = capacity                                        # boolean matrix, see the example above for more info.
        for i in range(n, 0, -1):                           # NOTE: The reverse order (to start at b[-1][-1])!!
            if b[i][c]:                                     # Only included corresponding items will be True.
                result_set.append(items[i-1])               # Add this item to the results set.
                c -= items[i-1].weight                      # Update the weight/capacity for the next iteration.
        return dp[-1][-1], result_set


class Item:
    def __init__(self, value, weight, name=None, units=1):
        self.value = value
        self.weight = weight
        self.name = name
        self.units = units

    def __repr__(self):
        return ((f"(Name: {self.name}, " if self.name else "(") +
                f"Value: {self.value}, Weight: {self.weight}" +
                (f", Units: {self.units})" if self.units > 1 else ")"))


args = [(130, [Item(65, 20), Item(35, 8), Item(245, 60),
               Item(195, 55), Item(65, 40), Item(99, 10),
               Item(275, 85), Item(155, 25), Item(120, 30),
               Item(75, 75), Item(320, 65), Item(40, 10),
               Item(200, 95), Item(100, 50), Item(220, 40),
               Item(150, 70)]),
        (5, [Item(6, 1), Item(10, 2), Item(12, 3)]),
        (50, [Item(6, 1), Item(10, 2), Item(12, 3)]),
        (1, [Item(10, 5), Item(40, 4), Item(30, 6), Item(60, 3)]),
        (10, [Item(10, 5), Item(40, 4), Item(30, 6), Item(60, 3)])]
fns = [knapsack_01_bf_via_itertools,
       knapsack_01_bf_via_combinatorics,
       knapsack_01_naive_via_rec,
       knapsack_01_dp_via_top_down,
       knapsack_01_dp_via_bottom_up]

for capacity, items in args:
    print(f"\nitems: {items}\ncapacity: {capacity}")
    for fn in fns:
        print(f"{fn.__name__}(items, capacity): {fn(copy.copy(items), capacity)}")
    print()

capacity = 260
items = [Item(65, 20), Item(35, 8), Item(245, 60), Item(195, 55),
         Item(65, 40), Item(99, 10), Item(275, 85), Item(155, 25),
         Item(120, 30), Item(75, 75), Item(320, 65), Item(40, 10),
         Item(200, 95), Item(100, 50), Item(220, 40), Item(15, 70),
         Item(65, 20), Item(35, 8), Item(245, 60), Item(195, 55),
         Item(65, 40), Item(99, 10), Item(275, 85), Item(155, 25),
         Item(120, 30), Item(75, 75), Item(320, 65), Item(40, 10),
         Item(200, 95), Item(100, 50), Item(99, 40), Item(150, 70)]
print(f"\nitems: {items}\ncapacity: {capacity}")
for fn in fns[2:]:  # Skipping Combinatorics approaches; they would not finish any time soon...
    t = time.time()
    print(f"{fn.__name__}(items, capacity),", end="")
    result = fn(items, capacity)
    print(f" took {time.time() - t} seconds: {result}")

