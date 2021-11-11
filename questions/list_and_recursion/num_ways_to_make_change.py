"""
    NUM WAYS TO MAKE CHANGE (CCI 8.11: COINS)

    Write a function which accepts a list of ints (representing coin denominations) and an amount n (representing the
    amount of change to be made), and outputs the total number of ways that the amount (n) can be made from the coins.
    Assume that there are no availability limits for the coins.

    Example:
        Input = 10
        Output = 4  # (or, 1 dime, 2 nickels, 1 nickle and 5 pennies, and 10 pennies)
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Input Validation?
#   - Can the list have duplicate values?
#   - Will the list be sorted?


# APPROACH: Recursive Approach
#
# Recursively try an increasing multiple (1, 2, ... ,n) for each coin denomination, maintaining then returning the
# number of 'ways' that sum to the given amount.
#
# Time Complexity: O(amount ** n), where n is the size of the coins list.
# Space Complexity: O(amount).
def make_change_rec(coins, amount):

    def _make_change_rec(n, coins, coins_i):
        if n == 0 or (coins_i == len(coins) - 1 and n % coins[coins_i] == 0):
            return 1
        if coins_i >= len(coins) or coins_i == len(coins) - 1:
            return 0
        ways = i = 0
        while i * coins[coins_i] <= n:
            ways += _make_change_rec(n - i * coins[coins_i], coins, coins_i + 1)
            i += 1
        return ways

    if coins is not None and amount is not None and amount >= 0:
        return _make_change_rec(amount, coins, 0)
    return 0


# APPROACH: Memoization/Top Down Dynamic Programming
#
# This approach has the same structure as the recursive approach above, however, it has been optimized via the use of
# memoization (or a cache), to reduce duplicate computations.
#
# Time Complexity: O(amount * n), where n is the size of the coins list.
# Space Complexity: O(amount).
def make_change_memo(coins, amount):

    def _make_change_memo(n, coins, coins_i, memo):
        if n == 0 or (coins_i == len(coins) - 1 and n % coins[coins_i] == 0):
            return 1
        if coins_i >= len(coins) or coins_i == len(coins) - 1:
            return 0
        if memo[n][coins_i] <= 0:
            ways = i = 0
            while i * coins[coins_i] <= n:
                ways += _make_change_memo(n - i * coins[coins_i], coins, coins_i + 1, memo)
                i += 1
            memo[n][coins_i] = ways
        return memo[n][coins_i]

    if coins is not None and amount is not None and amount >= 0:
        memo = [[0] * len(coins) for _ in range(amount + 1)]
        return _make_change_memo(amount, coins, 0, memo)
    return 0


# APPROACH: Tabulation/Bottom Up Dynamic Programming
#
# This approach simply builds the memoization/cache list, by recording the number of coins required for every value in
# the range of one to the amount (for each possible coin), then returning the final count.
#
# Time Complexity: O(n * amount), where n is the size of the coins list.
# Space Complexity: O(amount).
def make_change_tab(coins, amount):
    if coins is not None and amount is not None:
        if amount == 0:
            return 1
        if amount > 0:
            dp = [0] * (amount + 1)
            dp[0] = 1
            for i in coins:
                for j in range(1, amount + 1):
                    if j >= i:
                        dp[j] += dp[j - i]
                    # print(f"coin:{i}, amount:{j}, dp:{dp}")
            return dp[amount]
    return 0


def format_matrix(m):
    try:
        w = max([len(str(e)) for r in m for e in r]) + 1
    except (ValueError, TypeError):
        return f"\n{None}"
    return m if not m else '\t' + '\n\t'.join(
        [''.join([f'{e!r:{w}}' for e in r if len(r) > 0]) for r in m if len(m) > 0])


args = [([25, 10, 5, 1], 1),
        ([4, 3, 1], 6),
        ([25, 10, 5, 1], 0),
        ([25, 10, 5, 1], -1),
        ([25, 10, 5, 1], 10),
        ([1, 5, 10, 25], 10),
        ([25, 10, 5, 1], 69),
        ([25, 10, 5, 1], 101),
        # ([3, 5, 7, 8, 9, 10, 11], 500),  # This takes a long time with the plain recursive approach...
        ([10], 10),
        ([10], 100),
        ([10], 11),
        ([1, 2, 5], 5),
        ([], 0),
        ([], 7),
        ([], -7),
        ([], None),
        (None, 0),
        (None, -1),
        (None, None)]
fns = [make_change_rec,
       make_change_memo,
       make_change_tab]

for coins, n in args:
    for fn in fns:
        print(f"{fn.__name__}({coins}, {n}): {fn(coins, n)}")
    print()


