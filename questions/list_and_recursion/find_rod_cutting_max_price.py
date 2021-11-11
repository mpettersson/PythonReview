"""
    FIND ROD CUTTING MAX PRICE

    Given an integer n representing a rod of length n, and an integer list of prices (where the first price is for a rod
    with a length 1, the second price is for a rod of length 2, etc.), compute the maximum profit that can be be made by
    cutting and selling the rod.

    Consider possible total sale prices given a rod of length 4 and a price list of [1, 5, 8, 9, 10]:

        Length  Price
        ------  -----
        1       1
        2       5
        3       8
        4       9
        5       10

        Possible Cut Combinations:
            ◼◼◼◼        Lengths: 4              Prices:                 9
            ◼◼◼ ◼       Lengths: 3, 1           Prices: 8 + 1 =         9
            ◼◼ ◼◼       Lengths: 2, 2           Prices: 5 + 5 =         10
            ◼ ◼◼◼       Lengths: 1, 3           Prices: 1 + 8 =         9
            ◼◼ ◼ ◼      Lengths: 2, 1, 1        Prices: 5 + 1 + 1 =     7
            ◼ ◼◼ ◼      Lengths: 1, 2, 1        Prices: 1 + 1 + 5 =     7
            ◼ ◼ ◼ ◼     Lengths: 1, 1, 1, 1     Prices: 1 + 1 + 1 + 1 = 4

    Example:
        Input = 4, [1, 5, 8, 10]
        Output = 10
"""
import functools


# APPROACH: Naive/Plain Recursion
#
# For each integer position size, a choice to cut or not cut is made.  Since there are n-1 positions for consideration,
# therefore, the total number of possibilities is 2**n-1.  This is inefficient because because the same subproblems are
# repeatedly solved.
#
# Time Complexity: O(2 ** s), where s is the size of the rod.
# Space Complexity: O(s), where s is the size of the rod.
def find_rod_cutting_max_price_rec(size, prices):
    if isinstance(size, int) and size >= 0 and isinstance(prices, list) and len(prices) > 0 and all(map(lambda e: isinstance(e, int), prices)):
        if size == 0:
            return 0
        result = -float('inf')
        for i in range(1, size + 1):
            if i <= len(prices):                        # NOTE: Check if curr size (i) has a price, else SKIP.
                result = max(result, prices[i - 1] + find_rod_cutting_max_price_rec(size - i, prices))
        return result
    return 0


# APPROACH: (Top Down Dynamic Programming) Via Functools LRU Cache
#
# This solution is almost identical to the plain recursive approach above, however, it uses functools LRU cache to add
# memoization and prevent solving duplicate subproblems.
#
# Time Complexity: O(s ** 2), where s is the size of the rod.
# Space Complexity: O(s), where s is the size of the rod.
def find_rod_cutting_max_price_lru_cache(size, prices):

    @functools.lru_cache(None)
    def _rec(size):
        if size == 0:
            return 0
        result = -float('inf')
        for i in range(1, size + 1):
            if i <= len(prices):                        # NOTE: Check if curr size (i) has a price, else SKIP.
                result = max(result, prices[i - 1] + _rec(size - i))
        return result

    if isinstance(size, int) and size >= 0 and isinstance(prices, list) and len(prices) > 0 and all(map(lambda e: isinstance(e, int), prices)):
        return _rec(size)
    return 0


# APPROACH: Top Down Dynamic Programming W/ Memoization
#
# This approach recursively finds the optimal prices (similar to the plain recursive approach above), then stores the
# results in a memoization table (list) so that subproblems are not recomputed.  This is simply an optimization
# technique for (plain) recursive solutions.
#
# Time Complexity: O(s ** 2), where s is the size of the rod.
# Space Complexity: O(s), where s is the size of the rod.
def find_rod_cutting_max_price_memo(size, prices):
    def _rec(size, prices, memo):
        if size == 0:
            return 0
        if memo[size] is None:
            result = -float('inf')
            for i in range(1, size + 1):
                if i <= len(prices):                    # NOTE: Check if curr size (i) has a price, else SKIP.
                    result = max(result, prices[i - 1] + _rec(size - i, prices, memo))
            memo[size] = result
        return memo[size]

    if isinstance(size, int) and size >= 0 and isinstance(prices, list) and len(prices) > 0 and all(map(lambda e: isinstance(e, int), prices)):
        memo = [None] * (size + 1)
        return _rec(size, prices, memo)
    return 0


# APPROACH: Bottom Up Dynamic Programming (Tabulation)
#
# Similar to the top down dynamic programming, this approach uses a memoization table/cache to store precomputed values.
# However, since this works from the 'bottom up', the need for recursion is eliminated (a nested loop is used in stead),
# thus alleviating the need for setting up/tearing down recursive stacks.
#
# Time Complexity: O(s ** 2), where s is the size of the rod.
# Space Complexity: O(s), where s is the size of the rod.
def find_rod_cutting_max_price_tab(size, prices):
    if isinstance(size, int) and size >= 0 and isinstance(prices, list) and len(prices) > 0 and all(map(lambda e: isinstance(e, int), prices)):
        cache = [0] * (size + 1)
        for i in range(1, size + 1):
            curr_max = -float('inf')
            for j in range(0, i):                       # Nested j loop in place of recursion.
                if j < len(prices):                     # NOTE: Check if curr size (j) has a price else SKIP
                    curr_max = max(curr_max, prices[j] + cache[i - j - 1])
            cache[i] = curr_max
        return cache[size]
    return 0


args = [(4, [1, 5, 8, 9, 10]),
        (4, [1, 5, 6, 7, 8]),
        (5, [1, 5, 8, 9, 10]),
        (3, [1, 5, 8, 9, 10]),
        (2, [1, 5, 8, 9, 10]),
        (1, [1, 5, 8, 9, 10]),
        (7, [1, 2, 3, 4, 5, 6, 7]),
        (7, [1]),
        (0, [1, 2, 3, 4, 5, 6, 7]),
        (-1, [1, 2, 3, 4, 5, 6, 7]),
        (7, [1, 5, 8, 9, 10]),
        (20, [1, 5, 8, 9, 10])]
fns = [find_rod_cutting_max_price_rec,
       find_rod_cutting_max_price_lru_cache,
       find_rod_cutting_max_price_memo,
       find_rod_cutting_max_price_tab]

for size, prices in args:
    print(size, prices)
    for fn in fns:
        print(f"{fn.__name__}({size}, {prices}): {fn(size, prices[:])}")
    print()


