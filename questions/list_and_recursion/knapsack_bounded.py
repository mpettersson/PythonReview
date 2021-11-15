"""
    THE BOUNDED KNAPSACK PROBLEM

    Given a set of items that each have a value, a weight, and a number of units, determine the number of items/units to
    select as to maximize the total value, constrained by the given knapsack's capacity.

    NOTE: This variation of the problem is called the bounded knapsack problem because each item is bound by the number
          of units.

    Example:
                        # name             weight    value  units
                items = (("map",                9,     150,     1),
                         ("compass",           13,      35,     1),
                         ("water",            153,     200,     3),
                         ("sandwich",          50,      60,     2),
                         ("candy",             15,      60,     2),
                         ("canned food",       68,      45,     3),
                         ("banana",            27,      60,     3),
                         ("apple",             39,      40,     3),
                         ("cheese",            23,      30,     1),
                         ("beer",              52,      10,     3),
                         ("sunscreen",         11,      70,     1),
                         ("camera",            32,      30,     1),
                         ("t-shirt",           24,      15,     2),
                         ("pants",             48,      10,     2),
                         ("umbrella",          73,      40,     1),
                         ("waterproof pants",  42,      70,     1),
                         ("waterproof jacket", 43,      75,     1),
                         ("notes",             22,      80,     1),
                         ("sunglasses",         7,      20,     1),
                         ("towel",             18,      12,     2),
                         ("socks",              4,      50,     1),
                         ("book",              30,      10,     2))
                capacity = 400
        Input = items, capacity
        Output = 1010   # Or [socks, sunglasses, notes, waterproof jacket, sunscreen, cheese, 3 x banana, 2 x candy,
                        #     water, compass, map])
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible values for capacity (int, None, negative, etc.)?
#   - Does the full capacity need to be used (what should happen if can't use total capacity)?
#   - What should be returned (total, or list of items, what should happen if failure)?
#   - What are the possible sizes of the list (empty, max size)?
#   - What are the possible values in the list (int/float/None/negative)?
#   - What is the largest possible unit count?
#   - Any other unit requirements?
#   - Can the list have unique/duplicate values?
#   - Will the list be sorted?
#   - Can the list be modified?


# GENERAL APPROACH: Naive Split Then Solve With 0/1 Knapsack
#
# This 'naive' split simply takes items with more than one unit/instance and splits, or separates, each of the
# additional units/instances into a (duplicate) item with a unit/instance count of one.  Once the items have been
# normalized to all have a single unit/instance count, the problem can be solved using the 0/1 Knapsack approach.
#
# NOTE: This approach is acceptable if the number of units/instances are LOW.  However, if a LARGE number of units are
#       used, then a LARGE number of duplicate items will be created, thus, hindering performance.
#
# Consider the 'water' item from the example items list (above):
#                        ...
#                        ("water",            153, 200, 3),
#                        ...
# Using the naive split, this one item with a unit/instance count of 3 would become:
#                        ...
#                        ("water",            153, 200, 1),
#                        ("water",            153, 200, 1),
#                        ("water",            153, 200, 1),
#                        ...
# Or (since there all unit/instance counts would be 1) simply:
#                        ...
#                        ("water",            153, 200),
#                        ("water",            153, 200),
#                        ("water",            153, 200),
#                        ...
#
# Time Complexity: O(total_split_items * capacity), where total_split_items is the number of items after items with
#                  duplicate units/instances are split into separate items.
# Space Complexity: O(total_split_items * capacity), where total_split_items is the number of items after items with
#                   duplicate units/instances are split into separate items.


# APPROACH: Naive Split & 0/1 Knapsack Top Down
# SEE: knapsack_01_dp_via_top_down() (below) for more information and time/space complexity.
def bounded_knapsack_via_naive_split_and_knapsack_01_top_down_dp(items, capacity):
    items = sum(([(name, wt, val)]*n for name, wt, val, n in items), [])
    return knapsack_01_dp_via_top_down([Item(e[2], e[1], e[0]) for e in items], capacity)


# APPROACH: Naive Split & 0/1 Knapsack Bottom Up
# SEE: knapsack_01_dp_via_bottom_up() (below) for more information and time/space complexity.
def bounded_knapsack_via_naive_split_and_knapsack_01_bottom_up_dp(items, capacity):
    items = sum(([(name, wt, val)]*n for name, wt, val, n in items), [])
    return knapsack_01_dp_via_bottom_up([Item(e[2], e[1], e[0]) for e in items], capacity)


# GENERAL APPROACH: (Optimal) Log2/Power of Two Split Then Solve With 0/1 Knapsack
#
# This power of two split approach splits an item with more than one unit/instance count into ceil(log2(num unit/inst))
# separate items, each with a power of two up to floor(log2(num unit/inst)), and one with the remaining units.
# This allows for the 0/1 Knapsack approach to pick any number in the range via a combination of the (in this example
# 9) separated items.
#
# Consider IF the 'water' item from the example items list had a unit count of 300:
#                        ...
#                        ("water",            153, 200, 300),
#                        ...
# Then using the naive split approach (above) would result in 300 (duplicate) water items, this is ineffective:
#                        ...
#                        ("water",            153, 200),      # (1 of 300 water items)
#                        ("water",            153, 200),      # (2 of 300 water items)
#                        ("water",            153, 200),      # (3 of 300 water items)
#                        ...
#                        ("water",            153, 200),      # (298 of 300 water items)
#                        ("water",            153, 200),      # (299 of 300 water items)
#                        ("water",            153, 200),      # (300 of 300 water items)
#                        ...
# Instead, by using Log2/power of two splits, there would only be 9 water items (each with different unit counts):
#                        ...
#                        ("water",            153, 200, 1),   # (1 of 300 water items)
#                        ("water",            153, 200, 2),   # (1 of 300 water items)
#                        ("water",            153, 200, 4),   # (1 of 300 water items)
#                        ("water",            153, 200, 8),   # (1 of 300 water items)
#                        ("water",            153, 200, 16),  # (1 of 300 water items)
#                        ("water",            153, 200, 32),  # (1 of 300 water items)
#                        ("water",            153, 200, 64),  # (1 of 300 water items)
#                        ("water",            153, 200, 128), # (1 of 300 water items)
#                        ("water",            153, 200, 45),  # (1 of 300 water items)
#                        ...
#
# Time Complexity: O(n * ceil(log2(max_unit_count)) * capacity), where n is the number of items, and max_unit_count is
#                  the largest unit value of all items.
# Space Complexity: O(n * ceil(log2(max_unit_count)) * capacity), where n is the number of items, and max_unit_count is
#                   the largest unit value of all items.


# APPROACH: Log2/Power of Two Split & 0/1 Knapsack Top Down:
# SEE: knapsack_01_dp_via_top_down() (below) for more information and time/space complexity.
def bounded_knapsack_via_log2_split_and_knapsack_01_top_down_dp(items, capacity):
    log_two_split_items = []
    for name, weight, value, units in items:
        u = units
        n = 1
        while u:
            if n < u:
                log_two_split_items.append(Item(value * n, weight * n, name, n))  # NOTE: Don't forget the '* n'!
                u -= n
                n <<= 1
            else:
                log_two_split_items.append(Item(value * u, weight * u, name, u))  # NOTE: Don't forget the '* u'!
                u = 0
    return knapsack_01_dp_via_top_down(log_two_split_items, capacity)


# APPROACH: Log2/Power of Two Split & 0/1 Knapsack Bottom Up
# SEE: knapsack_01_dp_via_bottom_up() (below) for more information and time/space complexity.
def bounded_knapsack_via_log2_split_and_knapsack_01_bottom_up_dp(items, capacity):
    log_two_split_items = []
    for name, weight, value, units in items:
        u = units
        n = 1
        while u > 0:
            if n < u:
                log_two_split_items.append(Item(value * n, weight * n, name, n))    # NOTE: Don't forget the '* n'!
                u -= n
                n <<= 1
            else:
                log_two_split_items.append(Item(value * u, weight * u, name, u))    # NOTE: Don't forget the '* u'!
                u = 0
    return knapsack_01_dp_via_bottom_up(log_two_split_items, capacity)


# NOTE: The following 0/1 Knapsack approaches will not be included here (SEE: knapsack_01.py for full description/code).
#   - 0/1 Knapsack Approach: Brute Force Via Power Set/Itertools Combinations
#   - 0/1 Knapsack Approach: Brute Force Via Combinatorics/Iterative
#   - 0/1 Knapsack Approach: Naive Via Recursion
#
# REFERENCES:
#   - https://rosettacode.org/wiki/Knapsack_problem/Bounded
#   - https://cs.stackexchange.com/questions/86531/transforming-a-bounded-knapsack-to-0-1-knapsack
#
#
# (0/1 KNAPSACK) APPROACH: Memoization/Top Down Dynamic Programming
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


# (0/1 KNAPSACK) APPROACH: Tabulation/Bottom Up Dynamic Programming
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
# To build the list of items, start at the b[-1][-1], then do:
#   - If the current cell is True, add the row's item to the output list, then update the col as col-rows.weight.
#   - If the current cell is False, do nothing.
#   - Decrement the row (move one row up).
#
# Once at row 0, return the values. For the example above, the two cells (that cause the item to be append) are:
#   b['D'][10] and b['B'][7] (the full path is: b['D'][10]->b['D'][7]-> b['C'][7]->b['B'][7]->b['B'][3]->b['A'][7]).
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


capacity = 400
items = (("map", 9, 150, 1), ("compass", 13, 35, 1), ("water", 153, 200, 3), ("sandwich", 50, 60, 2),
         ("candy", 15, 60, 2), ("canned food", 68, 45, 3), ("banana", 27, 60, 3), ("apple", 39, 40, 3),
         ("cheese", 23, 30, 1), ("beer", 52, 10, 3), ("sunscreen", 11, 70, 1), ("camera", 32, 30, 1),
         ("t-shirt", 24, 15, 2), ("pants", 48, 10, 2), ("umbrella", 73, 40, 1), ("waterproof pants", 42, 70, 1),
         ("waterproof jacket", 43, 75, 1), ("notes", 22, 80, 1), ("sunglasses", 7, 20, 1), ("towel", 18, 12, 2),
         ("socks", 4, 50, 1), ("book", 30, 10, 2))   # Where each tuple is: (item, weight, value, num_units).
fns = [bounded_knapsack_via_naive_split_and_knapsack_01_top_down_dp,
       bounded_knapsack_via_naive_split_and_knapsack_01_bottom_up_dp,
       bounded_knapsack_via_log2_split_and_knapsack_01_top_down_dp,
       bounded_knapsack_via_log2_split_and_knapsack_01_bottom_up_dp]

print(f"\nitems: {items}\ncapacity: {capacity}")
for fn in fns:
    print(f"{fn.__name__}(items, capacity): {fn(items, capacity)}")
print()


