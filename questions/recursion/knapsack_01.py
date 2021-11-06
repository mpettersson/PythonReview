"""
    THE 01 KNAPSACK PROBLEM

    "Given a set of items that each have a value and a weight, determine which of those items to select to as to maximize
     the total value, constrained by the knapsack's capacity."

    NOTE: This variation of the problem is called the 01 knapsack problem because each item can be 'picked' or not
          'picked', and because fractional items are not allowed.

    Write a program for the knapsack problem that selects a subset of items that has a maximum value and satisfies the
    weight constraint.  All items have integer weights and values.  Return the value of the subset.

    Example:
        Input = [(65, 20), (35, 8), (245, 60), (195, 55), (65, 40), (99, 10), (275, 85), (155, 25), (120, 30), (75, 75),
                 (320, 65), (40, 10), (200, 95), (100, 50), (220, 40), (150, 70)], 130  # (price, weight), total_weight
        Output = 695    # Max value set: [(155, 25), (320, 65), (220, 40)]
"""
import itertools
import time


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
# Space Complexity: O(m), where m is the size of the max value set (could be O(1) if result_set isn't maintained).
def knapsack_01_bf_via_itertools(items, capacity):
    if items is not None and capacity is not None and capacity > 0:
        result_set = None
        result_tot = -float('inf')
        for r in range(len(items)):
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
# The recurrence relation for this approach is:
#       V[i][w]  =  max(V[i-1][w], V[i-1][w-i.w]+i.v)       if i.w < w
#                   V[i-1][w]                               otherwise
#   Where:
#       V is the Max Value/Price memoization table (0..i rows, 0..w columns, initialized to -1, start/end at [i][w])
#       i is the size of the items list; each item has a weight i.w and value i.v.
#       w is the weight capacity.
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
#      val:10, cap:5        val:0, cap:10     val:10, cap:5           val:0, cap:10
#          /    \               /   \             /   \                   /    \
#        ...    ...           ...  ...          ...   ...               ...    ...
#
# Time Complexity: O(2**n), where n is the number of elements in items list.
# Space Complexity:
def knapsack_01_naive_via_rec(l, capacity):

    def _rec(l, i, rem_cap):
        if i < 0:
            return 0, []
        excluded = _rec(l, i-1, rem_cap)
        if rem_cap >= l[i].weight:
            included = _rec(l, i-1, rem_cap - l[i].weight)
            included = (included[0] + l[i].value, included[1] + [l[i]])
            return max(included, excluded, key=lambda x: x[0])
        return excluded

    if l and capacity > 0:
        return _rec(l, len(l)-1, capacity)

# NOTE: If you only want the value total, then you can exclude the extra boolean matrix logic:
# def knapsack_01_naive_via_rec(l, capacity):
#     def _rec(l, i, rem_cap):
#         if i < 0:
#             return 0
#         excluded = _rec(l, i-1, rem_cap)
#         included = 0 if rem_cap < l[i].weight else (l[i].value + _rec(l, i-1, rem_cap - l[i].weight))
#         return max(included, excluded)
#     if l and capacity > 0:
#         return _rec(l, len(l)-1, capacity)


# APPROACH: Memoization/Top Down Dynamic Programming
#
# This approach optimizes the naive recursive approach above by adding a cache, or memoization table, (called dp below)
# to prevent duplicated computations.
#
# If given the following four items:
#     Items:     A   B   C   D
#     Values:   10  40  30  60
#     Weights:   5   4   6   3
#
# Then the completed top down dynamic programming cache, or memoization, table:
#              0      1      2      3      4     5      6      7      8      9      10    (Capacity)
#     A  [[    0,     0,  None,     0,     0, None,    10,    10,  None,  None,     10],
#     B   [ None,     0,  None,  None,    40, None,  None,    40,  None,  None,     50],
#     C   [ None,  None,  None,  None,  None, None,  None,    40,  None,  None,     70],
#     D   [ None,  None,  None,  None,  None, None,  None,  None,  None,  None,    100]]
#
# The completed top down dynamic programming boolean table (for tacking the included items):
#              0      1      2      3      4     5      6      7      8      9      10    (Capacity)
#     A  [[False, False, False, False, False, False,  True,  True, False, False,  True],
#     B   [False, False, False, False,  True, False, False,  True, False, False,  True],
#     C   [False, False, False, False, False, False, False, False, False, False,  True],
#     D   [False, False, False, False, False, False, False, False, False, False,  True]]
#
# NOTE: This approach ASSUMES INTEGER VALUES for prices and weights; modify with math.ceil() if REAL NUMS are wanted!
#
# Time Complexity: O(n * capacity), where n is the number of the items list.
# Time Complexity: O(n * capacity), where n is the number of the items list.
def knapsack_01_dp_via_top_down(items, capacity):

    def _rec(l, i, cap, dp, b):
        if i < 0:
            return 0
        if dp[i][cap] is None:
            excluded = _rec(l, i-1, cap, dp, b)
            included = 0 if cap < l[i].weight else (l[i].value + _rec(l, i-1, cap-l[i].weight, dp, b))
            if excluded < included:
                dp[i][cap] = included
                b[i][cap] = True
            else:
                dp[i][cap] = excluded
        return dp[i][cap]

    if items is not None and capacity is not None:
        n = len(items)
        dp = [[None] * (capacity + 1) for _ in range(len(items))]   # dp[-1][-1] has max value when done
        b = [[False] * (capacity + 1) for _ in range(len(items))]
        result_tot = _rec(items, n-1, capacity, dp, b)
        result_set = []                                             # The next few lines builds the result set from the
        c = capacity                                                # boolean mat, see the example above for more info.
        for r in range(n-1, -1, -1):                                # NOTE: The reverse order (to start at b[-1][-1])!!
            if b[r][c]:
                result_set.append(items[r])
                c -= items[r].weight
        return result_tot, result_set

# NOTE: If you only want the value total, then you can exclude the extra boolean matrix logic:
# def knapsack_01_dp_via_top_down(items, capacity):
#     def _rec(l, i, cap, dp):
#         if i < 0:
#             return 0
#         if dp[i][cap] is None:
#             excluded = _rec(l, i-1, cap, dp)
#             included = 0 if cap < l[i].weight else (l[i].value + _rec(l, i-1, cap-l[i].weight, dp))
#             dp[i][cap] = max(included, excluded)
#         return dp[i][cap]
#     if items is not None and capacity is not None:
#         n = len(items)
#         dp = [[None] * (capacity + 1) for _ in range(len(items))]   # dp[-1][-1] has max value when done
#         return _rec(items, n-1, capacity, dp)


# APPROACH: Tabulation/Bottom Up Dynamic Programming
#
# This approach is very similar to the top down dynamic programming (it uses a cache, or memoization table, to reuse
# computations), however, it iteratively works from the bottom up filling the whole cache, or memoization, table.
# (Where top down is recursive and only fills in, or computes, the directly required cells.)
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
# NOTE: This approach ASSUMES INTEGER VALUES for prices and weights; modify with math.ceil() if REAL NUMS are wanted!
#
# Time Complexity: O(n * capacity), where n is the number of the items list.
# Time Complexity: O(n * capacity), where n is the number of the items list.
#
# NOTE: This may appear to be a POLYNOMIAL time time for a np-complete (01 knapsack) problem.  HOWEVER, the metrics are
#       different; n is the size of a list and capacity is just a number--they must be 'the same'.  Therefore, the
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
            for w in range(capacity+1):                     # w = a discrete capacity from 0 to total capacity
                if items[i-1].weight <= w and dp[i-1][w] < items[i-1].value + dp[i-1][w-items[i-1].weight]:
                    dp[i][w] = items[i-1].value + dp[i-1][w-items[i-1].weight]
                    b[i][w] = True
                else:
                    dp[i][w] = dp[i-1][w]
        result_set = []                                     # The next few lines builds the result set from the
        c = capacity                                        # boolean matrix, see the example above for more info.
        for i in range(n, 0, -1):                           # NOTE: The reverse order (to start at b[-1][-1])!!
            if b[i][c]:                                     # If the
                result_set.append(items[i-1])               # Add this item to the results set.
                c -= items[i-1].weight                      # Update the weight/capacity for the next iteration.
        return dp[-1][-1], result_set


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"(Value: {self.value}, Weight: {self.weight})"


args = [(130, [Item(65, 20), Item(35, 8), Item(245, 60), Item(195, 55), Item(65, 40), Item(99, 10), Item(275, 85),
         Item(155, 25), Item(120, 30), Item(75, 75), Item(320, 65), Item(40, 10), Item(200, 95), Item(100, 50),
         Item(220, 40), Item(150, 70)]),
        (10, [Item(10, 5), Item(40, 4), Item(30, 6), Item(60, 3)])]
fns = [knapsack_01_bf_via_itertools,
       knapsack_01_bf_via_combinatorics,
       knapsack_01_naive_via_rec,
       knapsack_01_dp_via_top_down,
       knapsack_01_dp_via_bottom_up]

for capacity, items in args:
    print(f"\nitems: {items}\ncapacity: {capacity}")
    for fn in fns:
        print(f"{fn.__name__}(items, capacity): {fn(items, capacity)}")
    print()

capacity = 390
items = [Item(65, 20), Item(35, 8), Item(245, 60), Item(195, 55), Item(65, 40), Item(99, 10), Item(275, 85),
         Item(155, 25), Item(120, 30), Item(75, 75), Item(320, 65), Item(40, 10), Item(200, 95), Item(100, 50),
         Item(220, 40), Item(150, 70), Item(65, 20), Item(35, 8), Item(245, 60), Item(195, 55), Item(65, 40),
         Item(99, 10), Item(275, 85), Item(155, 25), Item(120, 30), Item(75, 75), Item(320, 65), Item(40, 10),
         Item(200, 95), Item(100, 50), Item(220, 40), Item(150, 70), Item(65, 20), Item(35, 8), Item(245, 60),
         Item(195, 55), Item(65, 40), Item(99, 10), Item(275, 85), Item(155, 25), Item(120, 30), Item(75, 75),
         Item(320, 65), Item(40, 10), Item(200, 95), Item(100, 50), Item(220, 40), Item(150, 70)]
print(f"\ncapacity: {capacity}\nitems: {items}")
for fn in reversed(fns):
    t = time.time()
    print(f"{fn.__name__}(items, capacity),", end="")
    result = fn(items, capacity)
    print(f" took {time.time() - t} seconds: {result}")


