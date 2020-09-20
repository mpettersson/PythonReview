"""
    COINS (CCI 8.11)

    Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write
    code to calculate the number of ways of representing n cents.

    Example:
        Input = 10
        Output = 4  # (or, 1 dime, 2 nickels, 1 nickle and 5 pennies, and 10 pennies)
"""
import time


# Recursive solution without Memoization
def make_change_rec(n):

    def _make_change_rec(n, coins, coins_i):
        if coins_i is len(coins) - 1:
            if n % coins[coins_i] is 0:
                return 1
            return 0
        ways = i = 0
        while i * coins[coins_i] <= n:
            ways += _make_change_rec(n - i * coins[coins_i], coins, coins_i + 1)
            i += 1
        return ways

    if n is not None and n >= 0:
        return _make_change_rec(n, [25, 10, 5, 1], 0)


# Recursive solution WITH Memoization
def make_change_memo(n):

    def _make_change_memo(n, coins, coins_i, memo):
        if memo[n][coins_i] > 0:
            return memo[n][coins_i]
        if coins_i is len(coins) - 1:
            if n % coins[coins_i] is 0:
                return 1
            return 0
        ways = i = 0
        while i * coins[coins_i] <= n:
            ways += _make_change_memo(n - i * coins[coins_i], coins, coins_i + 1, memo)
            i += 1
        memo[n][coins_i] = ways
        return ways

    if n is not None and n >= 0:
        coins = [25, 10, 5, 1]
        memo = [[0] * len(coins) for _ in range(n + 1)]
        return _make_change_memo(n, coins, 0, memo)


args = [-1, 0, 1, 5, 10, 25, 69]

for n in args:
    print(f"make_change_rec({n}): {make_change_rec(n)}")
print()

for n in args:
    print(f"make_change_rec_memo({n}): {make_change_memo(n)}")
print()

n = 3000
t = time.time(); print(f"make_change_rec({n}): {make_change_rec(n)} (took {time.time() - t} seconds)")
t = time.time(); print(f"make_change_memo({n}): {make_change_memo(n)} (took {time.time() - t} seconds)")


