"""
    THE 01 KNAPSACK PROBLEM WITH REAL NUMBERS

    Given a set of items that each have a real number values and weights, determine which of those items to select as to
    maximize the total value, constrained by the given knapsack's capacity.

    Example:
        items = [('beef',           3.8,        36.01),
                 ('pork',           5.4,        43.01),
                 ('ham',            3.6,        90.01),
                 ('greaves',        2.4,        45.01),
                 ('flitch',         4.0,        30.01),
                 ('brawn',          2.5,        56.01),
                 ('welt',           3.7,        67.01),
                 ('salami',         3.0,        95.01),
                 ('sausage',        5.9,        98.01)]
                  # name         weight         value
        capacity = 15
        Input = items, capacity
        Output = # SEE BELOW
"""
from collections import defaultdict
import copy
import time
from itertools import combinations
from math import ceil
from functools import lru_cache


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


"""
    GENERAL REAL NUMBER KNAPSACK APPROACHES AND RESULTS
    
    The following approaches are implemented below:
        - Plain Combinatorics (no changes were needed to handle real number weights). 
        - Plain/Cached Recursion (no changes were needed to handle real number weights)
        - Using a list of (default) dictionaries as the memoization table for top down dynamic programming.
        - Wrapping items weight in the ceiling function (i.e., math.ceil(items[i].weight)).
    
    NOTE: Out of the approaches, the only accurate results were found with the plain combinatorics.  Furthermore, the 
          possibility exists for the plain/cached recursion and the list of dictionaries top down dp approaches to 
          calculate an accurate result, however, higher precision is required.  
    
    The following is a high level summary of the results of the different approaches.

        knapsack_01_with_real_numbers_bf_via_itertools() and
        knapsack_01_with_real_numbers_bf_via_combinatorics()
            Total Value:    339.04,
            Used Weight:    15,
            Picked Items:  [(Name: brawn,   Value: 56.01,   Weight: 2.5),
                            (Name: ham,     Value: 90.01,   Weight: 3.6),
                            (Name: salami,  Value: 95.01,   Weight: 3.0),
                            (Name: sausage, Value: 98.01,   Weight: 5.9)]

        knapsack_01_with_real_numbers_naive_via_rec(),
        knapsack_01_with_real_numbers_naive_via_rec_with_lru_cache(),
        knapsack_01_with_real_numbers_dp_via_top_down_and_dicts():
            Total Value:    328.04,
            Used Weight:     14.90,
            Picked Items:  [(Name: greaves, Value: 45.01,   Weight: 2.4),
                            (Name: ham,     Value: 90.01,   Weight: 3.6),
                            (Name: salami,  Value: 95.01,   Weight: 3.0),
                            (Name: sausage, Value: 98.01,   Weight: 5.9)]

        knapsack_01_with_real_numbers_naive_via_rec_and_ceil(),
            Total Value:    308.04,
            Total Weight: {'Rounded': 14, 'Actual': 12.8}
            Picked Items:  [(Name: brawn,   Value: 56.01,   Weight: 2.5),
                            (Name: ham,     Value: 90.01,   Weight: 3.6),
                            (Name: salami,  Value: 95.01,   Weight: 3.0),
                            (Name: welt,    Value: 67.01,   Weight: 3.7)]

        knapsack_01_with_real_numbers_dp_via_top_down(),
        knapsack_01_with_real_numbers_dp_via_bottom_up_and_ceil()
            Total Value:    308.04,
            Total Weight: {'Rounded': 14, 'Actual': 12.799999999999999}
            Picked Items:  [(Name: brawn,   Value: 56.01,   Weight: 2.5),
                            (Name: ham,     Value: 90.01,   Weight: 3.6),
                            (Name: salami,  Value: 95.01,   Weight: 3.0),
                            (Name: welt,    Value: 67.01,   Weight: 3.7)]
"""


# APPROACH: Brute Force Via Power Set/Itertools Combinations
# SEE: knapsack_01.py for the 01 knapsack approaches, time and space complexities, and descriptions.
def knapsack_01_with_real_numbers_bf_via_itertools(items, capacity):
    if items is not None and capacity is not None and capacity > 0:
        result_set = None
        result_tot = -float('inf')
        result_wt = 0
        for r in range(len(items)):
            for s in combinations(items, r):
                if sum(x.weight for x in s) <= capacity:
                    price = sum(x.value for x in s)
                    if price > result_tot:
                        result_wt = sum(x.weight for x in s)
                        result_tot = price
                        result_set = set(s)
        return result_tot, result_wt, result_set


# APPROACH: Brute Force Via Combinatorics/Iterative
# SEE: knapsack_01.py for the 01 knapsack approaches, time and space complexities, and descriptions.
def knapsack_01_with_real_numbers_bf_via_combinatorics(items, capacity):

    def _gen_reversed_bits(n):
        while True:
            yield n & 1
            n >>= 1

    if items is not None and capacity is not None and capacity > 0:
        result_set = None
        result_tot = -float('inf')
        result_wt = 0
        for i in range(2**len(items)):
            g = _gen_reversed_bits(i)
            s = {e for e, b in zip(items, g) if b}
            if sum(x.weight for x in s) <= capacity:
                price = sum(x.value for x in s)
                if price > result_tot:
                    result_wt = sum(x.weight for x in s)
                    result_tot = price
                    result_set = s
        return result_tot, result_wt, result_set


# APPROACH: Naive Via Recursion
# SEE: knapsack_01.py for the 01 knapsack approaches, time and space complexities, and descriptions.
def knapsack_01_with_real_numbers_naive_via_rec(items, capacity):

    def _rec(items, i, capacity):
        if i < 0 or capacity <= 0:
            return 0, 0, []
        excluded = _rec(items, i-1, capacity)
        if capacity >= items[i].weight:
            included = _rec(items, i-1, capacity - items[i].weight)
            included = (included[0] + items[i].value, included[1] + items[i].weight, included[2] + [items[i]])
            return max(excluded, included, key=lambda x: x[0])
        return excluded

    if items and capacity > 0:
        return _rec(items, len(items)-1, capacity)


# APPROACH: Via Recursion With functools' lru_cache
# SEE: knapsack_01.py for the 01 knapsack approaches, time and space complexities, and descriptions.
def knapsack_01_with_real_numbers_naive_via_rec_with_lru_cache(items, capacity):

    @lru_cache(None)
    def _rec(i, capacity):
        if i < 0 or capacity <= 0:
            return 0, 0, []
        excluded = _rec(i-1, capacity)
        if capacity >= items[i].weight:
            included = _rec(i-1, capacity - items[i].weight)
            included = (included[0] + items[i].value, included[1] + items[i].weight, included[2] + [items[i]])
            return max(excluded, included, key=lambda x: x[0])
        return excluded

    if items and capacity > 0:
        return _rec(len(items)-1, capacity)


# APPROACH: Memoization/Top Down Dynamic Programming And A List Of Default Dictionaries
# SEE: knapsack_01.py for the 01 knapsack approaches, time and space complexities, and descriptions.
def knapsack_01_with_real_numbers_dp_via_top_down_and_dicts(items, capacity):

    def _rec(items, i, cap, dp, b):
        if i == 0:
            return 0
        if dp[i][cap] is None:
            excluded = _rec(items, i-1, cap, dp, b)
            included = 0 if cap < items[i-1].weight else (items[i-1].value +
                                                          _rec(items, i-1, cap - items[i-1].weight, dp, b))
            if excluded < included:
                dp[i][cap] = included
                b[i][cap] = True
            else:
                dp[i][cap] = excluded
        return dp[i][cap]

    if items is not None and capacity is not None:
        n = len(items)
        dp = [defaultdict(lambda: None) for _ in range(n+1)]      # dp[-1][-1] has max value when done
        b = [defaultdict(bool) for _ in range(n+1)]
        result_tot = _rec(items, n, capacity, dp, b)
        result_wt = 0
        result_set = []                                         # The next few lines builds the result set from the
        c = capacity                                            # boolean mat, see the example above for more info.
        for r in range(n, 0, -1):                               # NOTE: The reverse order (to start at b[-1][-1])!!
            if b[r][c]:
                result_set.append(items[r-1])
                c -= items[r-1].weight
                result_wt += items[r-1].weight
        return result_tot, result_wt, result_set


# APPROACH: Naive Via Recursion And The Ceiling Function
# SEE: knapsack_01.py for the 01 knapsack approaches, time and space complexities, and descriptions.
def knapsack_01_with_real_numbers_naive_via_rec_and_ceil(items, capacity):

    def _rec(items, i, capacity):
        if i < 0 or capacity <= 0:
            return 0, 0, 0, []
        excluded = _rec(items, i-1, capacity)
        if capacity >= items[i].weight:
            included = _rec(items, i-1, capacity - ceil(items[i].weight))
            included = (included[0] + items[i].value,
                        included[1] + ceil(items[i].weight),
                        included[2] + items[i].weight,
                        included[3] + [items[i]])
            return max(excluded, included, key=lambda x: x[0])
        return excluded

    if items and capacity > 0:
        result = _rec(items, len(items)-1, capacity)
        return result[0], {'Rounded': result[1], 'Actual': result[2]}, result[3]


# APPROACH: Memoization/Top Down Dynamic Programming And The Ceiling Function
# SEE: knapsack_01.py for the 01 knapsack approaches, time and space complexities, and descriptions.
def knapsack_01_with_real_numbers_dp_via_top_down_and_ceil(items, capacity):

    def _rec(items, i, cap, dp, b):
        if i == 0:
            return 0
        if dp[i][cap] is None:
            excluded = _rec(items, i-1, cap, dp, b)
            included = (0 if cap < ceil(items[i-1].weight) else
                        (items[i-1].value + _rec(items, i-1, cap-ceil(items[i-1].weight), dp, b)))
            if excluded < included:
                dp[i][cap] = included
                b[i][cap] = True
            else:
                dp[i][cap] = excluded
        return dp[i][cap]

    if items is not None and capacity is not None:
        n = len(items)
        dp = [[None] * (capacity + 1) for _ in range(n+1)]      # dp[-1][-1] has max value when done
        b = [[False] * (capacity + 1) for _ in range(n+1)]
        result_tot = _rec(items, n, capacity, dp, b)
        rounded_result_wt = 0
        actual_result_wt = 0
        result_set = []                                         # The next few lines builds the result set from the
        c = capacity                                            # boolean mat, see the example above for more info.
        for r in range(n, 0, -1):                               # NOTE: The reverse order (to start at b[-1][-1])!!
            if b[r][c]:
                result_set.append(items[r-1])
                c -= ceil(items[r-1].weight)
                rounded_result_wt += ceil(items[r-1].weight)
                actual_result_wt += items[r-1].weight
        return result_tot, {'Rounded': rounded_result_wt, 'Actual': actual_result_wt}, result_set


# APPROACH: Tabulation/Bottom Up Dynamic Programming And The Ceiling Function
# SEE: knapsack_01.py for the 01 knapsack approaches, time and space complexities, and descriptions.
def knapsack_01_with_real_numbers_dp_via_bottom_up_and_ceil(items, capacity):
    if items is not None and capacity is not None:
        n = len(items)
        dp = [[0] * (capacity+1) for _ in range(n+1)]       # dp[-1][-1] has max value when done
        b = [[False] * (capacity+1) for _ in range(n+1)]    # NOTE: Be VERY careful with the counters!
        for r in range(1, n+1):                             # r=0 is a padding row, r=1 to n are the list items.
            for c in range(capacity+1):                     # c = a discrete capacity from 0 to total capacity
                if ceil(items[r-1].weight) <= c and dp[r-1][c] < items[r-1].value + dp[r-1][c-ceil(items[r-1].weight)]:
                    dp[r][c] = items[r-1].value + dp[r-1][c-ceil(items[r-1].weight)]
                    b[r][c] = True
                else:
                    dp[r][c] = dp[r-1][c]
        rounded_result_wt = 0
        actual_result_wt = 0
        result_set = []                                         # The next few lines builds the result set from the
        c = capacity                                            # boolean mat, see the example above for more info.
        for r in range(n, 0, -1):                               # NOTE: The reverse order (to start at b[-1][-1])!!
            if b[r][c]:
                result_set.append(items[r-1])
                c -= ceil(items[r-1].weight)
                rounded_result_wt += ceil(items[r-1].weight)
                actual_result_wt += items[r-1].weight
        return dp[-1][-1], {'Rounded': rounded_result_wt, 'Actual': actual_result_wt}, result_set


class Item:
    def __init__(self, value, weight, name=None, units=1):
        self.value = value
        self.weight = weight
        self.name = name
        self.units = units

    def __repr__(self):
        return ((f"(Name: {self.name!r}, " if self.name else "(") +
                f"Value: {self.value}, Weight: {self.weight}" +
                (f", Units: {self.units})" if self.units > 1 else ")"))


args = [(15, [Item(36.01, 3.8, 'beef'), Item(43.01, 5.4, 'pork'), Item(90.01, 3.6, 'ham'), Item(45.01, 2.4, 'greaves'),
              Item(30.01, 4.0, 'flitch'), Item(56.01, 2.5, 'brawn'), Item(67.01, 3.7, 'welt'), Item(95.01, 3.0, 'salami'),
              Item(98.01, 5.9, 'sausage')])]
fns = [knapsack_01_with_real_numbers_bf_via_itertools,
       knapsack_01_with_real_numbers_bf_via_combinatorics,
       knapsack_01_with_real_numbers_naive_via_rec,
       knapsack_01_with_real_numbers_naive_via_rec_with_lru_cache,
       knapsack_01_with_real_numbers_dp_via_top_down_and_dicts,
       knapsack_01_with_real_numbers_naive_via_rec_and_ceil,
       knapsack_01_with_real_numbers_dp_via_top_down_and_ceil,
       knapsack_01_with_real_numbers_dp_via_bottom_up_and_ceil]

for capacity, items in args:
    print(f"\nitems: {items}\ncapacity: {capacity}")
    for fn in fns:
        print(f"{fn.__name__}(items, capacity):")
        t = time.time()
        result = fn(copy.copy(items), capacity)
        print(f"\tTotal Value: {result[0]}")
        print(f"\tTotal Weight: {result[1]}")
        print(f"\tSelected Items: {sorted(result[2], key=lambda x: x.name)}")
        print(f"\tTime: {time.time() - t} seconds.")
        print()
    print()


