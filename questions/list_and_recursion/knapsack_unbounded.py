"""
    THE UNBOUNDED KNAPSACK PROBLEM

    Given a set of items that each have a value, a weight, and an unlimited (unbounded) number of units, determine the
    set of items to select as to maximize the total value, constrained by the given knapsack's capacity.

    NOTE: This is an NP-hard combinatorial optimization problem.

    Example:
        Input = [(65, 20), (35, 8), (245, 60), (195, 55), (65, 40), (99, 10), (275, 85), (155, 25), (120, 30), (75, 75),
                 (320, 65), (40, 10), (200, 95), (100, 50), (220, 40), (150, 70)], 130  # (price, weight), total_weight
        Output = 695    # Max value set: [(155, 25), (320, 65), (220, 40)]
"""


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


# APPROACH: Brute Force Via Recursion
#
# Starting at the first item, this approach computes then returns the best option; either not using the item (which
# would result in an updated index) or using the item (which would result in another recursion loop with the SAME
# index) until either the end of the list, or there is not more capacity.
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
#  (include A)/         (exclude A)\                / (include B)        \ (exclude B)
#            /                      \              /                      \
#      val: 20, cap:0       val:0, cap:10     val:40, cap:6           val:0, cap:10
#          /    \               /   \             /   \                   /    \
#        ...    ...           ...  ...          ...   ...               ...    ...
#
# NOTE: The index on the include (left) side of the tree (above) DOES NOT increment!  This is the KEY difference
#       between the unbounded and 1/0 knapsack problems!!!
#
# Time Complexity: O(2**(n+c)), where n is the number of elements in items list and c is the capacity.
# Space Complexity: O(n+c), where n is the number of elements in items list and c is the capacity.
#
# NOTE: How the time complexity, O(2**(n+c)), is found:
#       1. Since an unbound knapsack allows item reuse, we can say the asymptotic time is O(2**(n+x)), where x is the
#          number of reused items.
#       2. Furthermore, the sum of the reused items (x) can not be more than the capacity (c).
#       3. In the worst case, the smallest weight item (s) would be equal to 1.
#       4. Thus c/s is c/1, or c.
#       5. Since x is less than or equal to c (see number 2), we O(2**(n+x)) <= O(2**(n+c)).
def knapsack_unbounded_bf_via_rec(items, capacity):

    def _rec(items, i, capacity):
        if i < 0 or capacity <= 0:
            return 0, []
        excluded = _rec(items, i-1, capacity)
        if capacity >= items[i].weight:
            included = _rec(items, i, capacity - items[i].weight)
            included = (included[0] + items[i].value, included[1] + [items[i]])
            return max(included, excluded, key=lambda x: x[0])
        return excluded

    if items and capacity > 0:
        return _rec(items, len(items)-1, capacity)
# NOTE: If you only want the value total, then you can exclude the extra boolean matrix logic:
# def knapsack_unbounded_bf_via_rec(items, capacity):
#     def _rec(items, i, capacity):
#         if i < 0 or capacity <= 0:
#             return 0
#         included = 0 if capacity < items[i].weight else items[i].value + _rec(items, i, capacity - items[i].weight)
#         excluded = _rec(items, i - 1, capacity)
#         return max(included, excluded)
#     if items and capacity > 0:
#         return _rec(items, len(items)-1, capacity)


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
#        [[None,   None,  None,  None,  None, None,  None,  None,  None,  None,   None],
#     A   [    0,     0,     0,     0,     0,   10,    10,    10,  None,  None,     20],
#     B   [    0,     0,     0,     0,    40, None,    40,    40,  None,  None,     80],
#     C   [ None,     0,  None,  None,    40, None,  None,    40,  None,  None,     80],
#     D   [ None,     0,  None,  None,    60, None,  None,   120,  None,  None,    180]]
#
# The completed top down dynamic programming boolean table (for tacking the included items):
#              0      1      2      3      4     5      6      7      8      9      10    (Capacity)
#        [[False, False, False, False, False, False, False, False, False, False, False],
#     A   [False, False, False, False, False,  True,  True,  True, False, False,  True],
#     B   [False, False, False, False,  True, False,  True,  True, False, False,  True],
#     C   [False, False, False, False, False, False, False, False, False, False, False],
#     D   [False, False, False, False,  True, False, False,  True, False, False,  True]]
#
# To build the list of items, start at the b[-1][-1], and while row > 0 and col > 0, do:
#   - If the current cell is True, add the row's item to the output list, then update the col as col-rows.weight.
#   - If the current cell is False, update/decrement the row.
#
# NOTE: This approach ASSUMES INTEGER VALUES for prices and weights; modify with math.ceil() if REAL NUMS are wanted!
#
# Time Complexity: O(n * capacity), where n is the number of the items list.
# Time Complexity: O(n * capacity), where n is the number of the items list.
def knapsack_unbounded_dp_via_top_down(items, capacity):

    def _rec(items, i, cap, dp, b):
        if i == 0:
            return 0
        if dp[i][cap] is None:
            excluded = _rec(items, i - 1, cap, dp, b)
            included = (0 if cap < items[i-1].weight else
                        (items[i-1].value + _rec(items, i, cap - items[i-1].weight, dp, b)))
            if excluded < included:
                dp[i][cap] = included
                b[i][cap] = True
            else:
                dp[i][cap] = excluded
        return dp[i][cap]

    if items is not None and capacity is not None:
        n = len(items)
        dp = [[None] * (capacity + 1) for _ in range(n+1)]   # dp[-1][-1] has max value when done
        b = [[False] * (capacity + 1) for _ in range(n+1)]
        result_tot = _rec(items, n, capacity, dp, b)
        result_set = []                                      # The next few lines builds the result set from the
        c = capacity                                         # boolean mat, see the example above for more info.
        r = n                                                # NOTE: The reverse order (to start at b[-1][-1])!!
        while 0 <= c and 0 <= r:
            if b[r][c]:
                result_set.append(items[r-1])
                c -= items[r-1].weight
            else:
                r -= 1
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
#     A   [    0,     0,     0,     0,     0,   10,    10,    10,    10,    10,     20],
#     B   [    0,     0,     0,     0,    40,   40,    40,    40,    80,    80,     80],
#     C   [    0,     0,     0,     0,    40,   40,    40,    40,    80,    80,     80],
#     D   [    0,     0,     0,    60,    60,   60,   120,   120,   120,   180,    180]]
#
# REMINDER: Start at dp[A][cap=0], working right, where dp[row][col] = max(dp[row-1][col], dp[row-1][col-A.weight].
#
# The completed bottom up dynamic programming boolean table (for tacking the included items):
#              0      1      2      3      4     5      6      7      8      9      10    (Capacity)
#        [[False, False, False, False, False, False, False, False, False, False, False],  PADDING (for simplified code)
#     A   [False, False, False, False, False,  True,  True,  True,  True,  True,  True],
#     B   [False, False, False, False,  True,  True,  True,  True,  True,  True,  True],
#     C   [False, False, False, False, False, False, False, False, False, False, False],
#     D   [False, False, False,  True,  True,  True,  True,  True,  True,  True,  True]]
#
# To build the list of items, start at the b[-1][-1], and while row > 0 and col > 0, do:
#   - If the current cell is True, add the row's item to the output list, then update the col as col-rows.weight.
#   - If the current cell is False, update/decrement the row.
#
# For the example above, the path taken is:
#   b['D'][10] -> b['D'][7] -> b['D'][4] ->b ['D'][1] ->b ['C'][1] -> b['B'][1] -> b['A'][1] -> b[0][1].
# And the cells that correspond to the picked items are:
#   b['D'][10], b['D'][7], b['D'][4]
#
# NOTE: This approach ASSUMES INTEGER VALUES for prices and weights; modify with math.ceil() if REAL NUMS are wanted!
#
# Time Complexity: O(n * capacity), where n is the number of the items list.
# Time Complexity: O(n * capacity), where n is the number of the items list.
#
# NOTE: This may appear to be a POLYNOMIAL time time for a np-complete (01 knapsack) problem.  HOWEVER, the metrics are
#       different; n is the size of a list and capacity is just a number--they must be 'the same'.  Therefore, the
#       capacity needs to be encoded, by say, the number of bits required to represent the capacity:
#               capacity_size = log(b, capacity)  ==>  capacity = b**capacity_size
#       So O(n * capacity) is really O(n * b**capacity_size), or PSEUDO-POLYNOMIAL, or WEAKLY-NP-COMPLETE.
def knapsack_unbounded_dp_via_bottom_up(items, capacity):
    if items is not None and capacity is not None:
        n = len(items)                                      # NOTE: Be VERY careful with the counters!
        dp = [[0] * (capacity+1) for _ in range(n+1)]       # dp[-1][-1] has max value when done.
        b = [[False] * (capacity+1) for _ in range(n+1)]    # backtrack/used/prev items matrix.
        for i in range(1, n+1):                             # r=0 is a padding row, i=1 to n are the list items.
            for cap in range(capacity+1):                   # c=discrete capacity from 0 to total capacity (inclusive).
                if items[i-1].weight <= cap and dp[i-1][cap] < items[i-1].value + dp[i][cap-items[i-1].weight]:
                    dp[i][cap] = items[i-1].value + dp[i][cap-items[i-1].weight]
                    b[i][cap] = True                        # INCLUDE the corresponding item (row - 1).
                else:
                    dp[i][cap] = dp[i-1][cap]
        result_set = []                                     # The next few lines builds the result set from the
        c = capacity                                        # boolean matrix, see the example above for more info.
        r = n                                               # NOTE: The reverse order (to start at b[-1][-1])!!
        while 0 < c and 0 < r:
            if b[r][c]:                                     # If included:
                result_set.append(items[r-1])                   # Add the corresponding item.
                c -= items[r-1].weight                          # Update column/capacity.
            else:                                           # Else:
                r -= 1                                          # Try the next row/item.
        return dp[-1][-1], result_set                       # Return the value and set.


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


args = [(130, [Item(65, 20), Item(35, 8), Item(245, 60), Item(195, 55), Item(65, 40), Item(99, 10), Item(275, 85),
               Item(155, 25), Item(120, 30), Item(75, 75), Item(320, 65), Item(40, 10), Item(200, 95), Item(100, 50),
               Item(220, 40), Item(150, 70)]),
        (10, [Item(10, 5), Item(40, 4), Item(30, 6), Item(60, 3)])]
fns = [knapsack_unbounded_bf_via_rec,
       knapsack_unbounded_dp_via_top_down,
       knapsack_unbounded_dp_via_bottom_up]

for capacity, items in args:
    print(f"\nitems: {items}\ncapacity: {capacity}")
    for fn in fns:
        print(f"{fn.__name__}(items, capacity): {fn(items, capacity)}")
    print()


